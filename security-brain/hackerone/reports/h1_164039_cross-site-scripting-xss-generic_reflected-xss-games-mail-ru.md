---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '164039'
original_report_id: '164039'
title: Reflected XSS @ games.mail.ru
weakness: Cross-site Scripting (XSS) - Generic
team_handle: mailru
created_at: '2016-08-28T18:12:07.521Z'
disclosed_at: '2016-10-18T19:42:51.395Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- cross-site-scripting-xss-generic
---

# Reflected XSS @ games.mail.ru

## Metadata

- HackerOne Report ID: 164039
- Weakness: Cross-site Scripting (XSS) - Generic
- Program: mailru
- Disclosed At: 2016-10-18T19:42:51.395Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I've found a reflected XSS in games.mail.ru. The vulnerable parameter is `url` in `/r` area.

#PoC
- Visit the following URL and click on *javascript:alert(document.domain)* - Alert will popup with domain.

https://games.mail.ru/r/?url=javascript:alert(document.domain)

{F115537}

- Also, to show current cookies, you can visit the following URL and click on *javascript:alert(document.cookie)* - Alert will popup with cookies.

https://games.mail.ru/r/?url=javascript:alert(document.cookie)

{F115538}

####Description
So, the input of `url` parameter was reflected in 'URL Context' means in the `<a href>` HtML tag.

It looks like you are properly sanitizing input means that `"` and `< >` are getting encoded into URL form, so that we cannot XSS it; but, there is another way. Since it is in URL context, we can use the following payload: `javascript:alert(document.domain)` 

As you can see that if I enter this input: `xyz"<` the " and < will be encoded like this `xyz%22%3C`

{F115539}

On the other side; you can see that if I input `javascript:alert(document.domain)`, it will be reflected into the `a href=` tag.

{F115540}

If you need more information, let me know.

Regards,
Ahsan

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
