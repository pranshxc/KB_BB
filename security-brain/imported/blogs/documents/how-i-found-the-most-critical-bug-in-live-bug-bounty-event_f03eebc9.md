---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-24_how-i-found-the-most-critical-bug-in-live-bug-bounty-event.md
original_filename: 2019-07-24_how-i-found-the-most-critical-bug-in-live-bug-bounty-event.md
title: How I found the most critical bug in live bug bounty event?
category: documents
detected_topics:
- xss
- sqli
- command-injection
- password-reset
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- sqli
- command-injection
- password-reset
- automation-abuse
- api-security
language: en
raw_sha256: f03eebc920326ef24756c2e6ca0276331f89c725b4844f94ddc4ffec2d6229e8
text_sha256: a62c4c2ba43df2427a929cac8b67a50c7c3bf174db6549f06c8d3d5e544c6f88
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How I found the most critical bug in live bug bounty event?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-24_how-i-found-the-most-critical-bug-in-live-bug-bounty-event.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, password-reset, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `f03eebc920326ef24756c2e6ca0276331f89c725b4844f94ddc4ffec2d6229e8`
- Text SHA256: `a62c4c2ba43df2427a929cac8b67a50c7c3bf174db6549f06c8d3d5e544c6f88`


## Content

---
title: "How I found the most critical bug in live bug bounty event?"
url: "https://medium.com/@innocenthacker/how-i-found-the-most-critical-bug-in-live-bug-bounty-event-7a88b3aa97b3"
authors: ["Lakshay (@inn0c3ntd3v1L)"]
bugs: ["Password reset", "Account takeover"]
publication_date: "2019-07-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5124
scraped_via: "browseros"
---

# How I found the most critical bug in live bug bounty event?

How I found the most critical bug in live bug bounty event?
Lakshay
Follow
3 min read
·
Jul 24, 2019

873

3

Hey Folks! Hope you guys are doing great.

Recently I attended Bounty-Bash (live bug bounty event of 2 days) held in Kathmandu, Nepal.

I went to the event and met so many bug-bounty hunters there and most of them were famous ones, so I was not expecting much out of myself 😐 but I did not lose hope and then the event started, all were provided with 3 web application targets.

And the thing noteworthy was that all were single scope targets, with no subdomains at all and all were testing environments not the main applications.

So I started hunting for XSS,SQL Injection and few other OWASP top 10 vulnerabilities, but I did not find anything interesting over there. Hence, I decided to test the password reset functionality of the web-application provided i.e “Having trouble signing in?”. I just clicked on it and it redirected me to Reset Password page.

I entered my username and clicked on proceed.

Press enter or click to view image in full size

After Proceeding I faced few security questions to answer and was not having any idea about the same :/ as the event manager provided us the username and password hence the create account functionality was disabled.

So I entered something randomly and captured the request of “OK” in my interceptor tool, now I have to see what response it is showing of my request so I intercepted the response as well and it was showing :

HTTP/1.1 401 Unauthorized

(“message”:”unsuccessful”,”statusCode:403,”errorDescription”:”Unsuccessful”)

I just played with the response and manipulated to :

HTTP/1.1 200 OK

(“message”:”success”,”statusCode:200,”errorDescription”:”Success”)

Get Lakshay’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

For better clarification, you can see the screenshot given below:

Press enter or click to view image in full size
Successfully manipulated the response and forwarded :)

Now I went back to my browser and saw that I had successfully bypassed it.

successfully bypassed it, now asking for password delivery type.

I have selected SMS and Email Functionality and again intercepted the request while clicking on proceed.

and I saw the request yeahhh!! and surprisingly I got the request with new password and confirm password, I entered “hacker” in both the fields.

Press enter or click to view image in full size
I just entered “hacker” in new password and confirm password fields.

as usual,forward the request and went back to browser.

Yippie…password has been changed successfully.

Yeahh!! :D Finally the password has been changed :)

So this vulnerability leads to full account takeover of any user without knowing the security answers.

As I was busy in hunting more vulnerabilities so my report was late and it was declared duplicate bug, so one lucky guy got away with it before me and won the most critical bug award.

But the company awarded me with the bounty :) as the bug was critical.

If you enjoyed it please do clap ! Keep Hunting !!

Follow Me on :

Twitter : https://twitter.com/inn0c3ntd3v1l

Linkedin : https://www.linkedin.com/in/inn0c3ntd3v1l
