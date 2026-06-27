---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '942481'
original_report_id: '942481'
title: Wordpress Users Disclosure (/wp-json/wp/v2/users/) on data.gov
weakness: Information Disclosure
team_handle: gsa_bbp
created_at: '2020-07-25T15:48:16.952Z'
disclosed_at: '2020-07-28T00:12:56.419Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 14
asset_identifier: www.data.gov
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Wordpress Users Disclosure (/wp-json/wp/v2/users/) on data.gov

## Metadata

- HackerOne Report ID: 942481
- Weakness: Information Disclosure
- Program: gsa_bbp
- Disclosed At: 2020-07-28T00:12:56.419Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

## Summary:
Hello TTS Bug bounty team!

I have found data.gov  User/admin usernames disclosed.
Using REST API, we can see all the WordPress users/author with some of their information.

## Steps To Reproduce:

  You can find the information disclosure by going to (data.gov/wp-json/wp/v2/users/)

Supporting Video:
{F922807}

Response:
```javascript
[{"id":600633,"name":"Aaron Borden","url":"","description":"","link":"https:\/\/www.data.gov\/author\/aaron-bordengsa-gov\/","slug":"aaron-bordengsa-gov","avatar_urls":etc....
```
## Fix:
Use this code will hide the users list and give 404 as the result, while rest of the api calls keep running as they were.
```javascript
add_filter( 'rest_endpoints', function( $endpoints ){
    if ( isset( $endpoints['/wp/v2/users'] ) ) {
        unset( $endpoints['/wp/v2/users'] );
    }
    if ( isset( $endpoints['/wp/v2/users/(?P<id>[\d]+)'] ) ) {
        unset( $endpoints['/wp/v2/users/(?P<id>[\d]+)'] );
    }
    return $endpoints;
});
```
## Similar reports:
(https://hackerone.com/reports/356047)
(https://hackerone.com/reports/370777)
(https://hackerone.com/reports/772744)

Thank you very much.

## Impact

Malicious counterpart could collect the usernames disclosed (and the admin user) and be focused throughout BF attack (as the usernames are now known), making it less harder to penetrate the data.gov systems.

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
