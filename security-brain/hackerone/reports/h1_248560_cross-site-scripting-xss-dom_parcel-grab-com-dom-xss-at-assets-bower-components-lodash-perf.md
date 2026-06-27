---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '248560'
original_report_id: '248560'
title: '[parcel.grab.com] DOM XSS at /assets/bower_components/lodash/perf/'
weakness: Cross-site Scripting (XSS) - DOM
team_handle: grab
created_at: '2017-07-12T05:59:20.188Z'
disclosed_at: '2017-08-16T14:01:13.772Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 19
tags:
- hackerone
- cross-site-scripting-xss-dom
---

# [parcel.grab.com] DOM XSS at /assets/bower_components/lodash/perf/

## Metadata

- HackerOne Report ID: 248560
- Weakness: Cross-site Scripting (XSS) - DOM
- Program: grab
- Disclosed At: 2017-08-16T14:01:13.772Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Summary:** DOM Based XSS (or as it is called in some texts, “type-0 XSS”) is an XSS attack wherein the attack payload is executed as a result of modifying the DOM “environment” in the victim’s browser used by the original client side script, so that the client side code runs in an “unexpected” manner ([Source](https://www.owasp.org/index.php/DOM_Based_XSS))

**Description:** It is observed in https://parcel.grab.com/assets/bower_components/lodash/perf/ endpoint that the value given in ```build``` and ```other``` GET parameters are accessed by client side script and written on page using ```document.write``` without output encoding - resulting DOM XSS. 

Vulnerable client side cod in page:
{F202292}

which will track back to script source - in switch default value has been set to ```build``` which will be same as user injected in parameter.
(Script link: https://parcel.grab.com/assets/bower_components/lodash/perf/asset/perf-ui.js)
{F202294}

## Browsers Verified In:
   * Mozilla Firefox (Latest)

## Steps To Reproduce:

Open any of below links in Mozilla Firefox and observe the script execution.

__Injected in ```build``` GET parameter:__
> https://parcel.grab.com/assets/bower_components/lodash/perf/?build=lodash%22%3E%3C/script%3E%3Ch1%3Evagg-a-bond%20is%20here%20:D%3C/h1%3E%3Cimg%20src=1%20onerror=alert(1)%3E&other=lodash

__Injected in ```other``` GET parameter:__
> https://parcel.grab.com/assets/bower_components/lodash/perf/?build=lodash&other=lodash%22%3E%3C/script%3E%3Ch1%3Evagg-a-bond%20is%20here%20:D%3C/h1%3E%3Cimg%20src=1%20onerror=alert(1)%3E


## Supporting Material/References:
Execution Screenshot:
{F202293}

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
