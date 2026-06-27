---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '770190'
original_report_id: '770190'
title: Unexpected access to process open files via file:///proc/self/fd/n
weakness: Information Disclosure
team_handle: curl
created_at: '2020-01-08T11:29:41.917Z'
disclosed_at: '2021-02-08T07:53:52.299Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
asset_identifier: https://github.com/curl/curl
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Unexpected access to process open files via file:///proc/self/fd/n

## Metadata

- HackerOne Report ID: 770190
- Weakness: Information Disclosure
- Program: curl
- Disclosed At: 2021-02-08T07:53:52.299Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
file_connect() routine (https://github.com/curl/curl/blob/1b71bc532bde8621fd3260843f8197182a467ff2/lib/file.c#L134) does not prevent access to /proc/self/fd pseudo filesystem. Application using libcurl and accepting URLs to fetch can be tricked to return content of any open file by passing a specially crafted file:///proc/self/fd/<number> URLs. Since the specific files are open by the application itself, they will always be accessible as long as the files remain open. This will bypass for example drop of privileges performed after opening the file(s).

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. Open a privileged file (for example /etc/shadow)
  2. Drop the process privileges
  3. Accept URL as user input
  4. Fetch URL with libcurl
  5. Send received data to user


## Supporting Material/References:

## Impact

Authorization bypass: Access to privileged files otherwise not accessible via file://

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
