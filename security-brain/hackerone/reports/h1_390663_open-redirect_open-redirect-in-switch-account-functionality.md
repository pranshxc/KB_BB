---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '390663'
original_report_id: '390663'
title: Open redirect in switch account functionality
weakness: Open Redirect
team_handle: revive_adserver
created_at: '2018-08-05T10:40:30.222Z'
disclosed_at: '2019-04-23T13:05:50.617Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: https://github.com/revive-adserver/revive-adserver
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- open-redirect
---

# Open redirect in switch account functionality

## Metadata

- HackerOne Report ID: 390663
- Weakness: Open Redirect
- Program: revive_adserver
- Disclosed At: 2019-04-23T13:05:50.617Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

To reproduce this vulnerability:
1. You have to be logged in user
2. Enter address: http://<your_local_installation>/www/admin/account-switch.php?return_url=http://127.0.0.1:12345/test 

This is due to unrestricted redirection url passed in in the `return_url` parameter. I would recommend to use some kind of whitelisting or a check if you are redirecting to the same domain you were before.

## Impact

This kind of open redirect vulnerabilities are used in fishing campaigns. I assume that in this case a support request containing a crafted url would have a higher chances of success. For additional malicious url obfuscation you can:
- add some unused parameters that would suggest identifiers of campaigns, other accounts and other revive specific information
- register a domain name similar to the attacked one

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
