---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '252699'
original_report_id: '252699'
title: Hyper Link Injection In email and Space Characters Allowed at Password Field.
team_handle: phabricator
created_at: '2017-07-23T06:38:42.271Z'
disclosed_at: '2017-07-23T20:53:42.433Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
---

# Hyper Link Injection In email and Space Characters Allowed at Password Field.

## Metadata

- HackerOne Report ID: 252699
- Weakness: 
- Program: phabricator
- Disclosed At: 2017-07-23T20:53:42.433Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello mongoose ,

I found that when you put email and password for signup, you can use space characters for the password which shouldn't be allowed. I also found that you can use hyperlink in First Name Field at next step when you are entering your personal information here and when you will get the first email of Welcome or a forget password request email hyperlink will be there at the Place of First name.

Prof Of Concept:
-----------------
* Sign Up [Here](https://admin.phacility.com/auth/register/)
* In the username Field type "www.yoursite.com" and Fill the Rest of the Form like Email and etc.
* In the Password Field type 8 Space Bars which means 8 space characters.
* Click Register.
* You will now receive a email to confirm your email which will have the Hyper Link "www.yoursite.com".

What can Hacker Do?
-----------------------

Now with the above bugs a hacker could create a profile using victim's Email and put a link to his phishing site at the first name and he create a account and there will be a email sent to victim's email id using your system. Victim will open your email as it is from a trustful source and might click the phishing link.

A hacker can also Brute Force your password as it is very weak and fully takeover any user that have created an account using space characters.

Regards,
Ali Ashber

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
