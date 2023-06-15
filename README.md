# Home Assistant Harvest Time Tracker

![installation_badge](https://img.shields.io/badge/dynamic/json?color=41BDF5&logo=home-assistant&label=integration%20usage&suffix=%20installs&cacheSeconds=15600&url=https://analytics.home-assistant.io/custom_integrations.json&query=$.harvest_time_tracker.total)

- [Home Assistant Harvest Time Tracker](#home-assistant-harvest-time-tracker)
  - [How to install](#how-to-install)
    - [HACS](#hacs)
    - [Manual](#manual)
  - [How to setup](#how-to-setup)
  - [Services](#services)
    - [Service harvest\_time\_tracker.add\_time\_with\_hours](#service-harvest_time_trackeradd_time_with_hours)
  - [FAQ](#faq)

Custom component to allow you to interact with your [Harvest](https://www.getharvest.com/) account. 

This integration is in no way affiliated with Harvest.

## How to install

There are multiple ways of installing the integration.

### HACS

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

This integration can be installed directly via HACS. To install:

* [Add the repository](https://my.home-assistant.io/redirect/hacs_repository/?owner=BottlecapDave&repository=homeassistant-harvesttimetracker&category=integration) to your HACS installation
* Click `Download`

### Manual

You should take the latest [published release](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/releases). The current state of `develop` will be in flux and therefore possibly subject to change.

To install, place the contents of `custom_components` into the `<config directory>/custom_components` folder of your Home Assistant installation. Once installed, don't forget to restart your home assistant instance for the integration to be picked up.

## How to setup

Please follow the [setup guide](./_docs/setup_account.md) to setup your initial account. This will include a few sensors be default depending on your account.

## Services

### Service harvest_time_tracker.add_time_with_hours

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
            project_id: 9012
            task_id: 3456
            date: >
              {{ (trigger.calendar_event.end | as_datetime).strftime("%Y-%m-%d") }}
            hours: >
              {{ ((trigger.calendar_event.end | as_datetime | as_timestamp) - (trigger.calendar_event.start | as_datetime | as_timestamp)) / 60 / 60 }}
            notes: >
              {{ trigger.calendar_event.summary }}
          target:
            entity_id: sensor.harvest_time_tracker_XXX_hours_today
```

## FAQ

Before raising anything, please read through the [faq](./_docs/faq.md). If you have found a bug or have a feature request please [raise it](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/issues) using the appropriate report template.