---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8724'
original_report_id: '8724'
title: Clickjacking
weakness: UI Redressing (Clickjacking)
team_handle: mailru
created_at: '2014-04-21T17:07:18.310Z'
disclosed_at: '2014-06-06T09:53:17.145Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking

## Metadata

- HackerOne Report ID: 8724
- Weakness: UI Redressing (Clickjacking)
- Program: mailru
- Disclosed At: 2014-06-06T09:53:17.145Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

URL :- http://promo.calendar.mail.ru/

POC :-

<html>
   <head>
     <title>Clickjack test page</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="http://promo.calendar.mail.ru/" width="500" height="500"></iframe>
   </body>
</html>

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
