---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '511536'
original_report_id: '511536'
title: Unprotected Api EndPoints
weakness: Violation of Secure Design Principles
team_handle: semmle
created_at: '2019-03-18T12:22:37.952Z'
disclosed_at: '2019-03-21T17:38:02.468Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 3
asset_identifier: lgtm-com.pentesting.semmle.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Unprotected Api EndPoints

## Metadata

- HackerOne Report ID: 511536
- Weakness: Violation of Secure Design Principles
- Program: semmle
- Disclosed At: 2019-03-21T17:38:02.468Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

## Summary:
I am able to automate the get/post requests of the following api end-points with a python script which can lead to heavy load to server resulting in dos attack or buffer overflow.
/internal_api/v0.2/getSuggestedProjects
/internal_api/v0.2/getLanguages
/internal_api/v0.2/getLoggedInUser
/internal_api/v0.2/getSecuritySettings
/internal_api/v0.2/getActiveOAuthGrants
/internal_api/v0.2/getAccountEmails
/internal_api/v0.2/getExternalAccounts
/internal_api/v0.2/getAuthenticationProviders
/internal_api/v0.2/getActivePRIntegrations
/internal_api/v0.2/getProjectLatestStateStats
/internal_api/v0.2/getBlogPosts
/internal_api/v0.2/setUsername
/internal_api/v0.2/savePublicInformation

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Create an account  lgtm-com.pentesting.semmle.net.
  2. Get The cookie and nonce value of your logged in session by intercepting post/get requests with burpsuite.
  3. Use the cookie and nonce value in dos.py script(attached) inorder to execute endless api calls.
  4.Watch Video Attached as POC. 

## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]
Video and Script is attached.

  * [attachment / reference]

## Impact

Leading to heavy load on server that can lead to dos attack or buffer overflow using post requests with no rate limit restriction.

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
