---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-02-04_facebook-groups-hack.md
original_filename: 2017-02-04_facebook-groups-hack.md
title: Facebook Groups Hack
category: documents
detected_topics:
- access-control
- command-injection
- password-reset
- business-logic
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- password-reset
- business-logic
- mobile-security
language: en
raw_sha256: f1f683749dec40aa445d7800758e043c935f3537a1a09b2f1ceb83d918eabf3e
text_sha256: 0e0b1213ea2ac32bfbed90d1a20fdcd2e7aee8cddce80cbcf82cd8aaacd13b27
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Groups Hack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-02-04_facebook-groups-hack.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, password-reset, business-logic, mobile-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `f1f683749dec40aa445d7800758e043c935f3537a1a09b2f1ceb83d918eabf3e`
- Text SHA256: `0e0b1213ea2ac32bfbed90d1a20fdcd2e7aee8cddce80cbcf82cd8aaacd13b27`


## Content

---
title: "Facebook Groups Hack"
url: "https://medium.com/@zahidali_93675/hijack-facebook-groups-721c08526326"
authors: ["Zahid Ali"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "3,000"
publication_date: "2017-02-04"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6229
scraped_via: "browseros"
---

# Facebook Groups Hack

Zahid Ali
Follow
2 min read
·
Feb 4, 2017

62

Facebook Groups Hack

In 2015, I reported to Facebook that it is possible to deactivate another user’s account through “Account Recovery Form”. This can be accomplished if the account has registered a phone number. Facebook allows users to submit form if they need help to recover account. However, that form was only available for the users who registered their Facebook ID with phone numbers.

I reported that due to account deactivation, a user can lose certain activity on an account.

I got reply from Facebook security member Annalise, that said,

“Locking accounts is intended in some scenarios to
protect users from attack. Thank you for sharing this information with
us. Although this issue does not qualify as a part of our bounty
program we appreciate your report. We will follow up with you on any
security bugs or with any further questions we may have.”

Same year, another researcher reported that, if a group has one admin and the admin account is deactivated, any member can become an admin of this group. Facebook rejected that bug and said,

Get Zahid Ali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

“On the deactivation page, we warn users that due to account deactivation they will lose the groups”

So, in 2016 I merged these 2 rejected report(s) and sent it to Facebook that due to account deactivation by attacker, victim will lose all the groups.

Here is the POC video.

They accepted and I got a bounty from Facebook. :)
