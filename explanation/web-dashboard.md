(exp-web-dashboard)=
# Anbox Cloud dashboard

The Anbox Cloud dashboard offers a web interface to create, manage and stream applications. The dashboard is especially helpful for developers new to Anbox Cloud and helps them by offering a simpler and intuitive management interface.

The dashboard comes pre-installed when you deploy the full version of Anbox Cloud (along with the streaming stack) or the Anbox Cloud appliance. It operates from behind a reverse proxy for performance and security reasons. The dashboard relies on OAuth for user authentication. The only OAuth provider supported right now is [Ubuntu One](https://login.ubuntu.com/).

## Dashboard views

The dashboard allows multiple views and management of various objects such as applications, instances and nodes to some extent. The operations available from the dashboard may be limited as compared to the CLI, however if you are new to the CLI, the dashboard can be a friendlier start to Anbox Cloud.

* Applications view - Allows creation, streaming and management of applications.
* Sessions view - Allows a list view of the sessions and their status.
* Instances view - Allows a detailed view of instances and the applications or images that they are created from, along with management options for the instances.
* Nodes view - Allows a list view of LXD nodes and their configuration details.

Apart from these views, the dashboard also allows you to work with the {ref}`exp-aar` and the {ref}`exp-ams`.

* Registry view - Allows a list view of applications uploaded to the registry.
* Configuration view - Allows you to edit the {ref}`ref-ams-configuration` attributes from the dashboard.

## Related topics

* {ref}`tut-installing-appliance`
* {ref}`howto-use-web-dashboard`
* {ref}`howto-deploy-anbox-juju`
