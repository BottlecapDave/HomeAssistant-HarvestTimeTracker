# Setup

Setup is done entirely via the [integration UI](https://my.home-assistant.io/redirect/config_flow_start/?domain=harvest_time_tracker).

You can do this for as many accounts as you would like.

## Name

A friendly name to help identify the account. This is optional, and if not supplied the `account_id` will be used.

## Personal access token

This can be obtained on the [Harvest website](https://id.getharvest.com/oauth2/access_tokens/new).

## Account Id

The id of the account this setup is for. This is associated with your personal access token.

## Start of the week

This is the day that determines the start of the week for the account. This will be used in weekly calculations.

## Entities

The full list of entities can be found in the [entities section](./entities.md).