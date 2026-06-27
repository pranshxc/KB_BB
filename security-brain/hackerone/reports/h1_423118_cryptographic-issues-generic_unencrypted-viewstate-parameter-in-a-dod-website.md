---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '423118'
original_report_id: '423118'
title: Unencrypted __VIEWSTATE parameter in a DoD website
weakness: Cryptographic Issues - Generic
team_handle: deptofdefense
created_at: '2018-10-12T21:03:39.953Z'
disclosed_at: '2020-05-14T17:43:23.942Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cryptographic-issues-generic
---

# Unencrypted __VIEWSTATE parameter in a DoD website

## Metadata

- HackerOne Report ID: 423118
- Weakness: Cryptographic Issues - Generic
- Program: deptofdefense
- Disclosed At: 2020-05-14T17:43:23.942Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi there i realise that the information passing to the server in the subdomain http://████████ can be seen without any encryption thought the __VIEWSTATE Parameter.

To reduce the change of someone interception the information the parameter should be encrypted due to the sensivity of the information passing thought there.

POC:
Well this quiet easy to explore it.
Go to the following website with burp turned on:
url: https://█████/

Intercept the traffic and check the response from the __VIEWSTATE parameter
and you will see the information passing in cleartext 

viewstate.jpg

Recommendations.
The __VIEWSTATE variable cipher is recommended in the application settings
(web.config).

References:
http://msdn.microsoft.com/en-us/library/ms178199(v=vs.85).aspx
https://www.acunetix.com/vulnerabilities/web/unencrypted-__viewstate-parameter

Best Regards Miguel Santareno

## Impact

It depends on the information passing around but for what can i see this is still a medium stuff

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
