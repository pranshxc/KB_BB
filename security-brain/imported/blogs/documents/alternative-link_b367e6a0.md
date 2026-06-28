---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-21_alternative-link.md
original_filename: 2021-12-21_alternative-link.md
title: Alternative link
category: documents
detected_topics:
- mfa
- xss
- command-injection
tags:
- imported
- documents
- mfa
- xss
- command-injection
language: en
raw_sha256: b367e6a06e1ad154b29fd730499f3d606970753bc4104ba5cd06092f6b84568d
text_sha256: ca4dfbfb859df333463d44bc1d76b5df6d190619a153ae606394f1714a2ec0a8
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Alternative link

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-21_alternative-link.md
- Source Type: markdown
- Detected Topics: mfa, xss, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `b367e6a06e1ad154b29fd730499f3d606970753bc4104ba5cd06092f6b84568d`
- Text SHA256: `ca4dfbfb859df333463d44bc1d76b5df6d190619a153ae606394f1714a2ec0a8`


## Content

---
title: "Alternative link"
page_title: "How I earned $$$ by bypassing 2FA - MoTaha"
url: "https://motaha22.github.io/bugbounty/2fa-bounty/"
final_url: "https://motaha22.github.io/bugbounty/2fa-bounty/"
authors: ["Mohamed Taha (@Mohamed12742780)"]
bugs: ["2FA / MFA bypass", "Forced browsing"]
publication_date: "2021-12-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3073
---

# How I earned $$$ by bypassing 2FA 

__less than 1 minute read

#### __On this page

Hi, I would like to share how I was able to bypass 2FA. This is a private program on Hackerone, so we will call it example.com.

### What is 2FA:

2FA is used as another layer of security to prevent Attackers from accessing the account if the attacker stole the password.

### The Vulnerability:

I went to the website and enabled 2FA, then logged out and try to login again.

The website asked to enter the 2FA code and the url was like:
  
  
  https://example.com/react-aspx/Authenticator.aspx
  

An idea came to my mind to enter the url of the dashboard directly which was like:
  
  
  https://example.com/home.aspx
  

and I was able to bypass 2FA and access the account.

Severity: Medium

Bounty: $$$

**__Categories:** [bugbounty](/categories/#bugbounty)

**__Updated:** March 1, 2022

Previous [Next](/bugbounty/bounty/ "How I found XSS vulnerability in Amazon in 5 minutes using shodan
")
