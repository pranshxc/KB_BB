---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '183796'
original_report_id: '183796'
title: XSS and open redirect in verkkopalvelu.lahitapiola.fi
weakness: Cross-site Scripting (XSS) - Generic
team_handle: localtapiola
created_at: '2016-11-21T14:35:23.649Z'
disclosed_at: '2016-12-10T11:56:58.418Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# XSS and open redirect in verkkopalvelu.lahitapiola.fi

## Metadata

- HackerOne Report ID: 183796
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: localtapiola
- Disclosed At: 2016-12-10T11:56:58.418Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Dears,
Kindly note that after submitting CSRF vulnerability in the subject subdomain which is still triaged https://hackerone.com/reports/178811 I Noticed After more testing to the subject domain that there is multiple endpoints vulnerable to an XSS and those are the same endpoints i included in my first report that vulnerable to CSRF.

**Description:**
The reason for the XSS basically is "CRLF injection" where i was able to inject http-headers to set custom cookies and custom content "XSS attack" within the response of the website.

"The parameter vulnerable here is parameter p" and you will see that below in the POC

**Endpoints Affected are:**
https://verkkopalvelu.lahitapiola.fi/a6/VerkkokauppaYTWAR/YT/Etusivu.jsf
https://verkkopalvelu.lahitapiola.fi/a6/ajoneuvolaskin/MA/Etusivu.jsf

## Browsers / Apps Verified In:

All Browsers

## Steps To Reproduce and POC :

1-https://verkkopalvelu.lahitapiola.fi/a6/VerkkokauppaYTWAR/YT/Etusivu.jsf?productMode=YT&locale=fi&ltapp=LT_Yksityistapaturmalaskuri&p=1412889500323ew2du7e081azeza%22%27%3E%3C%0D%0A+%0D%0A+%3Csvg/onload=alert%28/Xssed_By_G3nt3lman/%29%3E&selectedLanguage=fi&selectedArea=

2-https://verkkopalvelu.lahitapiola.fi/a6/ajoneuvolaskin/MA/Etusivu.jsf?productMode=YT&locale=fi&ltapp=LT_Yksityistapaturmalaskuri&p=1412889500323ew2du7e081azeza%22%27%3E%3C%0D%0A+%0D%0A+%3Csvg/onload=alert%28/Xssed_By_G3nt3lman/%29%3E&selectedLanguage=fi&selectedArea=

When you open each link a pop up will appear (/Xssesd_By_G3nt3lman)

## Additional material

Attached the POC

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
