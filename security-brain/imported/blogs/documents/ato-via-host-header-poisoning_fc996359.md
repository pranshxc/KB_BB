---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-08_ato-via-host-header-poisoning.md
original_filename: 2020-10-08_ato-via-host-header-poisoning.md
title: ATO via Host Header Poisoning
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- csrf
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- csrf
language: en
raw_sha256: fc99635991c6f6f2be132f0eecf7bcf4a3e3efe4e8bef83b1aa3b288f88db8a7
text_sha256: 2c6162c49a47bbc9a37addb7c58a532b0ebe2c6ce59e50a806b900e834e702bd
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: true
---

# ATO via Host Header Poisoning

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-08_ato-via-host-header-poisoning.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, csrf
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: True
- Raw SHA256: `fc99635991c6f6f2be132f0eecf7bcf4a3e3efe4e8bef83b1aa3b288f88db8a7`
- Text SHA256: `2c6162c49a47bbc9a37addb7c58a532b0ebe2c6ce59e50a806b900e834e702bd`


## Content

---
title: "ATO via Host Header Poisoning"
url: "https://medium.com/@sechunter/ato-via-host-header-poisoning-dc5c29d2fd0d"
authors: ["Shivam Kamboj Dattana (@sechunt3r)"]
bugs: ["Host header injection", "Account takeover", "Password reset"]
bounty: "2,000"
publication_date: "2020-10-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4209
scraped_via: "browseros"
---

# ATO via Host Header Poisoning

Top highlight

ATO via Host Header Poisoning
Shivam Kamboj Dattana
Follow
2 min read
·
Oct 8, 2020

303

1

Hello Everyone (Ram Ram Ji),

Get Shivam Kamboj Dattana’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This article is about an account takeover bug via host header poisoning. Redacted.com was vulnerable to host header injection in which remote attackers can exploit it to takeover any account of redacted.com.

Attacking Scenario:

As an attacker, I modified the POST request in which first I change the value of the Host header to evil.com but nothing happened then I add the X-Forwarded-Host header with evil.com value again nothing happened. It was my third attempt now, this time I changed the value of the Referrer header too and put the same value as the X-Forwarded-Host header value and it got worked for me.

Request was looked like:

POST /forgot HTTP/1.1
Host: redacted.com
X-Forwarded-Host: evil.com
Referrer: https://evil.com

username=<username>&_csrf_token=***REDACTED-SUSPECT-TOKEN***Press enter or click to view image in full size
Request Looks Like

After sending the request I got email with host as evil.com looks like:

Press enter or click to view image in full size
Got email with malicious host
Step to Reproduce (Acc. to Report):
Navigate to “​https://redacted.com/forgot".
Then enter your username & intercept that request with the help of Burp Suite.
Now add these two headers into the POST request:

X-Forwarded-Host: evil.com
Referrer: https://evil.com

4. Now forward that request and check your email that is linked with your username.

Timeline:
Press enter or click to view image in full size
Bounty Rewarded

June 26, 2019 — Reported to private program
August 01, 2019 — Report Triaged
August 08, 2019 — Bounty of $2000 USD awarded
October 24, 2019 — Vulnerability fixed

Special thanks to nullr3x (Big Bad Brother 🤑 )
