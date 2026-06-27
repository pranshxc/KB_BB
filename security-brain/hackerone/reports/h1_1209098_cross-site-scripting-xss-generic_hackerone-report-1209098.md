---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1209098'
original_report_id: '1209098'
title: HackerOne Report 1209098
weakness: Cross-site Scripting (XSS) - Generic
team_handle: reddit
created_at: '2021-05-26T02:31:17.597Z'
disclosed_at: '2021-10-21T19:53:59.363Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 7
asset_identifier: www.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HackerOne Report 1209098

## Metadata

- HackerOne Report ID: 1209098
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: reddit
- Disclosed At: 2021-10-21T19:53:59.363Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

hi 
security team i have found a XSS   in  old.reddit.com  and  in reddit.com
Description:
Cross-site scripting (also known as XSS) is a web security vulnerability that allows an attacker to compromise the interactions that users have with a vulnerable application. It allows an attacker to circumvent the same origin policy, which is designed to segregate different websites from each other. Cross-site scripting vulnerabilities normally allow an attacker to masquerade as a victim user, to carry out any actions that the user is able to perform, and to access any of the user's data. If the victim user has privileged access within the application, then the attacker might be able to gain full control over all of the application's functionality and data. 

Step-by-set Reproduction instructions 
1. open web browser and navigate to the page.
2. the open devtool
3. an add the payload 
4.  payload : eval('ale'+'rt(0)');     Function('ale'+'rt(1)')();

## Impact

The actual impact of an XSS attack generally depends on the nature of the application, its functionality and data, and the status of the compromised user. For example:

    In a brochureware application, where all users are anonymous and all information is public, the impact will often be minimal.
    In an application holding sensitive data, such as banking transactions, emails, or healthcare records, the impact will usually be serious.
    If the compromised user has elevated privileges within the application, then the impact will generally be critical, allowing the attacker to take full control of the vulnerable application and compromise all users and their data.

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
