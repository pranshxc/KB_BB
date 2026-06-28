---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-10_how-i-was-able-to-regain-access-to-account-deleted-by-admin-leading-to-.md
original_filename: 2021-01-10_how-i-was-able-to-regain-access-to-account-deleted-by-admin-leading-to-.md
title: How I was able to Regain access to account deleted by Admin leading to $$$
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
language: en
raw_sha256: eeafdd4c4b730d9e2fca93f5f5c08ed5f7b23c70e55dd20ac9292e3905cebe49
text_sha256: 0df78b8bbdbbd6e20f664289c78f1ea89e0cc8d34084c7af25a2599ae0523fb8
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to Regain access to account deleted by Admin leading to $$$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-10_how-i-was-able-to-regain-access-to-account-deleted-by-admin-leading-to-.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `eeafdd4c4b730d9e2fca93f5f5c08ed5f7b23c70e55dd20ac9292e3905cebe49`
- Text SHA256: `0df78b8bbdbbd6e20f664289c78f1ea89e0cc8d34084c7af25a2599ae0523fb8`


## Content

---
title: "How I was able to Regain access to account deleted by Admin leading to $$$"
url: "https://rajeshranjan457.medium.com/how-i-was-able-to-regain-access-to-account-deleted-by-admin-leading-to-a2c29025f8cd"
authors: ["Rajesh Ranjan (@_rajesh_ranjan_)"]
bugs: ["Logic flaw", "Broken authorization"]
publication_date: "2021-01-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4012
scraped_via: "browseros"
---

# How I was able to Regain access to account deleted by Admin leading to $$$

How I was able to Regain access to account deleted by Admin leading to $$$
Rajesh Ranjan
Follow
3 min read
·
Jan 10, 2021

508

2

Hello hackers, I hope you are doing well. Today I’m gonna explain about one of my finding, in which how I was able to access the account that was deleted by Admin. As this was Bugcrowd private program, so I’ll assume it as example.com

So this application has lots of functionalities. There was an option to invite users, and the endpoint was example.com/dashboard/setup/user-accounts. So I thought to give it a shot. Quickly, I sent an invitation to my email address which was rajesh_ranjan+invite1@bugcrowdninja.com, and got the following response, as you can see, it was 201 created

Press enter or click to view image in full size

So quickly, I head over to my email Inbox and accepted the invitation > created the username and password, and then visited example.com/dashboard/login, and entered the credentials. So following request and the response was generated

Press enter or click to view image in full size

Now I copied that response and pasted it to sublime :D. Again I went to the admin dashboard and deleted the user access from the application

Press enter or click to view image in full size

This time, headed to example.com/dashboard/login and tried to login with the same old credentials, and as expected I got the Login failed error

so, I thought, what else we can do now

So, I turned on the Intercept and captured the login Request > Intercepted the response

and modified the response from

To

and then forwarded the request, and to my surprise, I was logged in with that account :P. I quickly reported this to the program, and with a week, I was rewarded $$$ for this submission.

Note: You might be confused about, from where this response came from. So when we accept the invite > create a password and then head over to example.com/dashboard/login > Enter your credentials. at this step, this valid response was generated

Steps to reproduce

Admin side

Go to example.com/dashboard/setup/user-accounts, and enter the user email to send the invitation

User side

check inbox, open the invitation link, and then set the password for your account
now try to login on to example.com/dashboard with the credentials you set in step 1
Now copy the response, and keep it on Notepad

Admin side

comeback to admin side, and delete that invited user

user side

try to login again with the credentials, you’ll get login failed error
intercept the response, and modify it with the earlier one (a valid one), and you’ll be logged in successfully

Timeline:

Get Rajesh Ranjan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Reported: 07 Nov 2020

Triaged: 09 Nov 2020

Bounty Received: 14 Nov 2020

Connect me on Twitter https://twitter.com/_rajesh_ranjan_
