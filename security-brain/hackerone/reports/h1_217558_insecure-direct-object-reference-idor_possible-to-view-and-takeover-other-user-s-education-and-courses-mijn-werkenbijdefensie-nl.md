---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '217558'
original_report_id: '217558'
title: Possible to view and takeover other user's education and courses @ mijn.werkenbijdefensie.nl
weakness: Insecure Direct Object Reference (IDOR)
team_handle: radancy
created_at: '2017-03-31T21:42:51.044Z'
disclosed_at: '2017-05-27T14:56:30.934Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- insecure-direct-object-reference-idor
---

# Possible to view and takeover other user's education and courses @ mijn.werkenbijdefensie.nl

## Metadata

- HackerOne Report ID: 217558
- Weakness: Insecure Direct Object Reference (IDOR)
- Program: radancy
- Disclosed At: 2017-05-27T14:56:30.934Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Domain and URL:**
https://mijn.werkenbijdefensie.nl/instellingen/gegevens/#tab2

**Summary:** IDOR vulnerability in editing education/courses 

**Description:** It is possible to view and change courses and education of other users (also known as an IDOR). It's also possible to save these, and after saving the owner of the course/education is changed to the current user and removed from the other user. 

## Browsers Verified In:
  * Chrome Version 56.0.2924.87 @ Windows 10

## Steps To Reproduce:

  1. Log in to mijn.werkenbijdefensie.nl
  2. Go to https://mijn.werkenbijdefensie.nl/instellingen/gegevens/#tab2 (or click the tab "Opleidingen & Cursussen" in your personal data)
  3. Add an education or course
  4. Inspect the "edit"-button of the just created course. Change the data-id to an lower ID that does not belong to you.
  5. Click the edit button from which you changed the id. A popup will open with the data of the course that is not yours.
  6. Change this data and save it. The course will now be yours, and removed from the other users profile.

I've tested it with my own two user accounts, so no data of other users is leaked or changed by me.

## Known steps to resolve:
Check if the requested course/education belongs to the user.

## Supporting Material/References:

  * https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_(OTG-AUTHZ-004)

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
