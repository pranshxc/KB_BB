---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '300391'
original_report_id: '300391'
title: The parameter in the POST query allows to control size of returned page which
  in turn can lead to the potential DOS attack
weakness: Uncontrolled Resource Consumption
team_handle: localtapiola
created_at: '2017-12-25T00:23:13.002Z'
disclosed_at: '2018-04-11T10:42:45.301Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: www.lahitapiola.fi
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# The parameter in the POST query allows to control size of returned page which in turn can lead to the potential DOS attack

## Metadata

- HackerOne Report ID: 300391
- Weakness: Uncontrolled Resource Consumption
- Program: localtapiola
- Disclosed At: 2018-04-11T10:42:45.301Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace **all** the [square] sections below with the pertinent details. Do not remove any subsections of this template. If the report is not complete, we will most likely close your report with no further action. **QUALITY BEFORE QUANTITY**. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report. Use backticks for codesamples and URL's.

## Basic report information
**Summary:** The parameter in the POST query allows to control size of returned page which in turn can lead to the potential DOS attack

**Description:** I found the parameter in the POST query which allows to control the size of the returned page. Usually this query return the simple JSON error (F249324: 1.png)
If the 'dropdownSize' parameter was changed then we see the same error which is repeated the many times (F249325: 2.png)
This parameter allows to control the size of the returned page. If similar requests will be sent from a large number computers then this can be lead to the potential DOS attack
The POST query is attached (F249327: query.txt)

**Domain:** www.lahitapiola.fi

## Browsers / Apps Verified In:

  * Firefox ESR 45.3.0

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

  1. Change the value in the dropdownSize parameter from the attached query.txt and send the query

## Additional material

  * 1.png
  * 2.png
  * 3.png
  * query.txt

## Related reports, best practices

## Impact

The attacker can make a machine or network resource unavailable

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
