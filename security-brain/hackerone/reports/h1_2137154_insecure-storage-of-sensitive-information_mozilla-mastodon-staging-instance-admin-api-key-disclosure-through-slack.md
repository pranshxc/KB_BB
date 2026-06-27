---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2137154'
original_report_id: '2137154'
title: Mozilla Mastodon Staging Instance Admin API Key Disclosure Through Slack
weakness: Insecure Storage of Sensitive Information
team_handle: mozilla
created_at: '2023-09-05T21:31:18.540Z'
disclosed_at: '2023-09-11T16:03:55.015Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# Mozilla Mastodon Staging Instance Admin API Key Disclosure Through Slack

## Metadata

- HackerOne Report ID: 2137154
- Weakness: Insecure Storage of Sensitive Information
- Program: mozilla
- Disclosed At: 2023-09-11T16:03:55.015Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

I was able to find Admin Maston API Keys disclosed within Mozilla's #trust-and-safety-eng channel which was posted by a staff member of Mozilla.

## Steps To Reproduce:

  1. Authenticate to mozilla.slack.com as an NDA or Mozillla Staff Member (https://wiki.mozilla.org/NDA)
  2. Search the #trust-and-safety-eng channel for █████████  (Exposed token)
  3. Validate that the token through the following command:

tok=███
ep=https://stage.moztodon.nonprod.webservices.mozgcp.net
curl -H "Authorization: Bearer $tok" "$ep/api/v1/admin/accounts/" 

4. Observe the following output (I've redacted some as it shows the output of all Mastodon accounts):

████████

5. Please note that this was only one API call demonstrated. Maston has the ability to create new accounts, change passwords. delete accounts and delete tweets as referenced within their API documentation here with the  Admin API tokens -  https://docs.joinmastodon.org/methods/accounts/

## Supporting Material/References:

Please find attached the conversation where the API token was accidentaly leaked.

██████████

## Impact

## Summary:

The exposure of Admin Mastodon API tokens represents a critical security vulnerability with the potential for severe consequences. These tokens grant unauthorized individuals comprehensive access to the Mastodon server, allowing them to manipulate user data, spread malicious content, and compromise the integrity of the platform. Immediate action is required to mitigate this risk and protect both the system and its users.

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
