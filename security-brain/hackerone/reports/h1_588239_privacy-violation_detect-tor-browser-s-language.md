---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '588239'
original_report_id: '588239'
title: Detect Tor Browser's language
weakness: Privacy Violation
team_handle: torproject
created_at: '2019-05-23T01:21:29.119Z'
disclosed_at: '2019-05-29T09:58:51.005Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- privacy-violation
---

# Detect Tor Browser's language

## Metadata

- HackerOne Report ID: 588239
- Weakness: Privacy Violation
- Program: torproject
- Disclosed At: 2019-05-29T09:58:51.005Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Summary
Some error pages uses Tor Browser's language based text, and iframe can steal it.

#Details
Since the language of Tor Browser is used for the title of the link tag on 404 error page, an attacker can obtain the language of Tor Browser even if the user has set privacy.spoof_english to 2.
I attached a PoC and a video for this.

If the server returns empty response, Tor Browser will show this page in iframe:
```html
<html class="mozwebext">
    <head>
        <link rel="alternate stylesheet" type="text/css" href="resource://content-accessible/plaintext.css" title="Wrap Long Lines">
    </head>
    <body>
        <pre></pre>
    </body>
</html>
```

but if user uses Japanese (This is example, it can be used in other languages) version of Tor Browser, it'll show this page:
```html
<html class="mozwebext">
    <head>
        <link rel="alternate stylesheet" type="text/css" href="resource://content-accessible/plaintext.css" title="長い行を折り返す">
    </head>
    <body>
        <pre></pre>
    </body>
</html>
```

so parent window can steal it:
``` 
title="長い行を折り返す"
```

Maybe there are similar vulnerability in other error page.

## Impact

Attacker can steal language of Tor Browser even if the user has set privacy.spoof_english to 2.

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
