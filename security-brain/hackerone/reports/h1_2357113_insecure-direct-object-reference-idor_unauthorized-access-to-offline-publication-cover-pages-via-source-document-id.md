---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2357113'
original_report_id: '2357113'
title: Unauthorized Access to Offline Publication Cover Pages via SOURCE_DOCUMENT_ID
weakness: Insecure Direct Object Reference (IDOR)
team_handle: publitas
created_at: '2024-02-06T21:29:25.970Z'
disclosed_at: '2024-03-13T09:12:42.493Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 41
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Unauthorized Access to Offline Publication Cover Pages via SOURCE_DOCUMENT_ID

## Metadata

- HackerOne Report ID: 2357113
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: publitas
- Disclosed At: 2024-03-13T09:12:42.493Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I discovered a vulnerability that is related to accessing publication cover pages via a specific request using **sourceDocumentId**. When sending a request with the **source ID**, the system responds with a URL to the cover page of that publication. However,  the cover page is intended to be offline and not publicly accessible and the offline publication are only accessible by the account users. Beside that in the URL there is also the user id and the main id corresponding to that publication. So, due to a vulnerable endpoint we are able to disclose the cover page of an offline publication that we don't own.

{F3033179}

Vulnerable endpoint: ██████████

* Steps to Reproduce: 
1. Create account on ██████.
2. Create a new offline publication and take the **sourceDocumentId** of it.
3. Send a request to the program's endpoint with a valid **SOURCE_ID** corresponding to a specific publication.
4. Analyze the response to retrieve the URL of the publication's cover page.
5. Access the URL provided in the response, which contains both the user ID and the main ID of the publication.

## Impact

This vulnerability allows unauthorized access to offline publication cover pages, which may contain sensitive information not intended for public viewing. An attacker could potentially view confidential content from the cover pages of unpublished publications.

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
