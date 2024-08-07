import logging
from ..api_client import HarvestApiClient
from ..const import CONFIG_KIND, CONFIG_KIND_ACCOUNT, CONFIG_MAIN_ACCOUNT_ID, CONFIG_MAIN_API_KEY, CONFIG_MAIN_USER_ID

_LOGGER = logging.getLogger(__name__)

async def async_migrate_main_config(version: int, data: {}):
  new_data = {**data}

  if (version <= 1):
    new_data[CONFIG_KIND] = CONFIG_KIND_ACCOUNT

    api_client = HarvestApiClient(new_data[CONFIG_MAIN_API_KEY], new_data[CONFIG_MAIN_ACCOUNT_ID])

    user = await api_client.async_get_current_user()
    if user is None:
      raise ValueError("Failed to retrieve current user")

    new_data[CONFIG_MAIN_USER_ID] = user.id

  return new_data