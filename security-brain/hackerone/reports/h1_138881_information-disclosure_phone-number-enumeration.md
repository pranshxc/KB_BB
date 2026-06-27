---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '138881'
original_report_id: '138881'
title: Phone Number Enumeration
weakness: Information Disclosure
team_handle: uber
created_at: '2016-05-15T02:55:39.222Z'
disclosed_at: '2016-07-07T23:06:19.608Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- information-disclosure
---

# Phone Number Enumeration

## Metadata

- HackerOne Report ID: 138881
- Weakness: Information Disclosure
- Program: uber
- Disclosed At: 2016-07-07T23:06:19.608Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

I discovered it is possible to retrieve all Uber's customer's cell phone numbers using an API endpoint.

While going through a sign up form, I noticed that the page was making an ajax call to an API to validate the email address being entered and to make sure it doesn't already belong to an account. I began experimenting with the API and discovered that it will do the same type of validation for mobile numbers.

Response With Unused Mobile Number
{F93849}

Response With Used Mobile Number (my cell number)
{F93850}

Using this information, it is very easy to loop through numbers and generate a list of Uber's customer's mobile numbers. I created a simple proof-of-concept in Python showing how this can be done and attached it to this report. {F93853}

This screenshot shows the results of my PoC script after running through a small range of numbers above and below my wife's cell phone number. The 8054528808 number is hers. I have no relationship to the other numbers. Other than checking around my wife's and my cell phone numbers, I did not attempt to extract any other numbers or information.
{F93852}

Here is another screenshot after running the PoC script for numbers just above and below my number (4155083235).
{F93851}

Using this information, an attacker could launch a massive phishing campaign or just harass Uber customers. It would probably also be bad PR if someone were to dump all Uber's customer's cell phone numbers out on to the Internet.

Requiring a CSRF token in the API request would slow the process down considerably, but wouldn't completely eliminate it. Maybe requiring a CSRF token and adding some rate limiting might do it.

Thanks!

- Seth

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
