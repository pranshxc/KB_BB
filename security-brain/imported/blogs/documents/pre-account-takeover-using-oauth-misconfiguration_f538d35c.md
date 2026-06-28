---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-26_pre-account-takeover-using-oauth-misconfiguration.md
original_filename: 2020-11-26_pre-account-takeover-using-oauth-misconfiguration.md
title: Pre-Account Takeover using OAuth Misconfiguration
category: documents
detected_topics:
- oauth
- command-injection
- csrf
- api-security
tags:
- imported
- documents
- oauth
- command-injection
- csrf
- api-security
language: en
raw_sha256: f538d35c962a416a83d7bea35bdd92acd91349171c61a43479c08b9f650f1b4b
text_sha256: d4c1705ced3d94f87a7af01f29d1101600ad534b7d34ecff9a7468efe7e11bac
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Pre-Account Takeover using OAuth Misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-26_pre-account-takeover-using-oauth-misconfiguration.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, csrf, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `f538d35c962a416a83d7bea35bdd92acd91349171c61a43479c08b9f650f1b4b`
- Text SHA256: `d4c1705ced3d94f87a7af01f29d1101600ad534b7d34ecff9a7468efe7e11bac`


## Content

---
title: "Pre-Account Takeover using OAuth Misconfiguration"
url: "https://vijetareigns.medium.com/pre-account-takeover-using-oauth-misconfiguration-ebd32b80f3d3"
authors: ["the_unluck_guy (@7he_unlucky_guy)"]
bugs: ["OAuth"]
bounty: "800"
publication_date: "2020-11-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4106
scraped_via: "browseros"
---

# Pre-Account Takeover using OAuth Misconfiguration

Pre-Account Takeover using OAuth Misconfiguration
the_unlucky_guy
Follow
3 min read
·
Nov 26, 2020

496

3

Hello guys,

Today I am going to share one of my interesting findings on the private program of Bugcrowd. Since this is on a private program so I will be using target.com as the website name.

Let’s get started. Only 2 subdomains of the private program is in scope. I picked one of the subdomain a.target.com and there is a registration page to create a new account. There is an option that you can also signup using OAuth. So, I created one account using Google OAuth. After that, I explored the website a bit and look for functionality. I thought let’s try for some OAuth Misconfiguration related issues and testing for OAuth related bug is my favorite one. So I started looking for some OAuth Misconfig. I tried CSRF on linking/unlinking Google OAuth, unvalidated redirect after signup with OAuth, and some more known issues. There is a state parameter all over so csrf is not possible, I tried to bypass it but no luck.

I was thinking of what more can be done using OAuth. There is a change email functionality on the profile setting. So, I changed my OAuth email let’s say abc@gmail.com to def@gmail.com. It says if I change email, I am not able to login using Google OAuth.

I proceed with the Unlink option and the email changed successfully without verification of the new email. This time, I logged in again in my account using the email-password method. After a bit of thinking, I tried to log in using old Google OAuth(Already Unlinked) and I am successfully logged in to my old account. It’s like I Unlinked my login with Google OAuth but still able to log in using the OAuth method even after unlinking. So, here I got that there is Misconfiguration on OAuth. Since there is no verification of email after email change so I can use any other people’s email. To show an impact to the company there is an attack scenario :

Attacker creates an account on a.target.com using OAuth.
Attacker changed his/her email to victim email.
When the victim try to create an account on a.target.com, it says the email already exists. Now the victim will reset his/her password and logged in using email-password method.
Attacker also able to logged in the victim account using OAuth.

That’s all about the bug.

Get the_unlucky_guy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This bug is not having so much severity but still, some companies paid well.

Some companies paid nothing.

I hope you learned something new from this blog. I will write more of my findings soon so, stay tuned for my next write-up.

Twitter: 7he_unlucky_guy
