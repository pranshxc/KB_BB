---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-18_accessing-restricted-documents-with-extra-json-body-content.md
original_filename: 2021-06-18_accessing-restricted-documents-with-extra-json-body-content.md
title: Accessing Restricted Documents With Extra JSON Body Content
category: documents
detected_topics:
- api-security
- access-control
- command-injection
tags:
- imported
- documents
- api-security
- access-control
- command-injection
language: en
raw_sha256: 285da192968ab808838f7930937cf64ef6ba79dcc60aae7bb40b29a1ef61d9f9
text_sha256: b7f2ccb5d18e2227e73f9eefa952903e01aa2115dc48615b128d8cf8b6cae2af
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Accessing Restricted Documents With Extra JSON Body Content

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-18_accessing-restricted-documents-with-extra-json-body-content.md
- Source Type: markdown
- Detected Topics: api-security, access-control, command-injection
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `285da192968ab808838f7930937cf64ef6ba79dcc60aae7bb40b29a1ef61d9f9`
- Text SHA256: `b7f2ccb5d18e2227e73f9eefa952903e01aa2115dc48615b128d8cf8b6cae2af`


## Content

---
title: "Accessing Restricted Documents With Extra JSON Body Content"
url: "https://imranhudaa.medium.com/accessing-restricted-documentswith-extra-json-body-content-c59bc7224189"
authors: ["Imran Huda (@imranHudaA)"]
bugs: ["Mass assignment", "Broken authorization"]
bounty: "500"
publication_date: "2021-06-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3561
scraped_via: "browseros"
---

# Accessing Restricted Documents With Extra JSON Body Content

Accessing Restricted Documents With Extra JSON Body Content
Imran Huda
Follow
2 min read
·
Jun 17, 2021

299

2

The issue I’m going to share with you guys is few months old but recently I have found same issue on the program while I was re-checking my fixed issues. The program is private on Bugcrowd I’m not going to share such information that discloses the program. The program allows user’s to send,edit and manage documents easily within a team.

I have used two accounts here one is Admin and other is normal account.

I have created a document from Admin account and was trying to access the document from normal account without giving the access to the document.But sadly every api endpoint was giving me 403 error.

From the normal account while editing own account document I have noticed that the request had documentId in the json body.

While creating a blank document I thought to add the Admin documentId in the json request body

Here is the normal request :

POST /api/accounts/envelope/ HTTP/1.1

Host: redacted.com

{“enableResponsiveChoice”:false,”emailBlurb”:null,”emailSubject”:null,”autoNavigation”:false,”status”:”created”,”notification”:{“useAccountDefaults”:true}}

Notice that the request don’t have documentId

Get Imran Huda’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After adding the documentId in the request :

POST /api/accounts/envelope/ HTTP/1.1

Host: redacted.com

{“enableResponsiveChoice”:false,”emailBlurb”:null,”emailSubject”:null,”autoNavigation”:false,”status”:”created”,”notification”:{“useAccountDefaults”:true},”documentId”:”documentIdofAdmin”}

After making the request a new document is created with Admin document information.

Sadly this was only exploitable between own team members.

Later I have discovered several issue by using the same technique.

Press enter or click to view image in full size
***

Hope you enjoyed reading.
