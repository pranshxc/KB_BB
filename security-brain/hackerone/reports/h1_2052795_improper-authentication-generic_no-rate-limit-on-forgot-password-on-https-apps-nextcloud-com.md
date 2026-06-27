---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2052795'
original_report_id: '2052795'
title: No Rate Limit On Forgot Password on https://apps.nextcloud.com
weakness: Improper Authentication - Generic
team_handle: nextcloud
created_at: '2023-07-06T12:40:47.865Z'
disclosed_at: '2023-09-26T09:44:00.790Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: apps.nextcloud.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# No Rate Limit On Forgot Password on https://apps.nextcloud.com

## Metadata

- HackerOne Report ID: 2052795
- Weakness: Improper Authentication - Generic
- Program: nextcloud
- Disclosed At: 2023-09-26T09:44:00.790Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
     I have found no rate Limit on forgot password.

Summary:-
A rate limiting algorithm is used to check if the user session (or IP address) has to be limited based on the information in the session cache. In case a client made too many requests within a given time frame, HTTP servers can respond with status code 429: Too Many Requests. (wikipedia) I just realized that on the reset password page, the request has no rate limit which then can be used to loop through one request.

Step to reproduce:-
1-Go to https://apps.nextcloud.com/password/reset/.
2- Enter email address
3- Intercept burp and send request to intruder
4- Select the number 1 to 50 and click on start attack.
5- You will get 302 OK
6- I already attached the PoC video too if you don't understand my explanation and Sorry for inconvenience for video please do mute before watching video.

Suggested to fix:-
Use CAPTCHA verification if many requests are sent. 

Reference:-
https://hackerone.com/reports/751604

## Impact

If You Are Using Any Email Service Software API Or Some Tool Which Costs You For Your Email This Type Of Attack Can Result You In Financial Lose And It Can Also Slow Down Your Services It Can Take Bulk Of Storage In Sent Mail Although If Users Are Affected By This Vulnerability They Can Stop Using Your Services Which Can Lead To Business Risk
Attackers could use this vulnerability to bomb out the email inbox of the victim.

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
