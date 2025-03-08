from datetime import timedelta
import logging

from homeassistant.core import HomeAssistant

from .sensors.hours_today import HarvestHoursToday
from .sensors.hours_week import HarvestHoursWeek

from .const import (
  CONFIG_MAIN_NAME,
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

  account_id = config[CONFIG_MAIN_ACCOUNT_ID]
  account_name = config[CONFIG_MAIN_NAME] if CONFIG_MAIN_NAME in config else None
  api_client = hass.data[DOMAIN][account_id][DATA_API_CLIENT]
  
  entities = [
    HarvestDefaultTask(hass, account_name, account_id, api_client),
  ]

  async_add_entities(entities, True)
