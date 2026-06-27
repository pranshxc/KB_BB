---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1072616'
original_report_id: '1072616'
title: Stored XSS through name / last name on https://██████████/
weakness: Cross-site Scripting (XSS) - Stored
team_handle: deptofdefense
created_at: '2021-01-06T09:28:37.637Z'
disclosed_at: '2021-03-11T20:53:52.354Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS through name / last name on https://██████████/

## Metadata

- HackerOne Report ID: 1072616
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: deptofdefense
- Disclosed At: 2021-03-11T20:53:52.354Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**
There is stored XSS Vulnerability on https://█████/██████ by rendering unsafe input being registered on the account name and last name.

███


## Step-by-step Reproduction Instructions

1. Navigate to 
```javascript
https://█████/login/?next=/███%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252F████████%252Fcgi%252Flogin.cgi%253Freturn_to%253Dhttps%25253A%25252F%25252F███████%25252Fcgi%25252Fmyaccount.cgi%26client_id%3D6G3AXPQNPXK5SVESYCB8AMCPHQQ3ENCRK8G2QNWY%26state%3DBEAEb6NGMQ7kWZwZS2pNNFv4p7JwBk86%26scope%3Dopenid%2520profile
```
2. Create your account, with your name as <IMG SRC=X ONERROR=ALERT(1)>
3. Log in and navigate to https://███/██████

## Suggested Mitigation/Remediation Actions

Sanitizing the input on the account name fields will prevent the issue.

##Best Regards
nagli

## Impact

Executing javascript on behalf of the victim

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
