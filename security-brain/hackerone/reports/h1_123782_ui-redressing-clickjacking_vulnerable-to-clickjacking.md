---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '123782'
original_report_id: '123782'
title: Vulnerable to clickjacking
weakness: UI Redressing (Clickjacking)
team_handle: gratipay
created_at: '2016-03-17T05:08:24.054Z'
disclosed_at: '2016-05-13T09:24:41.615Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- ui-redressing-clickjacking
---

# Vulnerable to clickjacking

## Metadata

- HackerOne Report ID: 123782
- Weakness: UI Redressing (Clickjacking)
- Program: gratipay
- Disclosed At: 2016-05-13T09:24:41.615Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Reproduction steps:

1.Open URL :https://grtp.co/
2.put the url in the below code of iframe
<html>
   <head>
     <title>Clickjacking GRTP</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="https://grtp.co/" width="500" height="500"></iframe>
   </body>
</html>
3.Observe that site is getting displayed in Iframe

Impact:
By using Clickjacking technique, an attacker hijack's click's
meant for one page and route them to another page, most likely
for another application, domain, or both.

Standard:
SANS CWE-693

Remediation:
Frame busting technique is the better framing protection
technique.
Sending the proper X-Frame-Options HTTP response headers
that instruct the browser to not allow framing from other
domains

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
