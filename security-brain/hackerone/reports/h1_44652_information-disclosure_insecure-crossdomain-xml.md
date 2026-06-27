---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '44652'
original_report_id: '44652'
title: Insecure crossdomain.xml
weakness: Information Disclosure
team_handle: mobilevikings
created_at: '2015-01-21T22:07:04.442Z'
disclosed_at: '2015-04-04T00:03:14.034Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- information-disclosure
---

# Insecure crossdomain.xml

## Metadata

- HackerOne Report ID: 44652
- Weakness: Information Disclosure
- Program: mobilevikings
- Disclosed At: 2015-04-04T00:03:14.034Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

https://mobilevikings.be/crossdomain.xml contains the following xml file:
```
<?xml version="1.0"?>
<cross-domain-policy>
  <allow-access-from domain="*" secure="true" />
</cross-domain-policy>
```

This will make any one able to receive content from https://mobilevikings.be/.
More information about this issue is available here:
http://gursevkalra.blogspot.nl/2013/08/bypassing-same-origin-policy-with-flash.html
Best regards,

Olivier Beg

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
