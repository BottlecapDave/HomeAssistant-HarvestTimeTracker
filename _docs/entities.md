# Entities

- [Entities](#entities)
  - [Daily Hours](#daily-hours)
  - [Weekly Hours](#weekly-hours)
  - [Default Task](#default-task)

The following entities are available when setting up your account.

## Daily Hours

`sensor.harvest_time_tracker_{ACCOUNT_ID}_hours_today`

This sensor will present the total hours for today.

| Attribute Name | Note |
|----------------|------|
| `account_id` | The id of the account this sensor is for |
| `entries` | The entries that added up to todays total |

## Weekly Hours

`sensor.harvest_time_tracker_{ACCOUNT_ID}_hours_week`

This sensor will present the total hours for the week, starting from the day you elected as your week start.

| Attribute Name | Note |
|----------------|------|
| `account_id` | The id of the account this sensor is for |
| `entries` | The entries that added up to todays total |

## Default Task

`select.harvest_time_tracker_{ACCOUNT_ID}_default_task`

This select sensor is used to see all of your assigned tasks and select one which can be used as a default in automations (see [service example](../services.md#service-harvest_time_trackeradd_time_with_hours)).

| Attribute Name | Note |
|----------------|------|
| `account_id` | The id of the account this sensor is for |
| `client_id` | The id of the client that the selected task belongs to |
| `client_name` | The name of the client that the selected task belongs to |
| `project_id` | The id of the project that the selected task belongs to |
| `project_name` | The name of the project that the selected task belongs to |
| `task_id` | The id of the selected task |
| `task_name` | The name of the selected task |
