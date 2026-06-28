---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-05-10_simple-logical-bug-turned-into-a-bounty.md
original_filename: 2021-05-10_simple-logical-bug-turned-into-a-bounty.md
title: Simple logical Bug turned into a bounty
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: da8f73fbfa27a10899549380d7b4cf3dd3181e2ba5256534e74ca8419ab0b0a8
text_sha256: e777ae64a24d18d88ede25129e0d460d9ddb26da30c9cc35625337724be1abe3
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Simple logical Bug turned into a bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-05-10_simple-logical-bug-turned-into-a-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `da8f73fbfa27a10899549380d7b4cf3dd3181e2ba5256534e74ca8419ab0b0a8`
- Text SHA256: `e777ae64a24d18d88ede25129e0d460d9ddb26da30c9cc35625337724be1abe3`


## Content

---
title: "Simple logical Bug turned into a bounty"
url: "https://sndpgiriz.medium.com/simple-logical-bug-turned-into-a-bounty-a3d7ac214606"
authors: ["Sndp Giri"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw"]
bounty: "500"
publication_date: "2021-05-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3665
scraped_via: "browseros"
---

# Simple logical Bug turned into a bounty

Simple logical Bug turned into a bounty
Sndp Giri
Follow
1 min read
·
May 10, 2021

121

Hello all,

It’s me Sandeep Giri again! This is my second valid bug for Facebook Bug Bounty Program. I was rewarded $500 by the Facebook responsible disclosure program. Below is the explanation:

When a user creates a room as part of a group event, the room remains in the group’s rooms list even after the event is deleted. And the group admin cannot delete the room.

Get Sndp Giri’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Reproduction Steps:

A user creates an event with the option Online Video chat with the messenger.
From the admin’s account, the admin deletes the event.
Now, when the admin visits the room tab, the room remains undeleted. The admin doesn’t have any option to delete the room.

Impact

As an admin, she cannot join the room as the button would be disabled unless she has the link to the room. The attacker can invite group members and do a malicious activity or harass the group members.

Bounty Decision by Facebook

Thanks

Happy Learning :)
