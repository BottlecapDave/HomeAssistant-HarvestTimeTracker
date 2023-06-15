from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant

from .sensors.hours_today import HarvestHoursToday
from .sensors.hours_week import HarvestHoursWeek

from .const import (
  DOMAIN,
  
  CONFIG_MAIN_API_KEY,
  CONFIG_MAIN_ACCOUNT_ID,

  DATA_API_CLIENT,
)


from .sensors.default_task import HarvestDefaultTask

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=5)

async def async_setup_entry(hass, entry, async_add_entities):
  """Setup sensors based on our entry"""

  if CONFIG_MAIN_API_KEY in entry.data:
    await async_setup_default_sensors(hass, entry, async_add_entities)

async def async_setup_default_sensors(hass: HomeAssistant, entry, async_add_entities):
  config = dict(entry.data)

  if entry.options:
    config.update(entry.options)

  account_id = entry.data[CONFIG_MAIN_ACCOUNT_ID]
  api_client = hass.data[DOMAIN][account_id][DATA_API_CLIENT]
  
  entities = [
    HarvestDefaultTask(hass, account_id, api_client),
  ]

  async_add_entities(entities, True)
