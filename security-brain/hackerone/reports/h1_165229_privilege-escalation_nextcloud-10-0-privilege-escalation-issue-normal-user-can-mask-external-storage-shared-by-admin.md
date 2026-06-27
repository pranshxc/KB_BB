---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '165229'
original_report_id: '165229'
title: Nextcloud 10.0 privilege escalation issue - Normal user can mask external storage
  shared by admin
weakness: Privilege Escalation
team_handle: nextcloud
created_at: '2016-09-02T09:43:42.725Z'
disclosed_at: '2020-03-01T15:01:32.178Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 14
tags:
- hackerone
- privilege-escalation
---

# Nextcloud 10.0 privilege escalation issue - Normal user can mask external storage shared by admin

## Metadata

- HackerOne Report ID: 165229
- Weakness: Privilege Escalation
- Program: nextcloud
- Disclosed At: 2020-03-01T15:01:32.178Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Normal user(Non-privileged) can mask external storage shared by admin.
 
 
Scenario :
Created three users "admin", "attacker", "victim"
Created group "samplegroup" containing all the three users with "victim" as group admin
 
 
Steps:
1) User "admin" created external storage named "localstrg"(note: name is the attack vector) with properties:
 
Folder Name : localstrg
External Storage : Local
Authentication : None
Configuration : /
Available for : "samplegroup","admin" - groups
Settings : Enable sharing
 
2) On seeing this , user "attacker" created one more external storage with the same name "localstrg" with properties:
 
Folder Name : localstrg
External Storage : SFTP
Authentication : Username and Password
Configuration : Fill "Host", "Root" ," Username" ,"Password"
Settings : Enable sharing
 
3) After that, user "attacker" shared created external storage with group "samplegroup" which is having other two users
 
4) If suppose, user "victim" visits the external storage "localstrg" in his profile, he is only shown with files shared by user "attacker"
 
Prerequisite : Both attacker and victim should be in the same group
 
Using this vulnerability, non-privilged user can mask the external storage shared by admin to other users

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
