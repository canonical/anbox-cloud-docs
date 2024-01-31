The `amc wait` command instructs AMS to wait for an application to reach a specific condition. If the condition is not satisfied within the specified time (five minutes by default), a timeout error will be returned by AMS.

The supported conditions for an application are as follows:

Name            |  Value
----------------|------------
`instance-type` |  Supported instance type. See [Instance types](https://discourse.ubuntu.com/t/application-manifest/24197#instance-type-1) for a list of available instance types. This attribute is deprecated since 1.20 and will be removed in future releases.
`addons`        |  Comma-separated list of addons.
`tag`           |  Application tag name (deprecated, use `tags` instead).
`tags`          |  Comma-separated list of tags.
`published`     |  "true" or "false" indicating whether the application is published.
`immutable`     |  "true" or "false" indicating whether the application is changeable.
`status`        |  Application status, possible values: `error`, `unknown`, `initializing`, `ready`, `deleted`

One example of using the `amc wait` command is to wait for the application [bootstrap process](https://discourse.ubuntu.com/t/managing-applications/17760#bootstrap-process-2) to be done, since the application bootstrap is performed asynchronously by the AMS service and takes some time to process. The application cannot be used until the bootstrap is complete and the status is marked as `ready`.

    amc wait -c status=ready bcmap7u5nof07arqa2ag
