# [1.3.0](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/compare/v1.2.4...v1.3.0) (2025-03-08)


### Features

* Added ability to set a friendly name (1 hour dev time) ([cc88b81](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/cc88b812a5eb37afc874ff5012bdb23e73d14794))
* Added blueprint to add entries based on calendar events using AI (2 hours dev time) ([15f7786](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/15f77865f4c03a8f6e04604199530eb1dbfeb676))
* Added correct user agent for integration (5 minutes dev time) ([be10842](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/be1084265653709a0ba81059e4806a0a6af8517c))
* Added event entity which exposes all tasks that the account is assigned to (30 minutes dev time) ([ca7594f](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/ca7594f150b20631ea6ada1bc1d518cfe4d55f1f))

## [1.2.4](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/compare/v1.2.3...v1.2.4) (2024-10-05)


### Bug Fixes

* Fixed issue with migrating config entries from older versions of the integration ([b63e9c5](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/b63e9c5f4058f3775a0ce7448f95e5389f7c635c))

## [1.2.3](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/compare/v1.2.2...v1.2.3) (2024-09-22)


### Bug Fixes

* Fixed HA warning for registering an entity service with a non entity service schema (15 minutes dev time) ([3657a90](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/3657a9093ad08ed482a03289b38b0fcd09bffe00))

## [1.2.2](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/compare/v1.2.1...v1.2.2) (2024-08-07)


### Bug Fixes

* Fixed sensors displaying other users entries if the user has an admin or manager role (1.5 hours dev time) ([de7adfd](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/de7adfd3af031f55ae37beca86029871188f14a5))
* Removed entries from being saved in database due to size. They're still available in the UI and with automations ([b7f465e](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/b7f465e019eefb34d8f239193c71ccd06b04611c))

## [1.2.1](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/compare/v1.2.0...v1.2.1) (2024-08-05)


### Bug Fixes

* Fixed issue with 24 hour clock not having proceeding zero (15 minutes dev time) ([d7d7203](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/d7d72033773588f8ac5700c9a414914cc435cfea))

# [1.2.0](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/compare/v1.1.2...v1.2.0) (2024-08-03)


### Bug Fixes

* Fixed issue reading entries when company is configured to track via times (2 hours dev time) ([562dd41](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/562dd413072d0da85b609f7b0fb9a280ff680ff8))


### Features

* Added support for creating entries with start/end times (1.5 hours dev time) ([bf71f4c](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/bf71f4ca63306799c58c663152470d15d9b7e9ea))

## [1.1.2](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/compare/v1.1.1...v1.1.2) (2024-06-29)


### Bug Fixes

* Fixed warning around use of deprecated HA function (15 minutes dev time) ([b6e458b](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/b6e458b14e0613cd4c853661de6a13aa39f5a34a))

## [1.1.1](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/compare/v1.1.0...v1.1.1) (2024-01-13)


### Bug Fixes

* Added missing configuration translation ([68688cc](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/68688cc54625af684c98540df538cd659125ffc6))

# [1.1.0](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/compare/v1.0.1...v1.1.0) (2023-11-28)


### Features

* Added portuguese translations - Thanks @ViPeR5000 ([bc9b4b4](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/bc9b4b43840487b376cc65de410925c005106732))

## [1.0.1](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/compare/v1.0.0...v1.0.1) (2023-06-28)


### Bug Fixes

* Fixed default task to be in alphabetical order ([05b43ad](https://github.com/BottlecapDave/HomeAssistant-HarvestTimeTracker/commit/05b43adfaba9ab00bb2a605d634fe4d70929a641))

# 1.0.0 (2023-06-16)

Initial release
