---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '232650'
original_report_id: '232650'
title: Full Api Access and Run All Functions via Starbucks App
weakness: Improper Authentication - Generic
team_handle: starbucks
created_at: '2017-05-28T15:10:12.674Z'
disclosed_at: '2017-08-06T08:51:21.197Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 25
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Full Api Access and Run All Functions via Starbucks App

## Metadata

- HackerOne Report ID: 232650
- Weakness: Improper Authentication - Generic
- Program: starbucks
- Disclosed At: 2017-08-06T08:51:21.197Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The tested application is Starbucks Turkey Android App. https://play.google.com/store/apps/details?id=com.starbucks.tr&hl=en 

All these things are made without any login. I did not login the app.
1. I tried to intercept traffic between starbucks app and server with burp suite. I could not be successful because of the ssl pinning. 
2. Before the unpinnig ssl, I look around the app's all screens.
3. When i look at the messages tab i saw a proccess on my burp history. 
4. Application sent a request to https://crmproxy.protel.com.tr/api/v1/MobileInbox/Limit/20 this url and it took a response.
5. I evaluated this request then i saw the Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz token.
6. I tried to reach this url via browser however, i couldnt because it wants to basic authentication and i tried the default password which comes to mind but i couldnt be successful. 
7. I remembered when there was a request on burp which has Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz token and i tried to add this token in my all request while trying to access via browser.
8. Bingoooo! It worked! I reach the https://crmproxy.protel.com.tr this api server and i looked around it then i found the api docs.
9. Finally, i tried to sent all request in api docs, i was successful in all of them. 

I added to all screenshots below. If there is any question, i may answer them.

Thank you,

Yunus Y.

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
