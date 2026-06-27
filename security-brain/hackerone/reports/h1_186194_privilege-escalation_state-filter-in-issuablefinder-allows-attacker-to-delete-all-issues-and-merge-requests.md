---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '186194'
original_report_id: '186194'
title: State filter in IssuableFinder allows attacker to delete all issues and merge
  requests
weakness: Privilege Escalation
team_handle: gitlab
created_at: '2016-11-28T23:32:53.862Z'
disclosed_at: '2016-12-06T00:57:18.114Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 11
tags:
- hackerone
- privilege-escalation
---

# State filter in IssuableFinder allows attacker to delete all issues and merge requests

## Metadata

- HackerOne Report ID: 186194
- Weakness: Privilege Escalation
- Program: gitlab
- Disclosed At: 2016-12-06T00:57:18.114Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

# Vulnerability details
The state filter in the `IssuableFinder` class has the ability to filter issues and merge requests by state. This filter is implemented by calling `public_send` with unfiltered user input. This allows an attacker to call `delete_all` or `destroy_all`. Because the method is called **before** the project / group scope is applied, it deletes all issues and merge requests of the GitLab instance.

# Proof of concept
Create two users and a new project for each of them. It doesn't matter if they're private or not. Now create an issue (or merge request) for each project. Now browse to the Issues overview. When clicking All, you'll be redirected to http://gitlab-instance/root/xxxx/issues?scope=all&state=all. Simply substitude `all` with `delete_all` in the URL and ALL issues will be deleted: http://gitlab-instance/root/xxxx/issues?scope=all&state=delete_all. To delete all merge requests, substitude `issues` with `merge_requests`. When requesting the `delete_all` URL, a 500 internal server error will be shown. This is caused by the `delete_all` method returning a boolean instead of an `ActiveRecord::Relation` class. Do **NOT** call this on the GitLab production site.

# Origin
The vulnerability comes from the fact that unsanitized user input is passed into a `public_send` call that is being called on `model.all`. Here's the `execute` method of the `IssuableFinder`:

```ruby
def execute
  items = init_collection
  items = by_scope(items)
  items = by_state(items)
  items = by_group(items)
  items = by_project(items)
  items = by_search(items)
  items = by_milestone(items)
  items = by_assignee(items)
  items = by_author(items)
  items = by_label(items)
  items = by_due_date(items)
  sort(items)
end
```

Now take a look at the `by_state` method:

```ruby
def by_state(items)
  params[:state] ||= 'all'

  if items.respond_to?(params[:state])
    items.public_send(params[:state])
  else
    items
  end
end
```

The controllers are passing the `state` parameter without any form of sanitization or validation to the finder. Since you're passing around ActiveRecord relations, `delete_all` can be called early on in the relation chain. Since the scope hasn't been applied (the `by_project` is called later), this will affect all issues and merge requests.

# Remediation
Never pass unsanitized or unvalidated user input to `public_send` or `send`.

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
