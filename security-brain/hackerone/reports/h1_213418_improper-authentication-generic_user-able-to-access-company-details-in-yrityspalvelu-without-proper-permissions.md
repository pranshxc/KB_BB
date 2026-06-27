---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '213418'
original_report_id: '213418'
title: User able to access company details in yrityspalvelu without proper permissions
weakness: Improper Authentication - Generic
team_handle: localtapiola
created_at: '2017-03-14T15:28:11.444Z'
disclosed_at: '2018-06-22T08:03:47.678Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 63
asset_identifier: yrityspalvelu.tapiola.fi
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# User able to access company details in yrityspalvelu without proper permissions

## Metadata

- HackerOne Report ID: 213418
- Weakness: Improper Authentication - Generic
- Program: localtapiola
- Disclosed At: 2018-06-22T08:03:47.678Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** User able to access company details in yrityspalvelu without proper permissions

**Description:** User can access "any" company detail information, contracts, bills etc if able to do TUPAS authentication. If company already have "pääkäyttäjä" accounts made, this most like wont work. I tried with "clean/fresh" company.

**Domain:** https://yrityspalvelu.tapiola.fi/

## Browsers / Apps Verified In:

  * Chrome

## Steps To Reproduce:

 1. Go to https://yrityspalvelu.tapiola.fi/a3/YvpAuthWebKoha/verkkopalveluhakemus/
 2. Fill with company info you want examine (y-tunnus)
 3. Give any bogus user data
 4. Do TUPAS authentication and follow registration till end.
 5. Login using fresh credentials (email+passwd)
https://yrityspalvelu.tapiola.fi/a1/tatuma/jsp/kayttaja/kirjaudu.jsp
 6. View bills, company information, made insurance claims etc..

## Additional material

  * not this time.

## Related reports, best practices

*tick on "Minulla on lupa tehdä yrityksen verkkopalvelusopimus." should not be enough properly ensure user permission to view company information and in some cases quite sensitive one.

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
