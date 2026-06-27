---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2467999'
original_report_id: '2467999'
title: Jira Credential Disclosure within Mozilla Slack
weakness: Insecure Storage of Sensitive Information
team_handle: mozilla
created_at: '2024-04-17T17:46:50.588Z'
disclosed_at: '2024-04-23T12:13:25.734Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 58
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# Jira Credential Disclosure within Mozilla Slack

## Metadata

- HackerOne Report ID: 2467999
- Weakness: Insecure Storage of Sensitive Information
- Program: mozilla
- Disclosed At: 2024-04-23T12:13:25.734Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I was able to find Jira Admin API Keys disclosed within Mozilla's #███ Slack channel which was posted by a staff member of Mozilla.

## Steps To Reproduce:
  1.Navigate to the following file -█████
  2.Observe the exposed credentials on line 310-312 of the Python Script.
  3. Verify Groups with the following CURL request - `curl -u "██████:ATATT3xFfGF0V99l_█████████551CCC5D" -H "Content-Type: application/json" https://mozilla-hub.atlassian.net/rest/api/3/user/groups?accountId=████████`
 
4. Observe the following output which shows that the user is a Jira Administrator, Administrator and  Jira Service Desk user etc.

[{"name":"jira-servicedesk-users","groupId":"███","self":"███████:"jira-administrators","groupId":"████████","self":██████:"jira-software-users","groupId":"███","self":██████████:"jira-servicemanagement-customers-mozilla-hub","groupId":"██████████","self":███:"site-admins","groupId":"████████","self":██████:"administrators","groupId":"██████████","self":██████:"Managers","groupId":"█████","self":██████"}]

## Impact

## Summary:

Admin API credentials provide elevated privileges that can grant access to all projects, user accounts, configurations, and other sensitive data stored in Jira.

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
