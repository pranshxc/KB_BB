---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '790634'
original_report_id: '790634'
title: When you call your branch the same name as a git hash, it could be checked
  out by dependents
weakness: Resource Injection
team_handle: gitlab
created_at: '2020-02-07T16:49:44.872Z'
disclosed_at: '2021-08-19T21:09:21.671Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- resource-injection
---

# When you call your branch the same name as a git hash, it could be checked out by dependents

## Metadata

- HackerOne Report ID: 790634
- Weakness: Resource Injection
- Program: gitlab
- Disclosed At: 2021-08-19T21:09:21.671Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary

If we call a branch the same name like a git hash then the moment it's checked out somewhere, git prefers the branch name.
So let's say the git hash is "e91803d442559d6efb63102b10c919e10901b01d".
And someone referenced that hash in their program.
Now the developer or a hacker with access to the repo can create a branch named "e91803d442559d6efb63102b10c919e10901b01d".
Git will checkout the branch and not the hash when someone puts "git checkout e91803d442559d6efb63102b10c919e10901b01d".
GitHub prevents users from pushing branches that are the same name as hashes, but GitLab does not.

### Steps to reproduce

(Step-by-step guide to reproduce the issue, including:)

1. Take a hash of a commit A
2. Go to any other commit B
3. Create a branch that is named the same as the hash from commit A
4. Push
5. If someone references the hash in their program, their "git checkout" will checkout commit B. Because it will use the branch name instead of the hash


### Impact

Referencing a hash isn't secure anymore. It would reference a branch that has completely different data.
git shows a warning but "git checkout {...}" is often used.

### Examples

Any project that refs a git ref

### What is the current *bug* behavior?

Gitlab accepts pushed branches that are 40-char hexadecimals

### What is the expected *correct* behavior?

Gitlab shouldn't accept pushed branches that are 40-char hexadecimals (like Github does9

### Relevant logs and/or screenshots

-

### Output of checks

-

#### Results of GitLab environment info

-

## Impact

Redirect pinned refrs of libraries if there is control of a library. A referenced hash won't point to a hash anymore. An attacker can make the branch which has the hash's name contain any other data.

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
