---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1364797'
original_report_id: '1364797'
title: SSRF - pivoting in the private LAN
weakness: Server-Side Request Forgery (SSRF)
team_handle: concretecms
created_at: '2021-10-10T08:28:56.741Z'
disclosed_at: '2022-11-25T17:20:07.629Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
asset_identifier: https://github.com/concrete5/concrete5
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- server-side-request-forgery-ssrf
---

# SSRF - pivoting in the private LAN

## Metadata

- HackerOne Report ID: 1364797
- Weakness: Server-Side Request Forgery (SSRF)
- Program: concretecms
- Disclosed At: 2022-11-25T17:20:07.629Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The upload from remote servers features allows me to perform SSRF attack on the private LAN servers.

this features checks the following
* http response code needs to be 200 - easy, a non issue for attackers really
* checks the file exension   (can be bypassed with something like  http://192.168.1.148/index.php/test.png  - anything after index.php/  is ignorred and I control the file extension as well)
* some checks are performed on the IP, but any public and PRIVATE ips are allowed

I can read web  apps from the internal network, fingerprint them and exploit them (using GET only exploits).

This is how I've managed to read an phpinfo file from my local LAN:

http://192.168.1.157/info.php/test.html

The file is fetched, saved by the CMS locally (or S3) and then the output can be downloaded by the attacker as you can see in the attached screenshots.

ps: crayons

## Impact

An attacker can pivot in the private LAN and exploit local network apps.

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
