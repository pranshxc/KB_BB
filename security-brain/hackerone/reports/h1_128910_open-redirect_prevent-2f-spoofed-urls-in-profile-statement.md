---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '128910'
original_report_id: '128910'
title: prevent %2f spoofed URLs in profile statement
weakness: Open Redirect
team_handle: gratipay
created_at: '2016-04-07T08:13:13.625Z'
disclosed_at: '2017-08-21T13:30:11.505Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
tags:
- hackerone
- open-redirect
---

# prevent %2f spoofed URLs in profile statement

## Metadata

- HackerOne Report ID: 128910
- Weakness: Open Redirect
- Program: gratipay
- Disclosed At: 2017-08-21T13:30:11.505Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

https://gratipay.com%2f@google.com on clicking on this url this link will take to the google.com or any other malicious url. On seeing it will look like the link will take to the gratipay but onclicking the url it will redirect to the malicious site.Attacker with the help social engg. techniques will able to redirect the user to any Ransomware site for they nefarious purpose

POC:- Click on the link it will redirect to google.com

Fix:- The hostname must end in %2f, which gets URL-decoded to /.
This ensures that the browser only sends the request to the intended host.

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
