---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-12_bypass-apple-corp-sso-on-apple-admin-panel.md
original_filename: 2022-04-12_bypass-apple-corp-sso-on-apple-admin-panel.md
title: Bypass Apple Corp SSO on Apple Admin Panel
category: documents
detected_topics:
- sso
- access-control
- command-injection
- path-traversal
- api-security
tags:
- imported
- documents
- sso
- access-control
- command-injection
- path-traversal
- api-security
language: en
raw_sha256: 538034efb4df912218f99247297f804161bc4ffd02cacd436851bfd99c5b3132
text_sha256: 35abbdfd68425f9d32973fc6a9d8df19add5a02cdc7430181f5e544af9d7f1b6
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass Apple Corp SSO on Apple Admin Panel

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-12_bypass-apple-corp-sso-on-apple-admin-panel.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, path-traversal, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `538034efb4df912218f99247297f804161bc4ffd02cacd436851bfd99c5b3132`
- Text SHA256: `35abbdfd68425f9d32973fc6a9d8df19add5a02cdc7430181f5e544af9d7f1b6`


## Content

---
title: "Bypass Apple Corp SSO on Apple Admin Panel"
url: "https://medium.com/@StealthyBugs/bypass-apple-corp-sso-on-apple-admin-panel-dbfb72c7e634"
authors: ["Stealthy (@stealthybugs)"]
programs: ["Apple"]
bugs: ["Path traversal"]
bounty: "6,000"
publication_date: "2022-04-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2719
scraped_via: "browseros"
---

# Bypass Apple Corp SSO on Apple Admin Panel

Bypass Apple Corp SSO on Apple Admin Panel
Stealthy
Follow
2 min read
·
Apr 13, 2022

213

2

WhoAmI:

I am a twenty-year-old who has been in the bug bounty scene since 2018. Most of my time is on HackerOne, and I specialize in web application vulnerabilities. This blog is a way to share some of the interesting bugs and exploitation methods I have found over the years with the public.

Introduction:

This vulnerability takes place on the following Apple host.

https://rampadmin.apple.com

Apple’s corporate single sign protects the host via the IDMS authentication app, which blocks access to the website. However, some information is still available.

Get Stealthy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Using content discovery, I disclosed that the directory https://rampadmin.apple.com/adminexists. However, all endpoints and the directory itself are protected by authentication except one. The health check endpoint in the admin directory is visible to public users.

https://rampadmin.apple.com/admin/* → 302 SSO Auth required
https://rampadmin.apple.com/admin/healthcheck → 200 OK

So, using the Apache colon path traversal technique, I can bypass access control rules and view files in the admin directory.

https://rampadmin.apple.com/admin/data/existing_UAT_DS_App_Ids.json → 302 SSO Auth Required
https://rampadmin.apple.com/admin/healthcheck/..;/data/existing_UAT_DS_App_Ids.json → 200 OK

This works due to a misconfiguration that normalizes the URL path in the back end and transforms /..;/ to /../ . If you have not already, check out these slides for more information on this type of misconfiguration.

Impact:

I accessed files that disclosed administrative information about Apple’s internal architecture for their internal systems. These files gave me information about what systems exist, their name and associated IDs, and descriptions of the systems.

Apple promptly fixed the issue and awarded a bounty of 6,000$.

If you have any questions or want to reach out, ping me at my Twitter below. Thanks for reading!

https://twitter.com/stealthybugs
