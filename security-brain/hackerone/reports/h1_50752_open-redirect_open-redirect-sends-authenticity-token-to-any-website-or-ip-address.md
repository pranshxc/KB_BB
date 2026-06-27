---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '50752'
original_report_id: '50752'
title: open redirect sends authenticity_token to any website or (ip address)
weakness: Open Redirect
team_handle: x
created_at: '2015-03-10T01:01:35.464Z'
disclosed_at: '2015-03-14T02:05:46.716Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- open-redirect
---

# open redirect sends authenticity_token to any website or (ip address)

## Metadata

- HackerOne Report ID: 50752
- Weakness: Open Redirect
- Program: x
- Disclosed At: 2015-03-14T02:05:46.716Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
URL: https://mobile.twitter.com//example/messages (there is double slash before "example" word)
when you click "send" after writing a message the authenticity_token will send to https://example
this URL doesn't allow any dots in it, so i can not write //example.com 
but when i write a number it will redirect me to an ip, 
EG:
https://mobile.twitter.com//0/messages
>> 0.0.0.0
when i write a longer number it will redirect me to another ip
i fount this website that can change server or a website to ip
https://www.site24x7.com/find-ip-address-of-web-site.html
then i fount this website that can change any ip to a single number (without dots)
http://www.smartconversion.com/unit_conversion/IP_Address_Converter.aspx
so i'll change http://example.com to an ip by the first website
http://example.com = 93.184.216.34
now i'll change 93.184.216.34 to a single number without dots by the second website
93.184.216.34 = 1572395042
now to redirect from twitter to example.com
https://mobile.twitter.com//1572395042/messages
Thank you!

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
