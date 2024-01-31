To list all available applications, use the following command:

    amc application ls

## Filter applications

By default, `amc application ls` shows all applications. If you want to search for specific types of applications, e.g. only show a group of applications with a particular tag, you can use the `--filter` flag to filter and group applications.

The filter flag accepts a key-value pair as input for the filter. The following attributes are valid keys:

Name            |  Value
----------------|------------
`instance-type` |  Supported instance type. See [Instance types](https://discourse.ubuntu.com/t/application-manifest/24197#instance-type-1) for a list of available instance types. This attribute is deprecated since 1.20 and will be removed in future releases.
`addons`        |  Comma-separated list of addons.
`tag`           |  Application tag name (deprecated, use `tags` instead).
`tags`          |  Comma-separated list of tags.
`published`      |  "true" or "false" indicating whether the application is published.
`immutable`     |  "true" or "false" indicating whether the application is changeable.
`status`        |  Application status, possible values: `error`, `unknown`, `initializing`, `ready`, `deleted`

To list all applications with a tag called "game":

    amc application ls --filter tags=game

To apply multiple filters, pass multiple flags:

    amc application ls --filter published=true --filter tags=game

This will query all published applications that have the tag "game".
