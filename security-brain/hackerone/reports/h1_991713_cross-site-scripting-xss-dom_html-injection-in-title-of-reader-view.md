---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '991713'
original_report_id: '991713'
title: HTML injection in title of reader view
weakness: Cross-site Scripting (XSS) - DOM
team_handle: brave
created_at: '2020-09-25T23:46:38.995Z'
disclosed_at: '2023-06-22T05:52:53.227Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 29
asset_identifier: https://github.com/brave/brave-ios
asset_type: SOURCE_CODE
max_severity: none
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# HTML injection in title of reader view

## Metadata

- HackerOne Report ID: 991713
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: brave
- Disclosed At: 2023-06-22T05:52:53.227Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

Reader.html in Brave doesn't escape/trim HTML tags in %READER-TITLE%.
https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/Reader.html#L17
This allows any page to inject malicious HTML code in reader-mode page through `<title>{html code you want to inject}</title>`.

## Products affected: 

Brave iOS Version 1.20 (20.09.11.20), also current Nightly

## Steps To Reproduce:

* Open the following Google docs: https://docs.google.com/document/d/10kPw7PNOujlenF08i3jBgD4zqoG5148u8TRkoHj7io8/edit?usp=sharing
* Push reader-mode button shown in address bar.
* Malicious login form is rendered instead of the document
* Fill the form, then the user/password you filled are stolen to malicious website

## Supporting Material/References:

  * See attached movie file for the demonstration

## Impact

Malicious web contents can inject HTML code and manipulate readerized page (hosted in localhost:65XX).

Also, if injected HTML code contains a string `%READER-CONTENT%`, it is replaced to the original page contents.
https://github.com/brave/brave-ios/blob/87af4cbf0474bafd13673690aeee0c11059fbba2/Client/Frontend/Reader/ReaderModeUtils.swift#L29

So, attacker can steal user's sensitive information contained in the original HTML page through `<form><textarea>%READER-CONTENT%</textarea>`.
When you open the following Google search link in reader-mode, you can reproduce the above scenario as well.
https://www.google.com/search?q=%3Cform%3E%3Ctextarea%20name%3D%22dom%22%3E%25READER-CONTENT%25%3C%2Ftextarea%3E%3Cinput%20type%3D%22submit%22%3E%3C%2Fform%3E

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
