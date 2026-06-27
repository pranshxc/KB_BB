---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '343095'
original_report_id: '343095'
title: Session Cookie Without Secure Flag,
weakness: Information Disclosure
team_handle: ed
created_at: '2018-04-25T15:54:20.960Z'
disclosed_at: '2018-04-26T13:07:34.627Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
asset_identifier: git.edoverflow.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Session Cookie Without Secure Flag,

## Metadata

- HackerOne Report ID: 343095
- Weakness: Information Disclosure
- Program: ed
- Disclosed At: 2018-04-26T13:07:34.627Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Assigned to:-ED
Assigned by:- Kirtikumar Anandrao Ramchandani
Assigned on:- 25/04/2018
Bug overview:- Session Cookie without secure flag.
Cookie Name:-  _gitlab_session
Description:-Risk description:
Since the Secure flag is not set on the cookie, the browser will send it over an unencrypted channel (plain HTTP) if such a request is made. Thus, the risk exists that an attacker will intercept the clear-text communication between the browser and the server and he will steal the cookie of the user. If this is a session cookie, the attacker could gain unauthorized access to the victim's web session. 
Recommendation:I recommend reconfiguring the web server in order to set the flag(s) Secure to all sensitive cookies. 
Reference:-https://blog.dareboost.com/en/2016/12/secure-cookies-secure-httponly-flags/.

## Impact

The secure flag is an option that can be set by the application server when sending a new cookie to the user within an HTTP Response. The purpose of the secure flag is to prevent cookies from being observed by unauthorized parties due to the transmission of a the cookie in clear text.
To accomplish this goal, browsers which support the secure flag will only send cookies with the secure flag when the request is going to a HTTPS page. Said in another way, the browser will not send a cookie with the secure flag set over an unencrypted HTTP request.
By setting the secure flag, the browser will prevent the transmission of a cookie over an unencrypted channel.

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
