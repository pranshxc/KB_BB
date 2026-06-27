---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '173251'
original_report_id: '173251'
title: Password Reset emails missing TLS leads account takeover
weakness: Improper Authentication - Generic
team_handle: rubygems
created_at: '2016-09-30T21:38:06.666Z'
disclosed_at: '2016-10-04T16:29:07.210Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
asset_identifier: rubygems.org
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# Password Reset emails missing TLS leads account takeover

## Metadata

- HackerOne Report ID: 173251
- Weakness: Improper Authentication - Generic
- Program: rubygems
- Disclosed At: 2016-10-04T16:29:07.210Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I saw that the email is sent in clear-text instead of TLS (Transport Layer Security) any Man-in-the-middle attacker is able to read these sensitive Emails and get the password reset link which lead to account takeover.

Email details:
from:	help@rubygems.org
to:	Victim@gmail.com
date:	Fri, Sep 30, 2016 at 10:31 PM
subject:	Change your password
mailed-by:	rubygems.org
encryption:	ec2-52-43-250-235.us-west-2.compute.amazonaws.com did not encrypt this message

Thanks,
Diogo Real

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
