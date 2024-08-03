import pytest

from homeassistant.util.dt import (as_utc, parse_datetime)

from integration import get_test_context
from custom_components.harvest_time_tracker.api_client import HarvestApiClient

@pytest.mark.asyncio
async def test_when_get_company_is_called_then_tasks_returned():
    # Arrange
    context = get_test_context()
    client = HarvestApiClient(context.api_key, context.account_id)

    # Act
    result = await client.async_get_company()

    # Assert
    assert result is not None
    assert result.wants_timestamp_timers == True