---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1305477'
original_report_id: '1305477'
title: XSS because of Akamai ARL misconfiguration on ████
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2021-08-14T16:35:51.429Z'
disclosed_at: '2022-03-18T18:57:47.361Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# XSS because of Akamai ARL misconfiguration on ████

## Metadata

- HackerOne Report ID: 1305477
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-03-18T18:57:47.361Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello team,
I hope you're doing well & healthy.
I found a reflected XSS because of the misconfiguration of Akamai ARL.

███████

## References

      - https://github.com/war-and-code/akamai-arl-hack
      - https://twitter.com/SpiderSec/status/1421176297548435459
      - https://warandcode.com/post/akamai-arl-hack/
      - https://github.com/cybercdh/goarl
      - https://community.akamai.com/customers/s/article/WebPerformanceV1V2ARLChangeStartingFebruary282021?language=en_US

## Impact

If an attacker can control a script that is executed in the victim's browser, then they can typically fully compromise that user. Amongst other things, the attacker can:
    Perform any action within the application that the user can perform.
View any information that the user is able to view.
Modify any information that the user is able to modify.
Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user.

## System Host(s)
███████

## Affected Product(s) and Version(s)
Akamai ARL

## CVE Numbers


## Steps to Reproduce
Here is the **PoC**

http://███/7/0/33/1d/www.citysearch.com/search?what=x&where=place%22%3E%3Csvg+onload=confirm(document.location)%3E

## Suggested Mitigation/Remediation Actions
Web application owners should keep their infrastructure up to date, and follow secure development best practices, avoiding Open Redirects and XSS vulnerabilities.
Setting up specific WAF rules to detect and block XSS attacks and Open Redirects will increase the level of protection as well, and provide visibility to URLs that malicious users attempt to target.

Best regards.
@pirneci

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
