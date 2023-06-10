from datetime import timedelta
import logging
from homeassistant.util.dt import (utcnow)
from homeassistant.core import HomeAssistant


from .sensors.hours_today import HarvestHoursToday

from .const import (
  DOMAIN,
  
  CONFIG_MAIN_API_KEY,
  CONFIG_MAIN_ACCOUNT_ID,

  DATA_TIME_ENTRIES_COORDINATOR
)

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=1)

async def async_setup_entry(hass, entry, async_add_entities):
  """Setup sensors based on our entry"""

  if CONFIG_MAIN_API_KEY in entry.data:
    await async_setup_default_sensors(hass, entry, async_add_entities)

async def async_setup_default_sensors(hass: HomeAssistant, entry, async_add_entities):
  config = dict(entry.data)

  if entry.options:
    config.update(entry.options)
  
  entities = [
    HarvestHoursToday(hass, hass.data[DOMAIN][DATA_TIME_ENTRIES_COORDINATOR], entry.data[CONFIG_MAIN_ACCOUNT_ID])
  ]

  async_add_entities(entities, True)
