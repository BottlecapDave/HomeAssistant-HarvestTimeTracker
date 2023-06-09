# FAQ

- [FAQ](#faq)
  - [How do I increase the logs for the integration?](#how-do-i-increase-the-logs-for-the-integration)

## How do I increase the logs for the integration?

If you are having issues, it would be helpful to include Home Assistant logs as part of any raised issues. This can be done by setting the following values in your `configuration.yaml` file.

```yaml
logger:
  logs:
    custom_components.harvest_time_tracker: debug
```

If you don't have access to this file, then you should be able to set the log levels using the [available services](https://www.home-assistant.io/integrations/logger/).

Once done, you'll need to reload the integration and then check the "Full Home Assistant Log" from the `logs page`. You should then see entries associated with this component. These entries should be provided with any raised issues. Please remove an sensitive information before posting.