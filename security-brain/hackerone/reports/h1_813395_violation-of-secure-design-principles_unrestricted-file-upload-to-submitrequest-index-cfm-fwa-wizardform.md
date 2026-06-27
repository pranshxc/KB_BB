---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '813395'
original_report_id: '813395'
title: Unrestricted File Upload to ███████SubmitRequest/Index.cfm?fwa=wizardform
weakness: Violation of Secure Design Principles
team_handle: deptofdefense
created_at: '2020-03-09T03:37:09.345Z'
disclosed_at: '2020-06-11T18:14:05.511Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
tags:
- hackerone
- violation-of-secure-design-principles
---

# Unrestricted File Upload to ███████SubmitRequest/Index.cfm?fwa=wizardform

## Metadata

- HackerOne Report ID: 813395
- Weakness: Violation of Secure Design Principles
- Program: deptofdefense
- Disclosed At: 2020-06-11T18:14:05.511Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
An attacker is able to upload files of any type to `███SubmitRequest/Index.cfm?fwa=wizardform` as long as they are less than 5 MB.

**Description:**
The █████ ████ Request System allows a user to submit requests to the ██████████ ███ for event support. An attacker can exploit this request form by uploading malicious files due to an unrestricted file upload feature.

## Impact
An attacker is able to upload malicious files onto the server. These files are attached to a request for support from the ██████ █████████. If a member of the ██████ ████ were to open the malicious file, the attacker could gain remote code execution on ████ information systems. Alternatively, if the attacker finds out how to browse to the file, they could obtain a web shell on the target, giving them remote code execution.

## Step-by-step Reproduction Instructions

1. Browse to `██████PublicSite/index.cfm?fwa=newreq` and click on `Create a New Request`.
██████████
2. Fill in your e-mail address and click `Submit`.
██████████
3. Fill out the fields in the form.
███
████
███
███████
4. Before submitting the request, click the `Upload Files` tab.
█████
5. This page will allow you to upload any file you wish as long as it is under 5MB in size. I tested by uploading an executable (visual studio community installer) and a php file. These files were deleted from my request after submitting this report.
███████
6. Once uploaded, you can submit your request. An attacker would need to submit this request in hopes of the █████ ████████ downloading the malicious attachment.

## Suggested Mitigation/Remediation Actions
Restrict file uploads to safe extensions such as .jpg, .png, etc. to prevent an attacker from uploading malicious files onto the server.

## Impact

An attacker is able to upload malicious files onto the server. These files are attached to a request for support from the ████ ██████████. If a member of the ████ ██████████ were to open the malicious file, the attacker could gain remote code execution on ██████ information systems. Alternatively, if the attacker finds out how to browse to the file, they could obtain a web shell on the target, giving them remote code execution.

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
