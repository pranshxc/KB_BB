---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '530464'
original_report_id: '530464'
title: Stored XSS in Profile Comments
weakness: Cross-site Scripting (XSS) - Stored
team_handle: vanilla
created_at: '2019-04-07T05:49:32.437Z'
disclosed_at: '2019-07-17T20:14:14.560Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
asset_identifier: https://github.com/vanilla/vanilla/
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in Profile Comments

## Metadata

- HackerOne Report ID: 530464
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: vanilla
- Disclosed At: 2019-07-17T20:14:14.560Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
The Profile Comments page which is responsible for listing a profile's recent comments is vulnerable to stored XSS as it renders the contents of recent comments without sanitizing them.

## Steps to reproduce:

1. Ensure you are logged in to a user account (no special permissions are needed)
2. Go to any forum post
3. Comment any valid javascript markup (e.g. `<script>alert(1)</script>`)
4. From any account go to your users `Comments` page (`localhost/profile/comments/YOURUSER`)
5. XSS should trigger

## Video example:
#F463844

To verify the comments listing contains the script, the page source can be viewed:
#F463843

## Anything else we should know?
The same root issue might also be causing a self-xss in `My drafts` if you create a post with the same contents (`<script>alert(1)</script>`) and save it as a draft, although this is out-of-scope since it only affects the original user.

## Impact

An attacker could create a post or comment containing a payload and then send the link to their comments page to their victim. This if clicked would result in the victim triggering the payload without any other interaction other than loading the `comments` page. This is especially dangerous if an admin is targeted since the payload could trigger/read nearly anything the admin can do/read.

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
