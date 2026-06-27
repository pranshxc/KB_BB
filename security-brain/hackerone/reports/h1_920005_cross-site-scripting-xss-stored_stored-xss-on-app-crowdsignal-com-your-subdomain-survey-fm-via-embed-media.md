---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '920005'
original_report_id: '920005'
title: Stored XSS on app.crowdsignal.com + your-subdomain.survey.fm via Embed Media
weakness: Cross-site Scripting (XSS) - Stored
team_handle: automattic
created_at: '2020-07-09T18:51:17.320Z'
disclosed_at: '2020-11-18T14:20:06.021Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 94
tags:
- hackerone
- cross-site-scripting-xss-stored
---

# Stored XSS on app.crowdsignal.com + your-subdomain.survey.fm via Embed Media

## Metadata

- HackerOne Report ID: 920005
- Weakness: Cross-site Scripting (XSS) - Stored
- Program: automattic
- Disclosed At: 2020-11-18T14:20:06.021Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hello there,
I found a stored xss vulnerability.

Steps:
1. Go to `https://app.crowdsignal.com/dashboard`
2. Create a quiz.
3. Go to `https://app.crowdsignal.com/quizzes/{your-quiz-id}/question`
4. Add `Multiple Choice`
5. Put a name to answer 1.
6. Click Add media button.

{F901543}
7. Select Embed Media
8. Paste this:  `[wpvideo w0MiG12E]`
9. Insert it.
10. Open `Burp Suite` and click `Save` button.
11. Return to burp suite and paste this payload to `media[23168664]` parameter: `[wpvideo%20w0MiG12Exx1\"><svg/onload=prompt(document.domain)>]`
12. Forward the request and refresh the page. You will see xss alert.

Also go to `https://app.crowdsignal.com/sharing/quiz/{your-quiz-id}/` and copy survey.fm link. Go to it and you will see xss alert.

## Impact

Stealing cookies

Regards,
@mygf

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
