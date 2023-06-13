# Setup Account

- [Setup Account](#setup-account)
  - [Sensors](#sensors)
    - [Daily Hours](#daily-hours)
    - [Weekly Hours](#weekly-hours)

Setup is done entirely via the [integration UI](https://my.home-assistant.io/redirect/config_flow_start/?domain=harvest_time_tracker).


## Sensors

When you setup your account, you will get the following sensors

### Daily Hours

`sensor.harvest_time_tracker_{ACCOUNT_ID}_hours_today`

This sensor will present the total hours for today.

| Attribute Name | Note |
|----------------|------|
| `entries` | The entries that added up to todays total |

### Weekly Hours

`sensor.harvest_time_tracker_{ACCOUNT_ID}_hours_week`

This sensor will present the total hours for the week, starting from the day you elected as your week start.

| Attribute Name | Note |
|----------------|------|
| `entries` | The entries that added up to todays total |