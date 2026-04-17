---
html_meta:
  description: Share a session. A session in Anbox Cloud denotes the streaming session
    of an Anbox instance. Each session of an instance can be shared up to a maximum
    of 5.
---
(howto-share-session)=
# Share a session

A session in Anbox Cloud denotes the streaming session of an Anbox instance. Each session of an instance can be shared up to a maximum of 5 times. By default, each share will expire after 12 hours, with a maximum allowed duration of 30 days per share.

```{note}
This guide demonstrates the steps using the appliance deployment. If you are using the charmed deployment, use `anbox-stream-gateway` instead of `anbox-cloud-appliance.gateway` in the commands.
```

When you have a running instance with streaming enabled, use:

    sudo anbox-cloud-appliance.gateway session share <session_id> --description="share with John Doe"

A share of the session with `<session_id>` is created. 

When you have many such shares for various purposes, you may want to update or revoke a session share. To do that, first identify the ID of the share:

    sudo anbox-cloud-appliance.gateway share list --session-id=<session_id>

Notice that the description you provide at the time of creating the share helps in identification.

To update the expiry, run:

    anbox-stream-gateway share update <share_id> --expiry=24h

The `--expiry` flag accepts values in these formats:

- A relative duration such as 24h or 30m, calculated from the current time
- A date-only string in the format `YYYY-MM-DD`
- A date-time string in the format `YYYY-MM-DD HH:MM:SS`

To update the description, run:

    anbox-stream-gateway share update <share_id> --description=new_description

To revoke a share, run:

    anbox-stream-gateway share delete <share_id>
