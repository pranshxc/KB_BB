---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '209398'
original_report_id: '209398'
title: HTML Injection in email from http://www.lahitapiola.fi/henkilo/sivut/tonttutesti
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localtapiola
created_at: '2017-02-27T20:20:25.371Z'
disclosed_at: '2017-03-13T15:44:47.727Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HTML Injection in email from http://www.lahitapiola.fi/henkilo/sivut/tonttutesti

## Metadata

- HackerOne Report ID: 209398
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localtapiola
- Disclosed At: 2017-03-13T15:44:47.727Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** HTML Injection in email from http://www.lahitapiola.fi/henkilo/sivut/tonttutesti

**Description:** Tonttutesti´s kutsu kaverisi feature sends email to friend with a link to Localtapiola´s tonttutesti site. Fields "Nimesi" and "Kaverisi nimi" seem to be vulnerable.

**Domain:** http://www.lahitapiola.fi/henkilo/sivut/tonttutesti

## Browsers / Apps Verified In:

  *Chrome 56

## Steps To Reproduce:

1. Go to http://www.lahitapiola.fi/henkilo/sivut/tonttutesti
2. To Nimesi and Kaverisi nimi fields insert "><a href="https://google.com">test</a> 
3. Fill rest of fields with any date and proper emails addresses 
5. Go to email provided (kaverisi sähköpostiosoite)

## Additional material

  * Received Localtapiolas email in text:
 Hei b">test
 Kaverisi a">test kutsui sinut käyttämään vertailukonetta: Mikä tonttu olet?
 Kaverisi viesti:
 f">test
 Osoite: http://www.lahitapiola.fi/henkilo/sivut/tonttutesti

## Related reports, best practices

  * https://hackerone.com/reports/190867

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
