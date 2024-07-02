(howto-ts-initial-setup)=
# Troubleshoot issues with initial setup

You might encounter the following issues while setting up your system.

## Juju hook installation failure

*Applies to: Anbox Cloud*

> Several Juju units of my deployment show `hook: installation failure`. Why?

You used the wrong Ubuntu Pro token. Using the Ubuntu Pro (Infra-only) token will result in a failed deployment.

To deploy Anbox Cloud, you need an Ubuntu Pro subscription. Using a different token will result in a failed deployment. This failure is currently not recoverable.

## Socket permission error for `amc`

*Applies to: Anbox Cloud*

> I receive the following socket permission error when trying to use the `amc` command:
>
> ```text
> Post http://unix/1.0/images: dial unix /var/snap/ams/common/server/unix.socket: connect: permission denied
> ```
>
> What is wrong?

Most likely, you are trying to run the `amc` command as a user that is not part of the `ams` group. The socket has its ownership set to `root:ams`, so that only `root` or users that are part of the `ams` group are allowed to use the Unix domain socket.

By default, Anbox Cloud automatically adds the `ubuntu` user to the `ams` group during the installation. You can manually add further users to the `ams` group with the following command:

    sudo gpasswd -a <user_name> ams

To apply the change, you might need to log out and back in.