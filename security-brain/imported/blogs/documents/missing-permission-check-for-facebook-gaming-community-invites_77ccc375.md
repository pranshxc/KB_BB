---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-01_missing-permission-check-for-facebook-gaming-community-invites.md
original_filename: 2021-08-01_missing-permission-check-for-facebook-gaming-community-invites.md
title: Missing permission check for Facebook gaming community invites
category: documents
detected_topics:
- access-control
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- access-control
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 77ccc375dc4be180747a1ff847d80e3338d974635a37e7ca4814da86ae24e114
text_sha256: 7aad5e8643a37980681fa317bac2f65bb29b1dbddaf6b1dc00684cf47d915313
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Missing permission check for Facebook gaming community invites

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-01_missing-permission-check-for-facebook-gaming-community-invites.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `77ccc375dc4be180747a1ff847d80e3338d974635a37e7ca4814da86ae24e114`
- Text SHA256: `7aad5e8643a37980681fa317bac2f65bb29b1dbddaf6b1dc00684cf47d915313`


## Content

---
title: "Missing permission check for Facebook gaming community invites"
page_title: "Missing permission check for Facebook gaming community invites - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/missing-permission-check-for-facebook-gaming-community-invites/"
final_url: "https://philippeharewood.com/missing-permission-check-for-facebook-gaming-community-invites/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure", "Broken authorization"]
publication_date: "2021-08-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3456
---

Posted on [August 1, 2021August 21, 2021](https://philippeharewood.com/missing-permission-check-for-facebook-gaming-community-invites/)

# Missing permission check for Facebook gaming community invites

Facebook allows a user or page (gaming creator) to delegate users as community managers (CM) for moderating comments on live gaming videos. When a user invites a person as a CM, this will add the person to a pending community manager list. It’s assumed that the pending list should be private and known only to the creator and those invited. This was based on previous work at https://philippeharewood.com/missing-permission-check-when-viewing-pending-gaming-community-manager-list/

A user’s list of incoming gaming community invites (community_manager_invite_profiles) are disclosed

**Timeline**

Aug 1, 2021 – Report sent  
Aug 5, 2021 – Fixed by Facebook
