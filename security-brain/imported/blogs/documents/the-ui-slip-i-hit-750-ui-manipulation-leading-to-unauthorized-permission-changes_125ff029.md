---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-02-04_the-ui-slip-i-hit-750-ui-manipulation-leading-to-unauthorized-permission-changes.md
original_filename: 2024-02-04_the-ui-slip-i-hit-750-ui-manipulation-leading-to-unauthorized-permission-changes.md
title: 'The UI Slip I Hit 750$: UI Manipulation Leading to Unauthorized Permission
  Changes'
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
raw_sha256: 125ff0295902139af1fe5c0ce706de7871e01cf29d53806cb8bb940a50e8552c
text_sha256: 87513b2846fa71199acb58c5f092b16fe72740ee83975c51772b616a12ee1ba3
ingested_at: '2026-06-28T07:32:31Z'
sensitivity: unknown
redactions_applied: false
---

# The UI Slip I Hit 750$: UI Manipulation Leading to Unauthorized Permission Changes

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-02-04_the-ui-slip-i-hit-750-ui-manipulation-leading-to-unauthorized-permission-changes.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:31Z
- Redactions Applied: False
- Raw SHA256: `125ff0295902139af1fe5c0ce706de7871e01cf29d53806cb8bb940a50e8552c`
- Text SHA256: `87513b2846fa71199acb58c5f092b16fe72740ee83975c51772b616a12ee1ba3`


## Content

---
title: "The UI Slip I Hit 750$: UI Manipulation Leading to Unauthorized Permission Changes"
page_title: "750$: UI Manipulation Leading to Unauthorized Permission Changes | by Abhi Sharma | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/the-ui-slip-i-hit-750-ui-manipulation-leading-to-unauthorized-permission-changes-d65621d8dd96"
authors: ["Sumit Kumar"]
bugs: ["Privilege escalation", "Client-side enforcement of server-side security"]
bounty: "750"
publication_date: "2024-02-04"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 451
scraped_via: "browseros"
---

# The UI Slip I Hit 750$: UI Manipulation Leading to Unauthorized Permission Changes

Member-only story

750$: UI Manipulation Leading to Unauthorized Permission Changes
Abhi Sharma
Follow
3 min read
·
Feb 4, 2024

566

1

Discover how an U.I mistake allowed unauthorized permission changes in Private Program and bypass the membership requirements. Learn the steps to reproduce this security flaw and its potential impact on platform and user privacy.

Press enter or click to view image in full size

Understanding Target

ExamFront (Virtual name Of a Private Program) stands out as a specialized space for managing deals, partnerships, and collaborations. This platform is designed to streamline the intricate processes involved in deal-making, offering a centralized hub for organizations to orchestrate their business agreements seamlessly.

The Flow

Typically, when a user is created in the organization, they are granted all the default permissions. To remove these permissions, the organization requires the to obtain membership privileges. However, I have identified a flaw that enables an attacker to bypass this requirement and remove the user’s permissions directly through the UI.

The Flaw in the System

At the heart of this issue lies a subtle manipulation of the user interface (UI). The organization and users of the organization can change the permissions without membership by directly enabling the buttons throught the UI. This flaw pertains to the manipulation of the user interface…
