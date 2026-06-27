---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '305237'
original_report_id: '305237'
title: Malicious file upload (secure.lahitapiola.fi)
weakness: Violation of Secure Design Principles
team_handle: localtapiola
created_at: '2018-01-16T14:26:06.092Z'
disclosed_at: '2018-04-10T03:36:59.896Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 22
asset_identifier: secure.lahitapiola.fi
asset_type: URL
max_severity: critical
tags:
- hackerone
- violation-of-secure-design-principles
---

# Malicious file upload (secure.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 305237
- Weakness: Violation of Secure Design Principles
- Program: localtapiola
- Disclosed At: 2018-04-10T03:36:59.896Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Basic report information
**Summary:** 
Malicious file upload

**Description:** 
Hello!

I noticed that when a user sends new message you have restricted pretty strictly the files which is ok to upload. Like .svg:
{F254353}

How ever if a user impersonate another user (just a one example) and start the conversation with localtapiola's employee and will get the message from localtapiola an attacker can upload malicious files which can be used against your employees like .svg and .exe:
{F254354}

I sended one email to me with "malicious" svg file and it came through. This could obviously contain something much more badly than just a pop up window:
{F254352}

I want to underline that I'm not 100% sure is this expected behaviour but in my opinion files like .exe should not be allowed. And why an (attacker) user should be allowed to upload anything at this point? 

This is straight way to attack against your employees and/or bypass the original upload restrictions.

**Domain:** 
secure.lahitapiola.fi

## Browsers / Apps Verified In:

  * Newest version of FF

## Steps To Reproduce:

  1. Start conversation with secure service
  2. When you receive the first message via this service upload any file like .exe or .svg
  3. See that you can send these files

## Impact

An attacker can bypass upload restrictions.

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
