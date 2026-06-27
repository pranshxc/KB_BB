---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1699740'
original_report_id: '1699740'
title: nextcloudcmd incorrectly trusts bad TLS certificates
weakness: Improper Certificate Validation
team_handle: nextcloud
created_at: '2022-09-14T07:53:20.250Z'
disclosed_at: '2022-12-25T11:32:16.504Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: Desktop Client
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- improper-certificate-validation
---

# nextcloudcmd incorrectly trusts bad TLS certificates

## Metadata

- HackerOne Report ID: 1699740
- Weakness: Improper Certificate Validation
- Program: nextcloud
- Disclosed At: 2022-12-25T11:32:16.504Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Ref: https://github.com/nextcloud/desktop/issues/4927

### Bug description

I have a self hosted Nextcloud instance using my own private CA for TLS certs.  When running `nextcloudcmd` without the `--trust`, it disregards the cert validation failure as "This is not an actual error" and proceeds with the sync anyway.  I expected it to reject the untrusted server cert and assume it is a MITM attack:

```
# nextcloudcmd --non-interactive -n ~/Nextcloud https://nextcloud.lan
09-10 12:25:54:348 [ info nextcloud.sync.accessmanager ]:	2 "" "https://nextcloud.lan/ocs/v1.php/cloud/capabilities?format=json" has X-Request-ID "18ff47a0-a482-4456-a489-7aa747170c58"
09-10 12:25:54:348 [ info nextcloud.sync.networkjob ]:	OCC::JsonApiJob created for "https://nextcloud.lan" + "ocs/v1.php/cloud/capabilities" ""
09-10 12:25:54:545 [ info nextcloud.sync.account ]:	"SSL-Errors happened for url  \"https://nextcloud.lan/ocs/v1.php/cloud/capabilities?format=json\" \tError in  QSslCertificate(\"3\", [REDACTED] : \"The root certificate of the certificate chain is self-signed, and untrusted\" ( \"The root certificate of the certificate chain is self-signed, and untrusted\" ) \n " Certs are known and trusted! This is not an actual error.
09-10 12:25:54:871 [ info nextcloud.sync.networkjob.jsonapi ]:	JsonApiJob of QUrl("https://nextcloud.lan/ocs/v1.php/cloud/capabilities?format=json") FINISHED WITH STATUS "OK"
```

After [adding the root CA cert to the system's trust store](https://ubuntu.com/server/docs/security-trust-store) the validation passes and the warning goes away.

I am running the latest `nextcloud-desktop-cmd` package, version `2.6.2-1build1`, on Ubuntu Server 20.04.2 LTS.

I did not see this problem in the [NextCloud CVE list](https://www.cvedetails.com/vulnerability-list/vendor_id-15913/product_id-34622/Nextcloud-Nextcloud.htm).

### Steps to reproduce

Run `nextcloudcmd` against a server that has a TLS cert that the system won't validate.

### Expected behavior

Abort the operation if the server's TLS cert cannot be validated, unless `--trust` is specified to explicitly override the security checks.

### Which files are affected by this bug

src/libsync/account.cpp

### Operating system

Linux

### Which version of the operating system you are running.

Ubuntu 20.04.2 LTS

### Package

Distro package manager

### Nextcloud Server version

24.0.3

### Nextcloud Desktop Client version

2.6.2-1build1

### Is this bug present after an update or on a fresh install?

Fresh desktop client install

### Are you using the Nextcloud Server Encryption module?

Encryption is Disabled

### Are you using an external user-backend?

- [X] Default internal user-backend
- [ ] LDAP/ Active Directory
- [ ] SSO - SAML
- [ ] Other

## Impact

Possible MITM

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
