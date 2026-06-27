---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2041007'
original_report_id: '2041007'
title: Cross-Site Request Forgery
weakness: Cross-Site Request Forgery (CSRF)
team_handle: owncloud
created_at: '2023-06-28T07:05:46.266Z'
disclosed_at: '2023-11-05T09:16:00.422Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 104
asset_identifier: owncloud/core
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Cross-Site Request Forgery

## Metadata

- HackerOne Report ID: 2041007
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: owncloud
- Disclosed At: 2023-11-05T09:16:00.422Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

The application does not throw a CrossSiteRequestForgeryException, if the request does not contain the requesttoken header.

Steps to reproduce 
- run the docker image "owncloud/server:10.12.2" , redis and mariadb with docker-compose
-  log in the application as an admin user
- insert your cookies in

```bash
curl 'http://localhost:8080/settings/users/users' \
  -H 'Accept: */*' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'Cookie: oc_sessionPassphrase=<placeholder1>; oclt1tejv3yd=<placeholder2>' \
  -H 'Origin: http://abc:8080' \
  --data-raw 'username=new_admin&groups%5B%5D=admin&password=a&email=test%40mail.com' \
  --compressed
```

and run it.
- Login in the application with the username `new_admin` and the passwort `a`

To add an admin user is only an example. Most if not all requests does not require an CSRF token.

I think the cause of this vulnerability is the second condition of https://github.com/owncloud/core/blob/master/lib/private/AppFramework/Middleware/Security/SecurityMiddleware.php#L145, because the the value of `$this->request->getHeader("Authorization")` is an empty string and not null, if there are no `Authorization` header.

## Impact

Under the requirement, that the sameSite value of the cookies are set to `lax` or `none`, an attacker can create a website and if the victim surfs to this website cross site requests with the cookies of the victim are possible. Depending on the role/groups of the victim, the attacker can create an admin account with known username and passwort or share files with an other (possible attacker controlled) user and possible other actions.

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
