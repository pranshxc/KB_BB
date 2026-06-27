---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '356047'
original_report_id: '356047'
title: Wordpress Users Disclosure (/wp-json/wp/v2/users/)
weakness: Information Disclosure
team_handle: localtapiola
created_at: '2018-05-22T20:23:19.895Z'
disclosed_at: '2018-07-30T12:55:51.521Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 31
asset_identifier: www.lahitapiolarahoitus.fi
asset_type: URL
max_severity: none
tags:
- hackerone
- information-disclosure
---

# Wordpress Users Disclosure (/wp-json/wp/v2/users/)

## Metadata

- HackerOne Report ID: 356047
- Weakness: Information Disclosure
- Program: localtapiola
- Disclosed At: 2018-07-30T12:55:51.521Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

# Information
Using REST API, we can see all the WordPress users/author with some of their information.

### Step TO Reproduce
You can get user info by entering below url in your browser: 
https://www.lahitapiolarahoitus.fi/wp-json/wp/v2/users/



### Result 
```javascript
[
	{
		"id": 1,
		"name": "LTR",
		"url": "",
		"description": "",
		"link": "https://www.lahitapiolarahoitus.fi/author/ltr/",
		"slug": "ltr",
		"avatar_urls": {
			"24": "https://secure.gravatar.com/avatar/5afe7216f0e3cd2a501d30a0c16d0a1c?s=24&d=mm&r=g",
			"48": "https://secure.gravatar.com/avatar/5afe7216f0e3cd2a501d30a0c16d0a1c?s=48&d=mm&r=g",
			"96": "https://secure.gravatar.com/avatar/5afe7216f0e3cd2a501d30a0c16d0a1c?s=96&d=mm&r=g"
		},
		"meta": [],
		"_links": {
			"self": [
				{
					"href": "https://www.lahitapiolarahoitus.fi/wp-json/wp/v2/users/1"
				}
			],
			"collection": [
				{
					"href": "https://www.lahitapiolarahoitus.fi/wp-json/wp/v2/users"
				}
			]
		}
	},
	{
		"id": 2,
		"name": "LTREditor",
		"url": "",
		"description": "",
		"link": "https://www.lahitapiolarahoitus.fi/author/ltreditor/",
		"slug": "ltreditor",
		"avatar_urls": {
			"24": "https://secure.gravatar.com/avatar/8dbdec1ce9f301e17f889d87c228e0b4?s=24&d=mm&r=g",
			"48": "https://secure.gravatar.com/avatar/8dbdec1ce9f301e17f889d87c228e0b4?s=48&d=mm&r=g",
			"96": "https://secure.gravatar.com/avatar/8dbdec1ce9f301e17f889d87c228e0b4?s=96&d=mm&r=g"
		},
		"meta": [],
		"_links": {
			"self": [
				{
					"href": "https://www.lahitapiolarahoitus.fi/wp-json/wp/v2/users/2"
				}
			],
			"collection": [
				{
					"href": "https://www.lahitapiolarahoitus.fi/wp-json/wp/v2/users"
				}
			]
		}
	}
]
```

### Fix

Use this code will hide the users list and give 404 as the result, while rest of the api calls keep running as they were.
```php
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

Authors : __LTR__ , __LTREditor__ can be created scenario of doing bruteforce attacks to this users.

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
