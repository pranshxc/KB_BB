---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '271391'
original_report_id: '271391'
title: Potential server misconfiguration leads to disclosure of vendor/ directory
weakness: Forced Browsing
team_handle: zomato
created_at: '2017-09-25T02:56:01.478Z'
disclosed_at: '2017-10-23T05:47:08.128Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- forced-browsing
---

# Potential server misconfiguration leads to disclosure of vendor/ directory

## Metadata

- HackerOne Report ID: 271391
- Weakness: Forced Browsing
- Program: zomato
- Disclosed At: 2017-10-23T05:47:08.128Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,

Apologies for the weakness label, it was the closest I could find for what appears to be a server misconfiguration.

Typically, in MVC frameworks like Slim (which I see you are using here), Symfony, Laravel, etc., the front controller is the only thing exposed, leaving `vendor/`, `logs/`, and others outside of document root, inaccessible to web browsers.

However, it appears that here that's not the case, having `vendor/` accessible.

## PoC

`https://www.zomato.com/vendor/composer/installed.json`

`https://www.zomato.com/vendor/slim/slim/composer.json`

`https://www.zomato.com/vendor/bin/phpunit`

I can see that Slim is used, and various libraries are installed with `composer`.


## Why it's a concern

Recently, `phpunit` had an RCE vulnerability, that if exposed, would allow users to run arbitrary PHP code. PHPUnit is indeed installed: `https://www.zomato.com/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php`. However, it appears that you are fortunately running the patched version. Reference: `http://phpunit.vulnbusters.com/`.


## Additional notes

I did try other directories, like the `logs/` directory, but it doesn't seem to be exposed. Or at least the common `app.log` isn't available.

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
