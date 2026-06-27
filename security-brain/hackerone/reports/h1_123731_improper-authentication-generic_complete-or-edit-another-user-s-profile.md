---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '123731'
original_report_id: '123731'
title: Complete or Edit Another User's Profile
weakness: Improper Authentication - Generic
team_handle: veris
created_at: '2016-03-17T00:26:30.451Z'
disclosed_at: '2016-05-13T16:19:51.353Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 3
tags:
- hackerone
- improper-authentication-generic
---

# Complete or Edit Another User's Profile

## Metadata

- HackerOne Report ID: 123731
- Weakness: Improper Authentication - Generic
- Program: veris
- Disclosed At: 2016-05-13T16:19:51.353Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I've found an issue where verified users can complete and submit a profile on behalf of another user. I've attached two video POCs (unlisted on YouTube).

Completion - https://www.youtube.com/watch?v=erH7ShUpqso
Editing - https://youtu.be/IQboAIHNpq4

Steps to reproduce:
1. Register a new user account
2. Verify the account via the email from Veris
3. Do not complete the profile but note the url. Create a new account.
4. Complete the account creation for the second user.
5. Logged in as the second user, navigate to the profile creation url from the first user.
6. Submit the values.
7. User 1 receives an email that their profile has been created.

Additionally, even after a profile has been set up, you can still edit it as a second user, at least if the steps above are followed. Assuming you did the steps above:

8. Navigate back to the /portal/complete-profile/XXXXX/
9. Change the values and resubmit the form
10. User 1 receives an email that their profile has been updated

Please let me know if you need any additional information.

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
