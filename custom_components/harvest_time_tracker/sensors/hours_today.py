import logging

import re
from datetime import (datetime, timedelta)
import pytz

utc=pytz.UTC

import voluptuous as vol

from homeassistant.core import (HomeAssistant, callback)
from homeassistant.helpers.entity import generate_entity_id

from homeassistant.helpers.update_coordinator import (
  CoordinatorEntity,
)
from homeassistant.components.sensor import (
    SensorEntity,
    SensorStateClass
)
from homeassistant.helpers.restore_state import RestoreEntity

from homeassistant.util.dt import (now, as_utc, parse_datetime)

from ..api_client import HarvestApiClient

from ..const import (REGEX_DATE, REGEX_HOURS)

_LOGGER = logging.getLogger(__name__)

class HarvestHoursToday(CoordinatorEntity, SensorEntity, RestoreEntity):
  """Sensor for determining the total hours from today"""

  def __init__(self, hass: HomeAssistant, coordinator, account_id: str, client: HarvestApiClient):
    """Init sensor."""

    super().__init__(coordinator)
  
    self._state = None
    self._attributes = {
      "account_id": account_id
    }
    self._account_id = account_id
    self._client = client

    self.entity_id = generate_entity_id("sensor.{}", self.unique_id, hass=hass)

  @property
  def unique_id(self):
    """The id of the sensor."""
    return f"harvest_time_tracker_{self._account_id}_hours_today"
    
  @property
  def name(self):
    """Name of the sensor."""
    return f"Harvest Hours Today ({self._account_id})"

  @property
  def icon(self):
    """Icon of the sensor."""
    return "mdi:time"

  @property
  def extra_state_attributes(self):
    """Attributes of the sensor."""
    return self._attributes

  @property
  def state_class(self):
    """The state class of sensor"""
    return SensorStateClass.TOTAL_INCREASING

  @property
  def state(self):
    """Retrieve the previously calculated state"""
    entries = self.coordinator.data
    self._state = 0

    if entries is not None:
      today_start = now().replace(hour=0, minute=0, second=0, microsecond=0)
      today_end = (now() + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
      for entry in entries:
        entry_start = as_utc(entry.start)
        entry_end = as_utc(entry.end)
        if (entry_start >= today_start and entry_end < today_end):
          self._state = self._state + entry.hours

    return self._state

  async def async_added_to_hass(self):
    """Call when entity about to be added to hass."""
    # If not None, we got an initial value.
    await super().async_added_to_hass()
    state = await self.async_get_last_state()

    if state is not None and self._state is None:
      self._state = state.state
      self._attributes = {}
      for x in state.attributes.keys():
        self._attributes[x] = state.attributes[x]
    
      _LOGGER.debug(f'Restored HarvestHoursToday state: {self._state}')

  @callback
  async def async_add_time_with_hours(self, project_id: int, task_id: int, date: str, hours: str, notes: str = None):
    """Update sensors config"""

    # Inputs from automations can include quotes, so remove these
    trimmed_date = date.strip('\"')
    matches = re.search(REGEX_DATE, trimmed_date)
    if matches is None:
      raise vol.Invalid(f"Date '{trimmed_date}' must match format of YYYY-MM-DD.")
    
    # Inputs from automations can include quotes, so remove these
    trimmed_hours = hours.strip('\"')
    matches = re.search(REGEX_HOURS, trimmed_hours)
    if matches is None:
      raise vol.Invalid(f"Hours must be a valid float.")
    
    parsed_date = parse_datetime(f'{trimmed_date}T00:00:00')
    parsed_hours = float(trimmed_hours)
    await self._client.async_create_time_entry_with_hours(project_id, task_id, parsed_date, parsed_hours, notes)