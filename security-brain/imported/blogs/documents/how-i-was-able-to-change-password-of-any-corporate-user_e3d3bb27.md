---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-09_how-i-was-able-to-change-password-of-any-corporate-user.md
original_filename: 2023-04-09_how-i-was-able-to-change-password-of-any-corporate-user.md
title: How I was able to change password of any corporate user
category: documents
detected_topics:
- command-injection
- password-reset
- otp
- rate-limit
- csrf
tags:
- imported
- documents
- command-injection
- password-reset
- otp
- rate-limit
- csrf
language: en
raw_sha256: e3d3bb27d192ff7573b8a64f88d9519a0d8b6239df3fbf9b9fce8b0569e82100
text_sha256: fb7229a8e01ba32c2b55fef21abe91f42b30dde472289f112aaea84ddcfad514
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to change password of any corporate user

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-09_how-i-was-able-to-change-password-of-any-corporate-user.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, otp, rate-limit, csrf
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `e3d3bb27d192ff7573b8a64f88d9519a0d8b6239df3fbf9b9fce8b0569e82100`
- Text SHA256: `fb7229a8e01ba32c2b55fef21abe91f42b30dde472289f112aaea84ddcfad514`


## Content

---
title: "How I was able to change password of any corporate user"
url: "https://medium.com/@ch3tanbug/how-i-was-able-to-change-password-of-any-corporate-user-c68b9509840"
authors: ["CH3TAN"]
bugs: ["Account takeover", "Password reset", "Authentication bypass"]
publication_date: "2023-04-09"
added_date: "2023-04-24"
source: "pentester.land/writeups.json"
original_index: 1285
scraped_via: "browseros"
---

# How I was able to change password of any corporate user

How I was able to change password of any corporate user
CH3TAN
Follow
3 min read
·
Apr 9, 2023

180

1

Introduction

H
ey guys before we start i want to give you all a little introduction about myself. My name is Chetan kashyap and I am a bug-bounty hunter from India. This is my first time writing an article about my findings. But we all have to start at some point of time, so i guess i will start writing articles more often on my findings.

The Story

So this week as i was having 2–3 holidays from my college i decided to drop my assignments and try to hunt on a program from a good platform. I chose a program from Yeswehack. The program had a fairly large scope with 5–6 web applications in scope. I created a text file and stored all the in-scope target urls and fed it to my custom recon script which i call as subdig. I got a lot of live subdomains but half of them were login panels of the same type and after like investing 1–2hour on them i was unable to bypass them or get any type of juicy files/directories on those urls.

So then I decided to jump on the main application itself. I chose the first in-scope web-application of the program to begin my testing, let’s call it as usual redacted.com. The target was basically just like an e-commerce website where you could purchase things or gift things to someone. I tried all basic vulnerabilities like OTP bypass, No-rate limit on OTP , CSRF etc. After I was all exhausted i decided to move to the next in-scope web-application but then one thing on the target caught my eye. There was a small button that said corporate user login. I clicked that button and it redirected me to https://corporate.redacted.com/corporate/login. There I was greeted with an option to enter username and password. As i was not having any username i went back to my recon. This time i went to Github and used a simple dork “redacted.com” username and after looking at some code i was able to get an username. I did this because default it was not accepting any usernames like admin, test etc. Later after finding username on Github I found that username must be in form of user@xyz.com

I went on the target again and entered that username and entered any random password like userpassword. I intercepted that request in burp it was something like this.

Press enter or click to view image in full size
Get CH3TAN’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I changed the &isPasswordToBeChanged=false parameter to &isPasswordToBeChanged=true and BOOM! I was greeted with a page to enter my new password and confirm it.

I entered a new password but after hitting confirm it was showing an error that said some error occurred please contact the administrator. So i again entered the password and this time intercepted the response to this request in Burpsuite and changed the response key in the response from 3 to 1. And guess what the page said password changed. Now i was able to perform an ATO of any corporate user i just needed their username.

Conclusion

At
the end i would say that sometimes rather than gathering more and more assets to test on try to focus on a single asset and invest your time on that, you may find something fruity. Also take breaks and keep hustling. Do consider giving a clap if you like my write up it will motivate me to write more. See you next time until then BYE!
