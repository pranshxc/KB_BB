---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1708873'
original_report_id: '1708873'
title: Vulnerable moment-timezone version shipped
weakness: Cleartext Transmission of Sensitive Information
team_handle: nextcloud
created_at: '2022-09-22T14:19:37.944Z'
disclosed_at: '2023-02-08T05:44:57.412Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cleartext-transmission-of-sensitive-information
---

# Vulnerable moment-timezone version shipped

## Metadata

- HackerOne Report ID: 1708873
- Weakness: Cleartext Transmission of Sensitive Information
- Program: nextcloud
- Disclosed At: 2023-02-08T05:44:57.412Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
After this vulnerability refferences #1604606, I searching again about the vulnerabilities in other repositories and today we found a Information exposure in https://github.com/nextcloud/server Many communication channels can be "sniffed" by attackers during data transmission. For example, network traffic can often be sniffed by any attacker who has access to a network interface. This significantly lowers the difficulty of exploitation by attackers.



**Fix:**
Problem has been patched in version `0.5.35`, patch should be applicable with minor modifications to all affected versions. The patch includes changing the FTP endpoint with an HTTPS endpoint.
```json
        "moment-timezone": "^0.5.35",
        "version": "0.5.35",
        "resolved": "https://registry.npmjs.org/moment-timezone/-/moment-timezone-0.5.35.tgz",
        "integrity": "sha512-cY/pBOEXepQvlgli06ttCTKcIf8cD1nmNwOKQQAdHBqYApQSpAqotBMX0RJZNgMp6i0PlZuf1mFtnlyEkwyvFw==",
```

## Impact

* if Alice uses `grunt data` (or `grunt release`) to prepare a custom-build, moment-timezone with the latest tzdata from IANA's website
  * and Mallory intercepts the request to IANA's unencrypted ftp server, Mallory can serve data which might exploit further stages of the moment-timezone tzdata pipeline, or potentially produce a tainted version of moment-timezone (practicality of such attacks is not proved)

[GHSA-v78c-4p63-2j6c](https://github.com/moment/moment-timezone/security/advisories/GHSA-v78c-4p63-2j6c)

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
