import logging
import json
import aiohttp
from datetime import (datetime)

from homeassistant.util.dt import (parse_datetime)

from .time_entry import TimeEntry

from .task import Task

_LOGGER = logging.getLogger(__name__)

class ServerError(Exception): ...

class RequestError(Exception): ...

class HarvestApiClient:

  def __init__(self, api_key, account_id):
    if (api_key is None):
      raise Exception('API KEY is not set')
  
    if (account_id is None):
      raise Exception('Account ID is not set')

    self._api_key = api_key
    self._account_id = account_id
    self._base_url = 'https://api.harvestapp.com'

  async def async_get_time_entries(self, period_from: datetime, period_to: datetime) -> list:
    """Get all time entries"""
    page = 1
    has_next_page = True
    results = []

    while (has_next_page):
      async with aiohttp.ClientSession() as client:
        headers = { "Authorization": f"Bearer {self._api_key}", "Harvest-Account-Id": self._account_id }
        url = f'{self._base_url}/v2/time_entries?from={period_from.strftime("%Y-%m-%dT%H:%M:%SZ")}&to={period_to.strftime("%Y-%m-%dT%H:%M:%SZ")}&page={page}'
        async with client.get(url, headers=headers) as response:
          data = await self.__async_read_response__(response, url)
          if data is not None:
            results.extend(list(map(lambda d: TimeEntry(
              d["id"],
              d["client"]["id"],
              d["client"]["name"],
              d["project"]["id"],
              d["project"]["name"],
              d["task"]["id"],
              d["task"]["name"],
              float(d["hours"]),
              self.__to_iso_date(d["spent_date"], d["started_time"]),
              self.__to_iso_date(d["spent_date"], d["ended_time"]),
              d["notes"]
            ), data["time_entries"])))

            if data["total_pages"] < page:
              has_next_page = False
            
            page = page + 1
          else:
            has_next_page = False

    return results
  
  async def async_get_tasks(self) -> list:
    """Get all time entries"""
    has_next_page = True
    url = f'{self._base_url}/v2/users/me/project_assignments?is_active=true&page=1'
    results = []

    while (has_next_page):
      async with aiohttp.ClientSession() as client:
        headers = { "Authorization": f"Bearer {self._api_key}", "Harvest-Account-Id": self._account_id }
        async with client.get(url, headers=headers) as response:
          data = await self.__async_read_response__(response, url)
          if data is not None:
            for project_assignment in data["project_assignments"]:
              for task_assignment in project_assignment["task_assignments"]:
                results.append(Task(
                  task_assignment["task"]["id"],
                  project_assignment["client"]["id"],
                  project_assignment["client"]["name"],
                  project_assignment["project"]["id"],
                  project_assignment["project"]["name"],
                  task_assignment["task"]["name"],
                ))

            if data["links"]["next"] is not None:
              url = data["links"]["next"]
            else:
              has_next_page = False
            
          else:
            has_next_page = False

    return results
  
  async def async_create_time_entry_with_hours(
      self,
      project_id: str,
      task_id: str,
      spent_date: datetime,
      hours: float,
      notes: str
  ) -> TimeEntry:
    """Get all time entries"""
    async with aiohttp.ClientSession() as client:
      headers = { "Authorization": f"Bearer {self._api_key}", "Harvest-Account-Id": self._account_id }
      payload = {
        "project_id": project_id,
        "task_id": task_id,
        "spent_date": spent_date.strftime("%Y-%m-%d"),
        "hours": hours,
        "notes": notes
      }
      url = f'{self._base_url}/v2/time_entries'
      async with client.post(url, json=payload, headers=headers) as response:
        data = await self.__async_read_response__(response, url)
        return TimeEntry(
          data["id"],
          data["client"]["id"],
          data["client"]["name"],
          data["project"]["id"],
          data["project"]["name"],
          data["task"]["id"],
          data["task"]["name"],
          float(data["hours"]),
          self.__to_iso_date(data["spent_date"], data["started_time"]),
          self.__to_iso_date(data["spent_date"], data["ended_time"]),
          data["notes"]
        )

  def __to_iso_date(self, date, time):
    if date is None:
      return None
    
    if time is None:
      return parse_datetime(f'{date}T00:00:00')
    
    time_in_12_hours = datetime.strptime(time, "%I:%M %p")
    time_in_24_hours = datetime.strftime(time_in_12_hours, "%H:%M")

    return parse_datetime(f'{date}T{time_in_24_hours}:00')

  async def __async_read_response__(self, response, url):
    """Reads the response, logging any json errors"""

    text = await response.text()

    if response.status >= 400:
      if response.status >= 500:
        msg = f'DO NOT REPORT - Harvest server error ({url}): {response.status}; {text}'
        _LOGGER.debug(msg)
        raise ServerError(msg)
      elif response.status not in [401, 403, 404]:
        msg = f'Failed to send request ({url}): {response.status}; {text}'
        _LOGGER.debug(msg)
        raise RequestError(msg)
      return None

    try:
      return json.loads(text)
    except:
      raise Exception(f'Failed to extract response json: {url}; {text}')
