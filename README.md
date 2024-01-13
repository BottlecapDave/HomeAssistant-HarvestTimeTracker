# Home Assistant Harvest Time Tracker

![installation_badge](https://img.shields.io/badge/dynamic/json?color=41BDF5&logo=home-assistant&label=integration%20usage&suffix=%20installs&cacheSeconds=15600&url=https://analytics.home-assistant.io/custom_integrations.json&query=$.harvest_time_tracker.total) [![](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/bottlecapdave)

- [Home Assistant Harvest Time Tracker](#home-assistant-harvest-time-tracker)
  - [How to install](#how-to-install)
    - [HACS](#hacs)
    - [Manual](#manual)
  - [How to setup](#how-to-setup)
  - [Docs](#docs)
  - [FAQ](#faq)
  - [Sponsorship](#sponsorship)

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

Please follow the [setup guide](https://bottlecapdave.github.io/HomeAssistant-HarvestTimeTracker/setup/account) to setup the integration. This guide details the configuration, along with the sensors that will be available to you.

## Docs

To get full use of the integration, please visit the [docs](https://bottlecapdave.github.io/HomeAssistant-HarvestTimeTracker/).

## FAQ

Before raising anything, please read through the [faq](https://bottlecapdave.github.io/HomeAssistant-HarvestTimeTracker/faq.md). If you have found a bug or have a feature request please [raise it](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/issues) using the appropriate report template.

## Sponsorship

If you are enjoying this integration, why not make a one off or monthly [GitHub sponsorship](https://github.com/sponsors/bottlecapdave).
