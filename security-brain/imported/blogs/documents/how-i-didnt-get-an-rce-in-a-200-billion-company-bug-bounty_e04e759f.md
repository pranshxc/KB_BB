---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-12_how-i-didnt-get-an-rce-in-a-200-billion-company-bug-bounty.md
original_filename: 2022-09-12_how-i-didnt-get-an-rce-in-a-200-billion-company-bug-bounty.md
title: How I DIDN’T get an RCE in a $200 Billion company — Bug Bounty
category: documents
detected_topics:
- command-injection
- sso
tags:
- imported
- documents
- command-injection
- sso
language: en
raw_sha256: e04e759f2acaad10f97dd6106d467af83de4ab182a5f9705fc4c43f7315e98f3
text_sha256: 6185d6b0619e2682fd29a58b5ef857075a5b03ca09708522a7e1a9bdffb0fab4
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# How I DIDN’T get an RCE in a $200 Billion company — Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-12_how-i-didnt-get-an-rce-in-a-200-billion-company-bug-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, sso
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `e04e759f2acaad10f97dd6106d467af83de4ab182a5f9705fc4c43f7315e98f3`
- Text SHA256: `6185d6b0619e2682fd29a58b5ef857075a5b03ca09708522a7e1a9bdffb0fab4`


## Content

---
title: "How I DIDN’T get an RCE in a $200 Billion company — Bug Bounty"
url: "https://medium.com/@nynan/how-i-didnt-get-an-rce-in-a-200-billion-company-bug-bounty-377afb2fb4ec"
authors: ["nynan (@_nynan)"]
bugs: ["RCE", "Components with known vulnerabilities"]
publication_date: "2022-09-12"
added_date: "2022-11-30"
source: "pentester.land/writeups.json"
original_index: 2177
scraped_via: "browseros"
---

# How I DIDN’T get an RCE in a $200 Billion company — Bug Bounty

Member-only story

How I DIDN’T get an RCE in a $200 Billion company — Bug Bounty
BrownBearSec
Follow
4 min read
·
Sep 12, 2022

179

4

Press enter or click to view image in full size

At some point in time, I was hunting for CVE-2021–36356 on my subdomain list of over 1,000,000+ subdomains, and finally got a hit…

Considering becoming a member on medium? Use this link at no extra cost to yourself, and support me :) (https://medium.com/@nynan/membership)

This is largely a filler blog whilst I’m working on something bigger. If you follow this medium account you will be notified when I release my new blog “What I learnt from reading 217 subdomain takeover bug reports!”, which is looking to be very insightful. It should be soon.

CVE-2021–36356 is a critical vulnerability, which allows unauthenticated remote code execution in the KRAMER VIAware software. This vulnerability occurs because the /ajaxPages/writeBrowseFilePathAjax.php accepts all unfiltered input and writes it to a file.

The POST parameter radioBtnVal is where we input our PHP code, we will use this to upload a bind shell, but you can also use a reverse shell. A bind shell is less intrusive and more appropriate for a PoC whilst doing bug bounties.
The POST parameter associateFileName is where we will write the file, make sure it’s somewhere you can access from the web server like “/var/www/html/”
