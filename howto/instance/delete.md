(howto-delete-instance)=
# How to delete an instance

An instance can be deleted, which will cause any connected user to be disconnected immediately. The following command deletes a single instance:

    amc delete <instance_id>

Provide the ID of the instance that you want to delete.

In some cases, it is helpful to delete all instances currently available.
The `amc` command provides a `--all` flag for this, but be careful with this!

    amc delete --all
