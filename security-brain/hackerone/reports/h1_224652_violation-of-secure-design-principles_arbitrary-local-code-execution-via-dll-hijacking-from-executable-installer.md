---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '224652'
original_report_id: '224652'
title: Arbitrary local code execution via DLL hijacking from executable installer
weakness: Violation of Secure Design Principles
team_handle: brave
created_at: '2017-09-26T20:52:06.482Z'
disclosed_at: '2018-07-09T21:40:17.213Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
- violation-of-secure-design-principles
---

# Arbitrary local code execution via DLL hijacking from executable installer

## Metadata

- HackerOne Report ID: 224652
- Weakness: Violation of Secure Design Principles
- Program: brave
- Disclosed At: 2018-07-09T21:40:17.213Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

> NOTE! Thanks for submitting a report! Please fill all sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty.

## Summary:

The executable installer BraveSetup-ia32.exe is vulnerable to DLL hijacking: it loads (at least) version.dll from its application directory (which is typically the user's "Downloads" directory %USERPROFILE%\Downloads) instead Windows' system directory %SystemRoot%\System32

## Products affected: 

Windows 7 and newer versions, Brave version 0.18.36

## Steps To Reproduce:

Place the attached version.dll in %USERPROFILE%\Downloads, download the current BraveSetup-ia32.exe and execute it: version.dll displays message boxes showing its caller.

## Supporting Material/References:

See https://skanthak.homepage.t-online.de/sentinel.dll

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
