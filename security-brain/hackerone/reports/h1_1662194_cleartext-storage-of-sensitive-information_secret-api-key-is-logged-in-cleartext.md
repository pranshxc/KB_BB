---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1662194'
original_report_id: '1662194'
title: Secret API Key is logged in cleartext
weakness: Cleartext Storage of Sensitive Information
team_handle: omise
created_at: '2022-08-07T20:49:40.602Z'
disclosed_at: '2022-12-23T09:25:17.056Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 28
asset_identifier: github.com
asset_type: SOURCE_CODE
max_severity: high
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Secret API Key is logged in cleartext

## Metadata

- HackerOne Report ID: 1662194
- Weakness: Cleartext Storage of Sensitive Information
- Program: omise
- Disclosed At: 2022-12-23T09:25:17.056Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

While code-reviewing the repository <https://github.com/omise/omise-python/>, I have found that you log in clear-text some sensitive data. 

## Steps To Reproduce:

  1. Check here [omise/request.py#L88](https://github.com/omise/omise-python/blob/bfcf283378a823139b9f19f10e84d42a98c5b1ac/omise/request.py#L88) and here [omise/request.py#L111](https://github.com/omise/omise-python/blob/bfcf283378a823139b9f19f10e84d42a98c5b1ac/omise/request.py#L111)
 1. The code source explicitly logs in debugging mode the secret API key.
```
logger.debug('Authorization: %s', self.api_key)
```

 1. Activate logging level debug and run the following sample.py file 
```
import omise
omise.api_secret = 'skey_test_5sqdfyjv0rtqzs9f2x2'

customer = omise.Customer.create(
   description='John Doe',
   email='john.doe@example.com'
)
```

You will get:

{F1857247}

## Impact

- sensitive data logged in clear text may end up in unusual places: recorded demonstrations, copied logs, etc.

## Remediation

- I suggest you log at least a partial part of the secret API key if not remove the L88 and L111 in whole.

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
