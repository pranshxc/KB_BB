---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '145603'
original_report_id: '145603'
title: https://newsletter.nextcloud.com Directory listening and Information Disclosure
weakness: Information Disclosure
team_handle: nextcloud
created_at: '2016-06-18T01:14:36.842Z'
disclosed_at: '2016-06-18T16:16:24.252Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# https://newsletter.nextcloud.com Directory listening and Information Disclosure

## Metadata

- HackerOne Report ID: 145603
- Weakness: Information Disclosure
- Program: nextcloud
- Disclosed At: 2016-06-18T16:16:24.252Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

This is the domain that we are going to work about it as you know:

https://newsletter.nextcloud.com/

Firstly I want to tell https://newsletter.nextcloud.com/admin when you are trying to navigate this link it needs authentication.But when you are doing this with via IP http://88.198.160.137/admin/ you can reach the admin page.And with this you are gettin information about phpList.

view-source:http://88.198.160.137/index.php

Go that page you'll see this code in the source       title="powered by phpList version 3.2.5,

Let's talk about directory listening.

Again.when you are trying navigate this https://newsletter.nextcloud.com/images/ it is saying "Not authorized." but you can reach the directories via IP


PoC:

Take a look at links below

http://88.198.160.137/images/

http://88.198.160.137/admin/ui/

I can even access the designing page with this link

http://88.198.160.137/admin/ui/dressprow/pages/design.php

Probably this design page is helping you when you are creating the codes of html pages on the newsletter.Anyway an attacker can use this informations for future bugs,or he can provide useful information

Thanks already,

mefkan

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
