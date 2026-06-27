---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '915585'
original_report_id: '915585'
title: Social App does not validate server certificates for outgoing connections
weakness: Improper Certificate Validation
team_handle: nextcloud
created_at: '2020-07-04T22:45:44.180Z'
disclosed_at: '2020-11-17T16:37:41.232Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- improper-certificate-validation
---

# Social App does not validate server certificates for outgoing connections

## Metadata

- HackerOne Report ID: 915585
- Weakness: Improper Certificate Validation
- Program: nextcloud
- Disclosed At: 2020-11-17T16:37:41.232Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The Social App (https://apps.nextcloud.com/apps/social) does not validate the server TLS certificate for connections to other ActivityPub servers.
These connections are used to retrieve the public key for a user or posting a message to another ActivityPub server.
The public key for a user is used to validate the ActivityPub user.

The vulnerable code is at https://github.com/daita/my-small-php-tools/blob/d8778803612af20699c7efb0637bfe62478e596c/lib/Traits/TRequest.php#L151.
The initRequest method disables verifying of the peer's certificate by setting CURLOPT_SSL_VERIFYPEER to FALSE.
This code is called from CurlService.php (https://github.com/nextcloud/social/blob/97fb063479d4c0ad6fccdea3774601a619f8a886/lib/Service/CurlService.php#L265).

This issue has been tested on Nextcloud version version 19.0.0.12 with Social version 0.3.1.

## Impact

An attacker can perform a man-in-the-middle attack by impersonating the victim server by using a self-signed TLS certificate.
The attacker would have to be in a privileged network position between the Nextcloud instance and the target ActivityPub server.

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
