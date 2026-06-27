---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '168358'
original_report_id: '168358'
title: 'Clickjacking: X-Frame Header Missing'
weakness: UI Redressing (Clickjacking)
team_handle: yelp
created_at: '2016-09-14T16:27:14.287Z'
disclosed_at: '2017-11-09T20:08:58.295Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking: X-Frame Header Missing

## Metadata

- HackerOne Report ID: 168358
- Weakness: UI Redressing (Clickjacking)
- Program: yelp
- Disclosed At: 2017-11-09T20:08:58.295Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.

CODE:
<html>
   <head>
     <title>Clickjack test page</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="http://yelp.com" width="500" height="500"></iframe>
   </body>
</html>


For More :  https://www.owasp.org/index.php/Testing_for_Clickjacking_(OWASP-CS-004) 

Proof attatched !

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
