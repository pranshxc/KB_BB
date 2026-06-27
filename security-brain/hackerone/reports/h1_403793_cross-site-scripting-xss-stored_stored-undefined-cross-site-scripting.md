---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '403793'
original_report_id: '403793'
title: Stored 'undefined' Cross-site Scripting
weakness: Cross-site Scripting (XSS) - Stored
team_handle: khanacademy
created_at: '2018-09-01T10:14:55.867Z'
disclosed_at: '2018-09-05T16:26:12.709Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored 'undefined' Cross-site Scripting

## Metadata

- HackerOne Report ID: 403793
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: khanacademy
- Disclosed At: 2018-09-05T16:26:12.709Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello KhanAcademy Security Team,

I'm **rootbakar**, I found an XSS bug on 'BIO' in the profile, I used payload XSS **"/><svg/on<script>load=prompt(document.domain);>"/><svg/on<script>load= prompt (document.cookie);>** after I save it appears there is no trigger from the XSS, but when I try to change one of the values in the profile form and when I save it again an XSS trigger appears but with the words '**undefined**'. Every time I want to change both '**REAL NAME**' and '**LOCATION**' and when I press the save button again and after a few seconds an XSS trigger appears with the words '**undefined**'

**PoC**
This is Video Link
https://youtu.be/WGeaclSo_5A
(Not Public Video)

Best Regards,

**RootBakar**

## Impact

**Displayed 'undefined' XSS after user repeated click SAVE button**

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
