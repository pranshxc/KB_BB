---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1816181'
original_report_id: '1816181'
title: Reflected XSS via File Upload
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: reddit
created_at: '2022-12-24T00:12:22.663Z'
disclosed_at: '2023-05-18T13:52:31.214Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
asset_identifier: '*.reddithelp.com'
asset_type: WILDCARD
max_severity: high
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS via File Upload

## Metadata

- HackerOne Report ID: 1816181
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: reddit
- Disclosed At: 2023-05-18T13:52:31.214Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
Reflected XSS in " https://reddit.zendesk.com/hc/en-us/requests/new " via file upload

## Impact:

!!
attacker can send that email to victim and steal user account or cookies

Cross site scripting attacks can have devastating consequences. Code injected into a vulnerable application can exfiltrate data or install malware on the user’s machine. Attackers can masquerade as authorized users via session cookies, allowing them to perform any action allowed by the user account.

XSS can also impact a business’s reputation. An attacker can deface a corporate website by altering its content, thereby damaging the company’s image or spreading misinformation. A hacker can also change the instructions given to users who visit the target website, misdirecting their behavior.

* Perform any action within the application that the user can perform.
* View any information that the user is able to view.
* Modify any information that the user is able to modify.
* Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user.

Note ! 
svg work with all browsers
xml file work with all browsers except ( google chrome )


## Steps To Reproduce:

  1. go to " https://reddithelp.com/hc/en-us/requests/new  " and select any type of report
  2. type your email in email fileds and type any text in other fileds 
  3. in upload function upload  <svg>  or <xml> file I attached and send the request
 4. now go to your mail box go to reddit mail and select the file you uploaded 
 5. after downlaoded the file open it in browser it will fire !

## Supporting Material/References:

  * Upload this files to site

{F2089769}
{F2089770}

## Impact

Steal user cookie 
Account Takeover !
Perform any action within the application that the user can perform.
View any information that the user is able to view.
Modify any information that the user is able to modify.
Initiate interactions with other application users, including malicious attacks, that will appear to originate from the initial victim user

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
