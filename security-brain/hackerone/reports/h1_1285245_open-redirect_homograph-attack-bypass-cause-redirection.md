---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1285245'
original_report_id: '1285245'
title: Homograph attack bypass cause redirection
weakness: Open Redirect
team_handle: vanilla
created_at: '2021-07-31T00:49:40.696Z'
disclosed_at: '2022-07-10T21:38:40.400Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
asset_identifier: '*.vanillacommunities.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Homograph attack bypass cause redirection

## Metadata

- HackerOne Report ID: 1285245
- Weakness: Open Redirect
- Program: vanilla
- Disclosed At: 2022-07-10T21:38:40.400Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,
I read the report #563268 which is a great report that was able to trick users to click on links which appears to them normal links but in fact its malicious links So I tried to find a way to make this happen again and I found out that there is a  Homograph attack bypass which can redirect users to malicious sites.

**Vulnerable URL:**
```
https://rinkerboats.vanillacommunities.com/home/leaving?Target=http://www.ɡооɡⅼе.ϲоⅿ\:@%20
```
**Message:**
```
You are now leaving Rinker Boat Company. Click the link to continue to http://www.ɡооɡⅼе.ϲоⅿ\:@ 
```
This will redirect users to http://www.xn--l-r1aa78phba.xn--m-zmb38a/:@ and not http://www.google.com
In Homograph attack basically an attacker can change text to another and it will look like the original text for example google.com and ɡооɡⅼе.ϲоⅿ are not the same. You can know more 

##References:
https://www.charset.org/punycode?encoded=http%3A%2F%2Fxn--eby-7cd.com%2F&decode=Punycode+to+normal+text
http://www.chromium.org/developers/design-documents/idn-in-google-chrome

##Similar Reports:
https://hackerone.com/reports/861940
https://hackerone.com/reports/29491
https://hackerone.com/reports/175286
https://hackerone.com/reports/271324
https://hackerone.com/reports/143975

## Impact

Redirect users to malicious websites.

Regards,
Malek

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
