---
myst:
  html_meta:
    "description": "Explanation of Anbox Cloud concepts, covering architecture, components, applications, instances, security, capacity planning, and deployment."
---

(explanation)=
# Explanation

These topics explain how Anbox Cloud works, what its components do, and how they fit together.

## Architecture and components

The underlying architecture of Anbox Cloud, its variants and how the different components of Anbox Cloud relate to each other.

- {ref}`exp-anbox-cloud`
- {ref}`exp-ams`
- {ref}`exp-web-dashboard`
- {ref}`exp-aar`
- {ref}`exp-nodes`
- {ref}`exp-clustering`

## Workloads

Applications, images, instances, and projects for running and managing Android workloads.

- {ref}`exp-android-execution-models`
- {ref}`exp-images`
- {ref}`exp-custom-images`
- {ref}`exp-applications`
- {ref}`exp-instances`
- {ref}`exp-projects`
- {ref}`exp-addons`
- {ref}`AAOS <exp-aaos>`

## Rendering and streaming

The streaming stack, multi-display support, and the architecture behind graphics rendering in Anbox Cloud.

- {ref}`exp-application-streaming`
- {ref}`exp-multi-display`
- {ref}`exp-rendering-graphics`
- {ref}`exp-rendering-architecture`
- {ref}`exp-platforms`

## Security and access control

Isolation, cryptography, authentication and authorization mechanisms that protect your deployment and control access to its resources.

- {ref}`Security <exp-security>`
- {ref}`exp-auth`

## Deployment planning and performance

Resource requirements, capacity considerations, and factors that affect deployment performance.

- {ref}`exp-production-planning`
- {ref}`exp-resources-presets`
- {ref}`exp-capacity-planning`
- {ref}`exp-performance`

If you are new to Anbox Cloud, start with the {ref}`tutorials` for step-by-step instructions.
For operational tasks, see the {ref}`how-to-guides`.
For technical details, see the {ref}`reference`.

```{toctree}
:hidden:

addons
aar
android-execution-models
anbox-cloud
web-dashboard
ams
AAOS <aaos>
applications
application-streaming
multi-display
auth
capacity-planning
clustering
security/index
custom-images
images
instances
nodes
performance
production-planning
projects
rendering-architecture
rendering-graphics
resources
platforms
```
