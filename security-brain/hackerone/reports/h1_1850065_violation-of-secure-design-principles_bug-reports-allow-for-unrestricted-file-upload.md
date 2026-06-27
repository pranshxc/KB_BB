---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1850065'
original_report_id: '1850065'
title: '[█████] Bug Reports allow for Unrestricted File Upload'
weakness: Violation of Secure Design Principles
team_handle: deptofdefense
created_at: '2023-01-28T21:30:01.283Z'
disclosed_at: '2023-02-24T19:07:39.166Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- violation-of-secure-design-principles
---

# [█████] Bug Reports allow for Unrestricted File Upload

## Metadata

- HackerOne Report ID: 1850065
- Weakness: Violation of Secure Design Principles
- Program: deptofdefense
- Disclosed At: 2023-02-24T19:07:39.166Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The web page https://███████/ allows for users to submit bug reports. Users are allowed to attach a file to a bug report. The extension and size of files are not validated by the web server.

## Impact

An attacker can attach a malicious file to a bug report. If a support agent opened the malicious file, malware would be executed on the support agent's system.

## System Host(s)
████████

## Affected Product(s) and Version(s)
Version: 3.4 Build: 35 Revision: 1

## CVE Numbers


## Steps to Reproduce
1. Navigate to the following web page: https://████████/
2. Create an account
3. Log in to the account that you created
4. Click on the text that reads `Report a Bug`
5. Enter any text in to the `Description` input field
6. Attach a file with an allowed file extension to the bug report
7. Click on the text that reads `Submit`
8. Intercept the `HTTP` request and change the extension of the attached file to one that is not allowed

Observe that the bug report was successfully submitted. This should not be the case, as the attached file has a file extension that is not allowed. The same method can be used to attach a file whose size is greater than 5 megabytes.

## Suggested Mitigation/Remediation Actions
Ensure that the extension and size of a file are validated by the web server.

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
