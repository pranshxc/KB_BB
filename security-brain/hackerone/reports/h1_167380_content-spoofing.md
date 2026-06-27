---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '167380'
original_report_id: '167380'
title: content spoofing
team_handle: legalrobot
created_at: '2016-09-10T14:19:28.276Z'
disclosed_at: '2017-05-16T05:41:29.737Z'
has_bounty: false
visibility: full
substate: spam
vote_count: 13
tags:
- hackerone
---

# content spoofing

## Metadata

- HackerOne Report ID: 167380
- Weakness: 
- Program: legalrobot
- Disclosed At: 2017-05-16T05:41:29.737Z
- Has Bounty: No
- Visibility: full
- Substate: spam

## Original Report

1. go to 'Sign in to Legal Robot Ideas Portal' this link 'https://legalrobot.ideas.aha.io/portal_session/new'

2.and enters invalid login credential , the user will the redirected to this link: 'https://legalrobot.ideas.aha.io/auth/failure?message=invalid_credentials&strategy=password_portal_user&email=<email address>'

#note : view 1.png file in the attachment.

3.now remove 'password_portal_user'from the redirected link.

#note: view 2.png file in the attachment.

4.now remove 'invalid_credentials' from the redirected link

#note:view 3.png file in the attachment.

5.also remove email address showing in the url :'https://legalrobot.ideas.aha.io/auth/failure?message=invalid_credentials&strategy=password_portal_user&email=<email address>'

6.after all the changes ur will look like this: 'https://legalrobot.ideas.aha.io/auth/failure?message=&strategy=r&email='

7.now type 'you are Hacked!'      without quotes    and now ur will look like this:
'https://legalrobot.ideas.aha.io/auth/failure?message=you are Hacked!&strategy=r&email='

8. and you will the error massage content is changed from 'Login failed. If you are an Aha! User log in to Aha! first.'  to 'Single sign on failure:you are Hacked!' .

#now view 4.png file in the attachment

thankyou!

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
