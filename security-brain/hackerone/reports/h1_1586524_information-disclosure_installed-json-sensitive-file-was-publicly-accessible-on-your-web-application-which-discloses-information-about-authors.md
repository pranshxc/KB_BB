---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1586524'
original_report_id: '1586524'
title: installed.json sensitive file was publicly accessible on your web application
  which discloses information about authors and admins
weakness: Information Disclosure
team_handle: yelp
created_at: '2022-05-30T16:12:35.514Z'
disclosed_at: '2022-10-22T18:39:33.897Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 4
asset_identifier: blog.yelp.com
asset_type: URL
max_severity: none
tags:
- hackerone
- information-disclosure
---

# installed.json sensitive file was publicly accessible on your web application which discloses information about authors and admins

## Metadata

- HackerOne Report ID: 1586524
- Weakness: Information Disclosure
- Program: yelp
- Disclosed At: 2022-10-22T18:39:33.897Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

##kindly if you don't accept this issue please close it as informative , thanks in advance 

##Description:
The installed.json file is a sensitive file and it was publicly accessible on your webserver , which discloses some information about your web site and users such as authors like admin as shown below:
`"authors": [
            {
                "name": "Modern Tribe",
                "email": "admin@tri.be"
            }
`

##Steps to Produce:
1. Go to https://blog.yelp.com/vendor/composer/installed.json

##References :
https://www.acunetix.com/vulnerabilities/web/composer-installed-json-publicly-accessible/
https://hackerone.com/reports/461598

##Remediation:
Restrict Access to vendors directory

## Impact

Disclosure of information about components used by the web application.

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
