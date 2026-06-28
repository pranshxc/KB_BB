---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-08_view-the-contact-list-for-a-messenger-kid-as-a-parent-approved-contact.md
original_filename: 2019-01-08_view-the-contact-list-for-a-messenger-kid-as-a-parent-approved-contact.md
title: View the contact list for a Messenger Kid as a parent-approved contact
category: documents
detected_topics:
- access-control
- command-injection
- otp
- graphql
tags:
- imported
- documents
- access-control
- command-injection
- otp
- graphql
language: en
raw_sha256: 4c9428c392c721a79457b7e62cc4f6a5253ced7abb8147c593a2ad9fb0531bdd
text_sha256: b83bf4b606c16bfd80f5fa1b48c8e519de908fdf05ecb30c395da118ad0ba674
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# View the contact list for a Messenger Kid as a parent-approved contact

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-08_view-the-contact-list-for-a-messenger-kid-as-a-parent-approved-contact.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, graphql
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `4c9428c392c721a79457b7e62cc4f6a5253ced7abb8147c593a2ad9fb0531bdd`
- Text SHA256: `b83bf4b606c16bfd80f5fa1b48c8e519de908fdf05ecb30c395da118ad0ba674`


## Content

---
title: "View the contact list for a Messenger Kid as a parent-approved contact"
page_title: "View the contact list for a Messenger Kid as a parent-approved contact - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/view-the-contact-list-for-a-messenger-kid-as-a-parent-approved-contact/"
final_url: "https://philippeharewood.com/view-the-contact-list-for-a-messenger-kid-as-a-parent-approved-contact/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2019-01-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5481
---

Posted on [January 8, 2019](https://philippeharewood.com/view-the-contact-list-for-a-messenger-kid-as-a-parent-approved-contact/)

# View the contact list for a Messenger Kid as a parent-approved contact

[Messenger Kids](https://messengerkids.com/) is a messaging app for parents to moderate how kids contact friends and family. Parents can approve contacts in their list to talk to their child. However because the contact is now approved, this means that the approved user can now see all parent-approved contacts for the child.

Messenger Kids is a gated feature, to reproduce for a user check the following URL <https://www.facebook.com/messenger_kids/> for a quick test to see if it’s enabled. From there, if you are testing on your own, you will first need to create an account for the child then add the contact as the prerequisites.

Given a child for an approved contact, request the list in [GraphQL](https://www.facebook.com/notes/phwd/a-facebook-graphql-crash-course/1189337427822946/)
  
  
  node(kid_id) {  
  neo_approved_connections {  
  nodes {  
  id,  
  name  
  }  
  }  
  }

Going through the help section [https://messengerkids.com/](https://messengerkids.com/?fbclid=IwAR38KI3GxIV6JPPm3bboY4OAWl4xfqwLpboHT9ufQcdwTOMBpuGIqhqk4sc) didn’t provide any hints that this was intentional.

Timeline

Jan 8, 2019 – Report sent  
Jan 11, 2019 – Confirmation of submission by Facebook  
Aug 30, 2019 – Confirmation of patch by Facebook  
Sep 5, 2019 – Bounty awarded by Facebook
