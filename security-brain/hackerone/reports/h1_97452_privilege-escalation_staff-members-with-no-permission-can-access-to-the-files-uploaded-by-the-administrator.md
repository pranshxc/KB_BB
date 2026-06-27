---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '97452'
original_report_id: '97452'
title: Staff members with no permission can access to the files, uploaded by the administrator
weakness: Privilege Escalation
team_handle: shopify
created_at: '2015-11-03T14:49:32.997Z'
disclosed_at: '2016-07-07T15:49:04.516Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- privilege-escalation
---

# Staff members with no permission can access to the files, uploaded by the administrator

## Metadata

- HackerOne Report ID: 97452
- Weakness: Privilege Escalation
- Program: shopify
- Disclosed At: 2016-07-07T15:49:04.516Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Staff members with no permission can access to the files, uploaded by the administrator

### Test #1 
If the member has access only to the section  Products, Inventory, & Collections
1. Go to the Products -> Product Name -> Description
2. Click the button -> Add Image
3. In the section Uploaded images are all files uploded by the admin, so we can simply add them or download (screenshot attached)
4. Uploded images are in the section Settings -> Files (but we don't have access there)

### Test #2
If the member has NO access to the ALL sections
1. So we can not go to the page Products but....
2. Lets go here https://*.myshopify.com/admin/rte/assets
3. And we will see all files uploaded by admin (screenshot attached)
4. On this page we can simply find links for admin files

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
