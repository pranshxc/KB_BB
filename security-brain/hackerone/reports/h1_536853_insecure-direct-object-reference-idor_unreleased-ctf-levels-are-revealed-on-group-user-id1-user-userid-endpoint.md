---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '536853'
original_report_id: '536853'
title: Unreleased CTF Levels are Revealed on /group/user/ID1?user=USERID endpoint
weakness: Insecure Direct Object Reference (IDOR)
team_handle: security
created_at: '2019-04-12T17:21:55.416Z'
disclosed_at: '2019-04-23T00:31:38.116Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 153
asset_identifier: https://ctf.hacker101.com
asset_type: URL
max_severity: low
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Unreleased CTF Levels are Revealed on /group/user/ID1?user=USERID endpoint

## Metadata

- HackerOne Report ID: 536853
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: security
- Disclosed At: 2019-04-23T00:31:38.116Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
At this moment, the two new upcoming CTF levels for https://ctf.hacker101.com/ctf have not been revealed. However, an IDOR at the https://ctf.hacker101.com/group/user/ID1?user=USERID endpoint reveals them (see attached screenshot)

**Description:**

### Steps To Reproduce

1. Create a group.
2. At the group index page (https://ctf.hacker101.com/group/groupIndex/GROUPID), click on the "details" button for yourself.
3. At the bottom, you should see the unreleased CTF levels.

### Optional: Supporting Material/References (Screenshots)

 * Attached screenshot with unreleased CTF at bottom

## Impact

Low level, but the user could get ahead of others by knowing upcoming levels, especially if there are prizes for being the first to complete them. Plus it reveals an interesting IDOR endpoint linked to the database.

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
