---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '210908'
original_report_id: '210908'
title: XSS on 3rd party service Localtapiola is using
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localtapiola
created_at: '2017-03-05T18:29:22.822Z'
disclosed_at: '2017-03-18T22:45:21.938Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS on 3rd party service Localtapiola is using

## Metadata

- HackerOne Report ID: 210908
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localtapiola
- Disclosed At: 2017-03-18T22:45:21.938Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** Localtapiola is using careers.fi service to job applicants at
http://www.lahitapiola.fi/tietoa-lahitapiolasta/toihin-meille/avoimet-tyopaikat/haemme-juuri-nyt

**Description:** XSS on 3rd party (careers.fi) job service which may lead loss of personal data for the localtapiola job applicants.

**Domain:** http://www.lahitapiola.fi/tietoa-lahitapiolasta/toihin-meille/avoimet-tyopaikat/haemme-juuri-nyt and https://careers.fi/tapiola/add_application.cgi

## Browsers / Apps Verified In:

  * Chrome

## Steps To Reproduce:

  1. Go to http://www.lahitapiola.fi/tietoa-lahitapiolasta/toihin-meille/avoimet-tyopaikat/haemme-juuri-nyt
 2. Click Täytä hakemuslomake
 3. Click Rekisteröidy
 4. Käyttäjätunnus registration:
Käyttäjätunnus: test"><B>test
 Salasana: some
 Vahvista: some
 Rekisteröi
 
5. Login
 käyttäjätunnus: test"><B>test
 salana: some
 
If redirected to application page, click "keskeytä". Next page you see "käyttäjänimi" field upper right corner and bolded effect. Site seem terrible and put´s Localtapiola´s job applicants personal information in to jeopardy. Other Finnish companies use this site with job applications. If publishing this, please consider to cover all necessary company names, links and pictures to protect job applicants privacy as the site might hold more serious vulnerabilities e.g. SQL injections.

## Additional material

  * pic careers.png

## Related reports, best practices

  * Insist proper web application security tests when using 3rd party services

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
