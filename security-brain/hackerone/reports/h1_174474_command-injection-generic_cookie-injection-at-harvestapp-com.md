---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '174474'
original_report_id: '174474'
title: Cookie Injection at 'harvestapp.com'
weakness: Command Injection - Generic
team_handle: harvest
created_at: '2016-10-07T09:52:01.624Z'
disclosed_at: '2017-03-24T11:03:01.958Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- command-injection-generic
---

# Cookie Injection at 'harvestapp.com'

## Metadata

- HackerOne Report ID: 174474
- Weakness: Command Injection - Generic
- Program: harvest
- Disclosed At: 2017-03-24T11:03:01.958Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello guys,

**_Details:_**
Well, initially I was testing for CRLF (Carriage Return Line Feed) Injection, but how turned out, I was able to inject cookie without CRLF, just via # value at HTTP Request.

**_PoC:_**
Attacker able to inject new cookie from any application place, e.g.
`https://testerovusera.harvestapp.com/people/1412277/edit#NewLocalCookieKey=NewLocalCookieValue`
in this case cookie will be created to following path, and will be valid only there: _/people/1412277/_
**but**, it could be bypassed, if append root application path, e.g.
`https://testerovusera.harvestapp.com/people/1412277/edit#NewGlobalCookieKey=NewGlobalCookieValue;path=/;/`
{F126502}

**_Attacking scenario:_**
This vulnerability perfectly could be used in combination with other vulnerabilities:
- XSS thru Cookie;
- Session Fixation;
- CSRF protection bypass

**_Recommendation:_**
Properly validate what is going to cookie jar

Thank you,
Stas

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
