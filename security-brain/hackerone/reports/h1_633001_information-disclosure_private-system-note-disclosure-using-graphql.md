---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '633001'
original_report_id: '633001'
title: Private System Note Disclosure using GraphQL
weakness: Information Disclosure
team_handle: gitlab
created_at: '2019-06-30T23:09:55.030Z'
disclosed_at: '2019-12-13T13:31:58.430Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 17
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Private System Note Disclosure using GraphQL

## Metadata

- HackerOne Report ID: 633001
- Weakness: Information Disclosure
- Program: gitlab
- Disclosed At: 2019-12-13T13:31:58.430Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary
When you use the REST API or UI to view an issue's discussion/notes, private system note is hidden to member's only.

Such as moving an issue to a private project, making issue as duplicate of a confidential issue, someone mentioned this issue in a confidential issue.

They are properly hidden in REST and UI, but you can still see them in graphql

### Steps to reproduce
- Open a new private browser without an authenticated session
- visit https://gitlab.com/-/graphql-explorer
- paste this query and see the difference between UI https://gitlab.com/username16/ci-test/issues/1 <-- this is public project with public issue doing some private stuff and graphql response

```
query {
  project(fullPath:"username16/ci-test"){
    issue(iid:"1"){
      descriptionHtml

      notes{
        edges{
          node{
            bodyHtml
            system
            author{
              username
            }
            body
          }
        }
      }
    }}
  }
```

- You should notice it has moved to dynamic#1, which is not visible from UI
- also you should be able to see it was marked as duplicate of #2, which is not visible from UI cause #2 is confidential
- also you can see someone mentioned this issue in #2, which is not visible from UI cause #2 is confidentail

### Impact
Disclosure of all system note of an issue/MR/designs that should be private

## Reproduced on gitlab.com

## Impact

Disclosure of all system note of an issue/MR/designs that should be private

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
