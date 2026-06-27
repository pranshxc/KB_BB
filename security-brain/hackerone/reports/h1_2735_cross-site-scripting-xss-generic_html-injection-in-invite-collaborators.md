---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '2735'
original_report_id: '2735'
title: HTML injection in "Invite Collaborators"
weakness: Cross-site Scripting (XSS) - Generic
team_handle: relateiq
created_at: '2014-03-02T19:23:13.655Z'
disclosed_at: '2014-04-06T19:10:37.234Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 5
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# HTML injection in "Invite Collaborators"

## Metadata

- HackerOne Report ID: 2735
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: relateiq
- Disclosed At: 2014-04-06T19:10:37.234Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

I was able to edit the contents of the "Invite Collaborators" mail, by using HTML code as my first name. By exploiting this vulnerability, an attacker could send an email with custom text/html code from `notify@relateiq.com` (from the RelateIQ server) to any recipient. This can be used for phishing attacks (see attachment: example.png).

Steps to reproduce:

[1] Register as a new user
[2] When asked for a name, enter exploit code in first name field (see attachment: step2.png). 

For this demonstration I will use a simple example:
`You have been hacked. Click <a href="http://phishing-site">here</a> to reset your password.<div style="display:none">`

[3] Go through the final steps
[4] Go to home and send an invite to the target (see attachment: step4.png)

The target will now receive the phishing email (see attachment: email.png). In this simple example it is obvious that the email is fake, but better exploit code can be easily written.

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
