---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1057269'
original_report_id: '1057269'
title: PII Information Leak at https://████████.mil/
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2020-12-12T06:46:59.851Z'
disclosed_at: '2021-01-12T21:56:50.102Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- information-disclosure
---

# PII Information Leak at https://████████.mil/

## Metadata

- HackerOne Report ID: 1057269
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2021-01-12T21:56:50.102Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
While making use of some recon techniques I came across this file which is leaking PII information publically on the Internet. In the description section, I explain the contents of the file and why it shouldn't be public like this.

**Description:**
The file in the POC section contains more than 100 or 200 people as records. With their names, there are several other information classes present. The PII leak in this file is mainly the Names of the Individuals and their **Personal** Emails. If there were only official emails here, it would not be considered a PII leak because those emails are for official purposes and they are generally publically available. But in this case, not only their official emails are being leaked but also their personal emails. Personal emails belong only to the people and nothing official is related to those, an attacker should not have access to these emails because this is something private. This is a clear privacy violation for those who have lost their personal information to the public. The leaking file is perfect to be added into a database maintained by an attacker because it is arranged neatly in rows and columns. 

██████


## POC

https://██████████.mil/████████

## Step-by-step Reproduction Instructions

1. Go to https://█████████.mil/████████

2. Download the file.
3. View the PII


## Suggested Mitigation/Remediation Actions

- Take the file down from the Internet.
- Add an authentication mechanism to view the file.

## Impact

PII Information Leak.

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
