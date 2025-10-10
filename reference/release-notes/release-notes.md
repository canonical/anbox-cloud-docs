(ref-release-notes)=
# Release notes

This page outlines the release notes of all versions of Anbox Cloud. If you're interested in getting notified for the latest Anbox Cloud releases, subscribe to the [Anbox Cloud category](https://discourse.ubuntu.com/c/anbox-cloud/49) on the Ubuntu discourse.

For instructions on how to update your Anbox Cloud deployment to later versions, see {ref}`howto-upgrade-anbox-cloud` or {ref}`howto-upgrade-appliance`.

## Recent releases

| Release date   |  Release notes  |
|----|----|
| October 15, 2025 | [Anbox Cloud 1.27.2](1.27.2.md) |
| September 17, 2025 | [Anbox Cloud 1.27.1](1.27.1.md) |
| August 13, 2025 | [Anbox Cloud 1.27.0](1.27.0.md) |

## Upcoming release roadmap

The current, supported minor release is **1.27.0** and the next one will be **1.28.0** in November 2025.

The following target dates for upcoming releases are not final and could vary depending on various factors such as availability of Android security patches. The release notes link will be updated on the day of the release.

| Target date | Version | Planned updates |
|----|----|----|
| November 12, 2025 | Anbox Cloud 1.28.0 | * Telephony support for all Android versions<br/> * Ability to protect instances from destructive operations<br/> * Extended support for authentication and authorization<br/> * Enhancements to management of session shares<br/> * Conversion from YUV to RGB in Android containers using GPUs<br/> * WebRTC diagnostics to troubleshoot connection issues<br/> * Remove support for node controller charm<br/> * Android security updates<br/> * Bug fixes |
| December 10, 2025 | Anbox Cloud 1.28.1 | * Android security updates<br/> * Bug fixes |

## Release and support policy

Anbox Cloud follows a defined release cycle with frequent minor and patch releases.

Minor releases
: A new minor release of Anbox Cloud is released every three months. It includes new features and bug fixes.

Patch releases
: A patch release for Anbox Cloud is released every month and includes Android and Chrome security updates alongside Anbox Cloud specific bug fixes.

Anbox Cloud supports only the most recent release. Older releases are only supported for a short time after a new minor release was published.

Feature deprecations are generally announced two releases in advance before the deprecated features are dropped. See {ref}`ref-deprecation-notes` for details.

To ensure you receive latest security updates and bug fixes, you should upgrade to a new release of Anbox Cloud shortly after it is released.

If you are looking for additional support, see [Ubuntu Pro](https://ubuntu.com/support). Canonical can also provide [managed solutions](https://ubuntu.com/managed) for Anbox Cloud.


### What's new in 1.27.x?

Along with bug fixes and general improvements, Anbox Cloud 1.27.x includes:

* CLI client authentication using OIDC compatible identity providers (alpha release)
* Enhancements to the dashboard to show notifications and asynchronous operations
* Bug fixes

<details><summary>Click to view earlier releases' notes</summary>

|  Release date  |  Release notes  |
|----|----|
| July 16, 2025 | [Anbox Cloud 1.26.2](1.26.2.md) |
| June 18, 2025 | [Anbox Cloud 1.26.1](1.26.1.md) |
| May 14, 2025 | [Anbox Cloud 1.26.0](1.26.0.md) |
| April 16, 2025 | [Anbox Cloud 1.25.2](1.25.2.md) |
| March 12, 2025 | [Anbox Cloud 1.25.1](1.25.1.md) |
| February 12, 2025 | [Anbox Cloud 1.25.0](1.25.0.md) |
| January 15, 2025 | [Anbox Cloud 1.24.2](1.24.2.md) |
| December 11, 2024 | [Anbox Cloud 1.24.1](1.24.1.md) |
| December 4, 2024 | [Anbox Cloud 1.23.3](1.23.3.md) |
| November 13 2024 | [Anbox Cloud 1.24.0](1.24.0.md) |
| October 23 2024 | [Anbox Cloud 1.23.2 hotfix 1](1.23.2-hotfix1.md) |
| October 16 2024 | [Anbox Cloud 1.23.2](1.23.2.md) |
| September 18 2024 | [Anbox Cloud 1.23.1](1.23.1.md) |
| August 14 2024 | [Anbox Cloud 1.23.0](1.23.0.md) |
| July 18 2024 | [Anbox Cloud 1.22.2](1.22.2.md) |
| June 13 2024 | [Anbox Cloud 1.22.1](1.22.1.md) |
| May 15 2024 | [Anbox Cloud 1.22.0](1.22.0.md) |
| April 18 2024 | [Anbox Cloud 1.21.2](1.21.2.md) |
| March 13 2024 | [Anbox Cloud 1.21.1](1.21.1.md) |
| February 14 2024 | [Anbox Cloud 1.21.0](1.21.0.md) |
| January 17 2024 | [Anbox Cloud 1.20.2](1.20.2.md) |
|December 13 2023| [Anbox Cloud 1.20.1](1.20.1.md) |
|November 16 2023 | [Anbox Cloud 1.20.0](1.20.0.md) |
|October 11 2023|[Anbox Cloud 1.19.2](1.19.2.md)|
|September 13 2023|[Anbox Cloud 1.19.1](1.19.1.md)|
|August 30 2023|[Anbox Cloud 1.19.0-fix1](1.19.0-fix1.md)|
|August 16 2023|[Anbox Cloud 1.19.0](1.19.0.md)|
|July 12 2023|[Anbox Cloud 1.18.2](1.18.2.md)|
|June 14 2023|[Anbox Cloud 1.18.1](1.18.1.md)|
|May 17 2023|[Anbox Cloud 1.18.0](1.18.0.md)|
|April 17 2023|[Anbox Cloud 1.17.2](1.17.2.md)|
|March 16 2023|[Anbox Cloud 1.17.1](1.17.1.md)|
|February 15 2023|[Anbox Cloud 1.17.0](1.17.0.md)|
|January 24 2023|[Anbox Cloud 1.16.4](1.16.4.md)|
|January 17 2023|[Anbox Cloud 1.16.3](1.16.3.md)|
|January 12 2023|[Anbox Cloud 1.16.2](1.16.2.md)|
|December 14 2022|[Anbox Cloud 1.16.1](1.16.1.md)|
|November 16 2022|[Anbox Cloud 1.16.0](1.16.0.md)|
|October 20 2022|[Anbox Cloud 1.15.3](1.15.3.md)|
|October 12 2022|[Anbox Cloud 1.15.2](1.15.2.md)|
|September 14 2022|[Anbox Cloud 1.15.1](1.15.1.md)|
|August 24 2022|[Anbox Cloud 1.15.0](1.15.0.md)|
|July 18 2022|[Anbox Cloud 1.14.2](1.14.2.md)|
|June 16 2022|[Anbox Cloud 1.14.1](1.14.1.md)|
|May 23 2022|[Anbox Cloud 1.14.0](1.14.0.md)|
|April 13 2022|[Anbox Cloud 1.13.2](1.13.2.md)|
|March 21 2022|[Anbox Cloud 1.13.1](1.13.1.md)|
|February 24 2022|[Anbox Cloud 1.13.0](1.13.0.md)|
|February 15 2022|[Anbox Cloud 1.11.5](1.11.5.md)|
|January 28 2022|[Anbox Cloud 1.12.5](1.12.5.md)|
|January 21 2022|[Anbox Cloud 1.12.4](1.12.4.md)|
|January 20 2022|[Anbox Cloud 1.12.3](1.12.3.md)|
|December 16 2021|[Anbox Cloud 1.12.2](1.12.2.md)|
|November 30 2021|[Anbox Cloud 1.12.1](1.12.1.md)|
|November 16 2021|[Anbox Cloud 1.12.0](1.12.0.md)|
|November 1 2021|[Anbox Cloud 1.11.4](1.11.4.md)|
|October 18 2021|[Anbox cloud 1.11.3](1.11.3.md)|
|September 20 2021|[Anbox Cloud 1.11.2](1.11.2.md)|
|August 17 2021|[Anbox Cloud 1.11.1](1.11.1.md)|
|August 5 2021|[Anbox Cloud 1.11.0](1.11.0.md)|
|July 14 2021|[Anbox Cloud 1.10.3](1.10.3.md)|
|June 13 2021|[Anbox Cloud 1.10.2](1.10.2.md)|
|May 13 2021|[Anbox Cloud 1.10.1](1.10.1.md)|
|May 11 2021|[Anbox Cloud 1.9.5](1.9.5.md)|
|May 6 2021|[Anbox Cloud 1.10.0](1.10.0.md)|
|May 3 2021|[Anbox Cloud 1.9.4](1.9.4.md)|
|April 13 2021|[Anbox Cloud 1.9.3](1.9.3.md)|
|March 17 2021|[Anbox Cloud 1.9.2](1.9.2.md)|
|March 4 2021|[Anbox Cloud 1.9.1](1.9.1.md)|
|February 10 2021|[Anbox Cloud 1.9.0](1.9.0.md)|
|January 19 2021|[Anbox Cloud 1.8.3](1.8.3.md)|
|December 17 2020|[Anbox Cloud 1.8.2](1.8.2.md)|
|November 12 2020|[Anbox Cloud 1.8.1](1.8.1.md)|
|November 4 2020|[Anbox Cloud 1.8.0](1.8.0.md)|
|October 15 2020|[Anbox Cloud 1.7.4](1.7.4.md)|
|September 23 2020|[Anbox Cloud 1.7.3](1.7.3.md)|
|September 11 2020|[Anbox Cloud 1.7.2](1.7.2.md)|
|August 21 2020|[Anbox Cloud 1.7.1](1.7.1.md)|
|August 2020|[Anbox Cloud 1.7.0](1.7.0.md)|
|July 2020|[Anbox Cloud 1.6.3](1.6.3.md)|
|June 2020|[Anbox Cloud 1.6.2](1.6.2.md)|
|June 2020|[Anbox Cloud 1.6.1](1.6.1.md)|
|June 2020|[Anbox Cloud 1.6.0](1.6.0.md)|
|June 2020|[Anbox Cloud 1.5.2](1.5.2.md)|
|May 2020|[Anbox Cloud 1.5.1](1.5.1.md)|
|April 2020|[Anbox Cloud 1.5.0](1.5.0.md)|
|March 2020|[Anbox Cloud 1.4.0](1.4.0.md)|
|January 2020|[Anbox Cloud 1.3.3](1.3.3.md)|
|October 2019|[Anbox Cloud 1.3.2](1.3.2.md)|
|September 2019|[Anbox Cloud 1.3.1](1.3.1.md)|
|August 2019|[Anbox Cloud 1.3.0](1.3.0.md)|
|April 2019|[Anbox Cloud 1.2.1](1.2.1.md)|
|April 2019|[Anbox Cloud 1.2.0](1.2.0.md)|
|February 2019|[Anbox Cloud 1.1.1](1.1.1.md)|
|January 2019|[Anbox Cloud 1.1.0](1.1.0.md)|
|December 2018|[Anbox Cloud 1.0.1](1.0.1.md)|
|November 2018|[Anbox Cloud 1.0.0](1.0.0.md)|
</details>

## Security policy

The Anbox Cloud security policy is available at {ref}`ref-security-policy`.
