(ref-auth)=
# Authentication and authorization

## Global entitlements

This table lists the entitlements that can be assigned at a global level.

| Entitlement | Description |
|--------------|------------|
| `admin` | Provides unrestricted access to all resources in AMS |
| `can_view_config` | Allows requests to `GET /1.0/config` |
| `can_edit_config` | Allows requests to `PATCH /1.0/config`  |
| `can_view_tasks` | Allows requests to `GET /1.0/tasks` |
| `can_view_metrics` | Allows requests to `GET /1.0/metrics` |
| `can_view_registry_applications` | Allows requests to `GET /1.0/registry/applications` |
| `can_delete_registry_applications` | Allows requests to `DELETE /1.0/registry/applications/<id>` |
| `can_push_registry_applications` | Allows requests to `POST /1.0/registry/applications/<id>/push` |
| `can_pull_registry_applications` | Allows requests to `POST /1.0/registry/applications/<id>/pull`  |
| `can_create_addons` | Allows requests to `POST /1.0/addons`  |
| `can_create_groups` | Allows requests to `POST /1.0/auth/groups` |
| `can_create_applications` | Allows requests to `POST /1.0/applications` |
| `can_create_instances` | Allows requests to:<br/> `POST /1.0/instances`<br/>`POST /1.0/containers`  |
| `can_create_nodes` | Allows requests to `POST /1.0/nodes`  |
| `can_create_images` | Allows requests to `POST /1.0/images` |
| `can_view_operations` | Allows requests to:<br/> `GET /1.0/operations`<br/>`GET /1.0/operations/<id>`<br/>`GET /1.0/operations/<id>/wait`<br/>`DELETE /1.0/operations/<id>`  |

## Resource level entitlements

This table lists the resource types and their endpoints that can be assigned resource level permissions.

| Resource type | End point |
| ---- | ---- |
| identity | `/1.0/auth/identities/<id> `|
| group | `/1.0/auth/groups/<id>` |
| addon | `/1.0/addons/<id>` |
| application | `/1.0/applications/<id>` |
| image | `/1.0/images/<id>` |
| instance | `/1.0/instances/<id>`, `/1.0/containers/<id>` |
| node | `/1.0/nodes/<id>` |

The following entitlements define the level of access an identity or group has to resources and they are available across all resource types:

| Entitlement | Description  | Allowed HTTP methods  |
| ---- | ---- | --- |
| `can_edit`  | Grants permission to modify existing resources. | PATCH, PUT |
| `can_view`  | Grants permission to retrieve or read resource data.  | GET |
| `can_delete` | Grants permission to remove resources. | DELETE |

The following entitlements are available only for specific resource types:

| Resource type | Entitlement | Description | Allowed HTTP methods and endpoints |
| ---- | ---- | ---- | ---- |
| instance | `can_view_logs` | Grants permission to view instance or container logs. | `GET /1.0/instances/{id}/logs`<br/>`GET /1.0/instances/{id}/logs/{name}`<br/>`GET /1.0/containers/{id}/logs`<br/> `GET /1.0/containers/{id}/logs/{name}`  |
| instance | `can_exec` | Grants permission to execute commands within an instance or container. | `POST /1.0/instances/{id}/exec`<br/>`POST /1.0/containers/{id}/exec` |
| application | `can_publish`  | Grants permission to publish or update an application version. | `PATCH /1.0/applications/{id}/{version}`  |
