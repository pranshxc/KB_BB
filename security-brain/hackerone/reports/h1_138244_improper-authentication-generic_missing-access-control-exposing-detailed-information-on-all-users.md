---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '138244'
original_report_id: '138244'
title: Missing access control exposing detailed information on all users
weakness: Improper Authentication - Generic
team_handle: wp-api
created_at: '2016-05-12T10:25:47.029Z'
disclosed_at: '2016-10-17T23:40:44.282Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 16
tags:
- hackerone
- improper-authentication-generic
---

# Missing access control exposing detailed information on all users

## Metadata

- HackerOne Report ID: 138244
- Weakness: Improper Authentication - Generic
- Program: wp-api
- Disclosed At: 2016-10-17T23:40:44.282Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The WP REST API WordPress plugin fails to apply access controls for the 'edit' context. This means that with a single HTTP request, an attacker can obtain the following information for every single registered user: username, email address, first name, last name, date of registration, and detailed privilege information. This is a treasure trove of information for someone planning an attack - they know exactly which email addresses to target in order to gain admin privileges and complete control over the webserver.

To replicate this issue, simply send the following request while unauthenticated:
GET /wp-json/wp/v2/users?context=edit

Please note that I've submitted this report to a couple of entities directly affected by this vulnerability so they can implement a workaround.

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
