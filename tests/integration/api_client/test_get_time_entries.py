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