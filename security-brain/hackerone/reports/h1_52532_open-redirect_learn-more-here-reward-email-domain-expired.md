---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '52532'
original_report_id: '52532'
title: '"learn more here", reward email - domain expired.'
weakness: Open Redirect
team_handle: security
created_at: '2015-03-18T20:54:03.434Z'
disclosed_at: '2015-03-23T18:24:47.859Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
tags:
- hackerone
- open-redirect
---

# "learn more here", reward email - domain expired.

## Metadata

- HackerOne Report ID: 52532
- Weakness: Open Redirect
- Program: security
- Disclosed At: 2015-03-23T18:24:47.859Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Today I received an e-mail about a reward, below the e-mail there is something about `drastically reduced fees from Coinbase`, to be exactly, the following:

```
Thanks to drastically reduced fees from Coinbase, you are eligible to receive a 5% bonus when you receive your bounty payout in Bitcoin. Curious if Bitcoin is appropriate in your country? Learn more [here](http://bitlegal.io/).
```

The domain where "learn more here" points to is expired. See: http://www.nic.io/cgi-bin/whois?query=bitlegal.io this could potentially lead to phishing attacks.

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
