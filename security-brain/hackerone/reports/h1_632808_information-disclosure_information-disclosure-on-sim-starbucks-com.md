---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '632808'
original_report_id: '632808'
title: Information disclosure on sim.starbucks.com
weakness: Information Disclosure
team_handle: starbucks
created_at: '2019-06-30T12:11:42.971Z'
disclosed_at: '2019-11-13T00:41:11.544Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 56
asset_identifier: Other assets
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Information disclosure on sim.starbucks.com

## Metadata

- HackerOne Report ID: 632808
- Weakness: Information Disclosure
- Program: starbucks
- Disclosed At: 2019-11-13T00:41:11.544Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Description:** 
       Hi,there.I found the sim.starbucks.com host deployed the jira server which version is 7.9.2,there is many public vulnerability on this low version.

**Information disclosured vulnerability** 
1.(CVE-2019-3403)https://jira.atlassian.com/browse/JRASERVER-69242
visit the URL address,you can check the user whether is exist on this host
```
https://sim.starbucks.com/rest/api/2/user/picker?query=admin
```
So the attacker can enumerate all existing users on this jira server.

2.(CVE-2019-8442)https://jira.atlassian.com/browse/JRASERVER-69241
visit the URL address,the server will leaking some server's information
```
https://sim.starbucks.com/s/thiscanbeanythingyouwant/_/META-INF/maven/com.atlassian.jira/atlassian-jira-webapp/pom.xml
```


## Recommendations for fix
updated the jira server's version or fixed

PS:Can starbucks's team check my other report #533836 status?the report is not updated for too long.
Thank you.looking forward for your reply.
Best regards!
@johnstone

## Impact

Leaking some information about the server

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
