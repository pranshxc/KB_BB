---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '93154'
original_report_id: '93154'
title: Csrf near report abuse meme
weakness: Cross-Site Request Forgery (CSRF)
team_handle: imgur
created_at: '2015-10-09T20:37:17.090Z'
disclosed_at: '2015-12-09T17:48:07.924Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# Csrf near report abuse meme

## Metadata

- HackerOne Report ID: 93154
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: imgur
- Disclosed At: 2015-12-09T17:48:07.924Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hey team i would like to report a real csrf threat which allows attacker to make report abuse to any meme on behalf of the users 

how i found this bug :-

lets visit to any meme example :-

1> http://imgur.com/t/memes/ieTEJEd 
2> i clicked on post options 
3> i got an option called report i clicked on it
4> i selected a option of abusive/offensive 
5>started my intercept and click on report 
6> after intercepting i saw the post request having a unique token like ''Sid'' which maybe for form validations
7>i managed to delete the value of sid and still get a 200 ok status code and it was report abused 

below i will attach the snapshot of the original request edited and response :)

i ve attached images of original request and i have stripped off the formvalidation tokens and session values and passed the request i could still get a 200 ok status which means the vaidations are not properly checked server side

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
