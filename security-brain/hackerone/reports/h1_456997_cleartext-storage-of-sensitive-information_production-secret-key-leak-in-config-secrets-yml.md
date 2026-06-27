---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '456997'
original_report_id: '456997'
title: Production secret key leak in config/secrets.yml
weakness: Cleartext Storage of Sensitive Information
team_handle: grab
created_at: '2018-12-06T17:46:45.164Z'
disclosed_at: '2019-01-08T07:55:23.269Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 8
asset_identifier: '*.grab.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Production secret key leak in config/secrets.yml

## Metadata

- HackerOne Report ID: 456997
- Weakness: Cleartext Storage of Sensitive Information
- Program: grab
- Disclosed At: 2019-01-08T07:55:23.269Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

**Summary:** 
Production secret key leak in config/secrets.yml

**Description:** 
In Github, http://engineering.grab.com/ secret_key_base is leaked which is present in the config/secrets.yml

## Steps To Reproduce:

  1. Go to the below GitHub URL and we can verify that secret_key_base is present.
```
https://github.com/grab/blogs/blob/master/2017-01-29-deep-dive-into-database-timeouts-in-rails/config/secrets.yml
```

Mitigation:-
```
https://medium.com/@thejasonfile/hide-your-api-keys-hide-your-skype-api-keys-884427746f9c
```

## Impact

Proper Impact is explained here:-
https://stackoverflow.com/questions/44220691/rails-what-are-the-consequences-of-a-leaked-secret-key-base

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
