---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '168476'
original_report_id: '168476'
title: Incoming email hijacking on sc-cdn.net
weakness: Misconfiguration
team_handle: snapchat
created_at: '2016-09-15T02:13:20.493Z'
disclosed_at: '2016-09-23T22:53:53.259Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
- misconfiguration
---

# Incoming email hijacking on sc-cdn.net

## Metadata

- HackerOne Report ID: 168476
- Weakness: Misconfiguration
- Program: snapchat
- Disclosed At: 2016-09-23T22:53:53.259Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey guys!

Really interesting find here.

### Summary
These dangling MX records on `sc-cdn.net` have allowed me to purchase an email account with GoDaddy (owner of these servers) and send/receive email from an account on this domain.

```
sc-cdn.net.		3599	IN	MX	0 smtp.secureserver.net.
sc-cdn.net.		3599	IN	MX	10 mailstore1.secureserver.net.
```

### Reproduction
As I now "own" this email URL on GoDaddy, in theory you can't register another email address yourself. To prove that I've taken it over, feel free to email me on `rubyroobs@sc-cdn.net` and I'll be able to paste the message I receive into here to prove ownership of it.

### Mitigation
Delete these DNS records to avoid mail being hijacked on this domain.

### Impact
I believe impact of hijacking incoming emails on this address far outweighs the smaller consequences of missing SPF records. This would allow me to setup accounts on this email and in some cases allow me to prove control of the domain or impersonation of Snapchat staff.

Been super fun investigating this - not my typical find honestly :D. Let me know if you need any help triaging!

Cheers,
@rubyroobs

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
