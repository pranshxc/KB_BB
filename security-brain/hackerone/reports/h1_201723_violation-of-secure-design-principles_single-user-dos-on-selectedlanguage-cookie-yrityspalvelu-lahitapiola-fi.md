---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '201723'
original_report_id: '201723'
title: Single user DOS on selectedLanguage -cookie (yrityspalvelu.lahitapiola.fi)
weakness: Violation of Secure Design Principles
team_handle: localtapiola
created_at: '2017-01-28T09:06:51.006Z'
disclosed_at: '2017-03-11T05:28:26.062Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- violation-of-secure-design-principles
---

# Single user DOS on selectedLanguage -cookie (yrityspalvelu.lahitapiola.fi)

## Metadata

- HackerOne Report ID: 201723
- Weakness: Violation of Secure Design Principles
- Program: localtapiola
- Disclosed At: 2017-03-11T05:28:26.062Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

Hey,
I have found a way in which any attacker will send a link to user, and user will not able to use any of the service provided by lahitapiola.

#Steps to reproduce:

1: copy link :`https://yrityspalvelu.tapiola.fi/a2/YvpCommonWeb2/faces/Landingpages/Vakuutustodistus.xhtml?p=1310386997019&locale=fi&selectedLanguage=%22%3E%3Cimg%20src=x%20onerror=alert%282%29%3E`

Vulnerable parameter: `selectedLanguage`
Payload: any unwanted character.

2: Paste in browser,
and go.
and you will end up with an error,
`Palvelussa tapahtui virhe. Yritä myöhemmin uudelleen.
Siirry www.lahitapiola.fi etusivulle.
Your support ID is: 565608280756490943 ` 
{in my case in private browsing mode i direclty ended up on above error, but in local browsing mode, i didn't got any error}

3: Now visiting on any service of `lahitapiola` you will ended up on same error, visiting on any link in the lahitapiola will always ended up on an error.

#scenario:

Attacker will send an email in img src tag, as this is GET request, and when victim open that email, that link will execute, and user will not able to access any of the service, we can windup this issue with two, one is above and other one is CSRF issue.

I hope you will able to reproduce the issue.

Thanks

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
