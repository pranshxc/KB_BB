---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1351326'
original_report_id: '1351326'
title: firebase credentials leaks @ ███████
weakness: Information Disclosure
team_handle: mtn_group
created_at: '2021-09-26T08:37:48.559Z'
disclosed_at: '2022-09-05T22:59:23.270Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: mtn.com.gh
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# firebase credentials leaks @ ███████

## Metadata

- HackerOne Report ID: 1351326
- Weakness: Information Disclosure
- Program: mtn_group
- Disclosed At: 2022-09-05T22:59:23.270Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello.
I found firebase credentials leaks at ████.


## Steps To Reproduce:
Visit █████ >> Right click >> view source code.



## Supporting Material/References:

 <script>
      // Your web app's Firebase configuration
      // For Firebase JS SDK v7.20.0 and later, measurementId is optional
      var firebaseConfig = {
        apiKey: "AIzaSyBZtK5_-J1DFWLBFpLBIOkeK9D8ZDfqJ3g",
        authDomain: "██████",
        databaseURL: "█████",
        projectId: "quizgame-4f2e3",
        storageBucket: "██████",
        messagingSenderId: "██████████",
        appId: "1:████████:web:923994d50811422213a052",
        measurementId: "G-N94D6VRGVG"
      };
      // Initialize Firebase
      firebase.initializeApp(firebaseConfig);
      firebase.analytics();
    </script>

## Impact

Un authorize access to firebase database.

Kind regard
@█████████

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
