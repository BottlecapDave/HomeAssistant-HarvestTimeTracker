import logging

from homeassistant.exceptions import ConfigEntryNotReady

from .const import (
  CONFIG_MAIN_USER_ID,
  CONFIG_VERSION,
  DATA_USER_ID,
  DOMAIN,

  CONFIG_MAIN_API_KEY,
  CONFIG_MAIN_ACCOUNT_ID,
  CONFIG_MAIN_WEEK_START,

  DATA_API_CLIENT,
  DATA_WEEK_START,
)

from .api_client import HarvestApiClient
from .config.main import async_migrate_main_config
from .coordinators.time_entries import async_setup_time_entries_coordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor", "select", "event"]

async def async_migrate_entry(hass, config_entry):
  """Migrate old entry."""
  if (config_entry.version < CONFIG_VERSION):
    _LOGGER.debug("Migrating from version %s", config_entry.version)

    new_data = None
    new_options = None
    title = config_entry.title
    if CONFIG_MAIN_API_KEY in config_entry.data:
      new_data = await async_migrate_main_config(config_entry.version, config_entry.data)
      new_options = {**config_entry.options}
    
    hass.config_entries.async_update_entry(config_entry, title=title, data=new_data, options=new_options, version=CONFIG_VERSION)

    _LOGGER.debug("Migration to version %s successful", config_entry.version)

  return True

async def async_setup_entry(hass, entry):
  """This is called from the config flow."""
  hass.data.setdefault(DOMAIN, {})

  config = dict(entry.data)

  if entry.options:
    config.update(entry.options)

  if CONFIG_MAIN_API_KEY in config:
    await async_setup_dependencies(hass, config)

    # Forward our entry to setup our default sensors
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
  
  entry.async_on_unload(entry.add_update_listener(options_update_listener))

  return True

async def async_setup_dependencies(hass, config):
  """Setup the coordinator and api client which will be shared by various entities"""

  account_id = config[CONFIG_MAIN_ACCOUNT_ID]
  api_key = config[CONFIG_MAIN_API_KEY]

  if hass.data[DOMAIN] is None:
    hass.data[DOMAIN] = dict({
      account_id: {}
    })

  if account_id not in hass.data[DOMAIN]:
    hass.data[DOMAIN][account_id] = dict({})

  api_client = HarvestApiClient(api_key, account_id)
  hass.data[DOMAIN][account_id][DATA_API_CLIENT] = api_client

  week_start = config[CONFIG_MAIN_WEEK_START]
  hass.data[DOMAIN][account_id][DATA_WEEK_START] = week_start

  user_id = config[CONFIG_MAIN_USER_ID]
  hass.data[DOMAIN][account_id][DATA_USER_ID] = week_start

  await async_setup_time_entries_coordinator(hass, api_client, account_id, user_id, week_start)


async def options_update_listener(hass, entry):
  """Handle options update."""
  await hass.config_entries.async_reload(entry.entry_id)

async def async_unload_entry(hass, entry):
    """Unload a config entry."""
    unload_ok = True
    if CONFIG_MAIN_API_KEY in entry.data:
      unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    return unload_ok