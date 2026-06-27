---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '80883'
original_report_id: '80883'
title: Authentication errors in server side validaton of E-MAIL
weakness: Improper Authentication - Generic
team_handle: gratipay
created_at: '2015-08-06T12:00:40.577Z'
disclosed_at: '2015-08-10T13:26:24.963Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 1
tags:
- hackerone
- improper-authentication-generic
---

# Authentication errors in server side validaton of E-MAIL

## Metadata

- HackerOne Report ID: 80883
- Weakness: Improper Authentication - Generic
- Program: gratipay
- Disclosed At: 2015-08-10T13:26:24.963Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

To be honest, I'm not sure if there is any real security implications of this bug, but it's something which should be fixed at some point (since it'll be pretty easy).
I'm going to describe the issue with reproducible steps:
1. Navigate to Gratipay Settings Page. https://gratipay.com/~username/settings/
2. Try adding an invalid e-mail address. ex: `myemail@gmail.com'`.
3. You won't be able to, as it says "please add an e-mail address. means you're only allowed to add a valid e-mail address.

Now this can be bypassed by intercepting request. Let me show you how.
* Add a valid email address in e-mail field. ex:mail01@gmail.com
* Run any Request Repeater (ex: BURP Repeater, Live HTTP Header, Temper Data)
* Click **Add E-Mail Address** and intercept the request.
* Go to your repeater and you'll find there this form contents,

> POST https://gratipay.com/~lolzsec007/emails/modify.json
Post Content:
```
action=add-email&address=mymail%40gmail.com
```

* Change email address from `mymail%40gmail.com` to `mymail%40gmail.com"><h1>`
* Reply/Repeat your request.
* The **Invalid** Email address will get saved.

So that means, there is no server side validation for adding e-mail addresses.
Now in this point, i would like to talked about another issue that i noticed because of this process,
I discovered there is simply character limit for email addresses, as there is no server side validation implemented, an attacker can add an email address with as much characters he wants.
but as per RFC, an email address that has more than **255** characters, shouldn't be allowed.

Possible Fix:
* Implementation of server side validation for email address should resolve both issues.

Looking forward.
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
