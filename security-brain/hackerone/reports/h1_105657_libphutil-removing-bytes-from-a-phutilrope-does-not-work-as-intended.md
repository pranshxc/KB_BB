---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '105657'
original_report_id: '105657'
title: 'libphutil: removing bytes from a PhutilRope does not work as intended'
team_handle: phabricator
created_at: '2015-12-16T20:09:47.358Z'
disclosed_at: '2015-12-16T21:01:12.461Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
---

# libphutil: removing bytes from a PhutilRope does not work as intended

## Metadata

- HackerOne Report ID: 105657
- Weakness: 
- Program: phabricator
- Disclosed At: 2015-12-16T21:01:12.461Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Mongoose. This is a bug in libphutil, it doesn't seem to affect phabricator because the bytes are always removed one buffer at a time. I imagine this could cause security issues in applications made with libphutil as a framework, if they use PhutilRope directly. This is how it goes:

    $rope = new PhutilRope();
    $rope->append("aaa");
    $rope->append("bbb");
    $rope->append("ccc");
    $rope->append("rrrrddddddddd");
    $rope->removeBytesFromHead(4);

    echo $rope->getAsString();

should output "bbcccrrrrddddddddd" but will instead output "ddddddddd".

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
