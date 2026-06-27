---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '260005'
original_report_id: '260005'
title: RCE via ssh:// URIs in multiple VCS
weakness: OS Command Injection
team_handle: ibb
created_at: '2017-08-14T20:53:18.957Z'
disclosed_at: '2017-09-21T16:21:35.503Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 39
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- os-command-injection
---

# RCE via ssh:// URIs in multiple VCS

## Metadata

- HackerOne Report ID: 260005
- Weakness: OS Command Injection
- Program: ibb
- Disclosed At: 2017-09-21T16:21:35.503Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I'd like to submit an RCE issue within Git SVN and Mercurial, the CVEs are:

*  CVE-2017-9800 (Subversion)
* CVE-2017-1000116 (Mercurial (hg))
* CVE-2017-1000117 (Git)

Further Info can be found at:

http://blog.recurity-labs.com/2017-08-10/scm-vulns

And product specific:

* https://public-inbox.org/git/xmqqh8xf482j.fsf@gitster.mtv.corp.google.com/T/#u
* http://subversion.apache.org/security/CVE-2017-9800-advisory.txt
* https://about.gitlab.com/2017/08/10/gitlab-9-dot-4-dot-4-released/

I think these issues which all are based on the same flaw could be worth
an IBB Bounty. However I'd like to point out that we at Recurity Labs
would like the bounty being donated to a charity. The to be determined
charity will be something in the field of brain aneurysm, this is due to
the fact that Felix, the founder of Recurity Labs, currently is
recovering from a brain aneurysm.


So, just let us know what you think about this.

Cheers,

joern

P.S. I took the CVSS Score from the Subversion Advisory
the Redhat advisory states a score of 6.3 (CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L) I guess the truth is somewhere in between.

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
