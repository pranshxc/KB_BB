---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1051369'
original_report_id: '1051369'
title: Blind Stored XSS Payload fired at the backend on https://█████████/
weakness: Cross-site Scripting (XSS) - Stored
team_handle: deptofdefense
created_at: '2020-12-05T21:27:52.206Z'
disclosed_at: '2021-03-24T20:31:30.535Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 33
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Blind Stored XSS Payload fired at the backend on https://█████████/

## Metadata

- HackerOne Report ID: 1051369
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: deptofdefense
- Disclosed At: 2021-03-24T20:31:30.535Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
I have just gotten an email notification from my XSSHunter payload that my blind stored XSS has been triggered by an administrator on the █████████ site, in the following URL:

```javascript
https://█████/████
```

Admin IP address: 
████████

User-Agent:
█████████

Cookies:
```javascript
██████
```
Injection Image:

███████

DB Creds exposed:

██████████.█████\█████a

## Suggested Mitigation/Remediation Actions

Sanitizing the input on the back-end as well

##Best Regards
nagli

## Impact

Ability to capture administrator action when preforming activities on the back-end.
Extractions of DB credentials.
Access to private information.
Stealing the cookies of the administrator.

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
