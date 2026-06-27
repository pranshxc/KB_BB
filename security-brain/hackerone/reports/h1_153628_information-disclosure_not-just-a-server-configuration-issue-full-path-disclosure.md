---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '153628'
original_report_id: '153628'
title: '[Not just a server configuration issue] Full Path Disclosure'
weakness: Information Disclosure
team_handle: iandunn-projects
created_at: '2016-07-25T07:09:54.407Z'
disclosed_at: '2016-08-24T18:48:00.764Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# [Not just a server configuration issue] Full Path Disclosure

## Metadata

- HackerOne Report ID: 153628
- Weakness: Information Disclosure
- Program: iandunn-projects
- Disclosed At: 2016-08-24T18:48:00.764Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hey, I've just found a 'full path disclosure' in basic-google-maps-placemarks, so it's not just a server configuration issue! I've tested it on different servers (including windows, ubuntu, CentOS etc..) 

#PoC
So, if we visit `wp-content/plugins/basic-google-maps-placemarks/unit-tests.php` it is clearly disclosing the full path as you can see in the following links:

- http://jazzalajmi.com/espace-pro/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php 
- http://ywamnorthwoods.org/setapart/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php
- http://www.t1fx.com/teamt1fx/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php
- http://www.processinstruments.net/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php
- http://faas-bh.com/001/03udruzene/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php
- http://www.dominihost.com.br/1line/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php
- http://www.dominihost.com.br/1line/wp-content/plugins/basic-google-maps-placemarks/unit-tests.php

And eventually, in my localhost too:


{F107116}


Well, not all websites using basic-google-maps-placemarks, have a server configuration issue, so it's probably an issue in your plugin! :-)

###Impact:
Well, the possible impact is that if attacker gets into the server using other website, he might symlink and also get access to the site using that full path! 

>> *Request: Still if you are not going to fix this, please close as informativer*

Cheers,
Ahsan

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
