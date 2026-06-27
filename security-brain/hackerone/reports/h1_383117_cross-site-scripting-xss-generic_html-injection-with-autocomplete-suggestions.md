---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '383117'
original_report_id: '383117'
title: HTML injection with AutoComplete suggestions
weakness: Cross-site Scripting (XSS) - Generic
team_handle: nextcloud
created_at: '2018-07-18T13:45:00.816Z'
disclosed_at: '2018-08-10T09:41:28.528Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 5
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HTML injection with AutoComplete suggestions

## Metadata

- HackerOne Report ID: 383117
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: nextcloud
- Disclosed At: 2018-08-10T09:41:28.528Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1. As user1 set your displayname to `<a href="https://nextcloud.com">Name</a>`
2. As user2 autocomplete the name in the comments input (or Talk chat input)
3. Click on the user name you just autocompleted

User2 is redirected to `https://nextcloud.com`

Only works with HTML, not with `script`

## Impact

User1 can trick user2 to render any html

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
