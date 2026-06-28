---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-13_bugbounty-user-account-takeover-i-just-need-your-email-id-to-login-into-your-sho.md
original_filename: 2018-12-13_bugbounty-user-account-takeover-i-just-need-your-email-id-to-login-into-your-sho.md
title: '#BugBounty — “User Account Takeover-I just need your email id to login into
  your shopping portal account”'
category: documents
detected_topics:
- oauth
- otp
- idor
- access-control
- command-injection
- rate-limit
tags:
- imported
- documents
- oauth
- otp
- idor
- access-control
- command-injection
- rate-limit
language: en
raw_sha256: 1c136fb1933be767f6b13e8db439999d036dd7e1993cca99feeb3c80c37a0830
text_sha256: de50b2201612de5f9273c26e9757b53706182e10efe872442d6ba8ec1564a99c
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — “User Account Takeover-I just need your email id to login into your shopping portal account”

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-13_bugbounty-user-account-takeover-i-just-need-your-email-id-to-login-into-your-sho.md
- Source Type: markdown
- Detected Topics: oauth, otp, idor, access-control, command-injection, rate-limit
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `1c136fb1933be767f6b13e8db439999d036dd7e1993cca99feeb3c80c37a0830`
- Text SHA256: `de50b2201612de5f9273c26e9757b53706182e10efe872442d6ba8ec1564a99c`


## Content

---
title: "#BugBounty — “User Account Takeover-I just need your email id to login into your shopping portal account”"
page_title: "#BugBounty — “User Account Takeover-I just need your email id to login into your shopping portal account” | by Avinash Jain (@logicbomb) | Medium"
url: "https://medium.com/@logicbomb_1/bugbounty-user-account-takeover-i-just-need-your-email-id-to-login-into-your-shopping-portal-7fd4fdd6dd56"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["OAuth", "Authentication bypass", "Account takeover"]
publication_date: "2018-12-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5527
scraped_via: "browseros"
---

# #BugBounty — “User Account Takeover-I just need your email id to login into your shopping portal account”

#BugBounty — “User Account Takeover-I just need your email id to login into your shopping portal account”
Avinash Jain (@logicbomb)
Follow
3 min read
·
Dec 13, 2018

1K

2

Hi Guys,

A pending writeup about a very simple and yet critical vulnerability by which I was able to takeover any user account in a popular Online Shopping Portal. Let’s see what was the complete scenario —

The most crucial part in software development when it comes to security is the integration. Majority of security hack/loopholes happen mostly due to incorrect implementation while integrating third party services/modules with the application. Developers should not leave any misconfiguration open while implementing these services.

I went to the login section of the site and as every site has the option to “sign in with google/facebook” apart from usual “otp and password” login, it was also having the same functionality.

Login Page

I tried to login with google sign in and below is HTTP request for the same—

Press enter or click to view image in full size
Google Sigin with oauth2

Oauth2 signing authorization service is in use . Let’s see how it is implemented at the client side. Below is the HTTP request for the same —

Press enter or click to view image in full size
Login HTTP raw request

As can be seen in the above screenshot, there are 2 parameters which is being used for login verification the “accessToken” which is carrying google oauth2 sign in token and “login” parameter which is carrying user’s mail id.

Restating-Majority of security hack/loopholes happen mostly due to incorrect implementation while integrating third party services/modules with the application.

and the same happened here where oauth2 service was integrated but implementation comes out to be weak and vulnerable.

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I found that the code was just verifying either of the two things— “accessToken” provided by oauth2 or “login” the mail id of the user and where was the vulnerability present and so I replaced the “login” value with the mail id to one of my friend’s mail id who has his account in the site (which I could also get by user enumeration on the login page) and below is the response I got —

Press enter or click to view image in full size
Change the login value to victim’s mail id
Press enter or click to view image in full size
Login Successful

I was able to successfully login into my friend’s account and had access to his complete profile.

And this is how I could takeover any user’s account by just knowing the login mail id.

Report details-

10-July-2018 — Bug reported to the concerned company.

14-August-2018 — Bug was marked fixed.

14-August-2018— Re-tested and confirmed the fix.

05-October-2018 — Rewarded.

Thanks for reading!

~Logicbomb ( https://twitter.com/logicbomb_1 )
