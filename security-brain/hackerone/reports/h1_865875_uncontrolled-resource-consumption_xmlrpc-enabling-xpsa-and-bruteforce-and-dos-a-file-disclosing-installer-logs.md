---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '865875'
original_report_id: '865875'
title: XMLRPC, Enabling XPSA and Bruteforce and DOS + A file disclosing installer-logs.
weakness: Uncontrolled Resource Consumption
team_handle: mtn_group
created_at: '2020-05-04T17:15:07.880Z'
disclosed_at: '2021-06-14T08:02:16.423Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 22
asset_identifier: lonestarcell.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# XMLRPC, Enabling XPSA and Bruteforce and DOS + A file disclosing installer-logs.

## Metadata

- HackerOne Report ID: 865875
- Weakness: Uncontrolled Resource Consumption
- Program: mtn_group
- Disclosed At: 2021-06-14T08:02:16.423Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
[XMLRPC+Installer_logs+Backup_Filename+Admin_username+disclosure]

## Steps To Reproduce:

  1. I was able to successfully exploit XMLRPC with the traditional method, the brute-force was done the username was there in the Installer Logs
  2. path to XMLRPC is http://13.92.255.102/xmlrpc.php + the username is in https://lonestarcell.com/installer-log.txt 
  3. Pingback ping can be used to dos the target server when mishandled
## Supporting Material/References:
I was able to reproduce this whole https://www.netsparker.com/blog/web-security/xml-rpc-protocol-ip-disclosure-attacks/

## Impact

1)Automated once from multiple hosts and be used to cause a mass DDOS attack on the victim.
2) This method is also used for brute force attacks to stealing the admin credentials and other important credentials
3) File disclosure is causing most harm as internal criticals are popping out

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
