---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '299403'
original_report_id: '299403'
title: Domain spoofing in redirect page using RTLO
weakness: Open Redirect
team_handle: security
created_at: '2017-12-19T16:42:34.965Z'
disclosed_at: '2018-01-30T03:46:00.489Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 46
tags:
- hackerone
- open-redirect
---

# Domain spoofing in redirect page using RTLO

## Metadata

- HackerOne Report ID: 299403
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2018-01-30T03:46:00.489Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hello,

Domains can be spoofed on redirect page using RTLO. 


**Description (Include Impact):**

Using  `http://username@domain.com` & `RTLO` method, i found a way where redirect page host detection can be spoofed

#Steps
 1. Insert this on report  `[Just Click Here](https://google.com@%E2%80%AE@moc.rettiwt)`
2. On click of link, it will redirect to `/redirect` page . Here you will see that `Twitter.com` is highlighted domain. see screen shot below
3. Ideally, if there is any malformed url, it shows some kind of warning but not in this case.
4. Click on `Proceed` button and you will be redirected `https://moc.rettiwt/` instead


### Browser version, Device, etc
Tested on chrome for Mac but should work in all browsers
 
#POC link

https://google.com@%E2%80%AE@moc.rettiwt

###Screenshots

 {F248121}

## Impact

This can be used to spoof urls on hackerone 

Regards,
Ashish

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
