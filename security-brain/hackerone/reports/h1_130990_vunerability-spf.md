---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '130990'
original_report_id: '130990'
title: 'Vunerability : spf'
team_handle: paragonie
created_at: '2016-04-15T06:24:54.727Z'
disclosed_at: '2016-04-27T00:27:07.683Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
tags:
- hackerone
---

# Vunerability : spf

## Metadata

- HackerOne Report ID: 130990
- Weakness: 
- Program: paragonie
- Disclosed At: 2016-04-27T00:27:07.683Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Heĺlo sir,  im an independent security researcher. I found an vunerability in your website 
                   Your website  https://github.com/paragonie doesn't have valid spf records. To recover this do validate your spf.  Sender Policy Framework (SPF): This allows you specify which mail servers are allowed to send mails for your domain. There is of course nothing to stop a spammer sending a mail from their mail server for your domain, but e-mail clients can then check the SPF policy for your site, see it's not on the approved list and then choose to either ignore the mail completely, or at least mark it as likely spam. For more details https://en.m.wikipedia.org/wiki/Sender_Policy_Framework
Regards,
Neeraj

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
