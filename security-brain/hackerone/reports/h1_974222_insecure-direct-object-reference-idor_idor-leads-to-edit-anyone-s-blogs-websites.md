---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '974222'
original_report_id: '974222'
title: IDOR leads to Edit Anyone's Blogs / Websites
weakness: Insecure Direct Object Reference (IDOR)
team_handle: automattic
created_at: '2020-09-03T17:41:58.202Z'
disclosed_at: '2020-11-18T14:20:47.759Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 151
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR leads to Edit Anyone's Blogs / Websites

## Metadata

- HackerOne Report ID: 974222
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: automattic
- Disclosed At: 2020-11-18T14:20:47.759Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello there,
I hope all is well!

Steps:
1. Go to `https://intensedebate.com/signup` and create 2 accounts.
2. Login as victim and go to `https://www.intensedebate.com/edit-user-profile`
3. Click `Add Blog / Website` text and fill the form > click `Save Settings` button
4. Go to `https://www.intensedebate.com/edit-user-profile`, again and search `radMainSite` text in page source and copy value.   
{F975085}
5. Then login as attacker.
6. Go to `https://www.intensedebate.com/edit-user-profile` > click `Add Blog / Website` text and fill the form > click `Save Settings` button
7. Go to `https://www.intensedebate.com/edit-user-profile`, again and click `Save Settings` button > open burp suite and change `hidBlogID` parameter with victim's `hidBlogID`.
8. Forward the request and go to victim's account. Check your website informations. You will see it's changed.

PoC:   
{F975096}

## Impact

Changing victim's website/blog informations.

Best Regards,
@mygf

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
