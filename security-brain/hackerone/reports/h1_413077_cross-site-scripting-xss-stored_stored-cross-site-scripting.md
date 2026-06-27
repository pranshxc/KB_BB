---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '413077'
original_report_id: '413077'
title: Stored Cross Site Scripting.
weakness: Cross-site Scripting (XSS) - Stored
team_handle: 8x8
created_at: '2018-09-23T12:23:24.011Z'
disclosed_at: '2020-07-21T17:12:40.995Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
asset_identifier: '*.easycontactnow.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored Cross Site Scripting.

## Metadata

- HackerOne Report ID: 413077
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: 8x8
- Disclosed At: 2020-07-21T17:12:40.995Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hellow team 
I got Stored based XSS on your web :D

Here Is Step :

1. Go to https://www.easycontactnow.com/
2. Click "Try For Free" (Sign Up)
3. It will told you "Enter your details to get started". 
   So Enter your full name like : "><script>alert(1)</script>
   Then put all the other details.
4. Then Confirm your id and login.
5. Then Click dashboard and other thing :) 
6. Tada script executed done :D

POC : https://www.youtube.com/watch?v=gYyCAxaB6w0

Sorry for my bad english. 

Thanks :)

## Impact

Stored attacks are those where the injected script is permanently stored on the target servers, such as in a database, in a message forum, visitor log, comment field, etc. The victim then retrieves the malicious script from the server when it requests the stored information. Stored XSS is also sometimes referred to as Persistent or Type-I XSS.

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
