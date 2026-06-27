---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '361089'
original_report_id: '361089'
title: twitter api access token leaked on github
weakness: Cleartext Storage of Sensitive Information
team_handle: liberapay
created_at: '2018-06-02T13:37:08.127Z'
disclosed_at: '2018-06-02T14:06:24.030Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
asset_identifier: https://github.com/liberapay/liberapay.com
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# twitter api access token leaked on github

## Metadata

- HackerOne Report ID: 361089
- Weakness: Cleartext Storage of Sensitive Information
- Program: liberapay
- Disclosed At: 2018-06-02T14:06:24.030Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

sensitive token were leaked on GitHub page of liberapay . also mixpanel token was leaked
TWITTER_CONSUMER_KEY=QBB9vEhxO4DFiieRF68zTA
 TWITTER_CONSUMER_SECRET=mUymh1hVMiQdMQbduQFYRi79EYYVeOZGrhj27H59H78
+TWITTER_ACCESS_KEY=34175404-G6W8Hh19GWuUhIMEXK0LyZsy7N9aCMcy1bYJ9rI
+TWITTER_ACCESS_SECRET=K6wxV1OCsihZAkEPkWtoLYDiRJnWajBBWn4UgliTRQ
 TWITTER_CALLBACK=http://127.0.0.1:8537/on/twitter/associate
 MIXPANEL_TOKEN=cb9dec68ac0ee57071f0be39f164a417

## Impact

a attacker with your credentials can have severe impact

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
