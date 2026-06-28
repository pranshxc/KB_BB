---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-21_open-redirection-into-bentley-system.md
original_filename: 2022-04-21_open-redirection-into-bentley-system.md
title: Open Redirection into Bentley System
category: documents
detected_topics:
- oauth
- xss
- command-injection
tags:
- imported
- documents
- oauth
- xss
- command-injection
language: en
raw_sha256: d43b9c5551884eaab683017c8d266ecbcd7dbb4a709e61c947fda5164430b92b
text_sha256: b8cae563b9ad6d00a5f5d378d70cd49d34d1562355cc8ac1fb86dc12704f21bf
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Open Redirection into Bentley System

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-21_open-redirection-into-bentley-system.md
- Source Type: markdown
- Detected Topics: oauth, xss, command-injection
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `d43b9c5551884eaab683017c8d266ecbcd7dbb4a709e61c947fda5164430b92b`
- Text SHA256: `b8cae563b9ad6d00a5f5d378d70cd49d34d1562355cc8ac1fb86dc12704f21bf`


## Content

---
title: "Open Redirection into Bentley System"
url: "https://amit-lt.medium.com/open-redirection-into-bentley-system-d1ee188bfb25"
authors: ["Amit Kumar (@Amitlt2)"]
programs: ["Bentley Systems"]
bugs: ["XSS"]
publication_date: "2022-04-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2693
scraped_via: "browseros"
---

# Open Redirection into Bentley System

Open Redirection into Bentley System
Amit Kumar Biswas @Amitlt2
Follow
2 min read
·
Apr 21, 2022

30

1

Hello, Hackers Welcome to another write-up where I have shared a scenario of Open Redirection…

Press enter or click to view image in full size

Let's understand what is open redirection vulnerability:

An Open Redirection is when a web application or server uses a user-submitted link to redirect the user to a given website or page. Even though it seems like a harmless action, to let a user decide on which page he wants to be redirected to if exploited such a technique can have a serious impact, especially when combined with other vulnerabilities and tricks.

During my testing, I discovered a subdomain and I just search on google but was not able to find anything….:(

Press enter or click to view image in full size

I just open paramspider and fuzz for parameters suddenly I came out with one parameter which is post redirect URI path which is vulnerable to open redirection.

Affected Uri:- *.bentley.com/connect/endsession?post_logout_redirect_uri=https://attacker.com

post_logout_redirect_uri= is vulnerable

Understand the impact of open redirection

A user will be triggered by XSS attacks.

Phishing Attack.

Shared a Video Proof of Concept where you’ll be able to understand the attack.

Get Amit Kumar Biswas @Amitlt2’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Youtube:- https://youtu.be/mGePGEVT3XU

Thanks for taking the time to read my write-up and share it with your friends, Like & Follow for more updates.

Follow me:

Instagram

Twitter

Facebook

LinkedIn
