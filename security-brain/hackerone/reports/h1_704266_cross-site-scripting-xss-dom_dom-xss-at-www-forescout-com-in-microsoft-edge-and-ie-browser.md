---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '704266'
original_report_id: '704266'
title: DOM XSS at www.forescout.com in Microsoft Edge and IE Browser
weakness: Cross-site Scripting (XSS) - DOM
team_handle: forescout_technologies
created_at: '2019-09-30T13:12:39.890Z'
disclosed_at: '2020-04-07T08:37:19.705Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 93
asset_identifier: www.forescout.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# DOM XSS at www.forescout.com in Microsoft Edge and IE Browser

## Metadata

- HackerOne Report ID: 704266
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: forescout_technologies
- Disclosed At: 2020-04-07T08:37:19.705Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
I've found an DOM Based XSS on homepage 

## Steps To Reproduce:
1.Go to this url and you'll see alert pop
`https://www.forescout.com/#<img src=x onerror=alert('XSS')>`

But this will work just on ME/IE browsers because chrome and firefox have default encode system hash url

And vulnerable code is on your directly source code within jquery code. As you can see there is no encode in ==window.location.hash== code so when we open the page with #<img src=x onerror=alert(1)> it executes code.

`jQuery(window).load(function() {
    jQuery('a.fancybox-inline[href="' + window.location.hash + '"]:first').each(function() {
        jQuery(this).delay(700).trigger('click');
    });
});`

## Supporting Material/References:
I have uploaded a picture to show you POC


Regards 
Enesdex

## Impact

--Hacker can execute malicious codes in victim's browser
--Hacker can redirect user to malicious website
--Hacker can steal victim's cookies etc.

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
