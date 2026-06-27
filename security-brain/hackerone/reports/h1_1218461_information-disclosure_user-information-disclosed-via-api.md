---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1218461'
original_report_id: '1218461'
title: User information disclosed via API
weakness: Information Disclosure
team_handle: gsa_vdp
created_at: '2021-06-06T08:07:32.922Z'
disclosed_at: '2022-10-19T18:47:49.386Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: sam.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# User information disclosed via API

## Metadata

- HackerOne Report ID: 1218461
- Weakness: Information Disclosure
- Program: gsa_vdp
- Disclosed At: 2022-10-19T18:47:49.386Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

It appears that the requests for "system accounts" are fully available via an API endpoint that does not require authentication. 

The main issue is that among the information disclosed are user emails (many with gmail addresses) but the individual applications also include information that the user provides about their organization/integration such as IP addresses, physical locations and whether or not the system uses okta. 

## Steps To Reproduce:

Navigate to the following URL:  https://sam.gov/api/prod/iam/cws/v1/applications/

## Supporting Material/References:

Help desk article about what the [system accounts are](http://www.fsd.gov/gsafsd_sp?id=gsafsd_kb_articles&sys_id=c8d50f1d1b187c909ac5ddb6bc4bcbe2)

Here is an example object of what is returned from the endpoint:

```
{"uid":12345,"systemAccountName":"POC","interfacingSystemVersion":"beta.POCcom","systemDescriptionAndFunction":"example of data thgat is leaked","systemAdmins":"[]","systemManagers":"[{\"commonName\":\"James Bond\",\"uid\":\"fakepassword@gmail.com\",\"mail\":\"fake-fun@opayq.com\",\"name\":\"James Bond\",\"isGov\":false,\"id\":\"fake-fun@opayq.com\"}]","contractOpportunities":"","contractData":"","entityInformation":"","federalHierarchy":"","wageDeterminations":"","assistanceListings":"","referenceData":"","ipAddress":"","typeOfConnection":"","physicalLocation":"","securityOfficialName":"","securityOfficialEmail":"","uploadAto":"","authorizationConfirmation":false,"authorizingOfficialName":"","submittedDate":"2021-06-06T06:49:17.130+0000","submittedBy":"fake-fun@opayq.com","securityApprover":"","rejectedBy":"","rejectionReason":"","applicationStatus":"Draft","isGov":false,"migratedToOkta":false,"fips199Categorization":""}
```

## Impact

A threat actor could view personal information about users on the platform.

It is also theoretically possible that a threat actor could use information gathered from this endpoint to identify future targets and footholds.

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
