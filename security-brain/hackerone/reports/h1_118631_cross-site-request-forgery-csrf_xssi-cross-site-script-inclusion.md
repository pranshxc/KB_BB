---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '118631'
original_report_id: '118631'
title: XSSI (Cross Site Script Inclusion)
weakness: Cross-Site Request Forgery (CSRF)
team_handle: coinbase
created_at: '2016-02-24T23:00:33.343Z'
disclosed_at: '2017-08-22T22:38:07.744Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# XSSI (Cross Site Script Inclusion)

## Metadata

- HackerOne Report ID: 118631
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: coinbase
- Disclosed At: 2017-08-22T22:38:07.744Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

https://www.coinbase.com/pusher/auth returns sensetive  a json auth-token response that can be parsed by 
```javascript
JSON.parse()
```
from external site. this can easily be mitigated by putting /**/ or // chars at the beginning of the json response and thus making functions like JSON.parse unable to get the data extracted because of parsing errors.

I do know the url takes 2 post parameters and one of them being a **channel name** to properly get the json response. but if an attacker get access to that parameter, just once. he will forever be able to use it. 

for instance:
```html
<form action="https://www.coinbase.com/pusher/auth?callback=tothis" method="POST">
<input type="hidden" name="socket_id" value="1.266427">
<input type="hidden" name="channel_name" value="private-549850166bb03f3b19000147-QPCIGVGojmUh1w">
<input type="submit">
</form>
```
if I visit that URL I will get the json response, now persumably the channel_name would reset over time or when I log out. unfortunatly, that isn't true. if I log back in, that private channel_name would still result a token, in other words, never expiring and reusable. combining this with json parsing, it is possible for an attacker who knows the channel_name to steal the tokens, over and over.

Thanks,

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
