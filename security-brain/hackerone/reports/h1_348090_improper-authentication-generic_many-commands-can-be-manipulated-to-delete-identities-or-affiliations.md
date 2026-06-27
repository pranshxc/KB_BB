---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '348090'
original_report_id: '348090'
title: many commands can be manipulated to delete identities or affiliations
weakness: Improper Authentication - Generic
team_handle: hyperledger
created_at: '2018-05-07T06:47:29.590Z'
disclosed_at: '2022-08-10T14:23:14.558Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 41
asset_identifier: https://github.com/hyperledger/fabric-ca
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-authentication-generic
---

# many commands can be manipulated to delete identities or affiliations

## Metadata

- HackerOne Report ID: 348090
- Weakness: Improper Authentication - Generic
- Program: hyperledger
- Disclosed At: 2022-08-10T14:23:14.558Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Introduction:**

The Faric-ca  data in http body and authorization header for many commands that send from client to server are protected by signature.  

But I find the identity and affiliation commands still have the risk to be manipulated. Hacker can manipulate most other commands to delete identities or affiliations in a server (server start with –cfg.identities.allowremove and –cfg.affiliations.allowremove). 

Example 1: Manipulating list an identity command to delete any identity or affiliation. 
{F294541}
normal list identity command

you can manipulate it:

{F294542}
Manipulate the list command to delete command

If a hacker gets the request http data (maybe by sniffer), he can manipulate the GET method to DELETE method, and change the admin3 identity to any other valid identity in the server, he can delete it. 


Example 2: Manipulating add an identity command to delete an identity or affiliation. 
{F294543}
normal add an identity command

you can manipulated:
{F294544}
Manipulate the add identity command to delete an identity

or you can manipulated as:
{F294545}
Manipulate the add identity command as delete an affiliation command


Actually, you can also manipulate other commands by this way. Such as: enroll, revoke,register… and so on. 



**Analysis:**

The authentication and authorization checking just covers the Authorization header and body, 
but the code for deleting identity and affiliation gets the identity value and affiliation value from **url path**. They are not protected by signature. And you can manipulate the method from other to DELETE.  

**DELETE** /affiliations/**org1.dep2**?force=true HTTP/1.1
**DELETE** /identities/**admin2** HTTP/1.1

## Impact

If a hacker get any of the normal request data by some way (maybe by network sniffer), he can delete all identities or affiliations.

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
