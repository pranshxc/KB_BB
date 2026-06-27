---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '991718'
original_report_id: '991718'
title: hardcoded password stored in javascript of https://████.mil
weakness: Use of Hard-coded Password
team_handle: deptofdefense
created_at: '2020-09-26T00:29:16.498Z'
disclosed_at: '2020-11-02T21:44:35.411Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 6
tags:
- hackerone
- use-of-hard-coded-password
---

# hardcoded password stored in javascript of https://████.mil

## Metadata

- HackerOne Report ID: 991718
- Weakness: Use of Hard-coded Password
- Program: deptofdefense
- Disclosed At: 2020-11-02T21:44:35.411Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

**Summary:**

I have discovered a cleartext password stored within a javascript. This password allows me to authentication to https://█████.mil.

**Description:**

I have discovered a cleartext password stored within a javascript. This password allows me to authentication to https://███████.mil.


To confirm this vulnerability we will first navigate to https://███████.mil, you are now prompted to type a password. We will provide an incorrect password such as 'Password'.

██████████

███

We can confirm the password is invalid. However, reviewing the javascript data for '██████.chunk.js' we can confirm the authentication is validated based on a hardcoded password '█████████!'.

███████

We can now confirm if we can access the staging web app using hardcoded password.

██████

███████

## Impact

By knowing the password, it is possible to understand your password policy and structure which will encourage bruteforcing and password spray attacks in your environment.

## Step-by-step Reproduction Instructions

1. Navigate to https://█████████.mil.
2. Open your browser debugger by pressing F12.
3. Click on Network and refresh the page.
4. Open the javascript '██████████.chunk.js' and look for where the password is stored. You will see "(n=prompt("Enter Password","Password"),o="██████;" copy the password.
5. Now close out your browser debugger and refresh the page and type the password in.
6. You now have access to ████████.mil

## Suggested Mitigation/Remediation Actions

If this staging web application needs to be password protected, you can refer to the following AWS documentation on how to properly setup basic authentication https://docs.aws.amazon.com/speke/latest/documentation/authentication.html.

Resources:
https://owasp.org/www-community/vulnerabilities/Use_of_hard-coded_password

## Impact

By knowing the password, it is possible to understand your password policy and structure which will encourage bruteforcing and password spray attacks in your environment.

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
