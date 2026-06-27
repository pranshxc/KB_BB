---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '105463'
original_report_id: '105463'
title: risk of having secure=false in a crossdomain.xml
weakness: Memory Corruption - Generic
team_handle: imgur
created_at: '2015-12-15T21:14:04.269Z'
disclosed_at: '2016-03-03T17:26:21.681Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- memory-corruption-generic
---

# risk of having secure=false in a crossdomain.xml

## Metadata

- HackerOne Report ID: 105463
- Weakness: Memory Corruption - Generic
- Program: imgur
- Disclosed At: 2016-03-03T17:26:21.681Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

api.imgur.com permits SWF files on a non-HTTPS server to load data from this HTTPS server. Setting the secure attribute to false could compromise the security offered by HTTPS. In particular, setting this attribute to false opens secure content to snooping and spoofing attacks.

The allow-access-from node has an optional attribute 'secure'. So say the crossdomain.xml on api.imgur.com has : 

<allow-access-from domain="imgur.com" secure="false"/>
<allow-access-from domain="*.imgur.com" secure="false"/>
<allow-access-from domain="*.imgur-dev.com" secure="false"/>

If this is set to true (default), a flash client retrieved over HTTP cannot access data on the ideanetsetter.yahoo.com over HTTPS.

I can only think of one risk in setting secure to false: A user with a poisoned host file or DNS server might be diverted to a flash client on a fake http://subdomain.example.com.
This flash client can now access sensitive data on api.imgur.com 


Good Fix ,

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
