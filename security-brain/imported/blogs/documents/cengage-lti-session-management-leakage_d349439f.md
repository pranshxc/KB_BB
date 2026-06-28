---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-20_cengage-lti-session-management-leakage.md
original_filename: 2022-12-20_cengage-lti-session-management-leakage.md
title: Cengage LTI Session Management Leakage
category: documents
detected_topics:
- sso
- command-injection
- otp
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- sso
- command-injection
- otp
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: d349439fee0b169d0a2ac7ddbebe23b1089b4fbf39ddd401b2d5c73accf1b217
text_sha256: e7383337b5045e67c8fe1b9bda22dab20f28493652ba638b0d6a3bd629825003
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Cengage LTI Session Management Leakage

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-20_cengage-lti-session-management-leakage.md
- Source Type: markdown
- Detected Topics: sso, command-injection, otp, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `d349439fee0b169d0a2ac7ddbebe23b1089b4fbf39ddd401b2d5c73accf1b217`
- Text SHA256: `e7383337b5045e67c8fe1b9bda22dab20f28493652ba638b0d6a3bd629825003`


## Content

---
title: "Cengage LTI Session Management Leakage"
page_title: "Cengage LTI Session Management Leakage | Rapid7 Blog"
url: "https://www.rapid7.com/blog/post/2022/12/20/cengage-lti-session-management-leakage/"
final_url: "https://www.rapid7.com/blog/post/2022/12/20/cengage-lti-session-management-leakage/"
authors: ["Tony Porterfield"]
programs: ["Cengage"]
bugs: ["SSO", "Session management issue"]
publication_date: "2022-12-20"
added_date: "2022-12-23"
source: "pentester.land/writeups.json"
original_index: 1762
---

Prior to December 10, 2022, Cengage, an education technology provider in use in many higher education environments primarily in the United States, had two issues in the way it handled session management over its Learning Tools Integration (LTI) pipeline.

The first issue involves leaving unexpectedly long-lived sessions and accompanying login links in the end user's browser history as well as via cached GET requests, which could be used by unauthenticated attackers to impersonate the user. This appears to be an instance of [CWE-525](https://cwe.mitre.org/data/definitions/525.html), "Use of Web Browser Cache Containing Sensitive Information." This issue is estimated to have a CVSSv3 score of [4.5](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:N/A:N&version=3.1) (Medium). A fix for this issue is expected in March of 2023.

The second issue involves a failure to check the LTI launch signature from connected applications, which could allow an authenticated attacker to impersonate another user. This appears to be an instance of [CWE-347](https://cwe.mitre.org/data/definitions/347.html), "Improper Verification of Cryptographic Signature." This issue is estimated to have a CVSSv3 score of [6.5](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N&version=3.1) (Medium). Note, this issue has been fixed by the vendor.

## Product Description

Cengage is an education technology provider offering digital products including eTextbooks, homework tools and online learning platforms (such as WebAssign). Cengage's online learning platforms integrate with Learning Management Systems (LMS). For more information about Cengage's LMS integrations, please visit the [vendor's website](https://www.cengage.com/lms/).

## Credit

This issue was discovered by Tony Porterfield, Principal Cloud Solutions Architect at Rapid7, while observing a family member use the application as an end-user. It is being disclosed in accordance with Rapid7's [vulnerability disclosure policy](/security/disclosure/).

## Exploitation

For the CWE-525 issue, it was observed that the "Cengage Single Sign-On" link was usable in the browser history, even though the user had already logged out of the application:

![image1.png](https://www.rapid7.com/cdn/images/bltc3142617ec16bf5c/683de3f7bc38b15a87477dee/image1.png)

Clicking the circled link would log the user back in, and was active for at least an hour post-logout.

For the CWE-347 issue, it was observed that the signature check on an LTI launch request to https://gateway.cengage.com/rest/launchBasicLTI responds with a hidden form post containing the LTI parameters from https://gateway.cengage.com/launchBasicLTI/smartlink/basicLTILaunch.gwy as well as a field signatureVerified that is set to false if the signature is invalid. An end user could alter this response by setting signatureVerified to true, as shown below:

![image2.png](https://www.rapid7.com/cdn/images/blt4d5d5262808c3687/683de41a3beff030ffa7c55b/image2.png)

Once modified, the LTI session context would then be accepted by the server as authentic.

## Impact

For the CWE-525 issue involving cached credentials, an attacker wishing to impersonate an authenticated user would either need to have access to the browser session of the targeted user, or access to network proxy logs which can cache these tokens (thus, implying a privileged position either locally or on the local network). Assuming this is the case, the attacker could go on to read and alter personal information involving the student. It appears possible to similarly hijack the sessions of instructors or administrators, but this hasn't been tested or confirmed directly.

For the CWE-347 issue involving signature verification, an authenticated attacker may be able to assume sessions belonging to other users, possibly including other students, instructors, and administrators.

## Vendor Statement

Cengage is continuously implementing and refining measures aimed to protect the privacy and security of the customer information entrusted to us. We value the contributions of security researchers like you, as reviews like this help us strengthen our security posture. We use multiple tools and processes, including DAST, SAST, penetration testing and VDP to identify and address security defects in our software.

[The CWE-347 issue] was fixed on December 9, 2022. The second issue is currently in remediation, and we plan to launch a fix as soon as possible.

We continually update and regularly identify ways we can improve our products both to better the learning experience for students and instructors and to ensure information remains secure. If you have found something you would like to report, please submit at <https://bugcrowd.com/cengage-vdp>.

## Remediation

In December of 2022, Cengage released an update to its webassign.net service to address the CWE-347 (signature verification) issue, and is developing a fix for the CWE-525 issue, which we expect to see in March of 2023. Since this is a SaaS-based/cloud-hosted solution, end users, implementers, and integrators should not need to do anything to update or patch locally to address the signature verification issue — the latest version of the LTI implementation will already be available. Beyond this fix, end users have nothing to do to ensure they're safe from impersonation, as they're reliant on the provider to properly verify signatures.

While the SSO issue is being developed, end users would be wise to completely sign out of the local computer when complete with whatever academic tasks they were performing, as this would prevent opportunistic attackers from using stored session tokens locally. This is generally good advice anyway, even after the CWE-525 issue is resolved.

Avoiding caching session tokens inadvertently exposed through GET requests on a web proxy is more difficult for the average user to avoid, but as long as no untrusted users have access to proxy logs, the risk from exploiting proxy-cached session tokens is remote (an attacker who does have access to web proxies used by students, instructors, and administrators tend to already have more expansive offensive options).

## Disclosure Timeline

  * September, 2022: Issue discovered by Tony Porterfield
  * Mon, Sep 12, 2022: Contacted [Bugcrowd](https://bugcrowd.com/cengage-vdp), Cengage's VDP provider, to work out a disclosure agreement
  * Mon, Sep 19, 2022: Contact attempted to alternate contacts at Cengage
  * Wed, Sep 21, 2022: Agreement reached on disclosure terms
  * Thu, Sep 22, 2022: Vulnerability details communicated to Cengage via Bugcrowd with a public disclosure goal of November 15, 2022.
  * Fri, Sep 23, 2022: Triage begun at Bugcrowd (Issue 4464ed3d-3fb6-4287-ba46-786d21bebad0)
  * Sep 23 - Oct 25, 2022: Triage and reproduction work continued
  * Oct 26, 2022: Bugcrowd verified reproduction of the report
  * Nov 1, 2022: Extended disclosure time by approximately 30 days
  * Thu, Dec 15, 2022: Vendor provided update on fix status
  * Fri, Dec 20, 2022: This public disclosure

[![LinkedIn](/linkedin-logo.svg)](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F12%2F20%2Fcengage-lti-session-management-leakage&title=Cengage%20LTI%20Session%20Management%20Leakage)[![Facebook](/facebook-logo.svg)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F12%2F20%2Fcengage-lti-session-management-leakage)[![X](/x-logo.svg)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F12%2F20%2Fcengage-lti-session-management-leakage&text=Cengage%20LTI%20Session%20Management%20Leakage)[![Bluesky](/bluesky-dark-logo.svg)](https://bsky.app/intent/compose?text=Cengage%20LTI%20Session%20Management%20Leakage%20https%3A%2F%2Fwww.rapid7.com%2Fblog%2Fpost%2F2022%2F12%2F20%2Fcengage-lti-session-management-leakage)

#### Article Tags

  * [Vulnerability Disclosure](/blog/tag/vulnerability-disclosure/)
  * [Cloud Security](/blog/tag/cloud-security/)

[![Tod Beardsley](/_next/image/?url=https%3A%2F%2Fwww.rapid7.com%2Fcdn%2Fimages%2Fblt6cf094a2ceec5340%2F68404474afd14d7c456286fa%2FTod-Beardsley.jpg&w=256&q=75)Tod BeardsleyAuthor Posts](/blog/author/tod-beardsley/)
