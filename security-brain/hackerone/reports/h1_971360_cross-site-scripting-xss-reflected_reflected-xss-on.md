---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '971360'
original_report_id: '971360'
title: Reflected XSS on ███████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-08-31T15:56:07.056Z'
disclosed_at: '2020-09-03T17:20:00.027Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS on ███████

## Metadata

- HackerOne Report ID: 971360
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2020-09-03T17:20:00.027Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary**:
Reflected Cross site Scripting (XSS) on████leaving.html?url=%22%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

**Steps To Reproduce**:
1. Navigate to███leaving.html?url=
2. Enter a crafted XSS payload like "><script>alert("xss by nagli")</script>
3. Alert will pop :-)

█████████

**How can the system be exploited with this bug?**
The attacker can execute JS code, which could lead to stealing cookies and full account takeover.

**Recommendations for fix**
Content based escaping on the users input, in this case on the redirect parameter.

**Best Regards,**
nagli

## Impact

Attacker can execute JS code on the Victim Behalf.

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
