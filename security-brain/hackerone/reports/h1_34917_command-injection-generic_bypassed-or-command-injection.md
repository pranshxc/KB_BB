---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '34917'
original_report_id: '34917'
title: Bypassed or command injection
weakness: Command Injection - Generic
team_handle: blockio
created_at: '2014-11-07T17:39:56.369Z'
disclosed_at: '2015-01-01T03:41:26.120Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 2
tags:
- hackerone
- command-injection-generic
---

# Bypassed or command injection

## Metadata

- HackerOne Report ID: 34917
- Weakness: Command Injection - Generic
- Program: blockio
- Disclosed At: 2015-01-01T03:41:26.120Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Respected sir,

Step1:sign up an account
Step2:set secret pin
Step3:After that a tick box is asking " I will lose my coins if I forget my Secret PIN and Secret Mnemonic. I know this."..
Step4:If you check the tick box , the button "done" will enable.It is mandatory to check the box.

The bug is,

I bypassed this tick box feature.Without checking the tick box i applied command injection to the done button.
I changed the disabled to enabled in the coding part of the done button.Then i clicked done button without accepting the tickbox.

Please check the video for details..

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
