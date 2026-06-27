---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '158749'
original_report_id: '158749'
title: '[alpha.informatica.com] Expensive DOMXSS'
weakness: Cross-site Scripting (XSS) - Generic
team_handle: informatica
created_at: '2016-08-12T08:58:13.076Z'
disclosed_at: '2017-07-08T09:25:26.095Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 10
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# [alpha.informatica.com] Expensive DOMXSS

## Metadata

- HackerOne Report ID: 158749
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: informatica
- Disclosed At: 2017-07-08T09:25:26.095Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi again,

The page at https://alpha.informatica.com/assessmentBase/assessment.html contains the following JavaScript:

<script>
    var baseHeaderElement = '<base href="'+ window.location.pathname + '" />';
    $('head').append(baseHeaderElement);
</script>

An attacker can exploit this using a protocol-relative URL. In Chrome, open the following URL and either proxy though Burp or look at the network tab in the dev console: https://alpha.informatica.com//assessmentBase/assessment.html

You will see a failed GET request to https://assessmentbase/etc/designs/informatica-com/assessmentform/js/angular.min.js

A sufficiently rich attacker can register assessementbase, and make it serve malicious JavaScript, turning this into a reflected XSS vulnerability.

This issue was passively identified by burp suite's code analysis engine.

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
