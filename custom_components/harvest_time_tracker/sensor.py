from datetime import timedelta
import logging
import voluptuous as vol
from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv, entity_platform

from .sensors.hours_today import HarvestHoursToday

from .const import (
  DOMAIN,
  
  CONFIG_MAIN_API_KEY,
  CONFIG_MAIN_ACCOUNT_ID,

  DATA_API_CLIENT,
  DATA_TIME_ENTRIES_COORDINATOR
)

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=1)

async def async_setup_entry(hass, entry, async_add_entities):
  """Setup sensors based on our entry"""

  if CONFIG_MAIN_API_KEY in entry.data:
    await async_setup_default_sensors(hass, entry, async_add_entities)

  platform = entity_platform.async_get_current_platform()
  platform.async_register_entity_service(
    "add_time_with_hours",
    vol.All(
      vol.Schema(
        {
          vol.Required("project_id"): cv.positive_int,
          vol.Required("task_id"): cv.positive_int,
          vol.Required("date"): cv.string,
          vol.Required("hours"): cv.string,
          vol.Optional("notes"): cv.string,
        },
        extra=vol.ALLOW_EXTRA,
      ),
    ),
    "async_add_time_with_hours",
  )

async def async_setup_default_sensors(hass: HomeAssistant, entry, async_add_entities):
  config = dict(entry.data)

  if entry.options:
    config.update(entry.options)
  
  entities = [
    HarvestHoursToday(hass, hass.data[DOMAIN][DATA_TIME_ENTRIES_COORDINATOR], entry.data[CONFIG_MAIN_ACCOUNT_ID], hass.data[DOMAIN][DATA_API_CLIENT])
  ]

  async_add_entities(entities, True)
