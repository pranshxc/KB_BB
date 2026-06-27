---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '44492'
original_report_id: '44492'
title: Flaw in login with twitter to steal Oauth tokens
weakness: Improper Authentication - Generic
team_handle: x
created_at: '2015-01-21T05:37:34.318Z'
disclosed_at: '2015-02-18T18:39:53.370Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Flaw in login with twitter to steal Oauth tokens

## Metadata

- HackerOne Report ID: 44492
- Weakness: Improper Authentication - Generic
- Program: x
- Disclosed At: 2015-02-18T18:39:53.370Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey hi,

Steps to reproduce:
=============================================

I have been testing the twitter kit in fabric.
I added login with twitter integration to my application.
I pushed the application to my android phone , clicked login with twitter.
entered my username and password.

Searched my logcat for everything with the word "twitter" in it. 
I found the oauth token getting leaked via login with twitter integration on Fabric.
So any app that is using fabric's twitter kit ( login with twitter) is vulnerable to it.
Any other app installed on that particular phone hasaccess to logcat, and can read the logs.
which results in oauth token stealing.

Regards,
karthik
Wesecureapp

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
