---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '194351'
original_report_id: '194351'
title: Able to download arbitrary  PHP files at yelpblog.com
weakness: Privilege Escalation
team_handle: yelp
created_at: '2016-12-28T07:43:55.562Z'
disclosed_at: '2017-02-06T06:24:03.366Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- privilege-escalation
---

# Able to download arbitrary  PHP files at yelpblog.com

## Metadata

- HackerOne Report ID: 194351
- Weakness: Privilege Escalation
- Program: yelp
- Disclosed At: 2017-02-06T06:24:03.366Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

There is a misconfigured wordpress installation at yelpblog.com, through which i am able to download any php files in wp-includes folder.

For a PoC, you can open https://www.yelpblog.com/wp-includes/wp-db.php, and the wp-db.php will be download(along with all the data in it)

As we all know that these PHP files can sensative information of a website, and the wp-includes folder is the base of a WordPress installation, Being able to download php files is a clearly wrong behaviour of a wordpress installation.
The PHP files in wp-includes can have a lot of sensative information about the server, which may help a attacker in compromising the server. He can even do a source code analysis if he is able to download arbitrary 
PHP files.

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
