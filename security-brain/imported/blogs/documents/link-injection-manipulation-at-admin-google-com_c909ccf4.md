---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-09-23_link-injection-manipulation-at-admingooglecom.md
original_filename: 2016-09-23_link-injection-manipulation-at-admingooglecom.md
title: Link Injection Manipulation at admin.google.com
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: c909ccf43e48e8eb32f5af82bf40827b1fba11fb70f24c56918e1f56a788ea09
text_sha256: d6199fa37912ca5745d2e0842e74f0fe1efb41cdaae708a28ad9c9e780cd0ac9
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Link Injection Manipulation at admin.google.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-09-23_link-injection-manipulation-at-admingooglecom.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `c909ccf43e48e8eb32f5af82bf40827b1fba11fb70f24c56918e1f56a788ea09`
- Text SHA256: `d6199fa37912ca5745d2e0842e74f0fe1efb41cdaae708a28ad9c9e780cd0ac9`


## Content

---
title: "Link Injection Manipulation at admin.google.com"
url: "https://medium.com/@know.0nix/link-injection-manipulation-at-admin-google-com-6da3b15a2854"
authors: ["Ak1T4 (@akita_zen)"]
programs: ["Google"]
bugs: ["Hyperlink injection"]
publication_date: "2016-09-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6256
scraped_via: "browseros"
---

# Link Injection Manipulation at admin.google.com

Link Injection Manipulation at admin.google.com
Ak1T4
Follow
2 min read
·
Sep 23, 2016

127

1

I’ve found a link injection in google with href attribute who can compromise a user by a fake link or download evil file.

The issue:

We can inject any link at admin.google.com, adding a path to the url, the path in self is injected and rendered as link in the page, we can put any domain of our property and redirect the user or force the user to download an evil file.

The Impact:

An attacker can use this links for sending lots of emails, spreading in social networks, and cheat the user to click the link, infecting with malware a lot of users, redirect them or force to download evil files.

Technical Details:

The evil url endpoint -> https://admin.google.com/google-mail.info/accountchooser?u=click-above-google-mail.info@google

[google-mail.info] -> is a fake domain who i buy, this path is injected and rendered directly in the html web

[u=click-above-google-mail.info@google] is a text injection in google account info

The rendered page looks like this:

Press enter or click to view image in full size

We can see the link rendered and the text injection too. The google-mail.info is an evil domain who i buy and force the user to download a file or redirect them to an external evil site without any advise of google.

Get Ak1T4’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The google-mail.info domain injected in the path and rendered can be any domain, i use google-mail.info because is more trusted for the users, and is more easily to cheat the user to click it.

The Google Reply:

I send the report and the google reply was this:

“ Hey,

Thanks for the bug report.

We’ve taken a look at your submission and can confirm this is not a security vulnerability.Reports that demonstrate exploitation with a Reflected File Download and other social-engineering vectors usually fall out of scope for Google VRP. “

Here is a PoC Video who i send with the report:

NOTE: The issue/bug is not FIXED at all.-

Best Regards my friends and Happy Hacking

@ak1t4

https://twitter.com/knowledge_2104

HackerOne profile - ak1t4
Whiteh4t Hack3r & Zen Monk - https://twitter.com/knowledge_2014

hackerone.com
