---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-22_page-admin-disclosure-facebook-bug-bounty-2019.md
original_filename: 2019-06-22_page-admin-disclosure-facebook-bug-bounty-2019.md
title: Page Admin Disclosure | Facebook Bug Bounty 2019
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: f7b73e0953d1259000437c180965a539ebe2fee7861dab4b7365c14c33709ce4
text_sha256: b29ca9e95f0e4f9186a48bbde1d31c99ccc3446be6148808549198575e9c06db
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Page Admin Disclosure | Facebook Bug Bounty 2019

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-22_page-admin-disclosure-facebook-bug-bounty-2019.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `f7b73e0953d1259000437c180965a539ebe2fee7861dab4b7365c14c33709ce4`
- Text SHA256: `b29ca9e95f0e4f9186a48bbde1d31c99ccc3446be6148808549198575e9c06db`


## Content

---
title: "Page Admin Disclosure | Facebook Bug Bounty 2019"
url: "https://medium.com/@evilboyajay/page-admin-disclosure-facebook-bug-bounty-2019-ee9920e768eb"
authors: ["Ajay Gautam (@evilboyajay)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
bounty: "1,000"
publication_date: "2019-06-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5189
scraped_via: "browseros"
---

# Page Admin Disclosure | Facebook Bug Bounty 2019

Page Admin Disclosure | Facebook Bug Bounty 2019
Ajay Gautam
Follow
2 min read
·
Jun 22, 2019

394

2

Hello everyone, I have not written a blog for a long time, so I thought of writing it in. Today, I am going to share one of my Facebook valid issue that I discovered in 2019.

Vulnerability Type: Privacy / Authorization

Product Area: Events

Title: Facebook Page admin Disclosure

Vulnerability Description:

While a page admin adds a co-host to some people to their created event then a notification is sent to the user that the page has made him the host of the event. While you will open the event, it will show you like someone (Name of the admin) has invited you to join the event but in actually it was leaking page admin name.

Impact of the Vulnerability:

· Page admin can be disclosed.

· Unauthorizedly an invitation is sent by the page admin to co-host user.

Steps I proceed to reproduce this issue:

1. Create an event from a page

2. Add another account (be sure he/she is not admin of the page) as a co-host in the event.

Get Ajay Gautam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

3. Open another account and click the notification about the co-host.

4. You will see the name of the admin that has added you as a co-host like this

Ajay Gautam invited you

Video POC

Timeline

Initial Report: Feb 11, 2019

Facebook Reproduced/Sent to Product Team: Feb 14, 2019

Fixed: March 18, 2019

Bounty Awarded: March 20, 2019 (1000$)

Press enter or click to view image in full size

Contact Detail

ajay@nassincnepal.com
