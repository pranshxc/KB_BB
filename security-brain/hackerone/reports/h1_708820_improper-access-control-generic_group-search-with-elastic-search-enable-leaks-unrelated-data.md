---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '708820'
original_report_id: '708820'
title: Group search with Elastic search enable leaks unrelated data
weakness: Improper Access Control - Generic
team_handle: gitlab
created_at: '2019-10-07T09:11:08.570Z'
disclosed_at: '2019-12-14T11:25:39.733Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 95
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Group search with Elastic search enable leaks unrelated data

## Metadata

- HackerOne Report ID: 708820
- Weakness: Improper Access Control - Generic
- Program: gitlab
- Disclosed At: 2019-12-14T11:25:39.733Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary

Performing a group search when Elastic Search is enabled provides access to unrelated merge requests, issues activity, leaking the existence of private groups, plus their activity and MRs.
This happens both on the GUI and with the APIs 

### Steps to reproduce

Let's take this search on the Gitlab group: https://gitlab.com/search?utf8=%E2%9C%93&snippets=&scope=merge_requests&repository_ref=&search=%21435&group_id=9970

If you go at the end of the page, you see 5 MRs from other groups that should be private - I have no idea what are those projects - I have no relation to them, and I have no access to the group they belong to! (See attached screenshot).

A lot more data can be retrieved through the APIs, now revealing existence of groups/projects I shouldn't know they exist!

I haven't fully understand the logic of the issue, but basically every combination of ! followed by numbers (I had hits with !709, !999) leaks MRs from other groups.

While on the UI doesn't show much info, the APIs retrieve a lot of data.

It also leaks private activity on public issues.

If you search for `nextbit`, [link](https://gitlab.com/search?utf8=%E2%9C%93&snippets=&scope=notes&repository_ref=&search=nextbit&group_id=9970), you see that my main account has linked a private issue to a public issue. The activity should be private, and indeed it is not reported inside the issue itself, but it is reported in the search.

### Impact

Leaking existence of private groups, private issues activity, private MRs, with lot of metadata

## Impact

Leak of private MRs with metadata, activity of private issues, leak existence of private groups

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
