---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-20_change-any-link-at-httpsfbwatch.md
original_filename: 2020-05-20_change-any-link-at-httpsfbwatch.md
title: Change any link at https://fbwat.ch/
category: documents
detected_topics:
- access-control
- command-injection
- otp
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- otp
- business-logic
language: en
raw_sha256: 0b243b5ab33f80b16e183ae4870bb743821c01029b6a98123e084f5d58b9e563
text_sha256: 1ba511ed4292565e364d1c9bad2df1220d7ef63960f1e458599c362b142a26e0
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Change any link at https://fbwat.ch/

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-20_change-any-link-at-httpsfbwatch.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, business-logic
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `0b243b5ab33f80b16e183ae4870bb743821c01029b6a98123e084f5d58b9e563`
- Text SHA256: `1ba511ed4292565e364d1c9bad2df1220d7ef63960f1e458599c362b142a26e0`


## Content

---
title: "Change any link at https://fbwat.ch/"
page_title: "Change any link at https://fbwat.ch/ - These aren't the access_tokens you're looking for"
url: "https://philippeharewood.com/change-any-link-at-https-fbwat-ch/"
final_url: "https://philippeharewood.com/change-any-link-at-https-fbwat-ch/"
authors: ["Philippe Harewood (@phwd)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "1,000"
publication_date: "2020-05-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4570
---

Posted on [May 20, 2020](https://philippeharewood.com/change-any-link-at-https-fbwat-ch/)

# Change any link at https://fbwat.ch/

There is a call to update fbwat.ch short links for viewing videos at Facebook Watch. It was really flexible so much so that it was possible to redirect `https://fbwat.ch/1` to `https://www.facebook.com/nike`. This also means I can change any existing urls created for https://fbwat.ch/ urls.  
  
There is a utility feature available in the mobile share popup and sharing overlay under the Facebook video sharing plugin that allowed shorts urls to be created via the fbwat.ch domain.  
  
There was a second call if the user opted to update the url after creation, this call allowed one to overwrite any fbwat.ch url  
  
`new AsyncRequest('/update_fbwatch_short_url/').setData({destination_url:'https://www.facebook.com/nike',short_url:'https://fbwat.ch/1'}).send()`  
  
**Impact** (A verbatim explanation of the bounty by Facebook):  
  
Anyone can update the target URL of existing `https://fbwat.ch/` links.  
  
**Timeline**

May 20, 2020 – Report sent  
May 20, 2020 – Confirmation of submission by Facebook  
Jun 5, 2020 – Confirmation of patch by Facebook  
Jun 11, 2020 – $1000 Bounty awarded by Facebook
