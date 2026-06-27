---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1278254'
original_report_id: '1278254'
title: 'Built-in TLS module unexpectedly treats "rejectUnauthorized: undefined" as
  "rejectUnauthorized: false", disabling all certificate validation'
weakness: Improper Certificate Validation
team_handle: nodejs
created_at: '2021-07-26T16:29:32.712Z'
disclosed_at: '2021-09-10T17:53:06.439Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 20
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-certificate-validation
---

# Built-in TLS module unexpectedly treats "rejectUnauthorized: undefined" as "rejectUnauthorized: false", disabling all certificate validation

## Metadata

- HackerOne Report ID: 1278254
- Weakness: Improper Certificate Validation
- Program: nodejs
- Disclosed At: 2021-09-10T17:53:06.439Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!

**Summary:** "rejectUnauthorized: false" disables all TLS validation, and should not be set in almost all circumstances. The documentation says only the specific 'false' value will disable this validation, but in fact a 'undefined' value does also disables it, unexpectedly disabling TLS entirely.

**Description:**

The documentation for tls.connect (https://nodejs.org/api/tls.html#tls_tls_connect_options_callback) says:

> rejectUnauthorized <boolean> If not false, the server certificate is verified against the list of supplied CAs. An 'error' event is emitted if verification fails; err.code contains the OpenSSL error code. Default: true.

This is not true (see repro below) - in addition to `false`, an explicit `undefined` value does also disable server certificate verification.

This is very problematic, because it's reasonable to assume that `undefined` will be equivalent to setting the default, and it's also easy to accidentally produce undefined fields when dynamically building configuration. In any system that has done so, they are unknowingly silently not validating any TLS connections.

I've discovered this because I've found that https://www.npmjs.com/package/global-agent does exactly this (uses explicit undefineds when building options objects) and it is vulnerable because of this issue (i.e. all users of that package are by default unintentionally not validating TLS certificates for all connections).

This appears to affect all active node versions. Unless I'm missing something, this seems very bad.

## Steps To Reproduce:

Repro code:

```
const https = require('https');
const request = https.get('https://expired.badssl.com', { rejectUnauthorized: undefined });
request.on('error', (e) => console.log('Request failed:', e.message));
request.on('response', (e) => console.log('Request succeeded'));
```

  1. Run the above
  2. The request succeeds! It should not, because expired.badssl.com by design has an expired TLS certificate
  3. Remove the { rejectUnauthorized: undefined } option, or change it to 'true'
  4. It fails, as expected, due to an expired certificate.

## Impact:

This breaks all TLS and HTTPS security for anybody who accidentally provides an undefined value, assuming it will be equivalent to providing no value at all.

## Impact

Breaks all HTTPS protections, so complete disclosure or trivial manipulation of all HTTPS requests and responses by anybody capable of MITMing the TCP connection.

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
