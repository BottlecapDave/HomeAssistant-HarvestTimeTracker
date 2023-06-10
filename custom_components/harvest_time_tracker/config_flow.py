import voluptuous as vol
import logging

from homeassistant.config_entries import (ConfigFlow, OptionsFlow)
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv

from .const import (
  DOMAIN,
  
  CONFIG_MAIN_API_KEY,
  CONFIG_MAIN_ACCOUNT_ID,
  
  DATA_SCHEMA_ACCOUNT,
)

from .api_client import HarvestApiClient

_LOGGER = logging.getLogger(__name__)

class HarvestTimeTrackerConfigFlow(ConfigFlow, domain=DOMAIN): 
  """Config flow."""

  VERSION = 1

  async def async_setup_initial_account(self, user_input):
    """Setup the initial account based on the provided user input"""
    errors = {}

    # client = HarvestApiClient(user_input[CONFIG_MAIN_API_KEY], user_input[CONFIG_MAIN_ACCOUNT_ID])
    # account_info = await client.async_get_account(user_input[CONFIG_MAIN_ACCOUNT_ID])
    # if (account_info is None):
    #   errors[CONFIG_MAIN_ACCOUNT_ID] = "account_not_found"
    #   return self.async_show_form(
    #     step_id="user", data_schema=DATA_SCHEMA_ACCOUNT, errors=errors
    #   )

    # Setup our basic sensors
    return self.async_create_entry(
      title="Account", 
      data=user_input
    )

  async def async_step_user(self, user_input):
    """Setup based on user config"""

    if user_input is not None:
      # We are setting up our initial stage
      if CONFIG_MAIN_API_KEY in user_input:
        return await self.async_setup_initial_account(user_input)

    return self.async_show_form(
      step_id="user", data_schema=DATA_SCHEMA_ACCOUNT
    )

  @staticmethod
  @callback
  def async_get_options_flow(entry):
    return OptionsFlowHandler(entry)

class OptionsFlowHandler(OptionsFlow):
  """Handles options flow for the component."""

  def __init__(self, entry) -> None:
    self._entry = entry

  async def async_step_init(self, user_input):
    """Manage the options for the custom component."""

    if CONFIG_MAIN_API_KEY in self._entry.data:
      config = dict(self._entry.data)
      if self._entry.options is not None:
        config.update(self._entry.options)

      return self.async_show_form(
        step_id="user", data_schema=vol.Schema({
          vol.Required(CONFIG_MAIN_API_KEY, default=config[CONFIG_MAIN_API_KEY]): str
        })
      )

    return self.async_abort(reason="not_supported")

  async def async_step_user(self, user_input):
    """Manage the options for the custom component."""

    if user_input is not None:
      config = dict(self._entry.data)
      config.update(user_input)

      return self.async_create_entry(title="", data=config)

    return self.async_abort(reason="not_supported")