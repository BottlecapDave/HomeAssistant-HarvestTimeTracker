import voluptuous as vol
import homeassistant.helpers.config_validation as cv

DOMAIN = "harvest_time_tracker"

CONFIG_MAIN_API_KEY = "api_key"
CONFIG_MAIN_ACCOUNT_ID = "account_id"

DATA_SCHEMA_ACCOUNT = vol.Schema({
  vol.Required(CONFIG_MAIN_API_KEY): str,
  vol.Required(CONFIG_MAIN_ACCOUNT_ID): str,
})
