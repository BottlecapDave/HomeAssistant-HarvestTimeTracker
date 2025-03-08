# Entities

The following entities are available when setting up your account.

## Daily Hours

`sensor.harvest_time_tracker_{ACCOUNT_ID/NAME}_hours_today`

This sensor will present the total hours for today for the user associated with the configured API key.

| Attribute Name | type | Note |
|----------------|------|------|
| `account_id` | `string` | The id of the account this sensor is for |
| `entries` | `list` | The entries that added up to todays total |

Each entry has the following attributes

| Attribute Name | type | Note |
|----------------|------|------|
| `id` | `string` | The id of the entry |
| `client_id` | `string` | The id of the client the entry belongs to |
| `client_name` | `string` | The name of the client the entry belongs to |
| `project_id` | `string` | The id of the project this sensor is for |
| `project_name` | `string` | The name of the project the entry belongs to |
| `task_id` | `string` | The id of the task the entry belongs to|
| `task_name` | `string` | The name of the task the entry belongs to |
| `hours` | `float` | The hours logged for the entry |
| `start` | `datetime` | The start date of the entry. This will always have a time of midnight |
| `end` | `datetime` | The end date of the entry. This will always have a time of midnight. If this is for the same day, this will have the same value as `start` |
| `notes` | `string` | Any notes attached to the entry |

## Weekly Hours

`sensor.harvest_time_tracker_{ACCOUNT_ID/NAME}_hours_week`

This sensor will present the total hours for the week for the user associated with the configured API key. The week will start from the day you elected as your week start when configuring the integration.

| Attribute Name | type | Note |
|----------------|------|------|
| `account_id` | `string` | The id of the account this sensor is for |
| `entries` | `list` | The entries that added up to todays total |

Each entry has the following attributes

| Attribute Name | type | Note |
|----------------|------|------|
| `id` | `string` | The id of the entry |
| `client_id` | `string` | The id of the client the entry belongs to |
| `client_name` | `string` | The name of the client the entry belongs to |
| `project_id` | `string` | The id of the project this sensor is for |
| `project_name` | `string` | The name of the project the entry belongs to |
| `task_id` | `string` | The id of the task the entry belongs to|
| `task_name` | `string` | The name of the task the entry belongs to |
| `hours` | `float` | The hours logged for the entry |
| `start` | `datetime` | The start date of the entry. This will always have a time of midnight |
| `end` | `datetime` | The end date of the entry. This will always have a time of midnight. If this is for the same day, this will have the same value as `start` |
| `notes` | `string` | Any notes attached to the entry |

## Default Task

`select.harvest_time_tracker_{ACCOUNT_ID/NAME}_default_task`

This select sensor is used to select a default assigned task which can then be used in automations (see [service example](./services.md#service-harvest_time_trackeradd_time_with_hours)).

| Attribute Name | type | Note |
|----------------|------|------|
| `account_id` | `string` | The id of the account this sensor is for |
| `client_id` | `string` | The id of the client that the selected task belongs to |
| `client_name` | `string` | The name of the client that the selected task belongs to |
| `project_id` | `string` | The id of the project that the selected task belongs to |
| `project_name` | `string` | The name of the project that the selected task belongs to |
| `task_id` | `string` | The id of the selected task |
| `task_name` | `string` | The name of the selected task |

## Tasks

`event.harvest_time_tracker_{ACCOUNT_ID/NAME}_tasks`

This event sensor is used to see all of your assigned tasks and select one which can be used as a default in automations (see [service example](./services.md#service-harvest_time_trackeradd_time_with_hours)).

| Attribute Name | type | Note |
|----------------|------|------|
| `account_id` | `string` | The id of the account this sensor is for |
| `tasks`      | `list` | The list of tasks assigned to the user |

For each task, the following attributes are available

| Attribute Name | type | Note |
|----------------|------|------|
| `id` | `string` | The id of the task |
| `name` | `string` | The name of the task |
| `project_id` | `string` | The id of the project the task belongs to |
| `project_name` | `string` | The name of the project the task belongs to |
| `client_id` | `string` | The id of the client the task belongs to |
| `client_name` | `string` | The name of the client the task belongs to |