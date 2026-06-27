---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '893970'
original_report_id: '893970'
title: Sensitive information about a ██████
weakness: Cleartext Storage of Sensitive Information
team_handle: deptofdefense
created_at: '2020-06-08T17:05:58.567Z'
disclosed_at: '2020-09-21T14:49:17.901Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Sensitive information about a ██████

## Metadata

- HackerOne Report ID: 893970
- Weakness: Cleartext Storage of Sensitive Information
- Program: deptofdefense
- Disclosed At: 2020-09-21T14:49:17.901Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
https://████████/ is an U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.Due to some reason a document  which contains the information about a special ███ for the ████  █████ which possibly is ███████or █████.The pdf file is located at https://██████/spi/█████████.pdf and also contains some drawings for the packaging of the machine.

To confirm that it indeed was a confidential document it was found that a basic search related to this pdf returns a meta info containing a label about criminal penalties for foreign export:

"WARNING – This document contains technical data whose export is restricted by the Arms Export Control Act (Title 22, U.S.C., Sec 2751 et seq.) or the Export Administration Act of 1979, (Title 50, U.S.C., App. 2401 et seq.), as amended. Violations of these export laws are subject to severe criminal penalties. Disseminate in accordance with provisions of DoD Directive 5230.25."

To confirm that the file is not just another special ██████████ it was discovered that the SPI number is not labeled at https://███/████████/spi?OpenPage&TableRow=2.1.1#2.1.


## Step-by-step Reproduction Instructions

1.Open any browser of your choice 
2.Head over to https://███████/spi/███████.pdf
3.Observe the content listed in the pdf and analyse the products mentioned in there

## Product, Version, and Configuration (If applicable)
Null
## Suggested Mitigation/Remediation Actions
Removal of such documents or introduction of certain authentication mechanisms would be ideal.

## Impact

This exposes highly sensitive information about not just the packaging info but also the designs mentioned.
Any person can access this document and cause information leakage.

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
