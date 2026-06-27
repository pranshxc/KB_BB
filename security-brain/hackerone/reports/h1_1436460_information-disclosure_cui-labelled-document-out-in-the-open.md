---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1436460'
original_report_id: '1436460'
title: CUI Labelled document out in the open
weakness: Information Disclosure
team_handle: deptofdefense
created_at: '2021-12-27T05:05:12.326Z'
disclosed_at: '2022-02-14T21:26:10.447Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# CUI Labelled document out in the open

## Metadata

- HackerOne Report ID: 1436460
- Weakness: Information Disclosure
- Program: deptofdefense
- Disclosed At: 2022-02-14T21:26:10.447Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi DoD VDP, 

I have found a document and each page of it is marked CUI : "Controlled Unclassified Information".
According to your standards, this file shouldn't be publicly available on internet.

This document was last edited on █████████ 2021. 
My investigation leads me to think it could have been public since around █████████.

This presentation contains information that could be sensitive : 
-███████ 
-██████

The file can be found here : https://█████

Thank you and best wishes for 2022!

## References
https://www.dodcui.mil/Portals/109/Documents/Desktop%20Aid%20Docs/CUI%20Training%20Aids_Oct%2023%202020.pdf

## Impact

Information that should be controlled is now publicly accessible.

## System Host(s)
██████████

## Affected Product(s) and Version(s)
https://███████

## CVE Numbers


## Steps to Reproduce
1. Visit : https://███
2. Download the file.
3. Open the file.
4. Notice each page is labelled as "CUI" (bottom of each page).
5. See that document contains sensitive information.

## Suggested Mitigation/Remediation Actions
-Remove the document from public internet.

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
