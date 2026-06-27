---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1700896'
original_report_id: '1700896'
title: access nagios dashboard using default credentials in ** omon1.fpki.gov, 3.220.248.203**
weakness: Improper Access Control - Generic
team_handle: gsa_vdp
created_at: '2022-09-15T01:23:29.346Z'
disclosed_at: '2022-10-21T23:33:17.272Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 7
asset_identifier: '*.fpki.gov'
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# access nagios dashboard using default credentials in ** omon1.fpki.gov, 3.220.248.203**

## Metadata

- HackerOne Report ID: 1700896
- Weakness: Improper Access Control - Generic
- Program: gsa_vdp
- Disclosed At: 2022-10-21T23:33:17.272Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
when i performing recon on fpki.gov i found nagios dashboard in ** omon1.fpki.gov, 3.220.248.203**  and i accessed it using default credentials

username:  ** nagiosadmin **
password :  ** nagiosadmin **

## Steps To Reproduce:


  1. visit these urls : 
        **  https://omon1.fpki.gov/nagios/side.php **
        ** https://3.220.248.203/nagios/side.php **
  2. he will ask to put your credentials in basic authentication enter these credentials 
       
         username:  ** nagiosadmin **
         password :  ** nagiosadmin **

##POC:

look at poc pic

## Impact

attacker can make any action like an admin he has full control on your panal.

thanks , have a nice day :)

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
