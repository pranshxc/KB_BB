---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '864712'
original_report_id: '864712'
title: Page has a link to google drive which has logos and a few customer phone recordings
weakness: Cleartext Storage of Sensitive Information
team_handle: zomato
created_at: '2020-05-02T11:26:53.842Z'
disclosed_at: '2022-02-21T08:15:22.671Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 45
asset_identifier: '*.zomato.com'
asset_type: WILDCARD
max_severity: critical
tags:
- hackerone
- cleartext-storage-of-sensitive-information
---

# Page has a link to google drive which has logos and a few customer phone recordings

## Metadata

- HackerOne Report ID: 864712
- Weakness: Cleartext Storage of Sensitive Information
- Program: zomato
- Disclosed At: 2022-02-21T08:15:22.671Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

**Description:** 

* Go to ███████

Refer to the screenshot below

██████

As you can see in the above image, there is is link to access zomato logos.This redirected me to a google drive page which not only had logos but also customer care recordings where sensitive information like **Customer mobile numbers,customer names,what food they ordered,order id's** were disclosed.

Refer to the screenshot below.

███

Now go to **recordings** folder.

██████

As you can see in the above image,there are about 35 recordings wherein sensitive information is being disclosed.I guess everything is uploaded yesterday (May 1st).

I suspect there would be more of a recordings added to this folder as I see a folder named **Till Date Recordings** which is empty as of now.

## Steps To Reproduce:

1. Go to Go to █████
2.Click on the google drive link for logos
3.Go to recordings folder
4.Find all customercare recordings

## Supporting Material/References:

 The following is one of the audio recording found wherein customer number,name is disclosed.

  * ██████████

## Impact

Sensitive PII disclosure.

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
