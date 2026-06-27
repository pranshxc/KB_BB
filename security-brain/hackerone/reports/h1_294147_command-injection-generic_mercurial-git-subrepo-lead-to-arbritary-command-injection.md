---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '294147'
original_report_id: '294147'
title: Mercurial git subrepo lead to arbritary command injection
weakness: Command Injection - Generic
team_handle: ibb
created_at: '2017-12-01T03:32:27.925Z'
disclosed_at: '2019-09-26T20:15:09.181Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 9
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- command-injection-generic
---

# Mercurial git subrepo lead to arbritary command injection

## Metadata

- HackerOne Report ID: 294147
- Weakness: Command Injection - Generic
- Program: ibb
- Disclosed At: 2019-09-26T20:15:09.181Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi IBB,

I'd like to submit a issue exist in Mercurial.
```
It is possible that a specially malformed repository can cause Git subrepositories to run arbitrary code in 
the form of a .git/hooks/post-update script checked in to the repository in Mercurial 4.4 and earlier. 
Typical use of Mercurial prevents construction of such repositories, but they can be created 
programmatically.
```
Further details of my original report can be found at:
https://bz.mercurial-scm.org/show_bug.cgi?id=5730

And the Mercurial security advisory
https://www.mercurial-scm.org/wiki/WhatsNew#Mercurial_4.4.1_.282017-11-07.29

Thanks,
Terry

## Impact

A crafted mercurial repo with an evil git subrepo can lead to execute arbritary command on user's OS. And other web applications or clients support mercurial repo management or invoke hg related command also have a risk affected by this vulnerability.

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
