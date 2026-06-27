---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '386735'
original_report_id: '386735'
title: Login form on non-HTTPS page on http://stream.highwebmedia.com/auth/login/
weakness: Cleartext Transmission of Sensitive Information
team_handle: chaturbate
created_at: '2018-07-25T17:19:17.962Z'
disclosed_at: '2018-09-20T04:08:39.695Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 13
asset_identifier: '*.highwebmedia.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cleartext-transmission-of-sensitive-information
---

# Login form on non-HTTPS page on http://stream.highwebmedia.com/auth/login/

## Metadata

- HackerOne Report ID: 386735
- Weakness: Cleartext Transmission of Sensitive Information
- Program: chaturbate
- Disclosed At: 2018-09-20T04:08:39.695Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear Team,

##Summary##
A page on a http://stream.highwebmedia.com/auth/login/ is not fully protected by an SSL certificate. This could allow an attacker in a Man-in-the-Middle position to obtain usernames and passwords of users visiting the site.

Note the warning in screenshot 1, firefox has identified that this page is not protected with an SSL certificate, therefore the username and password will be sent over a plaintext connection. In itself, this may be enough to put some users off using your page.
Once submit is pressed on the login, it appears as though the request is sent over a HTTPS connection (when seen through Burp Suite or Wireshark), which suggests that the page does protect the username and password with SSL/TLS, 

## Steps To Reproduce:
  1. go to http://stream.highwebmedia.com/auth/login and setup wireshark 
  2. you can get username , password is in clear text

##Mitigation
If any part of a site is required to be protected by SSL, the entire site should be protected by SSL. Ts this would stop the attack outlined above from working, as a certificate error would be displayed to the user.
HTTP Strict Transport security could be used to mitigate this attack, which would tell all browsers not to allow a HTTP connection to this website.

## Supporting Material/References:
Please find attachement

## Impact

If a user were to visit this page from a public or shared network (eg, starbucks, airport, library, etc) and submit a comment, a malicious user on the same network would be able to obtain that users username and password by conducting a Man-in-the-Middle attack using sslstrip and wireshark.

This would allow the malicious user complete access to the user's account.

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
