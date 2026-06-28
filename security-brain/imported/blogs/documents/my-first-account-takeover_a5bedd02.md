---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-09_my-first-account-takeover_2.md
original_filename: 2022-11-09_my-first-account-takeover_2.md
title: My First Account Takeover
category: documents
detected_topics:
- idor
- automation-abuse
- xss
- sqli
- command-injection
- otp
tags:
- imported
- documents
- idor
- automation-abuse
- xss
- sqli
- command-injection
- otp
language: en
raw_sha256: a5bedd02cd03fc691cb412a6fb4cb5aa3d24261e4ab2dae4e7919ab66752fb44
text_sha256: a393f3521545c0f96f908163ea709d5b911f656610bf4109c2a1c9fa4c5ab2a7
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# My First Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-09_my-first-account-takeover_2.md
- Source Type: markdown
- Detected Topics: idor, automation-abuse, xss, sqli, command-injection, otp
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `a5bedd02cd03fc691cb412a6fb4cb5aa3d24261e4ab2dae4e7919ab66752fb44`
- Text SHA256: `a393f3521545c0f96f908163ea709d5b911f656610bf4109c2a1c9fa4c5ab2a7`


## Content

---
title: "My First Account Takeover"
page_title: "MY FIRST ACCOUNT TAKEOVER. Heyyyy buddies, | by JAI NIRESH J | Medium"
url: "https://medium.com/@nireshpandian19/my-first-account-takeover-fd5570f09c0a"
authors: ["JAI NIRESH J"]
bugs: ["Account takeover", "Logic flaw"]
publication_date: "2022-11-09"
added_date: "2022-11-14"
source: "pentester.land/writeups.json"
original_index: 1935
scraped_via: "browseros"
---

# My First Account Takeover

MY FIRST ACCOUNT TAKEOVER
JAI NIRESH J
Follow
3 min read
·
Nov 9, 2022

118

1

Heyyyy buddies,

Back with another juicy writeup. This time a Big one .. Yea the famous Account Take Over aka ATO.

Let’s cut out to the actual task.

As usual i was google dorking for programs to hunt on, and i had selected a few based on the scope and bounty. Later i picked one and started to hunt there !

Note : I reported this bug just yesterday, and they haven’t patched it yet ! Therefore let me call the site as “Magma.com” (in case you are wondering what is with the term “Magma”, that is my alias hacker name i used to go with 😅)

I was surfing through the web application for XSS and SQLI using my Burp Suite. I found some juicy responses when checking for responses, but sadly i could not find a way to escalate them to actual XSS.

I spent around some 3–4 days surfing the website and i could get only a couple of P4 s. I was literally exhausted !

Then i went back to the small automation tool that i had done for subdomain enumeration, and i ran them in the background.

When it was completed, it was very raw !!!! No juicee !!!

I did a lot of subdomain enumeration and guess what there were only around 4 subdomains active and i even tested for takeovers on the rest, but no luck.

The real fun came when i opened a subdomain called

staging.Magma.com

It was the exact replicate of the original website used for staging. I have come across a lot of subdomains with this staging in front of them like the one here now, but was not sure of their purpose.

May be they were used to work the same way the original website did but for testers and Developers.

I tried all those techniques that i tried in the main website www.Magma.com in this website too (staging.Magma.com).

Only then i saw this in their page

OUT OF SCOPE :

Vulnerabilities on sites hosted by third parties unless they lead to a vulnerability on the main website.

I then stopped checking for bugs there like XSS, SQLI, and IDORS on the staging.Magma.com as it is of no use.

ACCOUNT TAKING OVER PART :

Since the

staging.Magma.com

was an exact replicate of

www.Magma.com

it also had a signup/login page.

Get JAI NIRESH J’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The sign up process goes like :

An user enters his email
If the email already exists it asks for the password to login
If not, the user is required to enter his phone number and verify an OTP to create an account and log in.

SO basically, you require an email and a phone number to create an account. I had already created an account on the main website www.Magma.com

Therefore i tried to login with my same account on the “staging.Magma.com” too ! and i entered my email.

Guess what !?

It showed a signup page instead of a login form, as if the email has not been registered in their Database.

My sunken heart, looked a bit up for a moment !

Finally i understood that the database storing the email and the phone numbers in the login page is different for both the sites (staging and www).

Therefore i gave my existing email on the “staging.Magma.com” and as i told i was prompted with a sign up form, and now for the phone number i did not use the same number as i did on the main site.

Instead, i gave my Mom’s phone number and i was again prompted to enter an OTP to verify the phone number and when i did !

I WAS LOGGED INTO MY OLD ACCOUNT !!! that i created on the main website.

It took me a few seconds to figure out, what is happening here !
The registration or Sign in page of both the websites were different, but once we are past that, the account Database is not seperate, the staging.com’s email and phone number logs you into the main website’s account.

Bascially, an attacker if he knows the victim’s email, he navigates to the

staging.Magma.com/login-signup

and enteres the victim’s email and enters attacker’s phone number to verify the OTP and he is logged into the VICTIM’s account actually.

BOOM ! MY FIRST ACCOUNT TAKEOVER

Hope you liked it !

Keep hunting and learning ❤️
