---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260938'
original_report_id: '260938'
title: Homograph IDNs displayed in Description
team_handle: legalrobot
created_at: '2017-08-17T05:43:53.276Z'
disclosed_at: '2017-09-16T23:12:32.548Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
asset_identifier: app.legalrobot-test.com
asset_type: URL
max_severity: none
tags:
- hackerone
---

# Homograph IDNs displayed in Description

## Metadata

- HackerOne Report ID: 260938
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-09-16T23:12:32.548Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The IDN: http://ebаy.com/ is a homograph for the latin ebay.com. if you copy and paste a link, you might think that you are going to ebay.com. in fact, you are going to a homograph url http://xn--eby-7cd.com/

it would be safer to show the punycode version of the url so that it would be apparent that something weird is going on. that is, show http://eb@y.com/ instead of http://ebаy.com/

#STEPS TO REPRODUCE:

1. Login to your account https://app.legalrobot-uat.com
2. Navigate this URL:

      https://app.legalrobot-uat.com/roadmap

3. Click the "Add a new idea" button
4. Actually their is no problem on Name but in Description.
5. Put http://ebаy.com/ on Description
6. Click the "Add Idea" Button
7. Notice that it display http://ebаy.com/ See my attached photo {F213601}

Thanks,

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
