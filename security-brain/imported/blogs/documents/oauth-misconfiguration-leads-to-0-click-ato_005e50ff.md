---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-04-02_oauth-misconfiguration-leads-to-0-click-ato.md
original_filename: 2024-04-02_oauth-misconfiguration-leads-to-0-click-ato.md
title: Oauth Misconfiguration Leads to 0-Click ATO
category: documents
detected_topics:
- oauth
- command-injection
tags:
- imported
- documents
- oauth
- command-injection
language: en
raw_sha256: 005e50ff00a3d95550f23f4974bceb542b01861e65196786d00e7b800e529467
text_sha256: 2399109e489cc4502c48c6f3f29394f1edc0a35143a0bc86cf807543f050f03a
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# Oauth Misconfiguration Leads to 0-Click ATO

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-04-02_oauth-misconfiguration-leads-to-0-click-ato.md
- Source Type: markdown
- Detected Topics: oauth, command-injection
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `005e50ff00a3d95550f23f4974bceb542b01861e65196786d00e7b800e529467`
- Text SHA256: `2399109e489cc4502c48c6f3f29394f1edc0a35143a0bc86cf807543f050f03a`


## Content

---
title: "Oauth Misconfiguration Leads to 0-Click ATO"
url: "https://medium.com/@mohamed0xmuslim/oauth-misconfiguration-leads-to-0-click-ato-b407fe05fdf4"
authors: ["Muhammad Mostafa (@0xSekiro)"]
bugs: ["Account takeover", "Authentication bypass", "OAuth"]
publication_date: "2024-04-02"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 356
scraped_via: "browseros"
---

# Oauth Misconfiguration Leads to 0-Click ATO

Oauth Misconfiguration Leads to 0-Click ATO
Muhammad_Mostafa
Follow
2 min read
·
Apr 2, 2024

671

5

بسم الله

Don’t forget to pray for people in GAZA ❤️

Hello everyone

Today I will talk about a bug i never faced before

So let’s get started

First of all I have a private hackerone program which is an online market place

When I open the main website I got the main page and a login/register functionality so I decided to create an account

The thing is the website allows user to create an account with Facebook so what will happen if I didn’t share the email address from my Facebook account with the program ?

Every time you sign up in program with Facebook there is a permission page that you agree to share

First name
Last name
Email
Profile page

So you will get a page like this👆🏻

(This is not the program it is just a picture from Google )

So now what we can do ?

1- Sign up with Oauth using Facebook and don’t share your email address with the website (with edit Access button on permission page)

Get Muhammad_Mostafa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2- Now you will be redirected to a Create account page which have fields

First name
Last name
Username
Email address (Which is empty) cause you didn’t share the email address

First name and second name is got from your Facebook account

User name you enter any unique user name

Email address now is an empty field cause and disabled (in normal case it should be the email address you shared from your Facebook account )

Now you can click on create account button and intercept the request

You will see this

First_name={your first name of Facebook}&Second_name={Your second name of facebook}&Username={Username you entered}&email=

If you enter an email which is not registered in the website it will ask you to verify email before continue

But what if I enter an already verified email address which is any user email who have created an account before and verified his email 🤔

When I did this I have logged in to victim account without any user interaction

Thanks for reading

X: https://twitter.com/0xSekiro

Linkedin: https://www.linkedin.com/in/muhammad-mostafa-36a01a226

#bugbounty

#bugbountytips

#bugbountytip

#cybersecurity
