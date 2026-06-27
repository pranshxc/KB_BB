---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1004007'
original_report_id: '1004007'
title: ..; bypass leading to  tomcat scripts [Unauthenticated]
weakness: Improper Access Control - Generic
team_handle: informatica
created_at: '2020-10-09T21:35:33.737Z'
disclosed_at: '2020-10-13T09:26:31.917Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 24
tags:
- hackerone
- improper-access-control-generic
---

# ..; bypass leading to  tomcat scripts [Unauthenticated]

## Metadata

- HackerOne Report ID: 1004007
- Weakness: Improper Access Control - Generic
- Program: informatica
- Disclosed At: 2020-10-13T09:26:31.917Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello all 

Using the technique ..; i was able to bypass the protection mechanism to access Tomcat Example Scripts hosted at **https://███/**. 

## Steps to reproduce 

1 - Open all URL's bellow inside your browser

[ https://█████████/..;/examples/servlets/servlet/SessionExample]  | Will lead to Session Manipulation and potential Account Takeover. Because the session is global this servlet poses a big security risk as an attacker can potentially become an administrator by manipulating its session.

[https://████████/..;/examples/servlets/servlet/CookieExample] | Insecure Cookie Handling

[https://████████/..;/examples/servlets/] | Source Code Disclosure and an "Execute" option

[https://███████/..;/examples/servlets/servlet/RequestHeaderExample] | Internal IP disclosure

## PoC
i upload some images.

## Fixing
Isolate backend application, Remove the management console and other servlet contexts and Check behaviors between proxy and backend servers.
More info here, [https://i.blackhat.com/us-18/Wed-August-8/us-18-Orange-Tsai-Breaking-Parser-Logic-Take-Your-Path-Normalization-Off-And-Pop-0days-Out-2.pdf] --> Orange Tsai -- Blackhat talk -- thanks to him

## Impact

Apache Tomcat default installation contains the "/examples" directory which has many example servlets and JSPs. Some of these examples are a security risk and should not be deployed on a production server.
The Sessions Example servlet (installed at /examples/servlets/servlet/SessionExample) allows session manipulation. Because the session is global this servlet poses a big security risk as an attacker can potentially become an administrator by manipulating its session.

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
