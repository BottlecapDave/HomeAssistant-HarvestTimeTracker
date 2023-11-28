# Services

- [Services](#services)
  - [Service harvest\_time\_tracker.add\_time\_with\_hours](#service-harvest_time_trackeradd_time_with_hours)


## Service harvest_time_tracker.add_time_with_hours

Service for adding a time entry by specifying hours instead of time period.

| Attribute                | Optional | Description                                                                                                           |
| ------------------------ | -------- | --------------------------------------------------------------------------------------------------------------------- |
| `target.entity_id`       | `no`     | The name of the sensor for the account the time entry will be added to. This should be your day or week sensor        |
| `data.project_id`        | `no`     | The id of the project the entry should be logged against                                                              |
| `data.task_id`           | `no`     | The id of the task the entry should be logged against                                                                 |
| `data.date`              | `no`     | The date the entry is for. This should be in the format `YYYY-MM-DD`                                                  |
| `data.hours`             | `no`     | The hours to be logged in the entry                                                                                   |
| `data.notes`             | `yes`    | The optional notes to add to the entry                                                                                |

This can be used via automations in the following way.

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