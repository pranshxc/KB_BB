---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '176066'
original_report_id: '176066'
title: Denial of service attack on Brave Browser.
weakness: Uncontrolled Resource Consumption
team_handle: brave
created_at: '2016-10-16T00:14:22.107Z'
disclosed_at: '2017-02-10T23:56:24.807Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Denial of service attack on Brave Browser.

## Metadata

- HackerOne Report ID: 176066
- Weakness: Uncontrolled Resource Consumption
- Program: brave
- Disclosed At: 2017-02-10T23:56:24.807Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Hey there,

Basically,an HTML sent by an attacker to a victim can cause dos attack(whole system log's out) when that file is opened by the victim in his brave browser.This vulnerability is occurring because browser is not able to handle the input passed in alert() JavaScript function.This bug has been tested on latest brave browser in Linux platform.

## Products affected: 

Brave's Browser in Linux(Kali Linux)

## Steps To Reproduce:


1 create an html file like :-

Brave.html( it is attached as POC below) i couldn't write the content of file here because the value inside alert() parameter is too large to be displayed here.

2 Open the file in your Brave browser in Linux platform.

## Supporting Material/References:

I have attached an html file below just download it and open it up in brave browser on linux system and 

screen will show "OH! something went wrong and you will be logged out".

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
