---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1253926'
original_report_id: '1253926'
title: Domain Takeover [3737signals.com]
weakness: Phishing
team_handle: basecamp
created_at: '2021-07-08T00:28:59.201Z'
disclosed_at: '2021-08-13T18:23:31.997Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 43
asset_identifier: com.basecamp.bc3
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
- phishing
---

# Domain Takeover [3737signals.com]

## Metadata

- HackerOne Report ID: 1253926
- Weakness: Phishing
- Program: basecamp
- Disclosed At: 2021-08-13T18:23:31.997Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,
While i was analyzing the `Basecamp3` Android app i found `3737signals.com` on the source code as i understand you are passing it to the `intent`to view it on some case.

{F1368921}

When I opened it on the browser I got DNS error says `the domain name does not exist`

{F1368922}

As you can see at the bottom of the page `webmaster` is the domain name provider so I navigated to [webmaster.com](https://www.webmasters.com) and searched for `3737sihttps://www.webmasters.com/domains/new.php?domain=3737signals.com&Action=Submit&Domain=3737signals&Suffix=.com&x=0&y=0gnals.com` and found that it's available to [register](https://www.webmasters.com/domains/new.php?domain=3737signals.com&Action=Submit&Domain=3737signals&Suffix=.com&x=0&y=0) 

{F1368920}

I am not sure if it's yours but if it's not just notify me to self close the report

## Impact

- Fake website
- Malicious code injection
- Users tricking
- Company impersonation

This issue can have really huge impact on the companies reputation someone could post malicious content on the compromised site and then your users will think it's official but it's not.

Best Wishes,
MrMax

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
