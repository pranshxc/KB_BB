---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '156511'
original_report_id: '156511'
title: Incorrect logic in MySQL & MariaDB protocol leads to remote SSRF/Remote file
  read
weakness: Information Disclosure
team_handle: ibb
created_at: '2016-08-04T14:18:37.287Z'
disclosed_at: '2019-11-12T23:49:32.705Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
asset_identifier: IBB (Legacy)
asset_type: OTHER
max_severity: none
tags:
- hackerone
- information-disclosure
---

# Incorrect logic in MySQL & MariaDB protocol leads to remote SSRF/Remote file read

## Metadata

- HackerOne Report ID: 156511
- Weakness: Information Disclosure
- Program: ibb
- Disclosed At: 2019-11-12T23:49:32.705Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Overview
Wrong logic in realization of LOAD DATA LOCAL INFILE function leads to remote attacker can read files from server. Problem exists in many MySQL-drivers and frameworks, on many programming languages, like Python, Java, PHP etc.

For exploitation this vulnerability we need to connect to our special MySQL server (A) from "attacking" remote server (B).
For example:
- I found phpMyAdmin interface with connect to any server ability (AllowArbitraryServer option in config) on server B.
- Next I'm run special-MySQL server on my A host.
- Then connect through phpMyAdmin to host A
- After successful connection I can see content of /etc/passwd file from host B in log file on host A

## Details
For testing purposes take latest MySQL server, client and tcpdump
- Start server on local machine
- Run tcpdump
- Connect to local MySQL through native mysql-console client
- Run LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE pwn FIELDS TERMINATED BY '\n'
- Bye

Look inside packet dump file for LOCAL DATA INFILE query works:
- Client connect initialize.
- Server answers with greeting packet (protocol thread id, version, type of mysql authentication etc.)
- Next authentication packet (username, password, dbs)
- Next packet from client with query LOAD DATA LOCAL INFILE...
- Now here is strange packet from server. Call it `FB`-packet: `0c 00 00 01 fb 2f 65 74 63 2f 70 61 73 73 77 64`

`0c` - size
`000001` - packet No
`fb` - packet type
`2f6574632f706173737764` - filename (/etc/passwd)

There is problem looks like: server says to client what file he needs to read.
We need to create special MySQL server which do authorization with any data and then send FB packet with remote filename as payload. That's it.

In attach image successfully exploitation another MySQL administration interface - Adminer

Exploit: https://github.com/allyshka/Rogue-MySql-Server/blob/master/rogue_mysql_server.py
See also: http://russiansecurity.expert/2016/04/20/mysql-connect-file-read/

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
