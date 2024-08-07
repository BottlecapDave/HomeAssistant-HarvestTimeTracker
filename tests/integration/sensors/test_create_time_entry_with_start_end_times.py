import pytest
import uuid
from datetime import (timedelta)

from homeassistant.util.dt import (utcnow, parse_datetime)

from integration import get_test_context
from custom_components.harvest_time_tracker.api_client import HarvestApiClient
from custom_components.harvest_time_tracker.sensors import async_create_time_entry_with_start_end_times

@pytest.mark.asyncio
async def test_when_create_time_entry_with_start_end_times_then_time_entry_added():
    # Arrange
    context = get_test_context()
    client = HarvestApiClient(context.api_key, context.account_id)

    # Only run if our target company supports this function
    company = await client.async_get_company()
    if company.wants_timestamp_timers == False:
        return

    # Get a task that exists
    tasks = await client.async_get_tasks()
    assert tasks is not None
    assert len(tasks) > 0

    project_id = tasks[0].project_id
    task_id = tasks[0].id
    now = utcnow()
    date = now.strftime("%Y-%m-%d")
    start_time = "12:00:00"
    end_time = "13:00:00"
    notes = f"Integration Test - async_create_time_entry_with_start_end_times - {str(uuid.uuid4())}"

    # Act
    await async_create_time_entry_with_start_end_times(client, project_id, task_id, date, start_time, end_time, notes)

    # Assert
    period_from = utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    period_to = period_from + timedelta(days=1)
    entries = await client.async_get_time_entries(context.user_id, period_from, period_to)

    assert entries is not None
    assert len(entries) >= 1

    entry_exists = False
    for entry in entries:
        if entry.notes == notes:
            assert entry.start.date() == parse_datetime(now.strftime("%Y-%m-%dT00:00:00")).date()
            assert entry.end.date() == parse_datetime(now.strftime("%Y-%m-%dT00:00:00")).date()
            assert (entry.end - entry.start).total_seconds() == 3600
            assert entry.hours == 1.0
            entry_exists = True
            break
    
    assert entry_exists == True