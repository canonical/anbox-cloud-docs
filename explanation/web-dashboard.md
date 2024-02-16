The Anbox Cloud dashboard offers a web interface to create, manage and stream applications. The dashboard is especially helpful for developers new to Anbox Cloud and helps them by offering a simpler and intuitive management interface.

The dashboard comes pre-installed when you deploy the full version of Anbox Cloud (along with the streaming stack) or the Anbox Cloud appliance. It operates from behind a reverse proxy for performance and security reasons. The dashboard relies on OAuth for user authentication. The only OAuth provider supported right now is [Ubuntu One](https://login.ubuntu.com/).

## Dashboard views

The dashboard allows multiple views and management of various objects such as applications, instances and nodes to some extent. The operations available from the dashboard may be limited as compared to the CLI, however if you are new to the CLI, the dashboard can be a friendlier start to Anbox Cloud.

* Applications view - Allows creation, streaming and management of applications.
* Sessions view - Allows a list view of the sessions and their status.
* Instances view - Allows a detailed view of instances and the applications or images that they are created from, along with management options for the instances.
* Nodes view - Allows a list view of LXD nodes and their configuration details.

Apart from these views, the dashboard also allows you to work with the [Anbox Application Registry (AAR)](https://discourse.ubuntu.com/t/anbox-application-registry-aar/17761) and the [Anbox Management Service (AMS)](https://discourse.ubuntu.com/t/anbox-management-service-ams/24321).

* Registry view - Allows a list view of applications uploaded to the registry.
* Configuration view - Allows you to edit the [AMS configuration](https://discourse.ubuntu.com/t/ams-configuration/20872) attributes from the dashboard.

## Related information

* [How to use the web dashboard](https://discourse.ubuntu.com/t/20871)
* [Install Anbox Cloud](https://discourse.ubuntu.com/t/17744)
* [Install Anbox Cloud Appliance](https://discourse.ubuntu.com/t/22681)
