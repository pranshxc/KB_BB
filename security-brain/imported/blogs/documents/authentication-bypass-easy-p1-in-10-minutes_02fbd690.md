---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-16_authentication-bypass-easy-p1-in-10-minutes.md
original_filename: 2021-06-16_authentication-bypass-easy-p1-in-10-minutes.md
title: Authentication Bypass | Easy P1 in 10 minutes
category: documents
detected_topics:
- saml
- idor
- command-injection
- rate-limit
tags:
- imported
- documents
- saml
- idor
- command-injection
- rate-limit
language: en
raw_sha256: 02fbd6907b22d95ac1a7d2d2eca6aea7b16e92cd10510c7fb6a957c0ec398220
text_sha256: f3934cce132c93a2f64e2e4834202e21cd8e8e8d6c58733e0018bbf528d2e6c1
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Authentication Bypass | Easy P1 in 10 minutes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-16_authentication-bypass-easy-p1-in-10-minutes.md
- Source Type: markdown
- Detected Topics: saml, idor, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `02fbd6907b22d95ac1a7d2d2eca6aea7b16e92cd10510c7fb6a957c0ec398220`
- Text SHA256: `f3934cce132c93a2f64e2e4834202e21cd8e8e8d6c58733e0018bbf528d2e6c1`


## Content

---
title: "Authentication Bypass | Easy P1 in 10 minutes"
url: "https://infosecwriteups.com/authentication-bypass-easy-p1-in-10-minutes-54d5a2093e54"
authors: ["Anirudh Makkar (@anirudhmakkar)"]
bugs: ["Authentication bypass", "Forced browsing"]
publication_date: "2021-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3572
scraped_via: "browseros"
---

# Authentication Bypass | Easy P1 in 10 minutes

Top highlight

Authentication Bypass | Easy P1 in 10 minutes
Anirudh Makkar
Follow
2 min read
·
Jun 16, 2021

819

8

Recon always wins

Hello there, I am Anirudh Makkar from India. This is my first write up and I hope you guys like it. In this write-up, I will explain the power of Recon and Google Dorks. Don’t worry I’ll keep it short and crisp.

It was a Bugcrowd private program so can’t disclose the name. Let’s say redacted.com. So *.redacted.com was the scope that means I have a pretty wide scope to hunt on.

I started with Subdomain enumeration and probing using assetfinder, subfinder, and httpx.

1 domain caught my eye which was https://git.infotech.redacted.com. I opened that sub-domain in the browser and saw it was a Gitlab instance which redirected me to its SAML Login page powered by Okta Login. So, only internal users are allowed to log in to that GitLab instance with their company email address (email@redacted.com). I tried some default credentials but no luck!

Okta Login Page

I didn’t give up and jumped on to google to find some juicy stuff. I tried many google dorks but only there wasn’t anything sensitive. After few tries, I used “site:git.infotech.redacted.com ext:env” and found some usernames and group names of that GitLab instance.

Get Anirudh Makkar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I immediately tried https://git.infotech.redacted.com/username and https://git.infotech.redacted.com/groupname and I was able to bypass the authentication flow and directly access the source code present there. I found lots of sensitive data there like SQL credentials and LDAP credentials.

Press enter or click to view image in full size

A big thanks to all of you who helped me and supported me in every possible way.

Here’s what you get from this write-up:

Recon always helps.
If you’re stuck anywhere, just google it.
Keep learning.
Happy Hacking!

You can follow me on: Twitter, LinkedIn, Instagram for more bug bounty tips.
