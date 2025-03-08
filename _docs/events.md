# Events

The following events are fired as part of this integration

## Harvest Tasks Updated

`harvest_time_tracker_tasks_updated`

This event is fired when the harvest time tracker tasks have been retrieved from the API for a given account. This will fire regardless if the list of tasks has changed.

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