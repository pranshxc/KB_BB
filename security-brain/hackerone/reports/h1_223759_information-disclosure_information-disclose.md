---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '223759'
original_report_id: '223759'
title: information disclose
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2017-04-25T13:17:39.396Z'
disclosed_at: '2017-04-25T13:21:20.098Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# information disclose

## Metadata

- HackerOne Report ID: 223759
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2017-04-25T13:21:20.098Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello  Team . 
I Reported a  issue - disclosure SERVER Version !!

when i interrupt this https://demo.nextcloud.com/ Request , its  disclosure The  server version   Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.1e-fips
As you can See this Pic , or you can Interrupt the url useing Any Proxy tools like Burp Suite.  

So it's Mostly important to keep secret of server version. & Configure your web server to prevent information leakage from the SERVER header of its HTTP response.

Importatnt Things is An attacker might use the disclosed information to harvest specific security vulnerabilities for the version identified. 

Hope You guyz Fix This Probleam As soon As possible 
reference::https://hackerone.com/reports/141125
		https://hackerone.com/reports/135782
		https://hackerone.com/reports/167041
			
	
Thanks,
Best Regards ,
Mohammad Abdullah

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
