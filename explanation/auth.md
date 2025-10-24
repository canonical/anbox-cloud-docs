(exp-auth)=
# Authentication and authorization

## Identities

An identity in Anbox Cloud represents a user requiring access to resources in the Anbox Management Service (AMS) through its API endpoints. To get access to AMS and its resources, the identities first need to be added to AMS before they can make requests. Currently AMS supports OIDC and TLS identities.

```{note}
In earlier versions of Anbox Cloud before 1.28.0, the amc config trust add command was used to add a TLS identity.  Starting with the 1.28.0 release, the amc config trust add command is deprecated and replaced by the `amc auth identity` command.
```

## Authorization groups

An authorization group helps you manage multiple identities that need the same permissions together. When you assign a permission to an authorization group, all the identities that are part of that group inherit the permissions assigned to it.

AMS has a default authorization group called `admin`. This is an immutable group and cannot be removed. Use the `admin` authorization group to provide access to all objects and operations available within AMS.

## Permissions

Permissions define access for an authorization group. Permissions consist of three parts - *an entitlement*, *a resource type*, and optionally *a resource id*. 

There are two types of permissions:

**Global permissions** are a set of pre-defined permissions that can be assigned to a group to provide access to server level operations. In case of global permissions, the targeted resource name is `server`.   

**Resource permissions** help in providing entitlements to existing resources in AMS. For example, specific entitlements can be assigned at instance level to control what operations can be performed on that instance. The resource types can be any of these: *identity*, *group*, *addon*, *application*, *image*, *instance*, *node*.

The entitlements for resource permissions can be for all resource types in general or for a specific resource type. 

For a complete list of the global and resource level entitlements, see {ref}`ref-auth`.

## Methods of authorization

AMS uses OpenFGA to implement fine grained authorization for identities and authorization groups to manage user access to API endpoints and specific objects within the system.

AMS has two authorization modes:

**Basic authorization**, an authorization method in which only identities added to the admin group get unrestricted access to every resource within AMS. All existing authorization groups and their respective permissions are not evaluated when this method of authorization is used. This is the default method of authorization when fine grained authorization is not configured.

**Fine Grained authorization**, an advanced method of authorization in AMS which is enabled only if OpenFGA is configured within AMS. With this method, AMS scrutinizes permissions related to authorization groups using OpenFGA. 
When using this method, each user can be assigned specific permissions related to each individual object in AMS. For example, a user can be given access to only perform a read operation on a specific application within AMS.
