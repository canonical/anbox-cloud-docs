---
myst:
  html_meta:
    "description": "Reference documentation for Anbox Cloud security policy, covering vulnerability reporting and response process."
---

(ref-security-policy)=
# Security policy

The Anbox Cloud security policy defines how security vulnerabilities are assessed, addressed and communicated.

For information about supported versions and the release lifecycle, see our {ref}`release and support policy <release-and-support-policy>`.

## Security vulnerabilities

All our public repositories have a `SECURITY.md` file that details our security policy. This policy applies to security vulnerabilities affecting any component of Anbox Cloud, including components whose source is not publicly available.

## Reporting a vulnerability

Anbox Cloud follows the [Ubuntu Security disclosure and embargo policy](https://ubuntu.com/security/disclosure-policy). It contains more information about what you can expect when you contact us and what we expect from you.

If you discover a security vulnerability, see the [Anbox Cloud security policy](https://github.com/canonical/anbox-cloud-docs/blob/main/SECURITY.md) for information about how to report it.

## Response to reported vulnerabilities

The Anbox Cloud team will be notified of the issue and review the vulnerability. We may reach out to you for further information or clarification if needed.

If the issue is confirmed as a valid security vulnerability, we use the [NVD scoring system](https://nvd.nist.gov/vuln-metrics/cvss) to assess the severity and assign a CVE identifier.

We fix vulnerabilities classified as *critical* or *high* with the next release of Anbox Cloud.

For information about known vulnerabilities and available fixes, see the {ref}`security notices <ref-security-notices>`. Each Anbox Cloud release also includes a summary of security fixes in the {ref}`release notes <ref-release-notes>`.

## Related topics

Reference:

- {ref}`ref-security-notices`
- {ref}`ref-release-notes`

Explanation:
- {ref}`exp-security`