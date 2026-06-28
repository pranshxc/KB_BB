---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-21_how-i-earned-by-bypassing-2fa.md
original_filename: 2021-12-21_how-i-earned-by-bypassing-2fa.md
title: How I earned $$$ by bypassing 2FA
category: documents
detected_topics:
- mfa
- command-injection
tags:
- imported
- documents
- mfa
- command-injection
language: en
raw_sha256: f07b544cca35ac6b872811b583354d3de36578b06fe8a6825190574588aa8ae8
text_sha256: eab4316cd7506a19a9831d4cf19789b1d0907fc5b1fbe9efa97b53eb36b86bdb
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I earned $$$ by bypassing 2FA

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-21_how-i-earned-by-bypassing-2fa.md
- Source Type: markdown
- Detected Topics: mfa, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `f07b544cca35ac6b872811b583354d3de36578b06fe8a6825190574588aa8ae8`
- Text SHA256: `eab4316cd7506a19a9831d4cf19789b1d0907fc5b1fbe9efa97b53eb36b86bdb`


## Content

---
title: "How I earned $$$ by bypassing 2FA"
url: "https://medium.com/@mohamedtaha_42562/how-i-earned-by-bypassing-2fa-b5487942a86d"
authors: ["Mohamed Taha (@Mohamed12742780)"]
bugs: ["2FA / MFA bypass", "Forced browsing"]
publication_date: "2021-12-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3073
scraped_via: "browseros"
---

# How I earned $$$ by bypassing 2FA

How I earned $$$ by bypassing 2FA
Mohamed Taha
Follow
Dec 21, 2021

26

Hi, I would like to share how I was able to bypass 2FA. This is a private program on Hackerone, so we will call it example.com.

What is 2FA:

2FA is used as another layer of security to prevent Attackers from accessing the account if the attacker stole the password.

The Vulnerability:

I went to the website and enabled 2FA, then logged out and try to login again.

Get Mohamed Taha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The website asked to enter the 2FA code and the url was like:

https://example.com/react-aspx/Authenticator.aspx

An idea came to my mind to enter the url of the dashboard directly which was like:

https://example.com/home.aspx

and I was able to bypass 2FA and access the account.

Severity: Medium

Bounty: $$$

Facebook: https://facebook.com/mohamedtaha2001/

Twitter: https://twitter.com/Mohamed12742780

Thank you..
