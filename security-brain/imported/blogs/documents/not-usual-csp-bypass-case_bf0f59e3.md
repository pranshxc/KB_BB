---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-12_not-usual-csp-bypass-case.md
original_filename: 2022-12-12_not-usual-csp-bypass-case.md
title: Not usual CSP bypass case
category: documents
detected_topics:
- xss
- cloud-security
- command-injection
- file-upload
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- cloud-security
- command-injection
- file-upload
- automation-abuse
- api-security
language: en
raw_sha256: bf0f59e367ee6122c04815355772d957610ddf5d626a023ec17c3bc339e0c8ba
text_sha256: 7df169228bd76e0faeba449c34406abbadb277461a3d1bf8b18025ae2b968b49
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# Not usual CSP bypass case

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-12_not-usual-csp-bypass-case.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, command-injection, file-upload, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `bf0f59e367ee6122c04815355772d957610ddf5d626a023ec17c3bc339e0c8ba`
- Text SHA256: `7df169228bd76e0faeba449c34406abbadb277461a3d1bf8b18025ae2b968b49`


## Content

---
title: "Not usual CSP bypass case"
page_title: "CSP script-src: 'default'  — bypass | Medium"
url: "https://karol-mazurek95.medium.com/not-usual-csp-bypass-case-b538263e09d6"
authors: ["Karol Mazurek"]
bugs: ["Unrestricted file upload", "XSS", "CSP bypass"]
publication_date: "2022-12-12"
added_date: "2022-12-15"
source: "pentester.land/writeups.json"
original_index: 1787
scraped_via: "browseros"
---

# Not usual CSP bypass case

Member-only story

Not usual CSP bypass case
Karol Mazurek
Follow
5 min read
·
Dec 12, 2022

25

2

CSP default-src ‘self’ — bypass using the error page.

Press enter or click to view image in full size
INTRODUCTION

During one of the penetration tests, I managed to chain three application issues that finally enabled the execution of the Stored XSS vulnerability.

The vulnerability combines three flaws in the application:

Unrestricted file upload.
Misconfigured Content Security Policy.
Application error response body controlled by the user.
1. UNRESTRICTED FILE UPLOAD

The application allows users to upload images, and there is a whitelist of extensions that can be uploaded (.png | .jpg). All uploaded files are stored in the web-root folder of the server. For instance:

https://example.com/74d673a21b5f5d54cbc22fc3b24bcb5e.iix

The first issue is that it is possible to specify the uploaded file's content type, even if the extension in the request is (.png | .jpg).

The trick is to use a part of a JPG file at the bottom of the content:

ÿØÿàJFIFÿáVExifMM*>F(ÿâ°ICC_PROFILE lcms0mntrRGB XYZ

One thing to keep in mind, that casually the SVG file content starts with:

<?xml version="1.0" standalone="no"?>…
