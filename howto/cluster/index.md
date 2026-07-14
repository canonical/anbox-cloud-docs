---
myst:
  html_meta:
    "description": "How to manage an Anbox Cloud LXD cluster, including adding nodes, configuring capacity, and scaling up or down."
---

(howto-manage-cluster)=
# Manage cluster nodes

```{important}
Clustering is supported only for charmed Anbox Cloud deployments. The Anbox Cloud Appliance does not support clustering.
```

These guides describe how to distribute the load of your Anbox Cloud installation over several machines in a cluster. See {ref}`exp-clustering` for an introduction to how clustering works.

- {ref}`howto-configure-cluster-nodes`
- {ref}`howto-scale-up-cluster`
- {ref}`howto-scale-down-cluster`

```{toctree}
:hidden:

configure-nodes
Scale down <scale-down>
Scale up <scale-up>
```
