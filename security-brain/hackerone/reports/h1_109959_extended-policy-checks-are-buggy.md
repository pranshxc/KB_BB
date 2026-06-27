---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '109959'
original_report_id: '109959'
title: Extended policy checks are buggy
team_handle: phabricator
created_at: '2016-01-11T12:02:19.183Z'
disclosed_at: '2016-01-11T15:10:48.719Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
---

# Extended policy checks are buggy

## Metadata

- HackerOne Report ID: 109959
- Weakness: 
- Program: phabricator
- Disclosed At: 2016-01-11T15:10:48.719Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Mongoose. This issue is in the class PhabricatorPolicyFilter, lines 324, 338 and 339. The code refers to the index $key (a leftover from a previous foreach loop) where it should refer to $extended_key.

This will lead to all policy checks being skipped after $extended_objects[$key] is filtered out. I'm not sure if this has any consequences in practice, since the extended policy interface seems to have a limited use. Maybe it would be more serious having subprojects?

I can imagine a risk for the differential revisions: if any of the repositories failed to load (no idea if that can happen), the bugs in lines 338 and 339 would filter out the revision at $extended_objects[$key], and all the other revisions would then skip the checks.

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
