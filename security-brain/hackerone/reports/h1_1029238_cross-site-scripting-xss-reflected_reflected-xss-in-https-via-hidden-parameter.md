---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '1029238'
original_report_id: '1029238'
title: Reflected XSS in https://███████ via hidden parameter "████████"
weakness: Cross-site Scripting (XSS) - Reflected
team_handle: deptofdefense
created_at: '2020-11-07T23:07:53.967Z'
disclosed_at: '2022-01-19T19:30:22.449Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 2
tags:
- hackerone
- cross-site-scripting-xss-reflected
---

# Reflected XSS in https://███████ via hidden parameter "████████"

## Metadata

- HackerOne Report ID: 1029238
- Weakness: Cross-site Scripting (XSS) - Reflected
- Program: deptofdefense
- Disclosed At: 2022-01-19T19:30:22.449Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi everyone :)

I found a Reflected XSS on https://███████ via hidden parameter "████████" on the following authentication page : https://███████/██████████


## Steps To Reproduce:

- Use your favorite web browser
- Go to : 
```
https://███████/███████&███=TEST%22%3E%3Cscript%3Ealert(%27Reflected%20XSS%27)%3C/script%3E
```

An XSS is triggered !

The initial page was https://█████████/█████████

With a little research, you can find a hidden parameter "████████" which is directly reflected in the source code **without sanitize user entries**. Then just close the tag and inject our malicious code.

## Supporting Material/References:
Work on every browser (Firefox, Chrome ..)

## Suggested Mitigation/Remediation Actions

- Never trust user inputs, and therefore sanitize them.
- If the parameter "███" is useless in this page and in the authentication process, then it should be deleted.

## Impact

The damages of a reflexive XSS flaw are numerous: executing malicious javascript code, phishing, defacing ... We can also inject HTML code and mislead the user when displaying the web page.

From [OWASP](https://owasp.org/www-community/attacks/xss/) :

>Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

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
