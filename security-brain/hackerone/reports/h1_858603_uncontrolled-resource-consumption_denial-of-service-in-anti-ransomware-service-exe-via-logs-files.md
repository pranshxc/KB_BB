---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '858603'
original_report_id: '858603'
title: Denial of Service in anti_ransomware_service.exe via logs files
weakness: Uncontrolled Resource Consumption
team_handle: acronis
created_at: '2020-04-24T11:23:57.042Z'
disclosed_at: '2021-06-24T08:21:49.389Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: Acronis Cyber Protect Home Office (formerly Acronis True Image)
asset_type: DOWNLOADABLE_EXECUTABLES
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Denial of Service in anti_ransomware_service.exe via logs files

## Metadata

- HackerOne Report ID: 858603
- Weakness: Uncontrolled Resource Consumption
- Program: acronis
- Disclosed At: 2021-06-24T08:21:49.389Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

anti_ransomware_service.exe keeps a log in a folder where any unprivileged user has write permissions. The logs are generated in a predictable pattern allowing the unprivileged user to create a hardlink from the, not yet created, log file to the anti_ransomware_service itself. On reboot, this forces the anti_ransomware_service to try to write its log into its own process, crashing in a SHARING VIOLATION. This crash occurs on every reboot.

Steps to reproduce:
1. Download the symbolic link testing tools by James Forshaw:
    https://github.com/googleprojectzero/symboliclink-testing-tools
2. Create hardlink from the next log file in line. E.g. If active_protection.1.log exist but not active_protection.2.log, create the hardlink on number 2 and so on.
    CreateHardlink.exe "C:\ProgramData\Acronis\ActiveProtection\Logs\active_protection.2.log" "C:\Program Files (x86)\Common Files\Acronis\ActiveProtection\anti_ransomware_service.exe"
3. Reboot and verify that anti_ransomware_service.exe is not running.

## Impact

The anti_ransomware_service.exe stops working from the first reboot (step 3) and onwards. This is a silent fail meaning that the user is not aware of the failing protection of the anti_ransomware_service.exe making the user vulnerable to ransomware.

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
