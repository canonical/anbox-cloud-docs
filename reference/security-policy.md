(ref-security-policy)=
# Security policy

Learn about our [release and support policy](https://documentation.ubuntu.com/anbox-cloud/reference/release-notes/release-notes/#release-and-support-policy) for the nature of our releases and versions.

All our public repositories have a `SECURITY.md` file that details our security policy. However, Anbox Cloud has components for which the source is not publicly available. The same policy as listed below applies for a security vulnerability for any component of Anbox Cloud.

## Reporting a vulnerability

If you discover a security vulnerability with Anbox Cloud, report it using the following steps:

1. Do not publicly disclose the vulnerability before discussing it with us.
2. Report a bug at https://bugs.launchpad.net/anbox-cloud.

    **Important**: Remember to set the information type to *Private Security*. You will see a field with the text *This bug contains information that is:*
3. Provide detailed information about the vulnerability, including:
   - A description of the vulnerability
   - Steps to reproduce the issue
   - Potential impact and affected versions
   - Suggested mitigation, if possible

The [Ubuntu Security disclosure and embargo policy](https://ubuntu.com/security/disclosure-policy) contains more information about what you can expect when you contact us and what we expect from you.

## Response to reported vulnerabilities

The Anbox Cloud team will be notified of the issue and review the vulnerability. We may reach out to you for further information or clarification if needed.

If the issue is confirmed as a valid security vulnerability, we use the [NVD scoring system](https://nvd.nist.gov/vuln-metrics/cvss) for deciding the severity and assign a CVE number.

We fix vulnerabilities classified as _critical_ or _high_ with the subsequent monthly release of Anbox Cloud and also document them as {ref}`ref-security-notices`.
