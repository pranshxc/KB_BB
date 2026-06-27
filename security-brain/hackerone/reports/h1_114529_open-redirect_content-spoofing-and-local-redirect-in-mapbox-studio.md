---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '114529'
original_report_id: '114529'
title: Content Spoofing and Local Redirect in Mapbox Studio
weakness: Open Redirect
team_handle: mapbox
created_at: '2016-02-03T23:51:14.079Z'
disclosed_at: '2016-04-20T14:30:49.036Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- open-redirect
---

# Content Spoofing and Local Redirect in Mapbox Studio

## Metadata

- HackerOne Report ID: 114529
- Weakness: Open Redirect
- Program: mapbox
- Disclosed At: 2016-04-20T14:30:49.036Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hi**

I'm Found  Bug  It is Possible To Send His message Directly Through URL and Redirect Local .

**Details**
When you go to :- https://www.mapbox.com/studio/admin/ website redirect to 
 ~~~
https://www.mapbox.com/studio/forbidden/?message=Sorry,only admins allowed here.&redirect=/studio/&path=/studio/admin/
~~~
You can see  parameter **message** and **redirect** not safe against the manipulation and interference

**# Content Spoofing and Redirect**

**URL POC** 
~~~
https://www.mapbox.com/studio/forbidden/?message=Hi%20You%20Are%20%20Not%20%20in%20Mapbox%20Please%20Go%20%20To%20http://evil.com&redirect=/evil.com/&path=%2Fstudio%2Fadmin%2F
~~~
Message **Changed** and If Click On **Okay** Redirect on **evil.com**


**Regards**
**Hussain**

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
