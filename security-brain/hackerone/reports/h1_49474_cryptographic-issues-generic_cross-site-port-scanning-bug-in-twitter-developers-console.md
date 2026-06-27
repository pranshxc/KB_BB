---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '49474'
original_report_id: '49474'
title: Cross site Port Scanning bug in twitter developers console
weakness: Cryptographic Issues - Generic
team_handle: x
created_at: '2015-02-27T15:06:59.060Z'
disclosed_at: '2015-05-23T13:16:31.742Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- cryptographic-issues-generic
---

# Cross site Port Scanning bug in twitter developers console

## Metadata

- HackerOne Report ID: 49474
- Weakness: Cryptographic Issues - Generic
- Program: x
- Disclosed At: 2015-05-23T13:16:31.742Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

This vulnerability allow a port scanning a remote machine on internet . an attacker can scan a remote machine through this vulnerability using twitter ip as a proxy .

The vulnerability exit  on url https://dev.twitter.com/rest/tools/console
through console an attacker can use GET or POST request with basic authentication or no authentication for a successful port scan on a remote machine using any service .
let take as http://www.sd-host.net as target(which i setup with open port 80,2082,2083)

in the Request url i put this http://www.sd-host.net:80
and i get the following respond 
url: 
 it seems that port 80 is open on the remote machine 
then i changed the port to 8080 
hence its a close port i got following respond
refer poc 2
then i changed the port to 2082 (cpanel)
as it a password protected page (cpanel)

i got access denied 
refer poc 3

then i tried to access http://www.ibm.com/robots.txt over port 80
and got succeed 
following respond i got  refer poc 4 

when i changed the port to 809
i got respond  like this poc 5

hence its clear that we can access and perform attack on a remote machine using developer console 

by this vulnerability we can use twitter ip as proxy and exploit a remote service running on a remote machine

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
