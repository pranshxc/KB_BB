---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '49357'
original_report_id: '49357'
title: Substantially weakened authenticity verification when using 'Remember me for
  a week'
weakness: Cryptographic Issues - Generic
team_handle: security
created_at: '2015-02-27T03:48:46.203Z'
disclosed_at: '2015-03-12T16:29:30.505Z'
has_bounty: false
visibility: full
substate: informative
vote_count: 3
tags:
- hackerone
- cryptographic-issues-generic
---

# Substantially weakened authenticity verification when using 'Remember me for a week'

## Metadata

- HackerOne Report ID: 49357
- Weakness: Cryptographic Issues - Generic
- Program: security
- Disclosed At: 2015-03-12T16:29:30.505Z
- Has Bounty: No
- Visibility: full
- Substate: informative

## Original Report

Hello HackerOne,

I noticed that in order to access data bound to a user's permissions, say their own bug reports, or CSRF-token, you only need one certain cookie, which is ```remember_user_token```, and although it is sent when the user uses HackerOne in a normal fashion, the ```session``` cookie is ignored and thus not required. This only works if the user has the "Remember me for a week" option ticked when logging in.

Both cookies are values base64-encoded values. Decoding the ```session``` cookie value results in a binary sequence of 602 bytes, and the ```remember_user_token``` results in a sequence 38 bytes wide.

Both cookies also include a trailing 20 byte value, presumably a hash value. So ```session``` comprises 602 + 20 = 622 bytes, and ```remember_user_token``` 38+20 = 58.

Being able to see confidential data with the 58 bytes rather than 622 bytes obviously lowers the amount of computing power, the number of tries in a brute-force attack, or any way you want to see it, significantly. Presupposing that both values are uniformly random data, then:

```python
math.log10((256**622) / (256**58))
1358.2473404358832
```

In other words, that is 1358 orders of magnitude of difference, which is substantial.

I furthermore noticed that the various ```remember_user_token``` values that I yielded upon subsequent logins did not look random at all, but they instead looked quite similar to each other. Suspecting that the login date and time were encoded in this value, I did some statistical tests to see if I could reliably correlate the cookie value with the date and time it was set. Calculations involving these data ( cookie value -> base64 decode -> value of binary sequence as integer on one axis, login date/time as number of seconds since epoch on the other axis), eventually yielded me a 0.93 Pearson correlation coefficient for the last 8 bytes of the binary sequence in my (admittedly limited) test data. It follows that if my test data was sufficiently large to establish this degree of correlation, then knowing when a user logged in can further lower the amount of computation required to successfully guess the ```remember_user_token```. Even if the login time is not known, an attacker can user their common sense and assume no one logged in prior to the inception of HackerOne ( < 2013 ? ) nor in the future ( say > March 2015).

Finally, it looks to me that ```session``` is frequently updated with a new value whereas ```remember_user_token``` remains constant for the remainder of the session.

To reproduce:

```
curl https://hackerone.com/current_user -H 'Cookie: remember_user_token={{REMEMBER_USER_TOKEN}}'
```

Where {{REMEMBER_USER_TOKEN}} is the value that you copy from your browser once you are logged in. This also works for bug reports in the form

```
https://hackerone.com/reports/[0-9]\+.json
```

Guido

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
