---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164581'
original_report_id: '164581'
title: Oracle WebCenter Sites Support Tools available and Information disclosure (/cs/Satellite)
weakness: Information Disclosure
team_handle: localtapiola
created_at: '2016-08-30T23:58:38.568Z'
disclosed_at: '2016-11-17T22:20:14.383Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# Oracle WebCenter Sites Support Tools available and Information disclosure (/cs/Satellite)

## Metadata

- HackerOne Report ID: 164581
- Weakness: Information Disclosure
- Program: localtapiola
- Disclosed At: 2016-11-17T22:20:14.383Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Oracle WebCenter Sites Support Tools are available in: www.lahitapiola.fi

This software is password protected, but some pages are publicly available and reveal internal information.

The welcome page is located at: http://www.lahitapiola.fi/henkilo?pagename=Support/Home

This page reveal data as the running user: DefaultReader and the internal server name: s17334.tapiola.fi

Also other information like the server context:
* cs_version:'Oracle WebCenter Sites 11.1.1.6.1  Build Date: Nov 13 2013 at 19:25:33 Build Number: 66 Revision:160478'
* java_runtime_version:'1.6.0_38-b05'
* java_version:'1.6.0_38'
* java_vm_version:'20.13-b02'
* os_arch:'amd64'
* os_name:'Linux'
* os_version:'2.6.18-308.16.1.el5'
* os_proc: 4
* ws_info:'Apache Tomcat/7.0.35'

There are other available pages like:
http://www.lahitapiola.fi/henkilo?pagename=Support/Performance/Home
http://www.lahitapiola.fi/henkilo?pagename=Support/Performance/Standard/Home

These pages are also accessible through: http://www.lahitapiola.fi/cs/Satellite

For example: http://www.lahitapiola.fi/cs/Satellite?pagename=Support/Home

I have tested default Fatwire usernames and passwords, and it seems that they were changed, but anyway it is recommended to check the credentials of the users allowed to login from Internet.

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
