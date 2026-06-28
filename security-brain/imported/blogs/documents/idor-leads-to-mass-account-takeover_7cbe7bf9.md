---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-02-12_idor-leads-to-mass-account-takeover.md
original_filename: 2023-02-12_idor-leads-to-mass-account-takeover.md
title: IDOR Leads to MASS Account Takeover
category: documents
detected_topics:
- idor
- access-control
- command-injection
- password-reset
- automation-abuse
tags:
- imported
- documents
- idor
- access-control
- command-injection
- password-reset
- automation-abuse
language: en
raw_sha256: 7cbe7bf966b76ed4898d62339f501c3569335e8ee244ca7f84004c39fa3dd188
text_sha256: 0a7cc3cff49a8efa6c967eb3a151e9076527f0b91f2ee475b17549c6e2a6ca43
ingested_at: '2026-06-28T07:32:18Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR Leads to MASS Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-02-12_idor-leads-to-mass-account-takeover.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, password-reset, automation-abuse
- Ingested At: 2026-06-28T07:32:18Z
- Redactions Applied: False
- Raw SHA256: `7cbe7bf966b76ed4898d62339f501c3569335e8ee244ca7f84004c39fa3dd188`
- Text SHA256: `0a7cc3cff49a8efa6c967eb3a151e9076527f0b91f2ee475b17549c6e2a6ca43`


## Content

---
title: "IDOR Leads to MASS Account Takeover"
url: "https://yaseenzubair.medium.com/idor-leads-to-mass-account-takeover-7548a03f5672"
authors: ["Yaseen Zubair"]
bugs: ["IDOR", "Account takeover"]
publication_date: "2023-02-12"
added_date: "2023-02-13"
source: "pentester.land/writeups.json"
original_index: 1543
scraped_via: "browseros"
---

# IDOR Leads to MASS Account Takeover

IDOR Leads to MASS Account Takeover
Yaseen Zubair
Follow
2 min read
·
Feb 12, 2023

130

In most web applications, there is a high prevalence of misconfiguration problems, particularly with regard to authorization. While testing a private program, I noticed the user_id cookie and thought to experiment by altering its value using both Burp Suite and the Chrome extension, EditThisCookie as it was a 6-digit numeric value. Unfortunately, my efforts to impersonate other users were unsuccessful.

Get Yaseen Zubair’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Next, I attempted to search for an IDOR vulnerability by altering the cookie in the request. To my surprise, I was successful in this endeavor.

Testing Scenario:

I created two test accounts.
I initiated the request to change my email but intercepted the request with burp suite.
I modified the value of the user_id cookie to match that of my second account’s cookie.
Also, Email has to be new, and nonexistent on the server, so I used burp collaborator as my temporary email server, as check@xx.burpcolab.net
The request was successful.
To gain access to the victim’s account, initiate a forgot password request to your own email, for example check@xx.burpcolab.net
Use that forgot password link to change password and takeover victim’s account.
Press enter or click to view image in full size

The problem with this attack is that the attacker can not determine whose account to compromise, because there is no way of determining the user id of your victim. So the attacker can cause mass account lock-outs by changing the email of every user on the server by brute-forcing the cookie value.

Hope you have benefitted from this read,
Have a great day!
