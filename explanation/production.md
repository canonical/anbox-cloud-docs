When you are planning a production deployment, you should consider the aspects that you want to customise for best results. This topic covers the most common and important requirements when you are planning to move your Anbox Cloud deployment to production. While there could be other specifically tailored needs, this topic helps you identify your basic requirements and deployment strategy.

## Compute resource requirements 

Depending on your workload and the type of deployment you choose, hardware or cloud resource requirements can differ. See [requirements](https://discourse.ubuntu.com/t/requirements/17734) to get an idea about the kind of resources that are required to run a full Anbox Cloud deployment with the streaming stack or a minimal core version of the deployment without the streaming stack. 

You should pay special attention to the hardware requirements of applications that are used but not maintained by Anbox Cloud. 

## Software requirements 

Anbox Cloud deployments require the Ubuntu operating system. You should consider the Ubuntu OS, LXD, and Juju versions supported by Anbox Cloud for a production deployment. See [requirements](https://discourse.ubuntu.com/t/requirements/17734) to see compatible software versions.

## Networking requirements 

Consider the following questions to decide your networking requirements:

* In your deployment, how should your network structure and topology look like?
* Do you need subnets? If yes, what is the range of the subnets that you want to define?
* Do you require a virtual network and plan Juju spaces on top of it?
* Where is your Anbox Application Registry (AAR) deployed? How will the AMS in other clusters connect to AAR? Define any peering requirements that you may have, based on the number of clusters you have and where AAR is deployed. To know more about AAR, see the following links:
    * [Anbox Application Registry](https://discourse.ubuntu.com/t/anbox-application-registry-aar/17761)
    * [How to deploy an AAR](https://discourse.ubuntu.com/t/how-to-deploy-an-aar/17749) 
    * [How to configure an AAR](https://discourse.ubuntu.com/t/how-to-configure-an-aar/24319)

## Storage requirements

Based on your safety protocols, think about where you would want to host your storage. Also, refer to the following links that will help you plan and calculate your storage needs:

* [Requirements](https://discourse.ubuntu.com/t/requirements/17734)
* [etcd recommendations](https://etcd.io/docs/v3.5/op-guide/hardware/)
* [Capacity planning](https://discourse.ubuntu.com/t/about-capacity-planning/28717)

## Scalability, High availability, and redundancy

With Anbox Cloud, you can scale your deployment to as many clusters and subclusters as you require. It is a good idea to define how many Anbox clusters you want to deploy and how many subclusters per cluster. 

You should also assess the number of instances that you require for each model/service. For example, think about the number of Juju controller instances that you need. See [Make a controller highly available](https://juju.is/docs/olm/manage-controllers#heading--make-a-controller-highly-available) for more information.

Anbox Cloud comes with support for High Availability (HA) for both Core and the Streaming Stack.You can define HA by adding new Juju units. See [How to enable High availability?](https://discourse.ubuntu.com/t/how-to-enable-high-availability/17754) to plan your HA requirements.

## Security

Consider the following security aspects when you are planning for a production deployment:

### Secure communication

Communication between the Anbox Cloud components uses TLS encryption and authentication. Access is controlled through secure authentication tokens or temporary passwords. Secure communication is achieved using TLS and public-key encryption with a chain of trust up to a shared root Certificate Authority (CA). However, when the cluster is being brought up or a new unit is being added, the chain of trust and certificates required must be bootstrapped into the machines.

See [About Security](https://discourse.ubuntu.com/t/about-security/31217) for more information.

### Patching

You should keep your Anbox deployment updated to the latest available stable version. You should also update the other applications which make up Anbox. Keeping up to date ensures you have the latest fixes and security patches for smooth operation of your cluster.

For details about the Anbox Cloud release roadmap, see [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359).

## Data backup

Consider how frequently you want your data backed up and where you want to host your backed up data.

## Load balancing 

Load balancing solutions can differ based on your deployment model. You should assess the load balancing solution that you want to use and the number of load balancers that is ideal for your deployment model.

## Energy Efficiency

Anbox Cloud is optimised to use only as much energy as is necessary for an operation to complete. When planning for a production deployment, think through the following questions about energy efficiency to choose the most optimum way possible for your specific requirements:

* Does your hardware match the requirements for your use case?
* What trade-offs does your requirement allow to improve energy efficiency? For example, is there a way to use a lower streaming resolution? Lowering the resolution will impact the streaming experience but where possible, it could be a trade-off between being energy efficient and the quality of the stream. This needs to be decided based on how you use Anbox Cloud.
* Does your deployment use GPU encoding or CPU encoding?
* What is the bandwidth consumption of your deployment and what are the factors that could make it more efficient?
* Are you using the [appropriate platform](https://discourse.ubuntu.com/t/37322#supported-platforms-3) for your use case? For example, for automation use cases, `null` requires much less CPU usage than `webrtc` with GPU or CPU rendering.

## Monitoring and metrics

Although Anbox Cloud does not offer its own observability solution, Anbox Cloud gathers various performance metrics that you can access through API endpoints to create a monitoring solution.

To create a customised monitoring solution, see [Prometheus metrics](https://discourse.ubuntu.com/t/prometheus-metrics/19521) for a detailed understanding of available metrics to assess your monitoring needs for the production deployment. See [Performance](https://discourse.ubuntu.com/t/29416) to learn about the factors that could influence the performance of your deployment.

## Licensing and Support

You need the Ubuntu Pro subscription to use Anbox Cloud. Depending on the type of subscription you choose, your support model differs. You can refer to the [Ubuntu Pro website](https://ubuntu.com/pro) to learn and compare the different types of subscriptions. 

## Upgrade

When you consider a production deployment, it is important to assess your upgrade roadmap. For more information about upgrading Anbox Cloud and the prerequisites required for the upgrade process, see [How to upgrade Anbox Cloud](https://discourse.ubuntu.com/t/how-to-upgrade-anbox-cloud/17750). 

You can also choose to subscribe to the [announcements about Anbox Cloud releases](https://discourse.ubuntu.com/c/anbox-cloud/announcements/55) on discourse. For insights into the Anbox Cloud release roadmap, see [Release roadmap](https://discourse.ubuntu.com/t/release-roadmap/19359).