---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '411679'
original_report_id: '411679'
title: View Failed Approval and Pending videos other users
team_handle: chaturbate
created_at: '2018-09-20T08:30:43.257Z'
disclosed_at: '2018-10-21T05:50:04.326Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 27
asset_identifier: chaturbate.com
asset_type: URL
max_severity: critical
tags:
- hackerone
---

# View Failed Approval and Pending videos other users

## Metadata

- HackerOne Report ID: 411679
- Weakness: 
- Program: chaturbate
- Disclosed At: 2018-10-21T05:50:04.326Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

See videos uploaded by a user. The video is available when it waits for confirmation or is not accepted.

## Steps To Reproduce:

1 - Go victim page : https://chaturbate.com/p/akaxanxa/?tab=bio
2 - Open video : https://chaturbate.com/photo_videos/photo/big/[user_name]/[content_id]/

3 - Get random requests - https://chaturbate.com/photo_videos/photo/big/[user_name]/[ last content id + 1 ]/

4 - Done - If the id holds the content opens up as a result.

## Impact

By collecting user information, they can access their pending content.
I can share content on my site or blog as original content from my own name by playing the contents.

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
