---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '972355'
original_report_id: '972355'
title: GraphQL Query leads to sensitive information disclosure
weakness: Privacy Violation
team_handle: gitlab
created_at: '2020-09-18T05:27:28.778Z'
disclosed_at: '2021-03-08T11:18:28.535Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 12
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- privacy-violation
---

# GraphQL Query leads to sensitive information disclosure

## Metadata

- HackerOne Report ID: 972355
- Weakness: Privacy Violation
- Program: gitlab
- Disclosed At: 2021-03-08T11:18:28.535Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the (parenthesized) sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

### Summary

Graphql Query mentioned below disclosed emails of profiles which are not visible on their public pages in gitlab


### Steps to reproduce

1> Go to Gitlab Graphql Explorer (https://gitlab.com/-/graphql-explorer)
2>  Use the query to fetch the information 

    {
    users {
    edges {
      node {
        username
        email
        avatarUrl
        status {
          emoji
          message
          messageHtml
         }
        }
       }
      }
     }

3> Navigate through any of the public profile of the usernames  fetched  with url : https://gitlab.com/username
4> Email information is not displayed in the public profile while the graphql query fetches it 

### Impact

This can be abused since email address is not publicly visible through gitlab profile. Any person can access user emails and try to hack their accounts using brute-force etc.

### What is the current *bug* behavior?

It displays sensitive information about the user which is not available in their public profile 

### What is the expected *correct* behavior?

it should only display public profile information such as username but not email

### Relevant logs and/or screenshots

Screenshot attached

## Impact

This can be abused since email address is not publicly visible through gitlab profile. Any person can access user emails and try to hack their accounts using brute-force etc

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
