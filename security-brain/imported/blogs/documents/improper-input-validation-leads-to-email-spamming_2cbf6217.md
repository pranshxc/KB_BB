---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-27_improper-input-validation-leads-to-email-spamming.md
original_filename: 2022-08-27_improper-input-validation-leads-to-email-spamming.md
title: Improper Input Validation Leads To Email Spamming
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 2cbf6217178fb38b2af81579574cf809a13dbe90d4a1ccbe3af00440c1f66ade
text_sha256: 9a2e34438192ce4be2570838e0af38a3d545e84e12f6f0bae6c7de737c6cf37b
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Improper Input Validation Leads To Email Spamming

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-27_improper-input-validation-leads-to-email-spamming.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `2cbf6217178fb38b2af81579574cf809a13dbe90d4a1ccbe3af00440c1f66ade`
- Text SHA256: `9a2e34438192ce4be2570838e0af38a3d545e84e12f6f0bae6c7de737c6cf37b`


## Content

---
title: "Improper Input Validation Leads To Email Spamming"
url: "https://akshayravic09yc47.medium.com/improper-input-validation-leads-to-email-spamming-5d1a53b2a579"
authors: ["Akshay Ravi (@AKSHAYC09YC47)"]
bugs: ["Email content injection"]
publication_date: "2022-08-27"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2255
scraped_via: "browseros"
---

# Improper Input Validation Leads To Email Spamming

Improper Input Validation Leads To Email Spamming(Hyper link injection)
Akshay Ravi
Follow
2 min read
·
Aug 27, 2022

95

2

Hi Guys, In this article, I will share how did I found Improper Input Validation Leads To Email Spamming on my target (redacted.com)

So while i was testing on the target as usual there were option to edit our first and last name on the profile. so when i tested on that function i noticed that there were no input character limit and i was thinking like what i can do rather that DOS!!!

Press enter or click to view image in full size

So i started searching for any other interesting endpoints and suddenly one of the function caught me up.There was a option to invite other users via email, so when we try to invite any other user, they will receive mail like this

Press enter or click to view image in full size

So When i checked the invitation mail i noticed that instead of username, my first and last were showing, So i was thinking like what if i changed my first and last name to any other spam message !!.So i edited the first & last name to like this

Press enter or click to view image in full size

After changing the names, again used the invite function and i have received mail like this

Press enter or click to view image in full size

The email was received from their official support centre mail ID. and the interesting part was, i’m able to invite an existing user also, the domain were not validating the user whether they exists or not, so by this way i can do spamming, phishing etc via their support mail id

Get Akshay Ravi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So i reported this directly to the company.

2022 Aug 25: Reported

2022 Aug 26: Marked As Duplicate

THANKS🙏
