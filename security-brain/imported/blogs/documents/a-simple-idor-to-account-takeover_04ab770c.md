---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-11_a-simple-idor-to-account-takeover.md
original_filename: 2020-02-11_a-simple-idor-to-account-takeover.md
title: A Simple IDOR to Account Takeover
category: documents
detected_topics:
- idor
- access-control
- command-injection
- password-reset
- otp
tags:
- imported
- documents
- idor
- access-control
- command-injection
- password-reset
- otp
language: en
raw_sha256: 04ab770ca73febf8a8714eaf75a714652f512df6731f5a0a9885be61dbc1372b
text_sha256: 0144f55dede04f7c6cd777983c15e60e841b44f0fedfd6c40e7a13ca711fc2e6
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# A Simple IDOR to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-11_a-simple-idor-to-account-takeover.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, password-reset, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `04ab770ca73febf8a8714eaf75a714652f512df6731f5a0a9885be61dbc1372b`
- Text SHA256: `0144f55dede04f7c6cd777983c15e60e841b44f0fedfd6c40e7a13ca711fc2e6`


## Content

---
title: "A Simple IDOR to Account Takeover"
url: "https://medium.com/@swapmaurya20/a-simple-idor-to-account-takeover-88b8a1d2ec24"
authors: ["Swapnil Maurya (@swapmaurya20)"]
bugs: ["IDOR", "Account takeover"]
bounty: "4,500"
publication_date: "2020-02-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4775
scraped_via: "browseros"
---

# A Simple IDOR to Account Takeover

A Simple IDOR to Account Takeover
Swapmaurya
Follow
3 min read
·
Feb 11, 2020

1.4K

5

1

Getting Started with IDOR, What is IDOR?

Press enter or click to view image in full size
image source: https://avatao.com/

IDOR refers to Insecure Direct Object Reference which means you get access to something which is not intended to be accessible to you, or you don’t have the right privileges to execute that action on the web application. Technically it’s an access control issue that occurs when an application uses user-supplied input to access objects directly without any validation check to see if the request is made from its intended user or not. IDOR can be further related to Horizontal[exploiting application user pool] and Vertical[exploiting admin user] Privilege Escalation.

image source: https://www.business2community.com/

So assuming the program name to be example.com since it was a private program. Initially I wasn’t able to find any issue on the main domain and later gave up after getting 3 duplicates since it was a 3 years old Private program and I got the invite around October 2019.

Later in 2020 new year with a new vibe I blindly started searching for Vulnerabilities on the same program with a proper approach and Methodology, I took a glance over the program scope and saw that there where few subdomains which got my attention since it was having no known Vulnerabilities so I thought it is a good chance for me to break it down.

Within two Hours I got 4 Vulnerabilities in which Account Takeover was one of them. Lets see how was the approach in discovering it, So first I tested the login page , Registration page and the Forgot password page. While testing for the forgot password I saw that when the user changes the password to a new password the Email parameter was present in the Request body along with the new password and confirm new password parameter, So I thought why not change the email to someone else’s email id and finally when I did the same it gave me a full account access to the altered emails account.

Original Request:-

POST /login/internalResetPasswordSubmit?Toketoken=random_char&m=1234&nid=random_char HTTP/1.1
Host: subdomain.example.com
Cookie: all_required_cookies
{"email":"attacker_account@test.com","password":"new_passwd","confirmPassword":"new_passwd"}

Edited Request:-

POST /login/internalResetPasswordSubmit?Toketoken=random_char&m=1234&nid=random_char HTTP/1.1
Host: subdomain.example.com
Cookie: all_required_cookies
{"email":"victim_account@test.com","password":"new_passwd","confirmPassword":"new_passwd"}

So after forwarding the Edited Request in Burp the password will get changed for the victims account and it will directly log you into the Victims Account in the Browser.

Get Swapmaurya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Impact can be increased by changing the admins Account Password thus getting full access to admin account.

I Reported this at 12:30 am IST on 28th January

Got response from the team in the morning saying not able to replicate and asked me to takeover the test account created by them. So I wanted to reply them as soon as possible but when I received the comments on my report I was in college so I decided to reproduce the issue in our college lab, For that I somehow managed to setup the tools and pre-requisites in our college computer and when everything was ready I finally reproduced the same and changed the password of the test account created by the Bugcrowd Team and edited the profile with my username for proof of concept and sent the report.

Within 5 mins the report got Triaged and the priority was set to P1

Press enter or click to view image in full size

And the next day the company allotted the Bounty for my submission which can be seen in the above Screenshot.

So that’s it for now and Thanks for Reading and I hope you liked this content, will meet you in next upcoming blog post with a new Learning and Experience!!!

If you would like to know more about me refer this website

Swapnil Maurya
B.E in Computer Science and Engineering with focus on Security, actively contributing from past 2+ years through…

swapmaurya.in
