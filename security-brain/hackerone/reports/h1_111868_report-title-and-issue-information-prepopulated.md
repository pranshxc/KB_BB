---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '111868'
original_report_id: '111868'
title: Report title and issue information prepopulated
team_handle: security
created_at: '2016-01-20T15:10:27.559Z'
disclosed_at: '2016-07-15T22:20:11.510Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 15
tags:
- hackerone
---

# Report title and issue information prepopulated

## Metadata

- HackerOne Report ID: 111868
- Weakness: 
- Program: security
- Disclosed At: 2016-07-15T22:20:11.510Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

I think this may be N/A to the bounty program but I'm seeing a weird situation so just wanted to at least flag as I'm not sure what is causing it in the event it's something worth you looking into...

Working through possible exploits on █████ last night, I entered some code to try and have their smtp server send additional emails in my stores contact form:

```
test%0aMAIL+FROM:+██████████%0d%0aRCPT+TO:+███████%0d%0aDATA%0d%0aFrom:+█████████%0d%0
```

When I logged into my Hackerone account today to play with the Markdown parser on Hackerone.com, I noticed that code in the Title of the potential issue. I think I then pasted it into the information box and went to another couple of pages. When I returned, the information was in both the title and information boxes. I figure there may be a cookie saving my prepopulated values so I can come back to an unfinished report but it was odd that code I submitted to a Shopify form showed up on Hackerone....

I thought this might be a browser thing so I logged out of my Google account on Chrome and still saw the issue. Then I opened up IE and logged into Hackerone and saw the issue.

Perhaps unrelated, but figure I'll include it in case it helps, when I was using Burb Suite to intercept Shopify form submissions, I also noticed some requests to Hackerone but didn't really pay attention to them at the time...

Anyways, hope this isn't a total waste of your time.

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
