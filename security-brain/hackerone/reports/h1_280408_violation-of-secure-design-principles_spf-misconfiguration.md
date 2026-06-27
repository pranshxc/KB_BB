---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '280408'
original_report_id: '280408'
title: SPF Misconfiguration
weakness: Violation of Secure Design Principles
team_handle: infogram
created_at: '2017-10-19T12:40:13.474Z'
disclosed_at: '2017-11-06T09:03:07.410Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: infogram.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# SPF Misconfiguration

## Metadata

- HackerOne Report ID: 280408
- Weakness: Violation of Secure Design Principles
- Program: infogram
- Disclosed At: 2017-11-06T09:03:07.410Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I am just looking at your SPF records then found following. SPF Records missing safe check which can allow me to send mail on behalf of infogram.

#PoC:
The TXT records found for your domain are:
```
"v=spf1 include:_spf.google.com include:spf.mandrillapp.com include:mailgun.org ~all"
```
Simply anyone can use ```https://emkei.cz/``` service to trigger mail to anyone on behalf of infogram.
#Fix:

```v=spf1 include:_spf.google.com include:spf.mandrillapp.com include:mailgun.org -all```

>#*If team don't wanna hear about spf related checks please let me know. i'll close this report myself.*

Regards,
Mr.R3boot.

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
