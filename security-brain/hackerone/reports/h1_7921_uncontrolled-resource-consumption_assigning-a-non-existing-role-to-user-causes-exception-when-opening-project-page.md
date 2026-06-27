---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '7921'
original_report_id: '7921'
title: Assigning a non-existing role to user causes exception when opening project
  page
weakness: Uncontrolled Resource Consumption
team_handle: localize
created_at: '2014-04-17T20:28:01.081Z'
disclosed_at: '2014-04-19T11:20:36.009Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Assigning a non-existing role to user causes exception when opening project page

## Metadata

- HackerOne Report ID: 7921
- Weakness: Uncontrolled Resource Consumption
- Program: localize
- Disclosed At: 2014-04-19T11:20:36.009Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Reproduction:

- Create a new private project
- Log in as another user and go the the newly create project page. Request access there.
- Switch back to original user and check pending requests.
- At this point I was able to assign a non-existing role (I changed the dropdown list and chose 10 as value). Grant user access then.
- Log in again a the user that requested access. The dashboard indicates that the request was accepted. 
- Click on the project. The following error is given:

Fatal error: Uncaught exception 'Exception' with message 'Unknown role 10' in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/classes/Repository.php:358 Stack trace: #0 /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/classes/UI.php(1136): RepositoryPermissions->isInvitationMissing() #1 /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/classes/UI.php(204): UI::getPage_Project(Array, Array) #2 /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/classes/UI.php(179): UI::findPage(6, Array, Array) #3 /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php(158): UI::getPage(6) #4 {main} thrown in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/classes/Repository.php on line 358

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
