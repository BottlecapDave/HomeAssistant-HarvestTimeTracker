import pytest

from homeassistant.util.dt import (as_utc, parse_datetime)

from integration import get_test_context
from custom_components.harvest_time_tracker.api_client import HarvestApiClient

@pytest.mark.asyncio
async def test_when_get_time_entries_is_called_then_time_entries_returned():
    # Arrange
    context = get_test_context()
    client = HarvestApiClient(context.api_key, context.account_id)
    start_time = as_utc(parse_datetime("2023-06-09T00:00:00Z"))
    end_time = as_utc(parse_datetime("2023-06-10T00:00:00Z"))

    # Act
    result = await client.async_get_time_entries(start_time, end_time)

    # Assert
    assert result is not None
    assert len(result) == 2

    assert result[0].client_name == "Test Client"
    assert result[0].project_name == "Test Project"
    assert result[0].task_name == "Programming"
    assert result[0].hours == 0.07
    assert result[0].start == parse_datetime("2023-06-09T00:00:00")
    assert result[0].end == parse_datetime("2023-06-09T00:00:00")
    assert result[0].notes == ""

    assert result[1].client_name == "Example Client"
    assert result[1].project_name == "Example Project"
    assert result[1].task_name == "Programming"
    assert result[1].hours == 2.5
    assert result[1].start == parse_datetime("2023-06-09T00:00:00")
    assert result[1].end == parse_datetime("2023-06-09T00:00:00")
    assert result[1].notes == "this is a test"