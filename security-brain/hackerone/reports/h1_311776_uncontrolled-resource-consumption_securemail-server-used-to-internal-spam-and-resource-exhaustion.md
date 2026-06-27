---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '311776'
original_report_id: '311776'
title: Securemail server used to internal spam and resource exhaustion
weakness: Uncontrolled Resource Consumption
team_handle: localtapiola
created_at: '2018-02-02T18:57:21.929Z'
disclosed_at: '2018-02-15T20:28:39.023Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
asset_identifier: secure.lahitapiola.fi
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Securemail server used to internal spam and resource exhaustion

## Metadata

- HackerOne Report ID: 311776
- Weakness: Uncontrolled Resource Consumption
- Program: localtapiola
- Disclosed At: 2018-02-15T20:28:39.023Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
Confidential message systems fails to restrict large amount of receivers. This might lead to hardware exhausting and/or attacking localtapiola internal employees as securemail recipient.

**Description:** 
Despite https://secure.lahitapiola.fi/ is designed to send emails, there is small bug which allows user to exhaust server resources and or exhausting peoples work time. I used 376 different dummy non-existent *@lahitapiola.fi receiver in tests.

**Impact:**
Loss of worktime while checking thru every securemail email. It takes time to copy/paste received links and check if the contact is real or not. This is basically email spam with some steroids as sender server is lahitapiola´s trusted one. Mixing different senders addrs and attachments this could be neat tool to exploiters.

## Browsers / Apps Verified In:

  *Chrome, Firefox

## Steps To Reproduce:

  1. Go to https://secure.lahitapiola.fi/index and fill all fields. Intercept when sending email and add recipient email addresses separeted by comma in under Content-Disposition: form-data; name="recipient"


## Additional material

  * not applicable

## Related reports, best practices

  * Deltagon´s secure mail allows user to add more than one recipient by clicking "add row". This can be manually overrided. There is no limit or it is very high. Service should restrict amount of default receivers or allow email to be send only to email addresses inserted thru "add row" process.

## Impact

spamming from 'trusted' source internal lahitapiola´s employees.

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
