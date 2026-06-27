---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '212629'
original_report_id: '212629'
title: Gitlab.com is vulnerable to reverse tabnabbing. (#2)
weakness: UI Redressing (Clickjacking)
team_handle: gitlab
created_at: '2017-03-11T18:45:39.677Z'
disclosed_at: '2017-05-09T19:12:21.392Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
tags:
- hackerone
- ui-redressing-clickjacking
---

# Gitlab.com is vulnerable to reverse tabnabbing. (#2)

## Metadata

- HackerOne Report ID: 212629
- Weakness: UI Redressing (Clickjacking)
- Program: gitlab
- Disclosed At: 2017-05-09T19:12:21.392Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Dear GitLab bug bounty team,

# Summary
---

Gitlab.com is vulnerable to reverse tabnabbing in issues, comments, etc. This is the same type of issue as https://hackerone.com/reports/211065, but far worse since in the previous report only a user with developer access to a project could view the "Environments" tab. In this case, the issue affects anywhere where HTML can be added.

# Why does this vulnerability exist?
---

By creating a link with `https://gitlab.com@example.com` the parser ignores it and does not add the usual `rel="nofollow noreferrer"` which is located on all other links. I discovered this, because I noticed that internal links are treated differently than external links. So in the example above the victim ends up on `example.com`, which is where the same scenario as https://hackerone.com/reports/211065 can be performed.

In order to demonstrate this issue the following payload can be used:

~~~
<a href="https://gitlab.com@example.com" target="_blank">Reverse Tabnabbing</a>
~~~

# Where does the issue lie?
---

The issue appears to lie in the following lines of code:

~~~
it 'skips internal links' do
    internal = Gitlab.config.gitlab.url
    exp = act = %Q(<a href="#{internal}/sign_in">Login</a>)
    expect(filter(act).to_html).to eq exp
  end
~~~

Link to source code: https://github.com/gitlabhq/gitlabhq/blob/master/spec/lib/banzai/filter/external_link_filter_spec.rb#L16-L20

If you require further information feel free to contact me.

Yours sincerely,
Ed

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
