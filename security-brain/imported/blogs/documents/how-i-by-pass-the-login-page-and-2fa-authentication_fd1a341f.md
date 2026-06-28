---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-20_how-i-by-pass-the-login-page-and-2fa-authentication.md
original_filename: 2020-09-20_how-i-by-pass-the-login-page-and-2fa-authentication.md
title: How I By-pass the login page and 2FA authentication…..
category: documents
detected_topics:
- mfa
- otp
- command-injection
tags:
- imported
- documents
- mfa
- otp
- command-injection
language: en
raw_sha256: fd1a341fdc49451d4ad9cc1a1730f58c09db0ffc400b2a8288b6c6b5e3dec4c6
text_sha256: b0af9ab5d530a0030bdb94676ae61448533fddd3ac4119a47a442a45580c8452
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How I By-pass the login page and 2FA authentication…..

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-20_how-i-by-pass-the-login-page-and-2fa-authentication.md
- Source Type: markdown
- Detected Topics: mfa, otp, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `fd1a341fdc49451d4ad9cc1a1730f58c09db0ffc400b2a8288b6c6b5e3dec4c6`
- Text SHA256: `b0af9ab5d530a0030bdb94676ae61448533fddd3ac4119a47a442a45580c8452`


## Content

---
title: "How I By-pass the login page and 2FA authentication….."
page_title: "CyberSecurity | Bug Hunting| | Medium"
url: "https://medium.com/@merry6607/how-i-by-pass-the-login-page-and-2fa-authentication-3f33b06838c"
authors: ["Harsh"]
bugs: ["Authentication bypass", "OTP bypass", "2FA / MFA bypass"]
publication_date: "2020-09-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4250
scraped_via: "browseros"
---

# How I By-pass the login page and 2FA authentication…..

Top highlight

Press enter or click to view image in full size
How I By-pass the login page and 2FA authentication…..
Harsh
Follow
3 min read
·
Sep 21, 2020

30

1

Hello everyone !

This is my first writeup. So please don’t mind if I was not able to explain it properly.

Today I will share the write-up of my bug I found , Which is listed on “Bugcrowd under Private Program” where I was able to take complete account take over of any user with its Email address or Phone Number.

In this write up I will share 2 attacks.
Login page By - pass.
2Fa Authentication By-pass.
Let’s Start……

I can’t disclose the program name so let’s consider.

www.test.com/home

So what I see is there was a login page and Sign-up option. So I created 2 tested account.
Now the website won’t allow me login into it till I confirm my email address, so I need to confirm my email address so I did.
Now after confirming my email address the Website redirect me to the 2FA authentication. Well 2FA authentication was Also mandatory to login into.
First I thought this website is really protected and I won’t be able to find any vulnerability,but I was like let’s try it and i hit my burp so I can see that how login authentication actually works. So I captured the request. And in request I saw that the token is generated with my password and when I check the response the same token is being validated with login credentials true and status code 200.
So what I did is I try to login with my 2nd account and again I check the request/response. What I see is the same token is being generated again and against and is used to validate your credentials.

Note : So i get to know that there is same token generated everytime. So I copy the request and response in my notepad for true credentials.

6. Now what I did is I enter the wrong password and capture the request again I see the same token with my wrong password. But unfortunately in response it was invalid credentials status code: 400,here I was not disappointed what I did is I just paste the response of my true credentials of first account and I forward the request.

DANG I WAS ABLE TO BY PASS THE LOGIN PAGE. I WAS REALLY HAPPY AT THE MOMENT.

But very next moment I saw the 2Fa page I was like my vulnerability will not be considered because there is 2FA enabled on it and it’s mandatory to enable while creating your account.

7. Now again I try to capture the request in my burp and saw the response and I again I see the token is being generated when OTP is send to the user mobile number, Again I captured the request in my burp with correct OTP and check the response there was the same token with status code :200. Successfully login.

Get Harsh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

8. So what I did is I again enter the wrong OTP and capture the request. And change the response unfortunately I was not able to by pass the OTP at the time. The web browser was loading.

9. I was bit angry at the moment,then I started playing with response in burp so is there any way to by pass it through response manipulation.

10. Hard luck no success till now now at last I repeat the 8 step again my last try so I did it and left my PC alone and went out for market for some work. When I come and see my PC screen I was successfully login into the account.

BINGO. I was successfully login into it .

11. What I noticed is web browser is actually taking some time to get me login into it.

So this way I was able to by pass the login page and 2Fa just doing response manipulation.

That’s all for today guys. Thank you for reading.

#bugbounty

#cybersecurity

HAPPY HACKING…….!!!!!
