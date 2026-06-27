---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1330455'
original_report_id: '1330455'
title: DoD internal documents are leaked to the public
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2021-09-05T01:41:54.083Z'
disclosed_at: '2021-10-15T16:23:48.199Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 29
tags:
- hackerone
- information-disclosure
---

# DoD internal documents are leaked to the public

## Metadata

- HackerOne Report ID: 1330455
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2021-10-15T16:23:48.199Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello Team,

I found a zip file containing documents about DoD. From what I looked at are documents for new soldiers who are starting out, but I didn't just find these files but several others like advice, commander files, plans, certificates and others.

███
██████
█████████

In some of the files I found information such as name, surname, email, phone number and even signatures. Files like these shouldn't be exposed to the public.

██████████
█████████
█████
█████

Here is a list of the folders and documents that exist inside this zip file (it's quite big):

█████

## Impact

* Anyone can download these files and leak them to the public
* Plan something against a specific person for a crime

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Open in your browser the URL https://█████

2. Look for the file called "████" and download it

3. Extract the file and look at the documents

I found some certificates in the Formats folder, in the Welcome folder there is someone's phone number, command files are in the Commander Files folder.

## Suggested Mitigation/Remediation Actions
* Change the location of this zip file and the others
* Block viewing of files in this folder

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
