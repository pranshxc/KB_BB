---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '729341'
original_report_id: '729341'
title: Double linking cause XSS (but blokeced by CSP in gitlab.com)
weakness: Cross-site Scripting (XSS) - DOM
team_handle: gitlab
created_at: '2019-11-04T21:17:49.157Z'
disclosed_at: '2020-01-20T12:40:04.087Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 6
asset_identifier: gitlab.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# Double linking cause XSS (but blokeced by CSP in gitlab.com)

## Metadata

- HackerOne Report ID: 729341
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: gitlab
- Disclosed At: 2020-01-20T12:40:04.087Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

### Summary

URL display on Gitlab.com is currently broken.

There is a risk of XSS due to double conversion of URLs into links.
However, 12.5 incorporating the fix has not yet been released and is blocked by CSP at gitlab.com.


### Steps to reproduce

1. Login to gitlab.com
2. Create new project
3. Create a file with the following contents as `Gemfile`
4. Previe the  `Gemfile`
5. You can see in the developer tool that javascript execution has been blocked by CSP.

```ruby
gem '<img/src/onerror=alert(location)>', '2'
```


### Examples

The above code is converted to HTML as shown below and connected to XSS via the img tag.

```html
<span class="s1">'<a href="<a href=" https:="" rubygems.org="" gems="" "="">https://rubygems.org/gems/</a><img src="" onerror="alert(location)">" rel="nofollow noreferrer noopener" target="_blank"&gt;&lt;img/src/onerror=alert(location)&gt;'</span>
```

### What is the current *bug* behavior?

There is a problem with this MR (https://gitlab.com/gitlab-org/gitlab/merge_requests/18305/diffs) that was captured by Milestone 12.5.

The issue is here. https://gitlab.com/gitlab-org/gitlab/issues/35120

### What is the expected *correct* behavior?

It is expected that there will be no processing that links the URL in the screen twice.
Probably this MR. https://gitlab.com/gitlab-org/gitlab/merge_requests/19464


### Relevant logs and/or screenshots

{F625771}

screenshots https://gitlab.com/gitlab-org/gitlab/blob/master/Gemfile

### Output of checks

This bug only occurs on GitLab.com .

#### Results of GitLab environment info

The 12.5 version has not yet been released and will not occur in other environments.

## Impact

Since gitlab.com is blocked by CSP, there is almost no risk as XSS.
There are dangers of HTML injection and CSS injection.

If this issue is not fixed and a 12.5 release is made, XSS can occur in Gitlab CE / EE.

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
