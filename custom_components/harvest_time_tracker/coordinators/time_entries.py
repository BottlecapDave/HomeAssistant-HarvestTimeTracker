from datetime import timedelta
import logging

from homeassistant.util.dt import (utcnow, as_utc, parse_datetime)
from homeassistant.helpers.update_coordinator import (
  DataUpdateCoordinator
)

from ..const import (
  DOMAIN,

  DATA_WEEK_START,
  DATA_TIME_ENTRIES_COORDINATOR
)

from ..api_client import (HarvestApiClient)

from . import calculate_week_start

_LOGGER = logging.getLogger(__name__)

async def async_setup_time_entries_coordinator(hass, client: HarvestApiClient, account_id: str):
  """Create time entries coordinator"""

  async def async_update_data():
    """Fetch data from API endpoint."""
    current = utcnow()
    
    key = 'time_entries'
    period_from = calculate_week_start(current, hass.data[DOMAIN][account_id][DATA_WEEK_START] )
    period_to = (period_from + timedelta(weeks=1))

    try:
      hass.data[DOMAIN][account_id][key] = await client.async_get_time_entries(period_from, period_to)
    except:
      _LOGGER.debug('Failed to retrieve time entries')

    return hass.data[DOMAIN][account_id][key]

  hass.data[DOMAIN][account_id][DATA_TIME_ENTRIES_COORDINATOR] = DataUpdateCoordinator(
    hass,
    _LOGGER,
    name=f"time_entries",
    update_method=async_update_data,
    update_interval=timedelta(minutes=1),
  )

  return hass.data[DOMAIN][account_id][DATA_TIME_ENTRIES_COORDINATOR]