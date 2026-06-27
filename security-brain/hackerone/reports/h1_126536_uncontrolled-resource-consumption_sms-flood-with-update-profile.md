---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126536'
original_report_id: '126536'
title: SMS Flood with Update Profile
weakness: Uncontrolled Resource Consumption
team_handle: uber
created_at: '2016-03-28T17:32:52.809Z'
disclosed_at: '2016-06-13T22:22:33.269Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
- uncontrolled-resource-consumption
---

# SMS Flood with Update Profile

## Metadata

- HackerOne Report ID: 126536
- Weakness: Uncontrolled Resource Consumption
- Program: uber
- Disclosed At: 2016-06-13T22:22:33.269Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

SMS will send when user update the profile and keep updating the user profile will result in keep sending the SMS, Step to reproduce 
1. Login to https://riders.uber.com
2. Go to https://riders.uber.com/profile
3. Update the Account Information, any field for Example FirstName
4. A SMS wil be received in the PHONE, saying that , your account information is updated
5. Use OWSAP ZAP to replay the packet and UBER will keep sending the SMS

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
