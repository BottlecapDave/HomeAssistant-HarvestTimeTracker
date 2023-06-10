"""Diagnostics support."""
import logging

from homeassistant.components.diagnostics import async_redact_data

from .const import (
  DOMAIN,
)

_LOGGER = logging.getLogger(__name__)

async def async_get_device_diagnostics(hass, config_entry, device):
    """Return diagnostics for a device."""
    return {}