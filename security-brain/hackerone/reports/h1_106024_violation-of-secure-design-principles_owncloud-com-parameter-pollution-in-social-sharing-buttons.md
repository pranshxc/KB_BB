---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '106024'
original_report_id: '106024'
title: 'owncloud.com: Parameter pollution in social sharing buttons'
weakness: Violation of Secure Design Principles
team_handle: owncloud
created_at: '2015-12-19T05:57:36.018Z'
disclosed_at: '2016-03-14T12:19:11.597Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- violation-of-secure-design-principles
---

# owncloud.com: Parameter pollution in social sharing buttons

## Metadata

- HackerOne Report ID: 106024
- Weakness: Violation of Secure Design Principles
- Program: owncloud
- Disclosed At: 2016-03-14T12:19:11.597Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Owncloud ! 
For Example , We Have a Link :
```
https://owncloud.com/blog-you-can-soon-be-fined/
```
And We Change It To :-
```
https://owncloud.com/blog-you-can-soon-be-fined/?u=https://vk.com&text=another_site:https://hackerone.com/gorang_joshi
```
So When You Share It , While Using Your Sharing Buttons Present On Your Page , The Source Code Will Change :
Facebook : ```https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fowncloud.com%2Fblog-you-can-soon-be-fined%2F%3Fu%3Dhttps%3A%2F%2Fvk.com&text=another_site%3Ahttps%3A%2F%2Fhackerone.com%2Fgorang_joshi```


twitter :```https://twitter.com/intent/tweet?text=another_site%3Ahttps%3A%2F%2Fhackerone.com%2Fgorang_joshi&url=https%3A%2F%2Fowncloud.com%2Fblog-you-can-soon-be-fined%2F%3Fu%3Dhttps%3A%2F%2Fvk.com&original_referer=```

Thanks , The Same Report Was Reported By My Friend To Hackerone , You Can Check This Here :
```
https://hackerone.com/reports/105953
```
Thanks , Hope You'll Response Likewise :)

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
