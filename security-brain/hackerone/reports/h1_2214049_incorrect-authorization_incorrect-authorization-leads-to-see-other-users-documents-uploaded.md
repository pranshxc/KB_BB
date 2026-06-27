---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2214049'
original_report_id: '2214049'
title: Incorrect Authorization leads to see other users Documents Uploaded
weakness: Incorrect Authorization
team_handle: tennessee-valley-authority
created_at: '2023-10-18T09:24:44.973Z'
disclosed_at: '2023-11-30T15:45:03.044Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 24
asset_identifier: '*.mytva.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- incorrect-authorization
---

# Incorrect Authorization leads to see other users Documents Uploaded

## Metadata

- HackerOne Report ID: 2214049
- Weakness: Incorrect Authorization
- Program: tennessee-valley-authority
- Disclosed At: 2023-11-30T15:45:03.044Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
Hi team,
when user upload document, other user can see this docs only with link

## Steps To Reproduce:
1. loign to portal with user A : https://qcn.mytva.com
2. go to admin section and upload a document.
{F2782891}

3. click on link to see uploaded image. [like](https://qcn.mytva.com/Admin/FileHandler?ENC=RUFBQUFITmtabk00TjJGa1ptRTVNV0Z6TW5JMHV0S2hNTHNYR1J1SDNMMFBqeElLajlTNGNjTHcxVUhqcHhuL1R1cUxyVkxoS0RSRUFqUjRDTlFEd2E4S1diUkNYMlhGNFdSTDRrdE1yUUgvNkVhYWtUR251RjVYc1V6RDdwZkZXdTlCV0tZY2JmWGlVSkNjcHEyK0VvQU1Fc2R2RklDQW1MM25kNEZMTStxMTlhRnBrdStuOGs4N3lTU1Q1R2FsQ1ZrTHhnPT0)

{F2782892}

4. login to portal with user B
5. go to above url, we can see and download user A document.

{F2782896}

## Impact

any login user can see other user documents

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
