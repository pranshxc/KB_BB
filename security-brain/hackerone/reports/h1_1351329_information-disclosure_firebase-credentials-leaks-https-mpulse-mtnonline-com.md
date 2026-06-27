---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1351329'
original_report_id: '1351329'
title: firebase credentials leaks @ https://mpulse.mtnonline.com
weakness: Information Disclosure
team_handle: mtn_group
created_at: '2021-09-26T08:43:07.738Z'
disclosed_at: '2022-09-05T22:59:06.455Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 9
asset_identifier: mtnonline.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# firebase credentials leaks @ https://mpulse.mtnonline.com

## Metadata

- HackerOne Report ID: 1351329
- Weakness: Information Disclosure
- Program: mtn_group
- Disclosed At: 2022-09-05T22:59:06.455Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello.
I found firebase credentials leaks at https://mpulse.mtnonline.com

## Steps To Reproduce:
Visit https://mpulse.mtnonline.com >> right click >> view source code

## Supporting Material/References:
<!-- Firebase -->
    
    



    <!-- <script>
    // Initialize Firebase
    var config = {
    apiKey: "████",
    authDomain: "████████",
    databaseURL: "https://mpulse-25c68.firebaseio.com",
    projectId: "mpulse-25c68",
    storageBucket: "mpulse-25c68.appspot.com",
    messagingSenderId: "295133444438"
    };
    firebase.initializeApp(config);
    </script> -->

## Impact

Un authorize access to firebase database.


Kind regard
@aliyugombe

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
