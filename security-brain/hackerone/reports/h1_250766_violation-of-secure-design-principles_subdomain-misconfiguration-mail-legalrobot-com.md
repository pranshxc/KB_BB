---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '250766'
original_report_id: '250766'
title: Subdomain misconfiguration [mail.legalrobot.com]
weakness: Violation of Secure Design Principles
team_handle: legalrobot
created_at: '2017-07-18T08:14:45.944Z'
disclosed_at: '2017-07-31T01:46:28.610Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- violation-of-secure-design-principles
---

# Subdomain misconfiguration [mail.legalrobot.com]

## Metadata

- HackerOne Report ID: 250766
- Weakness: Violation of Secure Design Principles
- Program: legalrobot
- Disclosed At: 2017-07-31T01:46:28.610Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi Team,

You subdomain mail.legalrobot.com has a CNAME record that resolved to ghs.google.com and shows error when navigating to subdomain,
should remove CNAME entry for that subdomain pointing towards ghs.google.com.I couldn't verify the domain ownership process to fully takeover subdomain.
mail.legalrobot.com canonical name = ghs.google.com
For POC i have claim the domain of gsuite account using mail.legalrobot.com

Fix:
To fully resolve the issue you need to remove the CNAME record and put in place a web forwarding rule for mail.legalrobot.com towards new web landing page.

Please find the attachment of POC.

Thanks 
_prakash

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
