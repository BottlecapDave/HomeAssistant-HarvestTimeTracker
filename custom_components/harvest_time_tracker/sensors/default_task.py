import logging

import pytz

utc=pytz.UTC


from homeassistant.core import (HomeAssistant, callback)
from homeassistant.helpers.entity import generate_entity_id

from homeassistant.components.select import SelectEntity

from homeassistant.helpers.restore_state import RestoreEntity

from homeassistant.util.dt import (now)

from ..api_client import HarvestApiClient
from ..const import EVENT_TASKS_UPDATED

from . import async_create_time_entry_with_hours, async_create_time_entry_with_start_end_times, get_todays_hours

_LOGGER = logging.getLogger(__name__)

class HarvestDefaultTask(SelectEntity, RestoreEntity):
  """Sensor for determining the default task"""

  def __init__(self, hass: HomeAssistant, account_name: str, account_id: str, client: HarvestApiClient):
    """Init sensor."""
  
    self._state = None
    self._attributes = {
      "account_name": account_name,
      "account_id": account_id
    }
    self._account_id = account_id
    self._account_name = account_name
    self._client = client
    self._hass = hass

    self.entity_id = generate_entity_id("select.{}", self.unique_id, hass=hass)
    self._options = {}

  @property
  def unique_id(self):
    """The id of the sensor."""
    return f"harvest_time_tracker_{self._account_name if self._account_name is not None else self._account_id}_default_task"
    
  @property
  def name(self):
    """Name of the sensor."""
    return f"Harvest Default Task ({self._account_name if self._account_name is not None else self._account_id})"

  @property
  def icon(self):
    """Icon of the sensor."""
    return "mdi:note"

  @property
  def extra_state_attributes(self):
    """Attributes of the sensor."""
    return self._attributes

  @property
  def state(self):
    """The state of the entity"""

    return self._state

  @property
  def options(self) -> list[str]:
    """The options the selected option."""
    tasks = list(self._options.keys())
    tasks.sort()
    return list(["None"]) + tasks

  async def async_update(self):
    """Retrieve the latest tasks/projects"""
    
    try:
      _LOGGER.debug(f'Retrieving tasks for {self._account_id}...')
      tasks = await self._client.async_get_tasks()
      _LOGGER.debug(f'Tasks for {self._account_id} retrieved. {tasks}')
    except:
      _LOGGER.info('Failed to retrieve tasks')
      return

    new_options = {}
    for task in tasks:
      new_options[f'{task.client_name}->{task.project_name}->{task.name}'] = task.to_json()

    self._hass.bus.async_fire(EVENT_TASKS_UPDATED, {
      "account_id": self._account_id,
      "tasks": list(map(lambda x: x.to_json(), tasks))
    })

    self._options = new_options
  
  def select_option(self, option: str) -> None:
    """Change the selected option."""

    self._state = option

    if option in self._options:
      task = self._options[option]

      self._attributes["client_id"] = task["client_id"]
      self._attributes["client_name"] = task["client_name"]
      self._attributes["project_id"] = task["project_id"]
      self._attributes["project_name"] = task["project_name"]
      self._attributes["task_id"] = task["id"]
      self._attributes["task_name"] = task["name"]
    else:
      self._attributes["client_id"] = None
      self._attributes["client_name"] = None
      self._attributes["project_id"] = None
      self._attributes["project_name"] = None
      self._attributes["task_id"] = None
      self._attributes["task_name"] = None

  async def async_added_to_hass(self):
    """Call when entity about to be added to hass."""
    # If not None, we got an initial value.
    await super().async_added_to_hass()
    state = await self.async_get_last_state()

    if state is not None and self._state is None:
      self._state = state.state
      self._attributes = {}
      for x in state.attributes.keys():
        if (x != "options"):
          self._attributes[x] = state.attributes[x]
    
      _LOGGER.debug(f'Restored HarvestDefaultTask state: {self._state}')

  @callback
  async def async_add_time_with_hours(self, project_id: int, task_id: int, date: str, hours: str, notes: str = None):
    """Create time entry with hours"""

    await async_create_time_entry_with_hours(self._client, project_id, task_id, date, hours, notes)

  @callback
  async def async_add_time_with_start_end_times(self, project_id: int, task_id: int, date: str, start_time: str, end_time: str, notes: str = None):
    """Create time entry with start/end times"""

    await async_create_time_entry_with_start_end_times(self._client, project_id, task_id, date, start_time, end_time, notes)