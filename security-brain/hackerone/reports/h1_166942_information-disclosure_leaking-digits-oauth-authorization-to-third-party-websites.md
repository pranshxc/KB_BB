---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '166942'
original_report_id: '166942'
title: leaking Digits OAuth authorization to third party websites
weakness: Information Disclosure
team_handle: x
created_at: '2016-09-08T20:17:50.533Z'
disclosed_at: '2017-01-24T18:46:33.283Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- information-disclosure
---

# leaking Digits OAuth authorization to third party websites

## Metadata

- HackerOne Report ID: 166942
- Weakness: Information Disclosure
- Program: x
- Disclosed At: 2017-01-24T18:46:33.283Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hi,**

While authenticating digits to my Fabric account i have noticed that the callback_url is not solid i.e. any sub domain or any path is accepted as callback_url with host as fabric.io.
This issue can be exploited by leaking the authorization token to third party websites (websites mentioned on kit's page)

**Steps to reproduce:**
- Go to https://www.digits.com/login?consumer_key=YlNgs6zwm4QLmrzJBwRK3FcR5&callback_url=https://fabric.io/kits/ios/stripe&host=https://fabric.io
- Give access to Digits
- Now you will be redirected to https://fabric.io/kits/ios/stripe
- While on stripe kits page click on the stripe website URL (https://stripe.com)
- The authorization token will be leaked to stripe.com 
{F118436}

This issue can also be exploited on our organization member by actually leaking the consumer secret to our domain. 

**Steps to reproduce**
- Add the victim to your organization
- Create an crash issue under fabric
- add a note to that issue for ex: https://wesecureapp.com
- Note down the issue URL
{F118437}
Ex: https://fabric.io/img-srcx-onerrorprompt15/android/apps/app.myapplication/issues/56207e21f5d3a7f76bd5c20c
- Change the call back URL to issue url
https://www.digits.com/login?consumer_key=YlNgs6zwm4QLmrzJBwRK3FcR5&callback_url=https://fabric.io/img-srcx-onerrorprompt15/android/apps/app.myapplication/issues/56207e21f5d3a7f76bd5c20c&host=https://fabric.io
- Give digits permission
- You will be redirected to issue
- Now click the link in the notes and the OAuth token will be leaked to the attacker controlled domain.
{F118438}

**Regards,
Akhil**

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
