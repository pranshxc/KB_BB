---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-17_security-teams-internal-attachments-can-be-exported-via-export-as-zip-feature-on.md
original_filename: 2018-10-17_security-teams-internal-attachments-can-be-exported-via-export-as-zip-feature-on.md
title: Security teams Internal attachments can be exported via 'Export as .zip' feature
  on HackerOne
category: documents
detected_topics:
- command-injection
- information-disclosure
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- business-logic
- api-security
language: en
raw_sha256: 902944bf4476f4524343bd8181c1ae295603dc66cbe71b243ea438a23919d18f
text_sha256: b412cb47a6ec97d4cbec9ec4d7dce306dedd1982d44e4f95e9c76f401b5d55d9
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Security teams Internal attachments can be exported via 'Export as .zip' feature on HackerOne

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-17_security-teams-internal-attachments-can-be-exported-via-export-as-zip-feature-on.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, business-logic, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `902944bf4476f4524343bd8181c1ae295603dc66cbe71b243ea438a23919d18f`
- Text SHA256: `b412cb47a6ec97d4cbec9ec4d7dce306dedd1982d44e4f95e9c76f401b5d55d9`


## Content

---
title: "Security teams Internal attachments can be exported via 'Export as .zip' feature on HackerOne"
url: "https://medium.com/japzdivino/security-teams-internal-attachments-can-be-exported-via-export-as-zip-feature-on-hackerone-35ca6ec2bf8b"
authors: ["Japz Divino (@japzdivino)"]
programs: ["HackerOne"]
bugs: ["Logic flaw"]
bounty: "12,500"
publication_date: "2018-10-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5640
scraped_via: "browseros"
---

# Security teams Internal attachments can be exported via "Export as .zip" feature on HackerOne

Member-only story

Security teams Internal attachments can be exported via “Export as .zip” feature on HackerOne
Japz Divino
Follow
4 min read
·
Oct 17, 2018

104

Severity: High (7.5)
Weakness: Information Disclosure (CWE-200)
Bounty: $12,500

Hello Internet, this blog is about my findings on HackerOne’s own bug bounty program in late 2016, a simple information disclosure in which the HackerOne team decided to reward the highest bounty amount in a single hit/submission so far on their own bug bounty program due its business impact.

Research:

When a program has publicly disclosed a report on HackerOne, the platform supports two kinds of disclosure, Full disclosure and limited disclosure. A Full disclosure (normal disclosure) includes vulnerability information, attachments, and the full timeline of activity. However, a limited disclosure restricts visibility to a summary of the vulnerability and the timeline of activity (comments or actions).

On November 14, 2016 HackerOne releases an awesome feature which the ability to export the disclosed report, you can export the report using View raw text or Export as .zip

View raw text — This will show a text area where you can copy and paste the report timeline.

Export as .zip — This will allow you to download the complete report (including attachments) as a zip archive.

Findings / Submission
