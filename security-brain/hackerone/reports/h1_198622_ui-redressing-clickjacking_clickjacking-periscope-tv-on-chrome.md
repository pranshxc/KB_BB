---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '198622'
original_report_id: '198622'
title: Clickjacking Periscope.tv on Chrome
weakness: UI Redressing (Clickjacking)
team_handle: x
created_at: '2017-01-15T21:40:43.230Z'
disclosed_at: '2017-02-06T22:08:58.786Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking Periscope.tv on Chrome

## Metadata

- HackerOne Report ID: 198622
- Weakness: UI Redressing (Clickjacking)
- Program: x
- Disclosed At: 2017-02-06T22:08:58.786Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

The X-FRAME-OPTIONS header returned from https://www.periscope.tv is:
```
X-Frame-Options: ALLOW-FROM https://twitter.com/
```
But Chrome doesn't support this value for the header: https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet.
Because of that, no value for X-FRAME-OPTIONS is set and all of the periscope.tv pages are vulnerable to Clickjacking. You can see for example my attached poc (Make sure you test it on chrome) that I am framing my own user on periscope. I can use regular Clickjacking tricks to make the user follow other users and do practically any action on the site.

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
