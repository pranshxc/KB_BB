---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-24_bug-bounty-fastmail-topicboxcom-privileges-escalation-organization-takeover.md
original_filename: 2021-09-24_bug-bounty-fastmail-topicboxcom-privileges-escalation-organization-takeover.md
title: 'Bug-Bounty | FASTMAIL [topicbox.com: Privileges Escalation > Organization
  Takeover]'
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
language: en
raw_sha256: a2abfdb72a98e8a3e1f0ce6a0dff7566239bcb12e2f251137a9ad8732629e1d1
text_sha256: 1488e15dcd5bc960c33c67527836461c8745687f0cf0cda24f96371d2db87888
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Bug-Bounty | FASTMAIL [topicbox.com: Privileges Escalation > Organization Takeover]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-24_bug-bounty-fastmail-topicboxcom-privileges-escalation-organization-takeover.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `a2abfdb72a98e8a3e1f0ce6a0dff7566239bcb12e2f251137a9ad8732629e1d1`
- Text SHA256: `1488e15dcd5bc960c33c67527836461c8745687f0cf0cda24f96371d2db87888`


## Content

---
title: "Bug-Bounty | FASTMAIL [topicbox.com: Privileges Escalation > Organization Takeover]"
url: "https://medium.com/@the.white.soul.0/bug-bounty-fastmail-topicbox-com-privileges-escalation-organization-takeover-815466876ad4"
authors: ["Mohammed ELdawody"]
programs: ["Fastmail"]
bugs: ["Privilege escalation", "Logic flaw"]
publication_date: "2021-09-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3290
scraped_via: "browseros"
---

# Bug-Bounty | FASTMAIL [topicbox.com: Privileges Escalation > Organization Takeover]

Bug-Bounty | FASTMAIL [topicbox.com: Privileges Escalation > Organization Takeover]
Mohammed Eldawody
Follow
2 min read
·
Sep 24, 2021

29

Hi everyone

I would like to share with you one of my findings in Fastmail company, I was able to find an account takeover vulnerability in one of their sites “topicbox.com”

First I will explain how the site works.
The site provides a service where you create your own organization EXAMPLE.topicbox.com and create groups of people with different privileges

Each organization contains many groups and many users with different privileges.

There are 4 different permissions

1. Owner
2. Admin
3. Moderator
4. Member

Only owners of the organization can create Groups and make other users owners
Permissions are separated for each group, for example, I can be an admin in group 1 and be a member in group 2

— — — — — — — — — — — — — — — — — —

Get Mohammed Eldawody’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After searching and understanding how the site works I found the following:

We can break the access controls and escalate ourselves from admin to owner by sending this request #V1

Then after searching for a while I found this in the response body:

“isEnternal” I found that I can change it while I have ‘member’ permission.

But what does it do? after testing and looking around I found that

isEnternal is a feature that allows users to create their own groups. and automatically the creator will be the admin of the group

Using the vulnerability #V1 and this one I was able to take over any organization by doing the following

1. Join any organization as a member
2. Change “isEnternal”:false to true in my account data
3. Create a group and I will atomically be an admin in it
4. Make myself an owner. and by doing that I can remove anyone and do anything I want.

Thank you for reading and wish the ideas in this report will help you someday

Mohammed Eldawody
Discord: MoEldawody#4147
