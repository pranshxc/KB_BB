---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '800608'
original_report_id: '800608'
title: IDOR - Delete Users Saved Projects
weakness: Insecure Direct Object Reference (IDOR)
team_handle: deptofdefense
created_at: '2020-02-20T12:48:33.555Z'
disclosed_at: '2022-03-18T19:00:20.869Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# IDOR - Delete Users Saved Projects

## Metadata

- HackerOne Report ID: 800608
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: deptofdefense
- Disclosed At: 2022-03-18T19:00:20.869Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Target Url**
https://█████/██████████/█████████={Target_id}

**Summary:**
Hello, I found an IDOR bug in deleting users saved projects. Through changing the search id in the above url in a GET request, you can delete saved projects for any users.

## Step-by-step Reproduction Instructions

1. Navigate to your account -> Saved Searches.
2. Copy the url of the delete request `https://████/█████/████████={search_id}`
3. Replace your search id with the target victim search id and send the request. The target saved search will be deleted from the victim
To be more clear I uploaded this video, please watch it.
{}

## Suggested Mitigation/Remediation Actions
Check the user that is deleting the saved searches if he is legitimate and the real owner of that search or not.

## Impact

This would lead the attacker to delete all users saved searches through bruteforcing their ids. And since the id are incremented in an easy sequence, attacker can do this attack very fast.

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
