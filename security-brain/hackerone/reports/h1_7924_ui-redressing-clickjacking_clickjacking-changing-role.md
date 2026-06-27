---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7924'
original_report_id: '7924'
title: Clickjacking - changing role
weakness: UI Redressing (Clickjacking)
team_handle: respondly
created_at: '2014-04-17T20:32:11.294Z'
disclosed_at: '2014-04-21T10:17:11.086Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking - changing role

## Metadata

- HackerOne Report ID: 7924
- Weakness: UI Redressing (Clickjacking)
- Program: respondly
- Disclosed At: 2014-04-21T10:17:11.086Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I'm able to frame the page, when I make a frame with a opacity of 0 and a button at the position of the role switch I can change the role without the victim knowing that.

a POC screen :
http://prntscr.com/3ay0mh

a POC code : 
`<iframe src="https://app.respond.ly" style="width:100%;height:100%;margin:0;border:0;"></iframe>`

Best regards,

Olivier Beg

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
