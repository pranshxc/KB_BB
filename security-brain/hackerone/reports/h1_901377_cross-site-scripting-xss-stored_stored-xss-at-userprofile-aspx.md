---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '901377'
original_report_id: '901377'
title: Stored XSS at ██████userprofile.aspx
weakness: Cross-site Scripting (XSS) - Stored
team_handle: deptofdefense
created_at: '2020-06-18T04:37:20.849Z'
disclosed_at: '2020-07-08T17:38:27.299Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS at ██████userprofile.aspx

## Metadata

- HackerOne Report ID: 901377
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: deptofdefense
- Disclosed At: 2020-07-08T17:38:27.299Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Stored XSS vulnerability exists at ██████████userprofile.aspx under "say something about yourself...". XSS can be used for a variety of attacks. 

## Impact
XSS can be used to steal cookies, password or to run arbitrary code in the victim's browser. 

## Step-by-step Reproduction Instructions

1. Create an account at ███████
2. Go to your profile at ████userprofile.aspx
3. Go to "Say something about yourself..." and enter the XSS payload xxx<svg/onload=alert(document.cookie);>xxx
4. Observe that XSS triggers and reload the page to observe that it is stored XSS.

## Product, Version, and Configuration (If applicable)
███userprofile.aspx#

## Suggested Mitigation/Remediation Actions
Use secure coding techniques such as sanitizing input into form fields so attackers cannot inject scripts to perform XSS attacks. XSS vulnerabilities come from a lack of data escaping. 

##References
https://hackerone.com/reports/858255
https://dzone.com/articles/reflected-xss-explained-how-to-prevent-reflected-x
https://www.imperva.com/learn/application-security/reflected-xss-attacks/
https://www.hacksplaining.com/prevention/xss-reflected

## Impact

XSS can be used to steal cookies, password or to run arbitrary code in the victim's browser.

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
