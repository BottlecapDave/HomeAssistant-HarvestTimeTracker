import pytest

from homeassistant.util.dt import (as_utc, parse_datetime)

from integration import get_test_context
from custom_components.harvest_time_tracker.api_client import HarvestApiClient

@pytest.mark.asyncio
async def test_when_get_tasks_is_called_then_tasks_returned():
    # Arrange
    context = get_test_context()
    client = HarvestApiClient(context.api_key, context.account_id)

    # Act
    result = await client.async_get_tasks()

    # Assert
    assert result is not None
    assert len(result) == 3

    assert result[0].id is not None
    assert result[0].client_id is not None
    assert result[0].client_name == "Test Client"
    assert result[0].project_id is not None
    assert result[0].project_name == "Test Project"
    assert result[0].name == "Client Specific Task"
    
    assert result[1].id is not None
    assert result[1].client_id is not None
    assert result[1].client_name == "Test Client"
    assert result[1].project_id is not None
    assert result[1].project_name == "Test Project"
    assert result[1].name == "Programming"

    assert result[2].id is not None
    assert result[2].client_id is not None
    assert result[2].client_name == "Example Client"
    assert result[2].project_id is not None
    assert result[2].project_name == "Example Project"
    assert result[2].name == "Programming"