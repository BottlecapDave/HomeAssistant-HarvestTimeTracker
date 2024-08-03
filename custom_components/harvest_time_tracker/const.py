import voluptuous as vol
import homeassistant.helpers.config_validation as cv

DOMAIN = "harvest_time_tracker"

CONFIG_MAIN_API_KEY = "api_key"
CONFIG_MAIN_ACCOUNT_ID = "account_id"
CONFIG_MAIN_WEEK_START = "week_start"

DATA_API_CLIENT = "api_client"
DATA_WEEK_START = "week_start"

DATA_TIME_ENTRIES_COORDINATOR = "time_entries_coordinator"

DATA_SCHEMA_ACCOUNT = vol.Schema({
  vol.Required(CONFIG_MAIN_API_KEY): str,
  vol.Required(CONFIG_MAIN_ACCOUNT_ID): str,
  vol.Required(CONFIG_MAIN_WEEK_START): vol.In({
    "Saturday": "Saturday",
    "Sunday": "Sunday",
    "Monday": "Monday"
  }),
})

REGEX_DATE = "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
REGEX_TIME_WITH_SECONDS = "^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$"
REGEX_HOURS = "^[0-9]+(\\.[0-9]+)*$"