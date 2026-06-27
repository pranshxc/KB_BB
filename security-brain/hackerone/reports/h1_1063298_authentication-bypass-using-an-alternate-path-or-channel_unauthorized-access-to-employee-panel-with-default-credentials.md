---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1063298'
original_report_id: '1063298'
title: Unauthorized access to employee panel with default credentials.
weakness: Authentication Bypass Using an Alternate Path or Channel
team_handle: gsa_vdp
created_at: '2020-12-21T09:30:04.226Z'
disclosed_at: '2021-11-13T20:46:19.578Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 12
asset_identifier: cars.fas.gsa.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- authentication-bypass-using-an-alternate-path-or-channel
---

# Unauthorized access to employee panel with default credentials.

## Metadata

- HackerOne Report ID: 1063298
- Weakness: Authentication Bypass Using an Alternate Path or Channel
- Program: gsa_vdp
- Disclosed At: 2021-11-13T20:46:19.578Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hello, 
When hunting for your web application.

I have managed to go https://cars.fas.gsa.gov/cars/cars and get displayed with a form.
I have already tried to login to Cars and without success.
However i've noticed the loginChk() function and change the value of the form hence bypassing it and logging in succesfuly.

## Steps To Reproduce:


  1. go to https://cars.fas.gsa.gov/cars/cars
  2. type loginChk()  function in console. 
  3. It would return false. 
  4. Now  type in console ( can be opened using F12). 
       document.forms[0].scSelCen.value = "admin"
  5. Now try to login by clicking on CARS button.

## Supporting Material/References:
Navigator used : google chrome.

If you need any additional information. feel free to ask me.

PS :  I think the website went for a maintenance right now.
Even though i didn't use anything of that panel.

## Impact

Any attacker would have the access to admin panel and do whatever he wants.
As i can see , it's a platform for reporting accidents.

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
