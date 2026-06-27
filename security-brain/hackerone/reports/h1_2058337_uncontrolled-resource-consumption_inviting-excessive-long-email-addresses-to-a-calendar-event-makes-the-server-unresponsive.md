---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2058337'
original_report_id: '2058337'
title: Inviting excessive long email addresses to a calendar event makes the server
  unresponsive
weakness: Uncontrolled Resource Consumption
team_handle: nextcloud
created_at: '2023-07-09T05:36:23.481Z'
disclosed_at: '2023-10-16T13:50:04.871Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 46
asset_identifier: nextcloud/server
asset_type: SOURCE_CODE
max_severity: critical
tags:
- hackerone
- uncontrolled-resource-consumption
---

# Inviting excessive long email addresses to a calendar event makes the server unresponsive

## Metadata

- HackerOne Report ID: 2058337
- Weakness: Uncontrolled Resource Consumption
- Program: nextcloud
- Disclosed At: 2023-10-16T13:50:04.871Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

## Summary:
Due to the absence of a character limit in the email address field when sending emails, requests containing lengthy email addresses causes the server to get delay response, ultimately resulting in a denial of service.


## Steps To Reproduce:
1. As, a low privileged user, go to https://serveraddress/apps/calendar/dayGridMonth/now and create a new calendar.

{F2480561}

2. Click on Share link, click on share calendar link via email and intercept the request in burp entering a random email.

3. Send the request to repeater and observe the response time. The server will respond in ~600ms.

{F2480573}

{F2480610}

4. Now, use the attached payload of 50 MB (email_recipient.txt) in email and send the response. You will get response in about 10000 milllisecond. Larger the email length, longer will be the reponse time.



{F2480615}

[Note: you may use the following python script and payload attached below. POC attached :) ]

## Impact

Denial of service

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
