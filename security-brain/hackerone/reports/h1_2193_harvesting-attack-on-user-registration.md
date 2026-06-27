---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2193'
original_report_id: '2193'
title: harvesting attack on user registration
team_handle: security
created_at: '2014-02-22T09:58:02.931Z'
disclosed_at: '2014-05-19T08:35:25.997Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 5
tags:
- hackerone
---

# harvesting attack on user registration

## Metadata

- HackerOne Report ID: 2193
- Weakness: 
- Program: security
- Disclosed At: 2014-05-19T08:35:25.997Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

url: https://hackerone.com/users/sign_up

user account registration will ask for the applicant to provide all of the information required to create an account on a registration page. When the registration page is submitted, the application validates the uniqueness of the username and email address. The application then responds with
1.Username has already been taken
2. Email has already been taken

This behavior can be leveraged to harvest valid users of the application by attempting to register accounts with suspected usernames and emails and analyzing the responses.

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
