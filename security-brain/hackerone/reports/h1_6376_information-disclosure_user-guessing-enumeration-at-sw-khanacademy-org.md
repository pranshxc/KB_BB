---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '6376'
original_report_id: '6376'
title: User guessing/enumeration at sw.khanacademy.org
weakness: Information Disclosure
team_handle: khanacademy
created_at: '2014-04-08T01:24:28.601Z'
disclosed_at: '2014-04-15T19:04:05.632Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- information-disclosure
---

# User guessing/enumeration at sw.khanacademy.org

## Metadata

- HackerOne Report ID: 6376
- Weakness: Information Disclosure
- Program: khanacademy
- Disclosed At: 2014-04-15T19:04:05.632Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hi there,

I've discovered a possibility to check whether a specific email address is associated with an account at  sw.khanacademy.org. An attacker could use this issue to gather some information about his victim.

###Details

```
- Host: sw.khanacademy.org
- URL: https://sw.khanacademy.org/forgotpw
- Affected parameter: email
```

###Steps to reproduce

1. Open the url ```https://sw.khanacademy.org/forgotpw```
2. Enter the email address you'd like to check. (e.g. test@test.de)
3. Submit the form
4. The application will report an error that the email address wasn't found.

If the email address existed in the database, there would not be an error, but a success message that a reset link was sent or something. 

###PoC:

```
POST /forgotpw HTTP/1.1
Host: sw.khanacademy.org
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101 Firefox/28.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://sw.khanacademy.org/forgotpw
Cookie: [COOKIES]
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 41

email=test%40test.de&reset=Reset+password
```

###How to fix?
The application should always return a message like "If the email was found in the database, you'll receive a reset token soon." 
This leaves no information about the association between the application and the email/user.

Best regards,
Sebastian Neef

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
