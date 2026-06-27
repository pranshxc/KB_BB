---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '267177'
original_report_id: '267177'
title: stored xss in invited team member via email parameter
weakness: Cross-site Scripting (XSS) - Stored
team_handle: shopify
created_at: '2017-09-09T12:05:19.202Z'
disclosed_at: '2017-11-03T08:12:19.118Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: partners.shopify.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# stored xss in invited team member via email parameter

## Metadata

- HackerOne Report ID: 267177
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: shopify
- Disclosed At: 2017-11-03T08:12:19.118Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey there, while testing your program I found a stored XSS vulnerability which can placed by owners or **other staff members who have ability to manage members** and it will triggered by visiting invited team member page (e.g. https://partners.shopify.com/642416/invitations/15406).

### Reproduction Steps

1. login to partners.shopify.com.
2. navigate to *Team* (e.g. https://partners.shopify.com/642416/memberships).
3. click on *Invite owner*.
4. use `<svg/onload=alert(document.cookie)>abcdef@test.com` as email address.
5. click on *Send invite*.
6. you'll see a warning: *There was a problem connecting to Shopify*.
7. navigate to *Team* section again (e.g. https://partners.shopify.com/642416/memberships).
8. open invited user page (e.g. https://partners.shopify.com/642416/invitations/15411).

note: it does not matter who send the invitation, attack can be triggered by other team members (including owners) by opening invitation page.

also attached two file to show you that this vulnerability can placed by both owners and staff members with *manage members* access.

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
