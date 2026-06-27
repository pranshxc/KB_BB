---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '384782'
original_report_id: '384782'
title: User Information Disclosure via the REST API - /?_method=GET
weakness: Information Disclosure
team_handle: localtapiola
created_at: '2018-07-20T20:54:09.755Z'
disclosed_at: '2018-09-10T01:22:37.461Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
asset_identifier: www.lahitapiolarahoitus.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- information-disclosure
---

# User Information Disclosure via the REST API - /?_method=GET

## Metadata

- HackerOne Report ID: 384782
- Weakness: Information Disclosure
- Program: localtapiola
- Disclosed At: 2018-09-10T01:22:37.461Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
browser access to www.lahitapiolarahoitus.fi/wp-json is restricted for general public but it is still be accessible through which User information is leaked.

**Description:** 
By default Wordpress allow public access to Rest API to get information about all users registered on the system but you have restricted it internally. I saw several reports on this issue reported on lahitapiolarahoitus.fi. Now as a fix to those reports, requests to /wp-json/wp/v2/users are blocked and return an error like this:
> Refer to lahitapiolarahoitus.fi.JPG

It also successfully blocks requests such as /?rest_route=/wp/v2/users.
> Refer to lahitapiolarahoitus.fi1.JPG

However, the REST API allows simulating different request types. As such, we can perform a POST request with the “users” string in the body of the request, and tell the REST API to act like it’s received a GET request.

## Steps To Reproduce:

   > curl https://lahitapiolarahoitus.fi/?_method=GET -d rest_route=/wp/v2/users

## Browsers / Apps Verified In:

  * It is tested via curl command.

## Additional material

  > Refer to finalPOC.JPG

## Related reports, best practices

  * https://wpvulndb.com/vulnerabilities/8715

## Impact

It allows anonymous access to functionality that allows a hacker to list all users who have published a post on a WordPress site.

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
