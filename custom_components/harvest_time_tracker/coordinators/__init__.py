from datetime import datetime, timedelta

from homeassistant.util.dt import (as_utc, parse_datetime)

def calculate_week_start(current: datetime, week_start: str) -> datetime:
  day_offset = 0
  
  if (week_start == "Saturday"):
    day_offset = current.weekday() - 5 if current.weekday() >= 5 else current.weekday() + 2
  elif (week_start == "Sunday"):
    day_offset = 0 if current.weekday() == 6 else current.weekday() + 1
  elif (week_start == "Monday"):
    day_offset = 0 if current.weekday() == 0 else current.weekday()

  return as_utc(parse_datetime((current - timedelta(days=day_offset)).strftime("%Y-%m-%dT00:00:00Z")))