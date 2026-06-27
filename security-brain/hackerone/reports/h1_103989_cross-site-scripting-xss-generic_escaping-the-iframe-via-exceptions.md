---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '103989'
original_report_id: '103989'
title: Escaping the iframe via exceptions
weakness: Cross-site Scripting (XSS) - Generic
team_handle: khanacademy
created_at: '2015-12-07T22:53:14.542Z'
disclosed_at: '2015-12-29T20:46:52.266Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 0
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Escaping the iframe via exceptions

## Metadata

- HackerOne Report ID: 103989
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: khanacademy
- Disclosed At: 2015-12-29T20:46:52.266Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

You can throw an object with an `html` property to run arbitrary js
[Here](https://www.khanacademy.org/computer-programming/new-program/5946036004192256) is an example program that modifies a user's profile.  I made the program as private as possible by saving it with nouser and drawing nothing in the hopes that it will be ignored, but if you want me to delete it, I will.  The program will change your bio, so if you don't want that to happen, log out first.

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
