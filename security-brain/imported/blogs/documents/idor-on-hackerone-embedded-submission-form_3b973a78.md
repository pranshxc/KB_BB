---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-19_idor-on-hackerone-embedded-submission-form.md
original_filename: 2024-06-19_idor-on-hackerone-embedded-submission-form.md
title: IDOR on HackerOne Embedded Submission Form
category: documents
detected_topics:
- idor
- access-control
- command-injection
- graphql
tags:
- imported
- documents
- idor
- access-control
- command-injection
- graphql
language: en
raw_sha256: 3b973a78b0f17466896de2385e4b2788ce4681f5cdb69fc0e08ce1bb6cdc99b1
text_sha256: d3f8ba3f8e1eea3ab944538c20ce0a08a6b4b94c3c29147f0641d422318a9d88
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR on HackerOne Embedded Submission Form

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-19_idor-on-hackerone-embedded-submission-form.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, graphql
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `3b973a78b0f17466896de2385e4b2788ce4681f5cdb69fc0e08ce1bb6cdc99b1`
- Text SHA256: `d3f8ba3f8e1eea3ab944538c20ce0a08a6b4b94c3c29147f0641d422318a9d88`


## Content

---
title: "IDOR on HackerOne Embedded Submission Form"
url: "https://medium.com/pinoywhitehat/idor-on-hackerone-embedded-submission-form-9e59c6f044b3"
authors: ["Japz Divino (@japzdivino)"]
programs: ["HackerOne"]
bugs: ["IDOR", "GraphQL"]
bounty: "2,500"
publication_date: "2024-06-19"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 240
scraped_via: "browseros"
---

# IDOR on HackerOne Embedded Submission Form

Member-only story

IDOR on HackerOne Embedded Submission Form
Japz Divino
Follow
6 min read
·
Jun 19, 2024

850

10

Severity: Low (3.7) — Medium (4.4)
Weakness: Improper Access Control
Bounty: $2,500

Hey hackers! Hope you are all doing well :)
I just wanna share again my recent finding which is in limited disclosure so I am creating a write up to give more details and context. Please note that I will be redacting sensitive information that belongs to a private program.

I found an Insecure Direct Object Reference (IDOR) vulnerability that allows me to access sensitive information from private program such as intro text, response efficiency percentage, and structured scopes using the embedded submission form of HackerOne.

The following GraphQL below is used to fetch information

POST /graphql?embedded_submission_form_uuid=<UUID> HTTP/2
Host: hackerone.com
Cookie: <REDACTED>
<SNIP>
<SNIP

{
  "operationName": "EmbeddedSubmissionPage",
  "variables": {
  "uuid": "<UUID>",
  "product_area": "emdedded_submission_form",
  "product_feature": "submission_page"
  },
  "query": "query EmbeddedSubmissionPage($uuid: String!) {\n  me {\n  id\n  signal\n  reputation\n  __typename\n  }\n  embedded_submission_form(uuid: $uuid) {\n  id\n  promotionEnabled: promotion_enabled\n  typeface\n  accent_color\n  accent_text_color\n  link_color\n  button_color\n  button_text_color\n  team {\n  id\n  handle\n  name\n  abuse\n  offers_bounties\n  report_submission_form_intro\n  customized_report_template\n…
