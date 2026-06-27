---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '39139'
original_report_id: '39139'
title: URL Crashing browser. {Tested on firefox, Chrome and Safari}
weakness: Uncontrolled Resource Consumption
team_handle: security
created_at: '2014-12-12T07:08:08.313Z'
disclosed_at: '2016-05-25T02:16:57.692Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- uncontrolled-resource-consumption
---

# URL Crashing browser. {Tested on firefox, Chrome and Safari}

## Metadata

- HackerOne Report ID: 39139
- Weakness: Uncontrolled Resource Consumption
- Program: security
- Disclosed At: 2016-05-25T02:16:57.692Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi again Dear,

I am facing a strange behavior when I try to access this particular URL

 https://hackerone.com/reports/10373 

I test it  on multiple computer with different browser.
Browser goes into indefinite loop and disabled right click ,and after some time it crashes .

It seems like the problem is because of JavaScript .
when I tried to debug it:

It looks like the JS function this  creating problem 

 h.indexOf = function(e, t, n) {
        if (null == e) return -1;
        var r = 0,
            i = e.length;
        if (n) {
            if ("number" != typeof n) return r = h.sortedIndex(e, t), e[r] === t ? r : -1;
            r = 0 > n ? Math.max(0, i + n) : n
        }
        for (; i > r; r++)
            if (e[r] === t) return r;
        return -1
    }


Please have a look and revert if I am wrong.

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
