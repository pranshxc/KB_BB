---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '713407'
original_report_id: '713407'
title: ActiveStorage throws exception when using whitespace as filename, may lead
  to denial of service of multiple pages
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2019-10-14T05:08:15.447Z'
disclosed_at: '2019-12-13T17:17:24.587Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 110
asset_identifier: hackerone.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# ActiveStorage throws exception when using whitespace as filename, may lead to denial of service of multiple pages

## Metadata

- HackerOne Report ID: 713407
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2019-12-13T17:17:24.587Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**
Hi team, 
I've found an issue on the profile picture upload feature of your asset - https://hackerone.com, which can allow a malicious attacker to perform an application wide denial of service attack.
**Description:**
I was playing with the profile picture upload feature, then i observed that when we change the name of our profile picture to `+` , `%0d%0a` , or  `%20` and then refresh the profile page, it would give an internal server error. Then i observed the same behaviour at everyplace where my profile picture was being reflected for example the programs thanks section, hacktivity section or even the directory section. This leads to site wide Denial of Service that will deny all the users from performing any actions. 

### Steps To Reproduce

1. Login and visit edit profile page. 
2. Select a normal profile picture and click `Update Profile` button
3. Intercept this Request and change the filename to `+` by editing the request as shown in  ██████████
4. Turn off the intercept button and the refresh the update page.
5. Notice that it wont load. 
Now the similar behaviour can be observed at every place where your profile picture is shown.  

### Optional: Supporting Material/References (Screenshots)

 * █████

### Optional: Did you use [recon data made available by HackerOne](https://github.com/Hacker0x01/helpful-recon-data) to find this vulnerability?

no

## Impact

Application wide denial of service. The more places where the profile pictures are being shown, the higher the impact for example - hacktivity, program from page, thanks page, etc

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
