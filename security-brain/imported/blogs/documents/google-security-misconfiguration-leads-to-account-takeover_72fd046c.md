---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-02-08_google-security-misconfiguration-leads-to-account-takeover-.md
original_filename: 2022-02-08_google-security-misconfiguration-leads-to-account-takeover-.md
title: Google Security Misconfiguration Leads to Account Takeover !
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: 72fd046c3e044f177d41f6234bd326d2122425eaa4e3047b9ffa6335db9816f4
text_sha256: f290831984e1052a2d46c4f95eaa107f7f6a9440f1c3555ae8fd6a51608336a2
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Google Security Misconfiguration Leads to Account Takeover !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-02-08_google-security-misconfiguration-leads-to-account-takeover-.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `72fd046c3e044f177d41f6234bd326d2122425eaa4e3047b9ffa6335db9816f4`
- Text SHA256: `f290831984e1052a2d46c4f95eaa107f7f6a9440f1c3555ae8fd6a51608336a2`


## Content

---
title: "Google Security Misconfiguration Leads to Account Takeover !"
url: "https://medium.com/@harshbanshpal/you-can-takeover-any-google-account-f6f2d012466f"
authors: ["Harsh Banshpal"]
programs: ["Google"]
bugs: ["Logic flaw", "Spoofing"]
publication_date: "2022-02-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2929
scraped_via: "browseros"
---

# Google Security Misconfiguration Leads to Account Takeover !

Google Security Misconfiguration Leads to Account Takeover !
Harsh Banshpal
Follow
3 min read
·
Feb 8, 2022

418

9

Thank you for taking the time to read about “ Google Security Misconfiguration Leads to Account Takeover ! "

Google

Hello Readers , I’m Harsh Banshpal [ @harsh_ban_ ] , hope you are doing great , this is about the Google Security Misconfiguration Leads to Account Takeover !

I know you are also a Hacker or CyberSecurity Enthusiast with some great skills.

As you know 90% of the bug bounty programs does not accept phishing or email issues, but what if the company will send you the mail? [ Not an Email Spoofing ]

As you know Google have it’s own platform for reporting vulnerabilities called bughunters.google.com , after submitting a bug you’ll receive a confirmation mail from- buganizer-system+Component-No+Issue-No@google.com

So, when we reply to the email thread it’ll automatically add comments to your report https://bughunters.google.com/profile/xyz/tracker/xyz & https://issuetracker.google.com/issues/xyz.

I hope you are still with me

Press enter or click to view image in full size
Testing Your Patience !

Here’s where the fun begins.

So, I started to think what if I send a mail to this unique email by using other mail, Will it add a comment to our report?

And in the next moment BOOM!!! I was wrong 🤣 the comment was not added [It’s Google Man!!!]

Then, after playing with the functionality I thought what if I send a mail to this unique email by any mail spoofing services like emkei.cz

And in the next moment BOOM!!! The comment was not added :O

But uncommonly received a mail from noreply-buganizer-system@google.com with my Subject & Body.

Then I was like

BOOM!!!

Then, without wasting a time I created

Format of mail

Subject -
Security Alert

Get Harsh Banshpal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Body -
Unfortunately, We have seen some suspicious activity on your account.
Kindly Signin to verify your account https://bit.ly/xyz (Attacker’s Phishing Website) .

Google Security Team

& send this mail to buganizer-system+Component-No+Issue-No@google.com from victims mail [ From emkei.cz ] & victim will receive a mail from noreply-buganizer-system@google.com with crafted Subject & Body which is an error email.

Bug Submitted — 10.01.2022

Bug Triaged — 11.01.2022

Bug Closed (Won’t Fix Intended Behaviour) — 18.01.2022

Reply from Google

So at the end it’s phishing, isn’t it?

Then I replied

Yeah it’s phising, but it’s not a general phising, attacker can phish the victim because Google’s mail server are not protected & misconfigured. Hope you will look into the issue and consider fixing it.

Reply from Google

Thanks, but we won’t be making a change here.

I was like

Why? Just Why?

Thanks to 
Saransh Saraf aka (MR23R0)
 for the help :)

This is only for education purpose .

PS:

Phishing Tool — https://github.com/Ignitetch/AdvPhishing

Video POC — https://youtu.be/nUx_mjyfA4E

You can connect with me on-

Linkedin: https://www.linkedin.com/in/harshbanshpal/

Instagram: https://www.instagram.com/harsh_ban_/

Twitter: https://twitter.com/harshbanshpal
