---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '282843'
original_report_id: '282843'
title: UnResolved ChangeSet are Visible to Public That also Causes Information Disclosure
weakness: Information Disclosure
team_handle: wordpress
created_at: '2017-10-25T16:55:02.252Z'
disclosed_at: '2018-02-05T14:47:55.028Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 0
asset_identifier: irclogs.wordpress.org
asset_type: URL
max_severity: low
tags:
- hackerone
- information-disclosure
---

# UnResolved ChangeSet are Visible to Public That also Causes Information Disclosure

## Metadata

- HackerOne Report ID: 282843
- Weakness: Information Disclosure
- Program: wordpress
- Disclosed At: 2018-02-05T14:47:55.028Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello,

While testing Your Security I Observed that the Security Report Reported to You After Validation arranged for fix  or you can say that a public  repository created for the code powering the site at https://code.trac.wordpress.org/changeset/[ID]
that Leaks Following Things

1.UnResolved Bugs
2.PHP Code of Website

Impact
=====
Let an Attacker Dont Know The Vulnerabilities in Your System he can search for different id's like 469,470,471 Like this:-
https://code.trac.wordpress.org/changeset/469
https://code.trac.wordpress.org/changeset/470
https://code.trac.wordpress.org/changeset/471

Which is Disclosing PHP Code and Unresolved Security Bugs To Public An Attacker can see Unresolved Vulnerabilities From Here can Use it to destroy Your Services.


Thanks,
Abdulwahab Khan,
Independent Cyber Security Researcher.

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
