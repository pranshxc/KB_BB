---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '288950'
original_report_id: '288950'
title: Additional bypass allows SSRF for internal netblocks
weakness: Server-Side Request Forgery (SSRF)
team_handle: security
created_at: '2017-11-09T20:38:47.190Z'
disclosed_at: '2017-11-16T20:15:03.956Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 18
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Additional bypass allows SSRF for internal netblocks

## Metadata

- HackerOne Report ID: 288950
- Weakness: Server-Side Request Forgery (SSRF)
- Program: security
- Disclosed At: 2017-11-16T20:15:03.956Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

It turns out there is another bypass in the `private_address_check` gem. The gem does not include 0.0.0.0 in the exclusion list in the first place.

```
irb(main):001:0> require 'private_address_check'
=> true
irb(main):002:0> PrivateAddressCheck.private_address?("0.0.0.0")
=> false
```

I was able to bypass your filter by using http://0.0.0.0:22/ as you can see below:

{F238151}

Please find a hotfix for this issue attached to this report: {F238152}. The author of the gem has been notified and should hopefully provide a proper fix very soon.

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
