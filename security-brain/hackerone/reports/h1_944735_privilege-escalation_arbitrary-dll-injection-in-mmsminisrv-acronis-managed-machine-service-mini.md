---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '944735'
original_report_id: '944735'
title: Arbitrary DLL injection in mmsminisrv (Acronis Managed Machine Service Mini)
weakness: Privilege Escalation
team_handle: acronis
created_at: '2020-07-28T09:14:57.895Z'
disclosed_at: '2020-10-20T14:41:30.054Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: Acronis Cyber Protect Home Office (formerly Acronis True Image)
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Arbitrary DLL injection in mmsminisrv (Acronis Managed Machine Service Mini)

## Metadata

- HackerOne Report ID: 944735
- Weakness: Privilege Escalation
- Program: acronis
- Disclosed At: 2020-10-20T14:41:30.054Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

During initialization, **mms_mini.exe** (service binary of mmsminisrv) loads library *C:\Program Files (x86)\Common Files\Acronis\Home\libssl10.dll*. The library then tries to load non-existing file: *C:\bs_hudson\workspace\mod-openssl-fips-win\205\product\out\standard\vs_2013_release\OpenSSL\ssl\openssl.cnf*. The path seems to be hardcoded leftover from compilation. 
{F926518}

Because by default any user is able to create directories  on C:\ drive, it is possible to create missing directories and missing file (*openssl.cnf*). The OpenSSL config file implements support for loading additional DLL modules. Attacker may point to arbitrary DLL which will be loaded by service running with Local System privileges. Once service is restarted (e.g. due to system reboot), the planted library is loaded by the service and arbitrary code is executed. The code would typically add new Administrative user to the Windows system or establish reverse shell connection.

Successful injection of arbitrary library is shown on procmon log:
{F926535}

# Steps to reproduce
1. Create directories: ```mkdir C:\bs_hudson\workspace\mod-openssl-fips-win\205\product\out\standard\vs_2013_release\OpenSSL\ssl```
2. Inside, create openssl.cnf file with following content (replace DLL path with any path you wish):
    
    ``` 
openssl_conf = openssl_init
[openssl_init]
engines = engine_section
[engine_section]
woot = woot_section
[woot_section]
engine_id = woot
dynamic_path = c:\\temp\\cqbeacondll.dll
init = 0
    ```
3. Plant arbitrary DLL under *dynamic_path* location.
4. Wait for service to start (or force it by rebooting system)

## Impact

After successful attack, low privileged local user can elevate privileges up to Local System (the highest Windows privilege). The vulnerability can be also exploited by malware with local system access.

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
