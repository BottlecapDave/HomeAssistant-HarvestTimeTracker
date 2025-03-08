import logging

from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity import generate_entity_id

from homeassistant.components.event import (
    EventEntity,
    EventExtraStoredData,
)
from homeassistant.helpers.restore_state import RestoreEntity

from ..utils.attributes import dict_to_typed_dict
from ..const import EVENT_TASKS_UPDATED

_LOGGER = logging.getLogger(__name__)

class HarvestTasks(EventEntity, RestoreEntity):
  """Sensor for displaying the tasks associated with a given harvest account."""
  
  _unrecorded_attributes = frozenset({ "tasks" })

  def __init__(self, hass: HomeAssistant, account_name: str, account_id: str):
    """Init sensor."""

    self._hass = hass
    self._state = None
    self._last_updated = None
    self._account_id = account_id
    self._account_name = account_name

    self._attr_event_types = [EVENT_TASKS_UPDATED]
    self.entity_id = generate_entity_id("event.{}", self.unique_id, hass=hass)

  @property
  def unique_id(self):
    """The id of the sensor."""
    return f"harvest_time_tracker_{self._account_name if self._account_name is not None else self._account_id}_tasks"
    
  @property
  def name(self):
    """Name of the sensor."""
    return f"Harvest Tasks ({self._account_name if self._account_name is not None else self._account_id})"

  async def async_added_to_hass(self):
    """Call when entity about to be added to hass."""
    # If not None, we got an initial value.
    await super().async_added_to_hass()
    
    self._hass.bus.async_listen(self._attr_event_types[0], self._async_handle_event)

  async def async_get_last_event_data(self):
    data = await super().async_get_last_event_data()
    return EventExtraStoredData.from_dict({
      "last_event_type": data.last_event_type,
      "last_event_attributes": dict_to_typed_dict(data.last_event_attributes),
    })

  @callback
  def _async_handle_event(self, event) -> None:
    if (event.data is not None and "account_id" in event.data and event.data["account_id"] == self._account_id):
      self._trigger_event(event.event_type, event.data)
      self.async_write_ha_state()