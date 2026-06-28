---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-18_bugcrowd-report.md
original_filename: 2022-06-18_bugcrowd-report.md
title: Bugcrowd report
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: c46e63cdd245face2bdf9e48f5d2566d70b7cae3f4053ef1c4404574146521fd
text_sha256: 309e1b5926edc6c1422f97310627b56f622bed5b80123a1a5bbf7d765548ad09
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Bugcrowd report

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-18_bugcrowd-report.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `c46e63cdd245face2bdf9e48f5d2566d70b7cae3f4053ef1c4404574146521fd`
- Text SHA256: `309e1b5926edc6c1422f97310627b56f622bed5b80123a1a5bbf7d765548ad09`


## Content

---
title: "Bugcrowd report"
page_title: "Asana Desktop Application Includes Personal Access Token - CrowdStream - Bugcrowd"
url: "https://bugcrowd.com/disclosures/caf10f76-f1fb-4dea-8434-9ed2c56a40bb/asana-desktop-application-includes-personal-access-token"
final_url: "https://bugcrowd.com/disclosures/caf10f76-f1fb-4dea-8434-9ed2c56a40bb/asana-desktop-application-includes-personal-access-token"
authors: ["Lauritz Holtmann (@_lauritz_)"]
programs: ["Asana"]
bugs: ["Information disclosure", "Hardcoded credentials"]
bounty: "6,100"
publication_date: "2022-06-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2536
---

##### Summary by Asana

@lauritz discovered sensitive credentials bundled in our Asana Desktop for Mac application. Within hours of @lauritz's report, we revoked and rotated the credentials on our end. Following that we determined the root cause and in the subsequent days deployed mitigations and improved our build process to prevent similar issues in the future. Thanks @lauritz!
