---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1177287'
original_report_id: '1177287'
title: Password reset token leak on third party website via Referer header
weakness: Storing Passwords in a Recoverable Format
team_handle: upchieve
created_at: '2021-04-27T17:15:20.156Z'
disclosed_at: '2021-08-10T15:20:42.492Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 20
asset_identifier: app.upchieve.org
asset_type: URL
max_severity: none
tags:
- hackerone
- storing-passwords-in-a-recoverable-format
---

# Password reset token leak on third party website via Referer header

## Metadata

- HackerOne Report ID: 1177287
- Weakness: Storing Passwords in a Recoverable Format
- Program: upchieve
- Disclosed At: 2021-08-10T15:20:42.492Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

## Summary:

It has been identified that the application is leaking referrer token to third party sites. In this case it was found that the password reset token is being leaked to third party sites which is a issue knowing the fact that it can allow any malicious users to use the token and reset the passwords of the victim.

## Steps To Reproduce:

1) Request a password reset link for a valid account
2) Click on the reset link
3) Before resetting the password click on webiste
4) You will notice the following request in burpsuite


```
POST /events/1/NRJS-cb3c976936ae1bbb096?a=429165133&sa=1&v=1194.94d5a62&t=Unnamed%20Transaction&rst=56534&ck=1&ref=https://app.upchieve.org/setpassword/e2d710c6e099bf07d63507602a44c176 HTTP/1.1
Host: bam.nr-data.net
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0
Accept: */*
Accept-Language: en-US,en;q=0.5

```

## Impact

Password reset token leak on third party website via Referer header

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
