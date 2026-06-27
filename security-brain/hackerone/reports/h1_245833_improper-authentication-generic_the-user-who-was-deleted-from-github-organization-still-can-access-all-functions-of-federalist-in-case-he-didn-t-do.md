---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '245833'
original_report_id: '245833'
title: The user, who was deleted from Github Organization, still can access all functions
  of federalist, in case he didn't do logout
weakness: Improper Authentication - Generic
team_handle: gsa_bbp
created_at: '2017-07-04T13:48:23.900Z'
disclosed_at: '2017-09-05T19:48:53.548Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
asset_identifier: https://github.com/18f/federalist
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# The user, who was deleted from Github Organization, still can access all functions of federalist, in case he didn't do logout

## Metadata

- HackerOne Report ID: 245833
- Weakness: Improper Authentication - Generic
- Program: gsa_bbp
- Disclosed At: 2017-09-05T19:48:53.548Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

##Description
Hi. I found a non-critical session management bug, which still can have serious impact in some scenarios.
When user perform login to the Federalist through Github, federalist checks his Organization ID (but only upon login).
When the user was deleted from organization for some reasons, but he was logged in the Federalist (or saved his session cookies), he can still do any action on behalf of organization (create sites, delete sites etc).

##Reproduction Steps & POC
1) Add a test user to your organization, which have access to the federalist.
2) Login to the Federalist.
3) Remove the user from organization, or leave organization
4) Try to create or delete the site. Federalist doesn't know that this user has no permissions, and will allow him to use functions.

##Suggested fix
You should implement Organization ID checking in the requests.
Upon login, the endpoint `/v0/me` is called (once). But it can be a good idea to call it in a random periods of time and check the organization ID, and in case it will return 403 - invalidate user session.

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
