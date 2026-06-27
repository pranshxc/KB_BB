---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1735586'
original_report_id: '1735586'
title: Wordpress users Disclosure [ /wp-json/wp/v2/users/ ]
weakness: Information Disclosure
team_handle: mtn_group
created_at: '2022-10-14T13:29:55.961Z'
disclosed_at: '2022-11-27T03:25:02.082Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 29
asset_identifier: mtn.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Wordpress users Disclosure [ /wp-json/wp/v2/users/ ]

## Metadata

- HackerOne Report ID: 1735586
- Weakness: Information Disclosure
- Program: mtn_group
- Disclosed At: 2022-11-27T03:25:02.082Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Using REST API, we can see all the WordPress users/author with some of their information. Which can even be Personal information of employees/author. The file v2/users at:  https://www.mtn.com/wp-json/wp/v2/users/   is enabled and this give the attacker many users names like:  `Amogelang Maluleka` `Greg Davies` `karenbyamugisha` `Marc Ilunga` `mitchprinsloo`

## Steps To Reproduce:

  1.  Go to https://www.mtn.com/wp-json/wp/v2/users/  [ Allows anyone to view active usernames ]

{F1985941}

## Supporting Material/References:
https://hackerone.com/reports/356047
https://hackerone.com/reports/370777

###Fix:
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
