---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126410'
original_report_id: '126410'
title: CrashPlan Backup is Vulnerable Allowing to a DoS Attack Against Uber's Backups
  to ```backup.uber.com```
team_handle: uber
created_at: '2016-04-17T18:35:08.100Z'
disclosed_at: '2016-05-09T22:41:38.141Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
---

# CrashPlan Backup is Vulnerable Allowing to a DoS Attack Against Uber's Backups to ```backup.uber.com```

## Metadata

- HackerOne Report ID: 126410
- Weakness: 
- Program: uber
- Disclosed At: 2016-05-09T22:41:38.141Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

```backup.uber.com``` hosts a CrashPlan backup server on port 443. CrashPlan allows users to backup to a friends computer by entering a 6 digit alphanumeric code. This means there are 2,176,782,336 total CrashPlan friend codes. While this is a high number, it is completely possible to brute force this as CrashPlan does not have any rate limiting on their end point to check the validity of a code. 

By iterating through all the friend codes I would be able to find the friend code for the CrashPlan instance running on ```backup.uber.com``` thereby allowing me to upload my data to the server hosting ```backup.uber.com```. 

I wasn't quite sure what to categorize this as so I put it down as a denial of service vulnerability since it would allow me to fill the ```backup.uber.com``` server up with data so that employees would not be able to backup their data. 

In order to patch this you have to go into the settings in CrashPlan and disable "Inbound backup from other computers". If you are using this feature, you should add a firewall between ```backup.uber.com``` to block connections not originating from Uber. 

I am also reporting this to Code42 (creators of CrashPlan) to suggest that they switch to a secure default. 

Thanks,
David Dworken

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
