(exp-nodes)=
# Nodes

A node is a machine in the LXD cluster. Depending on whether it is running the management components of Anbox Cloud or streaming services, the node can serve multiple purposes such as a control node, worker node etc. The Anbox Management Service(AMS) hosts metadata that is necessary for its functioning on the nodes.

## Possible node statuses

The following table lists the different statuses that a node can have depending on its state and what each status means:

| Image status | Description |
|--------------------|-------------|
| `created` | The node is successfully created and ready to be used. |
| `initializing` | The status of the node when its corresponding LXD instance is currently being configured. |
| `initialized` | The status of the node after its corresponding LXD instance is initialized. |
| `online` | The node is available and can be used by the AMS. |
| `offline` | The node is not available and cannot be used by the AMS. |
| `deleted` | The node has been deleted and no longer available for use. |
| `error` | The node cannot be used because of an error. |
| `unknown` | A possible error occurred and the real state of the node cannot be determined. |

If you encounter the `error` or the `unknown` status, [file a bug](https://bugs.launchpad.net/anbox-cloud).
