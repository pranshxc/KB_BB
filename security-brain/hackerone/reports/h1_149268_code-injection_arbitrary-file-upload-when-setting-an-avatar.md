---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '149268'
original_report_id: '149268'
title: Arbitrary file upload when setting an avatar
weakness: Code Injection
team_handle: expressionengine
created_at: '2016-07-05T05:06:43.444Z'
disclosed_at: '2018-04-04T16:36:49.246Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- code-injection
---

# Arbitrary file upload when setting an avatar

## Metadata

- HackerOne Report ID: 149268
- Weakness: Code Injection
- Program: expressionengine
- Disclosed At: 2018-04-04T16:36:49.246Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hello,

When an administrator attempts to set an avatar from an external link, the parser just takes the source of whatever link they point it to and creates a file with the same extension and content in the uploads folder.

##Steps to reproduce:

1- Visit http://[HOST]/admin.php?/cp/members/profile/settings and scroll to the "Change avatar" section.
2- Choose "Link to avatar" and set it's value to `http://strukt.tk/test.svg`
3- After redirection, if you have a proxy, a request will be made to something like `http://[HOST]/images/avatars/test_1.svg` on your localhost. Try opening that in your browser and you should see an alert box over there.
4- You can try that with `https://ellislab.com/asset/file/ee_server_wizard.zip`, it will create a .zip file over there.

That being said, an attacker can use other file types and may be able to run arbitrary commands on the OS.

Regards

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
