import re
from datetime import datetime, timedelta

import voluptuous as vol

from homeassistant.util.dt import (as_utc, parse_datetime)
from homeassistant.exceptions import ServiceValidationError

from ..const import (
  DOMAIN,
  REGEX_DATE,
  REGEX_HOURS,
  REGEX_TIME_WITH_SECONDS
)

from ..api_client import (HarvestApiClient)

async def async_create_time_entry_with_hours(client: HarvestApiClient, project_id: int, task_id: int, date: str, hours: str, notes: str = None):
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

  company = await client.async_get_company()
  if (company is None or company.wants_timestamp_timers == True):
    raise ServiceValidationError(
      translation_domain=DOMAIN,
      translation_key="create_time_entry_with_hours_not_supported",
    )

  await client.async_create_time_entry_with_hours(project_id, task_id, parsed_date, parsed_hours, notes)

async def async_create_time_entry_with_start_end_times(client: HarvestApiClient, project_id: int, task_id: int, date: str, start_time: str, end_time: str, notes: str = None):
  # Inputs from automations can include quotes, so remove these
  trimmed_date = date.strip('\"')
  matches = re.search(REGEX_DATE, trimmed_date)
  if matches is None:
    raise vol.Invalid(f"Date '{trimmed_date}' must match format of YYYY-MM-DD.")
  
  # Inputs from automations can include quotes, so remove these
  trimmed_start_time = start_time.strip('\"')
  matches = re.search(REGEX_TIME_WITH_SECONDS, trimmed_start_time)
  if matches is None:
    raise vol.Invalid(f"Start time must be in 24 hour clock format (e.g. 10:00:00).")
  
  # Inputs from automations can include quotes, so remove these
  trimmed_end_time = end_time.strip('\"')
  matches = re.search(REGEX_TIME_WITH_SECONDS, trimmed_end_time)
  if matches is None:
    raise vol.Invalid(f"End time must be in 24 hour clock format (e.g. 10:00:00).")
  
  company = await client.async_get_company()
  if (company is None or company.wants_timestamp_timers == False):
    raise ServiceValidationError(
      translation_domain=DOMAIN,
      translation_key="create_time_entry_with_start_end_times_not_supported",
    )
  
  parsed_date = parse_datetime(f'{trimmed_date}T00:00:00')
  await client.async_create_time_entry_with_start_end_times(
    project_id,
    task_id,
    parsed_date,
    datetime.strptime(trimmed_start_time, "%H:%M:%S").time(),
    datetime.strptime(trimmed_end_time, "%H:%M:%S").time(),
    notes
  )

class HoursResult:
  hours: int
  entries: list

  def __init__(self,
               hours: float,
               entries: str
  ):
    self.hours = hours
    self.entries = entries

def get_todays_hours(today: datetime, entries: list) -> HoursResult:
  total_hours = 0
  applicable_entries = []

  if entries is not None:
    today_start = today.replace(hour=0, minute=0, second=0, microsecond=0)
    today_end = (today + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
    for entry in entries:
      entry_start = as_utc(entry.start)
      entry_end = as_utc(entry.end)
      if (entry_start >= today_start and entry_end < today_end):
        total_hours = total_hours + entry.hours
        applicable_entries.append(entry.to_json())

  return HoursResult(total_hours, applicable_entries)

def get_all_hours(entries: list) -> HoursResult:
  total_hours = 0
  applicable_entries = []

  if entries is not None:
    for entry in entries:
      total_hours = total_hours + entry.hours
      applicable_entries.append(entry.to_json())

  return HoursResult(total_hours, applicable_entries)