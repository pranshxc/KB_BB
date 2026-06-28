---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-05_a-short-white-box-code-audit-of-avo.md
original_filename: 2023-06-05_a-short-white-box-code-audit-of-avo.md
title: A short white box code audit of avo
category: documents
detected_topics:
- xss
- access-control
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- access-control
- command-injection
- automation-abuse
language: en
raw_sha256: adfcb74e5186cca3edeab7b3e867a536104c02fb69a761fe361e7bbdaf8a7685
text_sha256: 8c81b65e21b6cd4b805ba85d35d62b145d43a6a4e7c411bc7bc9f2297c9ecde4
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# A short white box code audit of avo

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-05_a-short-white-box-code-audit-of-avo.md
- Source Type: markdown
- Detected Topics: xss, access-control, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `adfcb74e5186cca3edeab7b3e867a536104c02fb69a761fe361e7bbdaf8a7685`
- Text SHA256: `8c81b65e21b6cd4b805ba85d35d62b145d43a6a4e7c411bc7bc9f2297c9ecde4`


## Content

---
title: "A short white box code audit of avo"
url: "https://evait.medium.com/a-short-white-box-code-audit-of-avo-2083b08f3a95"
authors: ["Paul Werther", "Anton Strilez (@mergon2089)"]
programs: ["Avo"]
bugs: ["Stored XSS", "DoS"]
publication_date: "2023-06-05"
added_date: "2023-06-06"
source: "pentester.land/writeups.json"
original_index: 1083
scraped_via: "browseros"
---

# A short white box code audit of avo

A short white box code audit of avo
Pentest Team @greenhats.com
Follow
2 min read
·
Jun 6, 2023

2

We conducted a two-day penetration test on the product “Avo”, which is a Ruby / Ruby on Rails gem for building administrative interfaces. Since greenhats®, our platform, uses this software for some production environments, it is enforced by internal policy to perform a small pentest / white box code audit to identify obvious potential risks. This approach differs from a comprehensive penetration test, which for this type and size of application should be scheduled for at least two weeks.

Although such reports contain sensitive data and most of the time will be for private access only, this report as well as the pentest itself will be part of the public community contribution from greenhats to the incredible Avo project, so it`s publicly accessible (links below). Due to the critical impact on the security of Avo users, we will release any findings after we have confirmed that they have been fixed in all of Avo’s latest release channels and all users are notified that they must update to be secure.

The entire code base of the product in version 3.0.0.pre12 was audited using both automated and manual techniques. In addition, the authentication and authorization parts were manually audited. Ruby on Rails itself contains many best practices for security implementations and greatly reduces the risk and potential of common vulnerabilities. In particular, the use of standard active record functions and an external, well-known gem for all search operations makes it more difficult to find typical vulnerabilities.

We discovered a bug in the displaying functionality of html-based content that could lead to hijacking of visitors’ or other administrators’ browsers. We also discovered a potentially critical security issue in the handling of polymorphic resources. Due to time constraints, we do not provide full exploitation of any of these findings. We believe that applying security mitigations even for potential vulnerabilities should be the main goal of any white box code audit, rather than spending too much time developing a full exploit. While this may be helpful in considering the risk of the specific findings, it is not the main objective of this particular test.

We hope that this small contribution will help to use Avo in a safer way and motivate more security researchers to take a closer look at the application.

Of course, all vulnerabilities will be reported in a responsive manner and published at the time a fix is released in the normal release cycle.

Get Pentest Team @greenhats.com’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Public discloure (v2.33.3 contains fixes for both vulnerabilities)

CVE-2023–34102 (Founder: FLX | Paul Werther)

CVE-2023-34103 (Founder Mys7ic | Anton Strilez)

You can download the full pentest report using the following link

Penetration test report — Avo v3.0.0.pre12–2023

Github advisories

Possible unsafe reflection / partial DoS

Stored XSS (Cross Site Scripting) in html content based fields
