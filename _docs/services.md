# Services

## add_time_with_hours

Adds a new time entry specified with hours. You should only use this method to create time entries when your account is configured to track time via duration.

| Attribute                | Optional | Description                                                                                                           |
| ------------------------ | -------- | --------------------------------------------------------------------------------------------------------------------- |
| `target.entity_id`       | `no`     | The name of the sensor for the account the time entry will be added to. This should be your day or week sensor        |
| `data.project_id`        | `no`     | The id of the project the entry should be logged against                                                              |
| `data.task_id`           | `no`     | The id of the task the entry should be logged against                                                                 |
| `data.date`              | `no`     | The date the entry is for. This should be in the format `YYYY-MM-DD`                                                  |
| `data.hours`             | `no`     | The hours to be logged in the entry                                                                                   |
| `data.notes`             | `yes`    | The optional notes to add to the entry                                                                                |

### Automation Example

Below is an example of adding an entry to a specific task when a calendar event with certain text ends. The entry has the hours of the calendar event. If the calendar entry is for something else, we add an entry to our elected default task.

```yaml
automations:
  - alias: Work - Timesheet
    trigger:
    - platform: calendar
      event: end
      entity_id: calendar.work
    condition:
    - condition: state
      entity_id: group.is_working
      state: 'on'
    action:
    - choose:
      - conditions:
        - condition: template
          value_template: >
            {{ "Client X" in trigger.calendar_event.summary }}
        sequence:
        - service: harvest_time_tracker.add_time_with_hours
          data:
            project_id: 1234
            task_id: 5678
            date: >
              {{ (trigger.calendar_event.end | as_datetime).strftime("%Y-%m-%d") }}
            hours: >
              {{ ((trigger.calendar_event.end | as_datetime | as_timestamp) - (trigger.calendar_event.start | as_datetime | as_timestamp)) / 60 / 60 }}
            notes: >
              {{ trigger.calendar_event.summary }}
          target:
            entity_id: sensor.harvest_time_tracker_XXX_hours_today
      default:
        - service: harvest_time_tracker.add_time_with_hours
          data:
            project_id: >
              {{ state_attr('select.harvest_time_tracker_XXX_default_task', 'project_id') }}
            task_id: >
              {{ state_attr('select.harvest_time_tracker_XXX_default_task', 'task_id') }}
            date: >
              {{ (trigger.calendar_event.end | as_datetime).strftime("%Y-%m-%d") }}
            hours: >
              {{ ((trigger.calendar_event.end | as_datetime | as_timestamp) - (trigger.calendar_event.start | as_datetime | as_timestamp)) / 60 / 60 }}
            notes: >
              {{ trigger.calendar_event.summary }}
          target:
            entity_id: sensor.harvest_time_tracker_XXX_hours_today
```

## add_time_with_start_end_times

Adds a new time entry specified with start/end times. You should only use this method to create time entries when your account is configured to track time via start and end time.

| Attribute                | Optional | Description                                                                                                           |
| ------------------------ | -------- | --------------------------------------------------------------------------------------------------------------------- |
| `target.entity_id`       | `no`     | The name of the sensor for the account the time entry will be added to. This should be your day or week sensor        |
| `data.project_id`        | `no`     | The id of the project the entry should be logged against                                                              |
| `data.task_id`           | `no`     | The id of the task the entry should be logged against                                                                 |
| `data.date`              | `no`     | The date the entry is for. This should be in the format `YYYY-MM-DD`                                                  |
| `data.start_time`        | `no`     | The time the entry started                                                                                            |
| `data.end_time`          | `no`     | The time the entry ended                                                                                              |
| `data.notes`             | `yes`    | The optional notes to add to the entry                                                                                |

### Automation Example

Below is an example of adding an entry to a specific task when a calendar event with certain text ends. The entry has the start/end of the calendar event. If the calendar entry is for something else, we add an entry to our elected default task.

```yaml
automations:
  - alias: Work - Timesheet
    trigger:
    - platform: calendar
      event: end
      entity_id: calendar.work
    condition:
    - condition: state
      entity_id: group.is_working
      state: 'on'
    action:
    - choose:
      - conditions:
        - condition: template
          value_template: >
            {{ "Client X" in trigger.calendar_event.summary }}
        sequence:
        - service: harvest_time_tracker.add_time_with_start_end_times
          data:
            project_id: 1234
            task_id: 5678
            date: >
              {{ (trigger.calendar_event.end | as_datetime).strftime("%Y-%m-%d") }}
            start_time: >
              {{ (trigger.calendar_event.start | as_datetime).strftime("%H:%M") }}
            end_time: >
              {{ (trigger.calendar_event.end | as_datetime).strftime("%H:%M") }}
            notes: >
              {{ trigger.calendar_event.summary }}
          target:
            entity_id: sensor.harvest_time_tracker_XXX_hours_today
      default:
        - service: harvest_time_tracker.add_time_with_start_end_times
          data:
            project_id: >
              {{ state_attr('select.harvest_time_tracker_XXX_default_task', 'project_id') }}
            task_id: >
              {{ state_attr('select.harvest_time_tracker_XXX_default_task', 'task_id') }}
            date: >
              {{ (trigger.calendar_event.end | as_datetime).strftime("%Y-%m-%d") }}
            start_time: >
              {{ (trigger.calendar_event.start | as_datetime).strftime("%H:%M") }}
            end_time: >
              {{ (trigger.calendar_event.end | as_datetime).strftime("%H:%M") }}
            notes: >
              {{ trigger.calendar_event.summary }}
          target:
            entity_id: sensor.harvest_time_tracker_XXX_hours_today
```