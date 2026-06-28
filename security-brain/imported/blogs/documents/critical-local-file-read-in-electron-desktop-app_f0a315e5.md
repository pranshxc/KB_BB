---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-17_critical-local-file-read-in-electron-desktop-app.md
original_filename: 2022-08-17_critical-local-file-read-in-electron-desktop-app.md
title: Critical Local File Read in Electron Desktop App
category: documents
detected_topics:
- command-injection
- path-traversal
tags:
- imported
- documents
- command-injection
- path-traversal
language: en
raw_sha256: f0a315e55155af3163b294d51c414688746a2895af1e3507e6e86383ade4dbfb
text_sha256: c534181383f0d40e9d26a80ee4679d72f8c11bb99b50396251d49227bed4e847
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# Critical Local File Read in Electron Desktop App

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-17_critical-local-file-read-in-electron-desktop-app.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `f0a315e55155af3163b294d51c414688746a2895af1e3507e6e86383ade4dbfb`
- Text SHA256: `c534181383f0d40e9d26a80ee4679d72f8c11bb99b50396251d49227bed4e847`


## Content

---
title: "Critical Local File Read in Electron Desktop App"
page_title: "Critical Local File Read in Electron Desktop App - CrowdStream - Bugcrowd"
url: "https://bugcrowd.com/disclosures/f7ce8504-0152-483b-bbf3-fb9b759f9f89/critical-local-file-read-in-electron-desktop-app"
final_url: "https://bugcrowd.com/disclosures/f7ce8504-0152-483b-bbf3-fb9b759f9f89/critical-local-file-read-in-electron-desktop-app"
authors: ["Renwa (@RenwaX23)"]
programs: ["Asana"]
bugs: ["LFI"]
bounty: "6,200"
publication_date: "2022-08-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2295
---

##### Summary by Asana

Renwa found a vulnerability in our Asana Desktop app that allowed a malicious actor to read local machine files that the user running the Asana Desktop app has access to if redirected to a malicious URL. We fixed this vulnerability within hours of the report and deployed a new Asana Desktop release within the next few days with the patch.

We track Bugcrowd submissions internally but we didn't follow up with this submission and close it out until a few months after the fix. We've been working on closing that process gap to ensure that we quickly respond to all our security researchers.
