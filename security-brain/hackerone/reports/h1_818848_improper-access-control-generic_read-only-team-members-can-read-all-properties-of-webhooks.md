---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '818848'
original_report_id: '818848'
title: Read-only team members can read all properties of webhooks
weakness: Improper Access Control - Generic
team_handle: security
created_at: '2020-03-13T17:07:03.545Z'
disclosed_at: '2020-04-29T17:21:29.411Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 28
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Read-only team members can read all properties of webhooks

## Metadata

- HackerOne Report ID: 818848
- Weakness: Improper Access Control - Generic
- Program: security
- Disclosed At: 2020-04-29T17:21:29.411Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:**

A team member can view all properties of webhooks despite not needing them.

### Steps To Reproduce

1. Have an admin of a program setup webhooks
2. As a team member (read-only)log in
3. Run the following graphql query:
```
    {
      query {
        team(handle: "security") {
          name
          webhooks {
            nodes {
              id
              secret
              url
            }
          }
        }
      }
    }
```
4. See that you get data back

## Impact

Read only users will be able to identify where webhooks exist and secrets

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
