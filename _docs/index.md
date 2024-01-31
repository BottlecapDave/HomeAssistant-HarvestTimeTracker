# Home Assistant Harvest Time Tracker

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

Please follow the [setup guide](./setup.md) to setup your initial account. This will include a few sensors be default depending on your account.

## Entities

The full list of entities that will be created once you've setup your account can be found in the [entities section](./entities.md).

## Services

The full list of available services can be found [here](./services.md).

## FAQ

Before raising anything, please read through the [faq](./faq.md). If you have found a bug or have a feature request please [raise it](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/issues) using the appropriate report template.

## Sponsorship

Please see the [sponsorship](./sponsorship.md) page for more information.