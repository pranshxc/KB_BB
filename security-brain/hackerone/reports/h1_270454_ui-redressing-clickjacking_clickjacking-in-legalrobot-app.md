---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '270454'
original_report_id: '270454'
title: Clickjacking in Legalrobot app
weakness: UI Redressing (Clickjacking)
team_handle: legalrobot
created_at: '2017-09-22T07:04:48.244Z'
disclosed_at: '2017-11-10T11:36:03.466Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: app.legalrobot-test.com
asset_type: URL
max_severity: none
tags:
- hackerone
- ui-redressing-clickjacking
---

# Clickjacking in Legalrobot app

## Metadata

- HackerOne Report ID: 270454
- Weakness: UI Redressing (Clickjacking)
- Program: legalrobot
- Disclosed At: 2017-11-10T11:36:03.466Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Dear Team,

#POC
Please find attached screenshots

#Steps to reproduce:

create index.html file with following content:
<iframe sandbox="allow-scripts allow-forms" src="https://app.legalrobot-uat.com/pending-verification" width="1000" height="600"></iframe>

Open index.html in browser

Actual result: Legalrobot email verification page is viewed in iframe.

#Remediation:
Frame busting technique is the better framing protection technique.
Sending the proper X-Frame-Options HTTP response headers that instruct the browser to not allow raming from other domains.

Same issue found in https://app.legalrobot.com/pending-verification as well.

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
