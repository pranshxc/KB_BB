---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-03_p5-to-p1-interesting-account-takeover.md
original_filename: 2022-01-03_p5-to-p1-interesting-account-takeover.md
title: 'P5 to P1: Interesting Account Takeover'
category: documents
detected_topics:
- xss
- password-reset
- command-injection
- otp
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- password-reset
- command-injection
- otp
- automation-abuse
- api-security
language: en
raw_sha256: 50e9f7bb4c3fe429a1df90992e2aee32c00bade0f52a11acb49524c8e47fe521
text_sha256: 85eb697821462a62ce713f6fd4761390a45e86c798166875cb6260a37c92461f
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# P5 to P1: Interesting Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-03_p5-to-p1-interesting-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, password-reset, command-injection, otp, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `50e9f7bb4c3fe429a1df90992e2aee32c00bade0f52a11acb49524c8e47fe521`
- Text SHA256: `85eb697821462a62ce713f6fd4761390a45e86c798166875cb6260a37c92461f`


## Content

---
title: "P5 to P1: Interesting Account Takeover"
url: "https://medium.com/@tushar.tilak.sharma/p5-to-p1-intresting-account-takeover-6e59b879494b"
authors: ["Tushar Sharma (@tusharSharma_0)"]
bugs: ["Account takeover", "Session expiration issue", "Password reset"]
bounty: "1,000"
publication_date: "2022-01-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3034
scraped_via: "browseros"
---

# P5 to P1: Interesting Account Takeover

P5 to P1: Interesting Account Takeover
Tushar Sharma
Follow
3 min read
·
Jan 3, 2022

666

11

Hello Guys,

This is my second write-up. You can check out my first writeup which is on Account Takeover through Stored XSS.

So let go,

I was recently hunting on private RDPs which I find through making my own google dorks. You can find them here: https://github.com/tushar-arch/Bug-Bounty-Dorks/blob/main/Bug-Bounty-Dorks.txt

I found a program that was launched only a few days ago. And I started subdomain enum and fired nuclei in the background while I go through the target manually.

I want you guys to please look into this vulnerability. i.e: Token does not invalidate after email change which is p5 according to BugcrowdVRT

Press enter or click to view image in full size

We will get back to this in a while….

So, I quickly signed up on the application and went through every functionality. After getting an idea of the application flow. I prepared myself to test the main app. I quickly fired up the Burp in the background and the first thing I tested was the signup functionality.

I tried duplicate sign-up and Rate-limits but couldn’t find anything. Then I remember one case which was highlighted by: https://twitter.com/Virdoex_hunter on his POC.

So I Sign up with an email: abc.ishack@gmail.com. Again I tried to sign up with the email: abcis.hack@gmail.com[ Mind the place of [.] ]. And I was able to sign up with the 2 accounts.

The application should not allow these because if your email is something@gmail.com, you own all dotted versions of your address: some.thing@gmail.com. And nobody can register an account on Gmail with the dotted version of your email. So the application should have not allowed me to do it. But unfortunately, it did.

So after making 2 accounts when I tried to request the password token for abcis.hack@gmail.com, it goes to the inbox of abc.ishack@gmail.com also when I tried to change the password, due to some backend logic the password for both the accounts gets changed.

I could have reported it as it is but the impact is quite low and I don’t have any attacking scenario to show the impact to the security team. So I kept searching and thinking of an attacking scenario.

After some time the email change functionality got my eye. So, you know I what I am gonna do ?

I signed up with a temporary email and requested a password reset. Now I changed the email. But the password reset token which is sent on the temporary email can still be used to change the password.

Get Tushar Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It's a p5 according to the Bugcrowd VRT, but here it's not

Now things are getting interesting!!!!

So I made the attacking scenario Step by Step:

I sign up with any email.
I request a password reset token to the email.
Login and change the email to the victim's email. ie: victim.ishacked@gmail.com [ Given that victim has an account with victimishacked@gmail.com] as the application allows us to make the account with dotted versions.
Now Go to the email inbox of the previous email and try to change the password.
When I Changed the password. It got successfully changed and when I tried to log in to[ victimishacked@gmail.com] with the new password. I was able to log in.

What happened here is: When I changed the email to victim.ishack@gmail.com[which the application allowed me even if the victimisack@gmail.com is already registered] the password token got chained to both the accounts.

I quickly made a good report with the Video POC and reported it. And after a few days, it got triaged and fixed. I was awarded $$$$.

Thanks for reading this and please ignore any mistakes.

Timeline :

01 November, 2021 — Reported

09 November, 2021 — Triaged

11 November 2021 — Fixed and Bounty Awarded $ 1000

Follow me on : Twitter: https://twitter.com/tusharSharma_0

Linkedin: https://www.linkedin.com/in/tushar-sharma-8557a716b/
