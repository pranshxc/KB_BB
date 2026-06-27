---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '203088'
original_report_id: '203088'
title: Brave payments remembers history even after clearing all browser data.
weakness: Information Disclosure
team_handle: brave
created_at: '2017-02-03T04:43:24.333Z'
disclosed_at: '2017-08-10T05:11:12.297Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 2
tags:
- hackerone
- information-disclosure
---

# Brave payments remembers history even after clearing all browser data.

## Metadata

- HackerOne Report ID: 203088
- Weakness: Information Disclosure
- Program: brave
- Disclosed At: 2017-08-10T05:11:12.297Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

> NOTE! Thanks for submitting a report! Please fill all sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty.

## Summary:

As a user you expect the browser to not persist data after clearing browser data. The Brave payments feature persists the websites details and usage.

## Products affected: 
Brave	                        0.13.1
rev	                                9dd06f9
Muon	                        2.0.18
libchromiumcontent	54.0.2840.100
V8	                                5.4.500.41
Node.js	                        7.0.0
Update Channel	        dev
os.platform	                darwin
os.release	                16.4.0
os.arch	                        x64

## Steps To Reproduce:

 * Open a porn site or any site and spend some time on it
 * Clear browsing data of the browser with all options enabled (screenshot attached)
 * It'll ask to restart the browser, do it (optional)
 * Now navigate to brave payments page
 * Voila! Your porn history is there

## Supporting Material/References:

  * Screenshot of the clear browsing data panel with all the settings enabled
  * Screenshot of the porn website listed on the brave payments page

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
