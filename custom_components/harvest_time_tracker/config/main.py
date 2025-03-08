import logging
from ..api_client import HarvestApiClient
from ..const import CONFIG_KIND, CONFIG_KIND_ACCOUNT, CONFIG_MAIN_ACCOUNT_ID, CONFIG_MAIN_API_KEY, CONFIG_MAIN_NAME, CONFIG_MAIN_USER_ID, DOMAIN

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

async def async_validate(config, entries):
  errors = {}
  
  if config is None:
    return errors

  client = HarvestApiClient(config[CONFIG_MAIN_API_KEY], config[CONFIG_MAIN_ACCOUNT_ID])
  user = await client.async_get_current_user()
  if (user is None):
    errors[CONFIG_MAIN_API_KEY] = "user_not_found"

  if CONFIG_MAIN_NAME in config and config[CONFIG_MAIN_NAME] != "":
    for entry in entries:
      entry_config = dict(entry.data)

      if entry.options:
        entry_config.update(entry.options)

      if entry_config[CONFIG_MAIN_ACCOUNT_ID] == config[CONFIG_MAIN_ACCOUNT_ID]:
        continue

      if (config[CONFIG_MAIN_NAME] == entry_config[CONFIG_MAIN_ACCOUNT_ID] or 
          (CONFIG_MAIN_NAME in entry_config and config[CONFIG_MAIN_NAME] == entry_config[CONFIG_MAIN_NAME])):
        errors[CONFIG_MAIN_NAME] = "name_not_unique"

  return (errors, user.id if user is not None else None)