---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1018568'
original_report_id: '1018568'
title: Server Side Request Forgery in 'Jabber settings' in Admin Control Panel
weakness: Server-Side Request Forgery (SSRF)
team_handle: phpbb
created_at: '2020-10-26T02:08:22.155Z'
disclosed_at: '2020-12-20T17:04:13.089Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: https://github.com/phpbb/phpbb
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# Server Side Request Forgery in 'Jabber settings' in Admin Control Panel

## Metadata

- HackerOne Report ID: 1018568
- Weakness: Server-Side Request Forgery (SSRF)
- Program: phpbb
- Disclosed At: 2020-12-20T17:04:13.089Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Overview
The 'Jabber settings' panel inside the Administrator Control Panel can be used to access resources that would otherwise only be accessible by the host machine, including resources/services hosted on the `localhost` interface. This can be performed by setting the 'jabber server' parameter to the desired IP address, such as `127.0.0.1` and the port to the desired port. In some cases, service type/version numbers can be gathered as well as this information is printed to screen.

## How to trigger
Set 'jabber server' to 127.0.0.1
Set 'Jabber port' to whatever port you want to check.
Check the 'Enabled' radio button
Click submit

If the port is closed, you will see a socket error message 'Connection refused' error like this:
{F1051582}

Some such as mysqld simply return:
> Could not authorize on Jabber server.

## Example Recording
I have hosted an internal sshd service on `127.0.0.1:2222` to demonstrate that software type and version information is returned to the Administrator Control Panel. I am `ssh`'d into `phpbb-ubuntu`, which is running the aforementioned sshd service in debug mode so you can see the request hit. 
{F1051590}

## Setup info
Base OS: Ubuntu 20.04.1
phpbb Version: 3.3.1
{F1051573}

## Impact

An attacker could use this to interact with and enumerate services and resources on behalf of the host machine (including resources hosted on the `localhost` interface). This can be used to port scan and, in some cases, perform service versioning/enumeration on the `localhost` interface as well as on machines hosted on the same network as the phpbb host machine.

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
