---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-09_a-malicious-editor-of-a-page-can-support-to-a-community-action-which-cant-be-uns.md
original_filename: 2019-07-09_a-malicious-editor-of-a-page-can-support-to-a-community-action-which-cant-be-uns.md
title: A malicious editor of a page can support to a community action which can’t
  be unsupported by the admin!
category: documents
detected_topics:
- sso
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- sso
- access-control
- command-injection
- api-security
language: en
raw_sha256: e2c3cf03abf4dd4ff16d9ac21dc5301603da8152861ed9b5c0ce040597c6d7ff
text_sha256: 9baf976e4adeaea2ddbecd0a0bb7a067bd28ed65c4c2375c3aa61daf64b827c9
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# A malicious editor of a page can support to a community action which can’t be unsupported by the admin!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-09_a-malicious-editor-of-a-page-can-support-to-a-community-action-which-cant-be-uns.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `e2c3cf03abf4dd4ff16d9ac21dc5301603da8152861ed9b5c0ce040597c6d7ff`
- Text SHA256: `9baf976e4adeaea2ddbecd0a0bb7a067bd28ed65c4c2375c3aa61daf64b827c9`


## Content

---
title: "A malicious editor of a page can support to a community action which can’t be unsupported by the admin!"
url: "https://medium.com/@hazzaazi31/a-malicious-editor-of-a-page-can-support-to-a-community-action-which-cant-be-unsupported-by-the-f568c3762042"
authors: ["mAshraf"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2019-07-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5161
scraped_via: "browseros"
---

# A malicious editor of a page can support to a community action which can’t be unsupported by the admin!

A malicious editor of a page can support to a community action which can’t be unsupported by the admin!
mAshraf
Follow
2 min read
·
Jul 9, 2019

60

Facebook is expanding its efforts to retain its users, with a feature called community action which allows users to initiate an idea to advocate an action which may support by other users. then the creator has to tag the community action to the associated government entity. the tag is only implemented when the number of supporters reach 5 supporters of the action. a user that interests to support an action can interact with that community action as either user or on behalf of a page. the pages has roles, at this time, only page admin and page editors can support to a community action. The two roles ( admin and editor ) may not see or agree to support a specific Community action. I mean the editor can go rogue and support an action in which admin may not be admired. so when it comes to roles, of course the admin is super power, and has the ability to refuse or abandon any activity in which he is not admired, to unsupport, in this case, to any community action supported by any page editor in that the admin is not agree to support that community action. contrary to that, there was a vulnerability in which the admin himself abandoning to unsupport to that unwanted community action.

TIMELINE :

21 Feb 2019 : Report sent

25 Feb 2019 : Escalation by Facebook

26 Feb 2019 : Sec Team sent to Product Team

04 Mar 2019 : Facebook asked to confirm patch

05 Mar 2019 : Patch Confirmation sent to Facebook

Get mAshraf’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

05 Mar 2019 : Bounty Awarded by Facebook

IMPACT :

a page editor can support a community action on behalf of a page, and the action cannot be unsupported even by the page admin.

Steps to Reproduce :

1. An editor of a page interacts to a community action as the page ( Facebook allows a user to interact to a community action to either as a user or page if He manages one) “
then he supports to the community action interacting on behalf of the page.

2. Then the admin of the page tries to “Unsupport” to the community action, then an error is displayed! “This Content is no longer Available!” which Implies that he can not unsupport it!

Here is a PoC Video :

More to Follow….
