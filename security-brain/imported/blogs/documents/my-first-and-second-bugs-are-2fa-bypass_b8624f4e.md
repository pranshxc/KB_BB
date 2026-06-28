---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-03_my-first-and-second-bugs-are-2fa-bypass.md
original_filename: 2022-10-03_my-first-and-second-bugs-are-2fa-bypass.md
title: My First And Second Bugs Are — 2FA Bypass
category: documents
detected_topics:
- mfa
- otp
- sso
- access-control
- command-injection
- information-disclosure
tags:
- imported
- documents
- mfa
- otp
- sso
- access-control
- command-injection
- information-disclosure
language: en
raw_sha256: b8624f4ecc32b86a1b23fcf3076448f6e52c10df33ea345683df9fa8109b1a3c
text_sha256: 80763df08bf88f92410bc115015201fd1357499d2070659d4434466eb8539851
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# My First And Second Bugs Are — 2FA Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-03_my-first-and-second-bugs-are-2fa-bypass.md
- Source Type: markdown
- Detected Topics: mfa, otp, sso, access-control, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `b8624f4ecc32b86a1b23fcf3076448f6e52c10df33ea345683df9fa8109b1a3c`
- Text SHA256: `80763df08bf88f92410bc115015201fd1357499d2070659d4434466eb8539851`


## Content

---
title: "My First And Second Bugs Are — 2FA Bypass"
page_title: "MY FIRST AND SECOND BUGS ARE — 2FA BYPASS | by JAI NIRESH J | Medium"
url: "https://medium.com/@nireshpandian19/my-first-and-second-bugs-are-2fa-bypass-1f6fd823b467"
authors: ["Jai Niresh J"]
bugs: ["2FA / MFA bypass", "HTTP response manipulation", "Information disclosure"]
publication_date: "2022-10-03"
added_date: "2022-10-04"
source: "pentester.land/writeups.json"
original_index: 2089
scraped_via: "browseros"
---

# My First And Second Bugs Are — 2FA Bypass

MY FIRST AND SECOND BUGS ARE — 2FA BYPASS
JAI NIRESH J
Follow
3 min read
·
Oct 3, 2022

279

2

Hey there guys,

This write up is about my very first bug and the second one that i found shortly after the first one, which are IMPROPER AUTHENTICATION CONTROLS that led to a 2FA bypass.

FIRST ONE :

The first bug was on a cryptocurrency wallet website, (lets call it redacted.com).
The bug was quite simple, an account with the 2FA authorization would recieve a response similar to

{
... ,
... ,
required: false
}

and would get redirected to the dashboard.

Whereas, a 2FA authentication enabled account would recieve a response similar to the below one.

{
... ,
... ,
required: true
}

I was pretty excited on seeing these parameters, and i immediately fired up my BURP proxy and intercepted these requests and obviously changed the required parameter’s value from true -> false, and guess what !

I was redirected to the dashboard due to the client side response manipulation, and BOOM ! I got all the details of the account, and in no time i was logged in to the account !

LESSON LEARNT : Always check for juicy parameters on the response.

SECOND ONE :

This was a bit tough to find, not because of it’s complexity, but it involved multiple endpoints which took time to find them.

This was an altogether different website, (lets call it bluedacted.com)

Get JAI NIRESH J’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The first thing i checked here was the response of the login request, and to my excitement the response looked like

400 BAD REQUEST
.
.
.
{
error:"xxx",
message:"xxx",
need2FA:true
}

On noticing the juicy parameter -> “need2FA” , i was once again excited and in no time my burp was fired up and i tried out the same kind of response manipulation like the first one, and the same way i was redirected to the dashboard.

Unfortunately, that was it ! I was just redirected to the inner dashboard and option pages, but did not get the details of the user i tried to login.

Soon, i found out that the bluedacted.com website uses an Authorization token in it’s request, and this token is provided only if the 2FA step gets completed. This was enough to make my heart sink !

Since i manipulated the response, i never got my Auth token and all the requests made by my browser had this

Authorization: Bearer undefined

Neverthless, i did not give up, later that day when i was loittering around on the webpage, i came across an order page, where customers can order items, and it contained a LOGIN FORM which makes an ajax request to the server to fetch just the customer ID and the Name of the customer logging in.

SOON, i tried the credentials of my 2FA protected account and YEAH ! It got me my name and my customer ID without asking for the OTP.

This was not enough, I must escalate this to login to the account, as any sensible hacker would do, i went to my Developer tools and checked for the ajax responses made by my browser, and guess what !

The response was a JSON which had the details of my account and an Authorization token like

{
"customer_ID": 1452,
"name": Magma,
"token": xxxxxxxxxxxxxxxx
}

I rushed into the previous actual login page, and i replaced the Authorization: Bearer undefined -> with my actual token i got here, and

BOOOM !!! WE ARE BACK IN BUSINESS.

Once again it was a 2FA bypass !

LESSON LEARNT : Always spider around all the login pages and forms.

You could expect a lot of writeups, following this in the coming days !

Thank You
