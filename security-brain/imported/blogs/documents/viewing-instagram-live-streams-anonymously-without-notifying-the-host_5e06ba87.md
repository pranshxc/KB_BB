---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-02_viewing-instagram-live-streams-anonymously-without-notifying-the-host.md
original_filename: 2022-09-02_viewing-instagram-live-streams-anonymously-without-notifying-the-host.md
title: Viewing Instagram live streams anonymously without notifying the host
category: documents
detected_topics:
- idor
- command-injection
- business-logic
- mobile-security
tags:
- imported
- documents
- idor
- command-injection
- business-logic
- mobile-security
language: en
raw_sha256: 5e06ba8735e881be494dc2bd71540958b5a50bdecb34fbf439f8a02985de8a3e
text_sha256: 6c3ab1162e22f25f7ad7475b1ec5c7153a152e402df2de1ed167e54b5864eca0
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Viewing Instagram live streams anonymously without notifying the host

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-02_viewing-instagram-live-streams-anonymously-without-notifying-the-host.md
- Source Type: markdown
- Detected Topics: idor, command-injection, business-logic, mobile-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `5e06ba8735e881be494dc2bd71540958b5a50bdecb34fbf439f8a02985de8a3e`
- Text SHA256: `6c3ab1162e22f25f7ad7475b1ec5c7153a152e402df2de1ed167e54b5864eca0`


## Content

---
title: "Viewing Instagram live streams anonymously without notifying the host"
page_title: "[#0015] Viewing Instagram live streams anonymously without notifying the host | feed"
url: "https://feed.bugs.xdavidhu.me/bugs/0015"
final_url: "https://feed.bugs.xdavidhu.me/bugs/0015"
authors: ["David Schütz (@xdavidhu)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR", "Logic flaw", "Privacy issue"]
publication_date: "2022-09-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2224
---

#0015  
Vendor: Meta  
Status: wont-fix  
Reported: May 01, 2022  
Disclosed: Sep 02, 2022 (124 days) 

# Viewing Instagram live streams anonymously without notifying the host

**Description/Impact:**

An attacker can set up a rule to drop all requests the Instagram app is making to `/api/v1/live/[broadcast_id]/heartbeat_and_get_viewer_count/` and join a livestream. Since all heartbeat requests will fail, the host will not get notified that attacker joined the livestream, and the viewer count will not increase. Meanwhile the attacker will have full access to the livestream, anonymously.

I tested the attack on private “practice” livestream. I assume the behaviour is the same on a public live stream. Exploiting this bug on a private “practice” livestream is more impactful than on a public one.

The attacker could watch the livestream while the host assumes that the attacker is not there. If there are no other viewers, the host will assume he/she is still alone in the livestream, even though the attacker is watching.

**Repro Steps:**

Mobile app version: 232.0.0.16.114

[setup]

  0. Create 2 instagram users: Victim & Attacker
  1. Message each other & approve the message requests, so that the users can freely send messages to each other

[repro]

  1. [Victim] Open the new live stream UI and set the audience (eye icon) to “Practice”
  2. [Victim] Start the live stream
  3. [Victim] Click the share icon and send the live stream to Attacker (this is necessary because its a “Practice” live. As i mentioned before this should work on public lives as well.)
  4. [Attacker] Start proxying the requests with Burp, and set up a new “Match and replace” rule under `Proxy` -> `Options`. Set Type to `Request header`, match to `heartbeat_and_get_viewer_count` and replace to `heartbeat_and_get_viewer_counts`
  5. [Attacker] Open the message Victim sent in Step 3. and click on the live stream
  6. [Attacker] Watch the livestream anonymously while for Victim it looks like he/she is in the live stream alone

_This report has been part of the Meta BountyConEDU 2022 live hacking event in Madrid, Spain._

* * *

### Discussion:

**Vendor - 2022-05-01**

Hi Dávid,

Thank you for the report. The viewer count isn’t meant to be a security or a privacy measure nor guarantee accuracy. For the case of private “practice” live case, the victim would not send the link of their live if they want don’t want any one else to see it. For the case of public live - lives are meant to be watched by people so it doesn’t really matter if someone can watch it “anonymously”. As such, I am going to close the report, but look forward to receiving more reports from you :)

Thanks,  
_[redacted]_  
Security engineer

* * *

**Me - 2022-05-01**

Hi _[redacted]_ ,

I disagree, I think this is a privacy issue. Here is why I think that:

I was able to reproduce that the host can’t see the attacker when clicking his/her username on the top left corner. On that screen all viewers should be visible. This means that the host can’t even remove the attacker from the livestream.

This allows the attacker to anonymously snoop on a livestream indefinitely, without the victim knowing, which is a privacy issue.

Thank you,  
David

* * *

**Me - 2022-05-01**

An example scenario:

  1. Victim starts a new practice livestream
  2. Victim invites 10 people to the stream
  3. One person joins, they start to talk one-on-one, while waiting for others to join, expecting they are alone
  4. Attacker snoops on the livestream, potentially leaking sensitive conversations/content

The example is similar to a Google Meet / Zoom call. Even though you join a call with a public link, you trust the user interface to inform you about who is in the call with you.

Thank you,  
David

* * *

**Vendor - 2022-05-01**

Hi Dávid, When someone has a live session, it should be assumed that their actions are recorded and live streamed, therefore privacy cannot be expected. If a user wants no one to see or hear them, they should not do a live stream or turn off the live stream, camera or microphone.

Thanks,

_[redacted]_ , Security
