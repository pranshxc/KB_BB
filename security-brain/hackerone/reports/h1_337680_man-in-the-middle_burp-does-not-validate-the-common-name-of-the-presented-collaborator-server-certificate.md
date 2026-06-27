---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '337680'
original_report_id: '337680'
title: burp does not validate the common name of the presented collaborator server
  certificate
weakness: Man-in-the-Middle
team_handle: portswigger
created_at: '2018-04-14T09:38:54.788Z'
disclosed_at: '2018-06-13T16:14:32.117Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 38
asset_identifier: Burp Suite Pro/Community
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: high
tags:
- hackerone
- man-in-the-middle
---

# burp does not validate the common name of the presented collaborator server certificate

## Metadata

- HackerOne Report ID: 337680
- Weakness: Man-in-the-Middle
- Program: portswigger
- Disclosed At: 2018-06-13T16:14:32.117Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Burp is not validating correctly if the presented certificate in collaborator server. It warns if it is a self signed one, but if it is a legitimate one (any valid CA), it appears not to be checking the CN.


This is an issue for the polling service, since it allows for the connection to be intercepted and burp will happily send through the polling request.

For PoC, just use a valid certificate for a completely different domain than the one used on the burp collaborator server, and connect to it. All checks will be ok, and when polling the server (using the scanner for instance), there's no warning or failure, and burp connects.
I haven't extensively tested all possible options, but using a valid wildcard certificate from a totally different domain works.

(note: there's also the functional bug of burp stating the connections are ok, but the target being tested will then fail to connect to any TLS service on the collaborator)

## Impact

If the attacker is able to perform a MITM on the tester (either adjacent to him, or to the collaborator server, or somewhere along the path), he will be able to intercept the HTTPS polling connection to the collaborator server, and potentially obtain the records.

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
