---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '280366'
original_report_id: '280366'
title: Login Cross Site Request Forgery
weakness: Cross-Site Request Forgery (CSRF)
team_handle: infogram
created_at: '2017-10-27T10:36:11.988Z'
disclosed_at: '2017-10-27T11:34:22.851Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 2
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Login Cross Site Request Forgery

## Metadata

- HackerOne Report ID: 280366
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: infogram
- Disclosed At: 2017-10-27T11:34:22.851Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

Login form is not protected against Cross Site Request Forgery.
An attacker can craft html page containing POST information to have victim sign into an attacker's account, where the victim can add information assuming he/she is logged into the correct account, where in reality, the victim is signed into the attacker's account where the changes are visible to the attacker.

The real issue here, is that when the victim runs the html Proof of Concept, the account is logged in to attacker's without any visible warnings, thus the victim is capable of theft of data and potentially vulnerable to account takeover.

Steps to reproduce
1. Create victim account
2. Create attacker account
3. Run attached Proof of Concept in same browser as victim and press submit (The POF can be modified to look like a fake blog post relating to infogram as someone searching a blog post is likely logged in and using the web application already)
4. On the victim browser, he/she is logged in as an attacker without any indication unless the page is manually refreshed.
5. Go to library and add a facebook post, or a chart.
6. On attacker browser, refresh page and navigate to library. You will see the victims added, or edited projects.


Mitigation

Please add a csrf token to login request or make some type prompt that the session has ended when the new login from attacker occurs.

I have attached a video proof of concept with audio of my voice explaining and instructing.
I have also attached the HTML proof of concept.

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
