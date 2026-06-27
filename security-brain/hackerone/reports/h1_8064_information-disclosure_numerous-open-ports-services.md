---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '8064'
original_report_id: '8064'
title: Numerous open ports/services
weakness: Information Disclosure
team_handle: localize
created_at: '2014-04-18T19:01:05.591Z'
disclosed_at: '2014-04-21T13:34:31.325Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# Numerous open ports/services

## Metadata

- HackerOne Report ID: 8064
- Weakness: Information Disclosure
- Program: localize
- Disclosed At: 2014-04-21T13:34:31.325Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Looks like you have numerous open ports that also show service versions. An attacker can leverage this information when trying an attack. Ports should be filtered and banners should be removed/generalized.

nmap -sV www.localize.io

Starting Nmap 6.40-2 ( http://nmap.org ) at 2014-04-18 11:08 PDT
Stats: 0:02:11 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 84.62% done; ETC: 11:11 (0:00:19 remaining)
Nmap scan report for www.localize.io (178.77.99.228)
Host is up (0.22s latency).
rDNS record for 178.77.99.228: www.doppelkopf.me
Not shown: 981 closed ports
PORT     STATE    SERVICE            VERSION
21/tcp   open     ftp                ProFTPD 1.3.4a
22/tcp   open     ssh                OpenSSH 5.3p1 Debian 3ubuntu7 (Ubuntu Linux; protocol 2.0)
25/tcp   filtered smtp
53/tcp   open     domain             ISC BIND none
80/tcp   open     http               Apache httpd
106/tcp  open     pop3pw             poppassd
110/tcp  open     pop3               Courier pop3d
143/tcp  open     imap?
443/tcp  open     ssl/http           Apache httpd
465/tcp  open     ssl/smtp           Postfix smtpd
993/tcp  open     ssl/imaps?
995/tcp  open     ssl/pop3           Courier pop3d
1248/tcp filtered hermes
3306/tcp open     mysql              MySQL 5.1.66-0ubuntu0.10.04.3
4662/tcp filtered edonkey
6346/tcp filtered gnutella
6881/tcp filtered bittorrent-tracker
6969/tcp filtered acmsoda
8443/tcp open     ssl/http           sw-cp-server httpd (Parallels Plesk WebAdmin version psa-11.0.9-110120608.16)

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
