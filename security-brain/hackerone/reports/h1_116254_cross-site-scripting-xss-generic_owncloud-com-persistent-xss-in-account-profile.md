---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '116254'
original_report_id: '116254'
title: 'owncloud.com: Persistent XSS In Account Profile'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: owncloud
created_at: '2016-02-13T15:22:17.701Z'
disclosed_at: '2016-02-15T17:17:22.680Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# owncloud.com: Persistent XSS In Account Profile

## Metadata

- HackerOne Report ID: 116254
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: owncloud
- Disclosed At: 2016-02-15T17:17:22.680Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Quotation marks are not sanitized in one of the HTML tags inside of the profile when dealing with first & last names. It is an <iframe> tag. In the attached PoC screenshot, I included a functional first name that triggers an alert() call. Inside, I pasted the HTML tag where it breaks.

I don't know owncloud inside-out, so I don't know if anybody else is able to see my user profile. If they are, then this would be able to pull anybody else's session cookies. However, even if not, it could still be used to BeEF-hook others if they access your account or you get one-time access to their account, so it should still be fixed.

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
