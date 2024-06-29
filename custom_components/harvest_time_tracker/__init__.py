import logging
import asyncio

from homeassistant.exceptions import ConfigEntryNotReady

from .const import (
  DOMAIN,

  CONFIG_MAIN_API_KEY,
  CONFIG_MAIN_ACCOUNT_ID,
  CONFIG_MAIN_WEEK_START,

  DATA_API_CLIENT,
  DATA_WEEK_START,
)

from .api_client import HarvestApiClient

from .coordinators.time_entries import async_setup_time_entries_coordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor", "select"]

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

  hass.data[DOMAIN][account_id][DATA_API_CLIENT] = HarvestApiClient(api_key, account_id)
  hass.data[DOMAIN][account_id][DATA_WEEK_START] = config[CONFIG_MAIN_WEEK_START]

  await async_setup_time_entries_coordinator(hass, hass.data[DOMAIN][account_id][DATA_API_CLIENT], account_id)


async def options_update_listener(hass, entry):
  """Handle options update."""
  await hass.config_entries.async_reload(entry.entry_id)

async def async_unload_entry(hass, entry):
    """Unload a config entry."""
    unload_ok = True
    if CONFIG_MAIN_API_KEY in entry.data:
      unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    return unload_ok