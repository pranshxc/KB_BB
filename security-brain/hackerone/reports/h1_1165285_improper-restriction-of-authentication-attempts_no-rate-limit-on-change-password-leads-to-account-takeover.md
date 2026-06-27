---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1165285'
original_report_id: '1165285'
title: No Rate limit on change password leads to account takeover
weakness: Improper Restriction of Authentication Attempts
team_handle: reddit
created_at: '2021-04-14T23:05:27.853Z'
disclosed_at: '2021-12-13T22:47:48.125Z'
has_bounty: false
visibility: full
substate: duplicate
vote_count: 6
asset_identifier: old.reddit.com
asset_type: URL
max_severity: critical
tags:
- hackerone
- improper-restriction-of-authentication-attempts
---

# No Rate limit on change password leads to account takeover

## Metadata

- HackerOne Report ID: 1165285
- Weakness: Improper Restriction of Authentication Attempts
- Program: reddit
- Disclosed At: 2021-12-13T22:47:48.125Z
- Has Bounty: No
- Visibility: full
- Substate: duplicate

## Original Report

## Summary:
I found when login and go to changing password, there is no rate limit on that function, which leads to takeover the account.

## Steps To Reproduce:

1-Create account on (https://old.reddit.com) & move to your setting,```In my case I chose !23Qweasdzxc as the password.```

2-Go to change password on (https://old.reddit.com/prefs/update/#) & enter the wrong password in old password   and enter new password and confirm the password.


3-Intercept the request & send it to Burp Intruder .

4-Make word-list & and start Brute Forcing.```Make sure to add the correct password in the wordlist, I made  8890 words in the wordlist```

finally you can see the correct password in the response.like the following response .
███


And as you can see I made more than 8000 requests.
and there is no rate limit.
{F1265803}

## Impact

If the attacker gets the user's cookies  through XSS or in somehow,he is able to takeover the account.

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
