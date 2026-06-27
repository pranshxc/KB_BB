---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '212508'
original_report_id: '212508'
title: Single User DOS on SelectedLocale -cookie (verkkopalvelu.tapiola.fi)
weakness: Uncontrolled Resource Consumption
team_handle: localtapiola
created_at: '2017-03-11T09:06:28.659Z'
disclosed_at: '2017-12-13T09:53:48.026Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Single User DOS on SelectedLocale -cookie (verkkopalvelu.tapiola.fi)

## Metadata

- HackerOne Report ID: 212508
- Weakness: Uncontrolled Resource Consumption
- Program: localtapiola
- Disclosed At: 2017-12-13T09:53:48.026Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,
I want to report again similar issue to #201723 , but cookie is setting up on different parameter.

## Basic report information
**Summary:**
found a way in which any attacker will send a link to user, and user will not able to use any of the service provided by lahitapiola.

**Affected Websites**
1. verkkopalvelu.tapiola.fi
2. www.lahitapiola.fi

**Domain:** 
verkkopalvelu.tapiola.fi

## Browsers / Apps Verified In:

  * Latest Version of Firefox 

## Steps To Reproduce:

####Payload: `"><img src ` (only)

####Vulnerable Parameter: selectedLocale

  1. Send this url to victim using html tag:

```
https://verkkopalvelu.tapiola.fi/a3/PalauteWeb/?locale=fi&ltapp=Palautelomake&p=1302686354497&selectedLanguage=fi%27&selectedArea=&selectedLocale=en%22%3E%3Cimg%20src
```

For your testing purpose, copy this link in your browser, and paste it and go, now click on any link on website, you will be ended up on this page:

 {F167978}

  2: User will not able to use any of the above effected localtapiola's services, untill user manually delete the cookie.

## Additional material

  * See POC video

{F167981}


Thanks
Regards
Neeraj

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
