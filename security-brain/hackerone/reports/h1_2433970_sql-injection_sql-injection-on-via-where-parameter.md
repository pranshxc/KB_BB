---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2433970'
original_report_id: '2433970'
title: SQL injection on ██████████ via 'where' parameter
weakness: SQL Injection
team_handle: deptofdefense
created_at: '2024-03-25T22:28:56.151Z'
disclosed_at: '2024-05-03T18:04:22.062Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
tags:
- hackerone
- sql-injection
---

# SQL injection on ██████████ via 'where' parameter

## Metadata

- HackerOne Report ID: 2433970
- Weakness: SQL Injection
- Program: deptofdefense
- Disclosed At: 2024-05-03T18:04:22.062Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

An sql injection vulnerability is produced on 'where' parameter of ArcGIS server allows to retreive db content

## PoC

1- Go to https://█████/arcgis/rest/services/Data/ANC_External/MapServer/1/query?where=&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=html, this will show a web form.

2- On `where` field, insert the following query : `1=1`, the query is a 1=1 that is true, so it will show all record content of the DB.

██████████

███████

3- So if you inserts `1=0` on where column, the server response will be empty and didn't show any info.

NOTE: i will attach the sql injection vulnerability confirmed by esri support: https://support.esri.com/en-us/knowledge-base/arcgis-10-1-sp1-for-server-contains-a-blind-sql-injecti-000011683

## Impact

An attacker is able to exploit sql injection via arcGIS server

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1- Go to https://██████/arcgis/rest/services/Data/ANC_External/MapServer/1/query?where=&text=&objectIds=&time=&timeRelation=esriTimeRelationOverlaps&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&distance=&units=esriSRUnit_Foot&relationParam=&outFields=&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&havingClause=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&historicMoment=&returnDistinctValues=false&resultOffset=&resultRecordCount=&returnExtentOnly=false&sqlFormat=none&datumTransformation=&parameterValues=&rangeValues=&quantizationParameters=&featureEncoding=esriDefault&f=html, this will show a web form.

2- On `where` field, insert the following query : `1=1`, the query is a 1=1 that is true, so it will show all record content of the DB.

3- So if you inserts `1=0` on where column, the server response will be empty and didn't show any info.

## Suggested Mitigation/Remediation Actions
Esri released an update to ArcGIS Server 10.1 Service Pack 1. If you cannot patch, please consider the following workarounds.

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
