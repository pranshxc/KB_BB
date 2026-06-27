---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '335341'
original_report_id: '335341'
title: Disclosure of Users Information via Wordpress API (?rest_route)
weakness: Information Disclosure
team_handle: localtapiola
created_at: '2018-04-10T00:05:37.436Z'
disclosed_at: '2018-05-22T13:49:32.365Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 7
asset_identifier: www.lahitapiolarahoitus.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- information-disclosure
---

# Disclosure of Users Information via Wordpress API (?rest_route)

## Metadata

- HackerOne Report ID: 335341
- Weakness: Information Disclosure
- Program: localtapiola
- Disclosed At: 2018-05-22T13:49:32.365Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** 
It's possible to get information about the users registered (such as: id, name, login name, etc.) without authentication in Wordpress via API on www.lahitapiolarahoitus.fi. 

**Description:** 
By default Wordpress allow public access to Rest API to get informations about all users registered on the system. 

## Steps To Reproduce:

  1. It's possible to reproduce the attack by browsing the URL:
https://www.lahitapiolarahoitus.fi/?rest_route=/wp/v2/users/1
https://www.lahitapiolarahoitus.fi/?rest_route=/wp/v2/users/2

  2. Just increase the last number of the Endpoing of API  (/?rest_route=/wp/v2/users/{id}) to get all users registered information on the Wordpress

**Remediation:** 
There are 2 ways that it's possible to fix this problem.
**FIX 1** - It's possible to remove this access for anyone by change the source code where when someone request the Rest API and the server send a 404 (Not Found) message for the user who made the request. 
Reference: https://github.com/WP-API/WP-API/issues/2338

**FIX 2** - It's also possible to create a rewrite rule on .htaccess (if the webserver it's Apache) to redirect any request that contain rest_route (eg.: "^.\*rest_route=/wp/\*") to a Not Found (404) or a Default Page.

## Impact

It's possible to get all the users registered on the system and create a bruteforce directed to these users.

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
