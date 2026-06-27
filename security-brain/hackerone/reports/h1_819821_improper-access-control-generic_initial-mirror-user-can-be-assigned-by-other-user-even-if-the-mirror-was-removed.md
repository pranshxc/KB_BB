---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '819821'
original_report_id: '819821'
title: Initial mirror user can be assigned by other user even if the mirror was removed
weakness: Improper Access Control - Generic
team_handle: gitlab
created_at: '2020-03-15T22:22:03.892Z'
disclosed_at: '2020-08-26T13:52:40.826Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Initial mirror user can be assigned by other user even if the mirror was removed

## Metadata

- HackerOne Report ID: 819821
- Weakness: Improper Access Control - Generic
- Program: gitlab
- Disclosed At: 2020-08-26T13:52:40.826Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

### Summary

Even if the mirror was removed, `project.mirror_user` still will be persisted. So any maintainer can create "pull" mirror with initial mirror user:
```
  # safe_mirror_params.rb

  def valid_mirror_user?(mirror_params)
    return true unless mirror_params[:mirror_user_id].present?

    default_mirror_users.map(&:id).include?(mirror_params[:mirror_user_id].to_i)
  end

  def default_mirror_users
    # mirror is removed, but "project.mirror_user" is still presented here
    [current_user, project.mirror_user].compact.uniq 
  end
```

### Steps to reproduce

1. Login as the user with "maintainer" role (let's call this user "permanent maintainer").
2. Create any "pull" mirror for the project.
3. Remove created mirror.
4. Login as the other user with "maintainer" role (let's call this user "temporary maintainer").
5. Open "Mirroring repositories" section in the project settings. "Temporary maintainer" can create a new "pull" mirror, but with "permanent maintainer" as the mirror user. So the below rule is not enforced:

> This user will be the author of all events in the activity feed that are the result of an update, like new branches being created or new commits being pushed to existing branches. **Upon creation or when reassigning you can only assign yourself to be the mirror user.**

### Impact

This feature can be used as the backdoor. "Temporary maintainer" can add controlled repository there, so even if "temporary maintainer" will be removed from the project, he still can push the commits to a repository with maintainer privileges (because the mirror user is "permanent maintainer"). 

Any who use "pull" repository mirror feature is vulnerable by this. And of course this guys, because there might at least few cases when someone might need to create "pull" repository mirror in gitlab some time before:
1. Want to test it before move from some other project hosting.
2. Started by using only gitlab CI (in which case this might be necessary to create "pull" mirror in gitlab project; see ["Benefits" section here](https://about.gitlab.com/solutions/github/)) and now moved to gitlab
3. It was just some dev/business requirement.

### What is the current *bug* behavior?

"project.mirror_user" relationship is presented even if the project repository mirror is removed. 

### What is the expected *correct* behavior?

If the mirror removed, then "project.mirror_user" relationship also should be removed, so no one can create "pull" mirror with "project.mirror_user" as the mirror user, so this rule can be enforced:

> Upon creation or when reassigning you can only assign yourself to be the mirror user.

## Impact

This feature can be used as the backdoor. "Temporary maintainer" can add a controlled repository there, so even if "temporary maintainer" will be removed from the project, he still can push the commits to a repository with maintainer privileges (because the mirror user can be set to "permanent maintainer").

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
