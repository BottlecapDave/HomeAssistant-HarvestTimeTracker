from datetime import timedelta
import logging

from homeassistant.util.dt import (utcnow, as_utc, parse_datetime)
from homeassistant.helpers.update_coordinator import (
  DataUpdateCoordinator
)

from ..const import (
  DOMAIN,

  DATA_TIME_ENTRIES_COORDINATOR
)

from ..api_client import (HarvestApiClient)

_LOGGER = logging.getLogger(__name__)

async def async_setup_time_entries_coordinator(hass, client: HarvestApiClient):
  """Create time entries coordinator"""

  async def async_update_data():
    """Fetch data from API endpoint."""
    current = utcnow()
    
    key = 'time_entries'
    period_from = as_utc(parse_datetime((current + timedelta(days=-current.weekday())).strftime("%Y-%m-%dT00:00:00Z")))
    period_to = as_utc(parse_datetime((current + timedelta(days=1)).strftime("%Y-%m-%dT00:00:00Z")))

    try:
      hass.data[DOMAIN][key] = await client.async_get_time_entries(period_from, period_to)
    except:
      _LOGGER.debug('Failed to retrieve time entries')

    return hass.data[DOMAIN][key]

  hass.data[DOMAIN][DATA_TIME_ENTRIES_COORDINATOR] = DataUpdateCoordinator(
    hass,
    _LOGGER,
    name=f"time_entries",
    update_method=async_update_data,
    update_interval=timedelta(minutes=1),
  )

  return hass.data[DOMAIN][DATA_TIME_ENTRIES_COORDINATOR]