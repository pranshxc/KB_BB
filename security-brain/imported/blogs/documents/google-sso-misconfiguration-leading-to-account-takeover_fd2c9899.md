---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-14_google-sso-misconfiguration-leading-to-account-takeover.md
original_filename: 2022-10-14_google-sso-misconfiguration-leading-to-account-takeover.md
title: Google SSO misconfiguration leading to Account Takeover
category: documents
detected_topics:
- sso
- command-injection
tags:
- imported
- documents
- sso
- command-injection
language: en
raw_sha256: fd2c98992a92e8d54c214f73f91b88c68322555beb3f2a7f5b4ab55c037f9db9
text_sha256: 0279703d2d08dc491fb1a1f7e38083fdcc29a3484f56a939d649eded9c7b728a
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Google SSO misconfiguration leading to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-14_google-sso-misconfiguration-leading-to-account-takeover.md
- Source Type: markdown
- Detected Topics: sso, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `fd2c98992a92e8d54c214f73f91b88c68322555beb3f2a7f5b4ab55c037f9db9`
- Text SHA256: `0279703d2d08dc491fb1a1f7e38083fdcc29a3484f56a939d649eded9c7b728a`


## Content

---
title: "Google SSO misconfiguration leading to Account Takeover"
url: "https://0x4kd.medium.com/google-sso-misconfiguration-leading-to-account-takeover-cf9bcf63e76e"
authors: ["0x4KD (@0x4kd)"]
bugs: ["Authentication bypass", "Account takeover", "SSO"]
publication_date: "2022-10-14"
added_date: "2022-10-17"
source: "pentester.land/writeups.json"
original_index: 2039
scraped_via: "browseros"
---

# Google SSO misconfiguration leading to Account Takeover

Google SSO misconfiguration leading to Account Takeover
0x4KD
Follow
4 min read
·
Oct 14, 2022

67

1

I’m a technical guy. However, this post doesn’t contain any technical details (but that’s because this bug doesn’t require any).
I need to admit it: finding this bug was pure luck.
No skill was involved at all.

Press enter or click to view image in full size
Account Takeover representation by Dall-E
Some context…

A couple of weeks ago, a client for whom I worked last year called me because he needed some help describing the service we developed for him. He was going to sell the company and was being asked for the technical details.

There was an explicit requirement that would have forced me to examine all the code and search for specific information, but I was feeling too lazy to do that. So I thought about my options:

Either I spend the next two hours examining every line of code…
Or I can search for an online tool that does the job for me! 🎉

We all know how this ends. You end up wasting your time looking for a service and getting nothing done. I could have spent my time doing it manually.

Lucky me, I tried searching for a tool instead.

Discovering the bug

I remembered I used a webpage about 3 years ago that had a similar feature, so I decided to investigate.

Once I logged in, I was expecting to find my previous projects, but they were all missing. Instead, many “random” GitHub repositories were attached to my account. They were from a big, known company… And they were not Open Source, I can tell you that. 😝

Why do I never get permission for publishing the name of these companies?
It doesn’t matter how do I argue with them, they’ll always want to keep it secret.
…
I guess that’s why I work in computer science and not in politics.
Zero persuassion techniques😅

Suddenly, I realized that that was not my account. I went to the settings page and saw a different email. I didn’t even know how did I manage to log in to their account.

“Let’s try to do it again”, my mind said. Open a new Chrome profile, go to the webpage, log in using Google… Again. I’m in their account.

That’s when I decided to use a different Google account.
Maybe — I thought — using a different email address leads me to a different account. And I was right.

Get 0x4KD’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But then… Pattern detected?

The first letter of my email was matching the first letter of the app account.

Coincidence? Not sure, yet. Let’s use multiple emails:

n*******@domain.com (Google email) => n*******@whatever.com (App)
e*******@domain.com (Google email) => e*******@whatever.com (App)
a*******@domain.com (Google email) => a*******@whatever.com (App)
z*******@domain.com (Google email) => z*******@whatever.com (App)

So yeah, I had discovered a way to access, at least, 35 accounts (a-z0–9).

Understanding the issue

Eventually, while trying different emails, I ended up in the account I was expecting to access in the first place: The account with my projects. That’s when I realized what the problem was: I tried to log in with an email that wasn’t registered on the website. I was signing in when I should have registered first.

FFS, that’s not the account I used for my projects. I had them stored into a different, specific account that I created using Google Suite.
Should I have gone to the register page instead of using the login popup?

So I went to the register page, used one of the previous emails (one that I knew didn’t exist but had led me to an account that was not mine), and registered successfully. I logged out, and when I logged in… I was inside the correct account.

Conclusions

The developers assumed that if a user was using the login popup, the user must have been present in the database. This led to grabbing a database entry no matter if there was an exact match.
“Signing Up” and “Signing In” using SSO should have the same auth flow, and the backend should have decided whether to add a new user into the database or grab an existing one if the data matched!

So, what do you do, in these situations?

This is not a bug bounty program, and you didn’t have access to pentest the application in the first place. Are you in trouble?
Well, you might be, but that’s not what usually happens.

I searched for the support email and sent them the details: not asking for a bounty, with reproducible steps, and an apology for running several tests to understand the issue.

They answered quite fast, confirming that the issue was fixed and granting me some credit inside the application.

It’s not a monetary bounty, but I’m happy anyway. — I thought.

The bad news is that the application couldn’t get my problem fixed. But hey, in the end, someone ended up paying for the two hours that it took me to do the job manually 😉
