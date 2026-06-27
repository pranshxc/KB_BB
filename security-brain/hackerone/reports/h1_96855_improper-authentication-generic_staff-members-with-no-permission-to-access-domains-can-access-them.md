---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '96855'
original_report_id: '96855'
title: Staff members with no permission to  access domains can access them.
weakness: Improper Authentication - Generic
team_handle: shopify
created_at: '2015-10-30T20:15:33.890Z'
disclosed_at: '2015-11-03T01:11:15.180Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Staff members with no permission to  access domains can access them.

## Metadata

- HackerOne Report ID: 96855
- Weakness: Improper Authentication - Generic
- Program: shopify
- Disclosed At: 2015-11-03T01:11:15.180Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi , I have found that if a staff member has a permission to access settings but has no permissions to access domains he can bypass this by just going to: `*store.myshopify.com/admin/settings/domains` .

in the side menu the `domains` tab will be disabled and the user shouldn't be able to access it,but he can access it by just going the domains page url.

#Steps to reproduce:
1. Add a new staff member and limit his access o `settings` only , and don't check the `domains` option , so the member should only have access to settings and shouldn't have access to domains.
2. Logout then login with the staff member and go to: `*yourstore.myshopify.com/admin/settings/domains` and you'll be able to add , delete and modify domains.

Thanks

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
