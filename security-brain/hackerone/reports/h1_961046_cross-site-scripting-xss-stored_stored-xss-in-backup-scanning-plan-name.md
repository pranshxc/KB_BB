---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '961046'
original_report_id: '961046'
title: Stored XSS in backup scanning plan name
weakness: Cross-site Scripting (XSS) - Stored
team_handle: acronis
created_at: '2020-08-17T20:33:22.911Z'
disclosed_at: '2021-06-28T03:11:24.488Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 115
asset_identifier: beta-cloud.acronis.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS in backup scanning plan name

## Metadata

- HackerOne Report ID: 961046
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: acronis
- Disclosed At: 2021-06-28T03:11:24.488Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Dear Acronis Security Team,

##Summary:

There is a possibility of storing an XSS on the https://mc-beta-cloud.acronis.com/ui/ console.

##Steps To Reproduce:

1. Login to the console with the given account
2. Go to "Backup Scanning" under "PLANS"
3. Click on "Create Plan"
4. Specify the location of the "Backups to scan" (in my case I selected my PC where the agent is installed)
5. Name the plan with this payload "/><svg/onload=prompt(document.domain)>
6. The XSS will fire up many times showing a self XSS alert
7. Keep pressing "OK" till the alert goes away
8. Click on "Create" to create the plan then click on the edit icon then click on "Save Changes"
9. The Self XSS alert may re-pop up several times, just keep pressing the "OK" button
10. Reload the pages by re-visiting  https://mc-beta-cloud.acronis.com/ui/  or going between the tabs
11. Click again on  "Backup Scanning" under "PLANS"
12. Select the plan create with the payload "/><svg/onload=prompt(document.domain)>
13. Try to Edit it and the stored XSS will fire up.

##Supporting Material/References:

Please refer to the attached screenshot & video for reference.

##Browser Tested:

Mozilla Firefox 68.9.0esr (64-bit)

##Operating System Tested:

   Windows 10 Professional 64-bit
    Kali Linux 2020 32-bit

## Impact

An XSS attack allows an attacker to execute arbitrary JavaScript in the context of the attacked website and the attacked user. This can be abused to steal session cookies, perform requests in the name of the victim or for phishing attacks.

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
