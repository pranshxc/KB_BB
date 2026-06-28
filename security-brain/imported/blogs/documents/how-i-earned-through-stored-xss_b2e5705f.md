---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-16_how-i-earned-through-stored-xss.md
original_filename: 2021-04-16_how-i-earned-through-stored-xss.md
title: How I earned $$$$ through Stored XSS
category: documents
detected_topics:
- xss
- idor
- access-control
- command-injection
- otp
- csrf
tags:
- imported
- documents
- xss
- idor
- access-control
- command-injection
- otp
- csrf
language: en
raw_sha256: b2e5705f84bcd33196c29971d23b3bc508a8e79e6d42c73cdf45062c2caeae92
text_sha256: c235538fd764e58f41875067488bbb8bfb43e5170af1778de3c7b2136b945690
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: true
---

# How I earned $$$$ through Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-16_how-i-earned-through-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, idor, access-control, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: True
- Raw SHA256: `b2e5705f84bcd33196c29971d23b3bc508a8e79e6d42c73cdf45062c2caeae92`
- Text SHA256: `c235538fd764e58f41875067488bbb8bfb43e5170af1778de3c7b2136b945690`


## Content

---
title: "How I earned $$$$ through Stored XSS"
url: "https://pharish4948.medium.com/how-i-earned-3200-in-4hours-through-stored-xss-38597877d3e1"
authors: ["Harish"]
bugs: ["Stored XSS", "CSTI"]
bounty: "3,205"
publication_date: "2021-04-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3737
scraped_via: "browseros"
---

# How I earned $$$$ through Stored XSS

How I earned $$$$ through Stored XSS
Harish
Follow
4 min read
·
Apr 15, 2021

764

2

Introduction:

The article is about a bug on a private program which I found. The bug reported was a stored xss through AngularJS CSTI. I’ll be sharing my mindset and what I experienced when found this vulnerability.(Might not be for experts, I’m a beginner so please leave your suggestions in comment and Sorry for the bounty bait it’s $800 for each endpoint)

Mindset:

So I was hunting on this application built with different technologies and many user roles.

Different User Roles — Check
Many functionalities — Check
Many Technologies used— Check

It ticked my checks for a perfect application a Pentester/Bug bounty hunter would love to test on.

Tip: When testing a application, go as deep as possible i.e test every button, every functionality and every single thing that is accessible.

U29ycnkgZm9yIHRoZSBib3VudHkgYmFpdCwgSSdtIGRvaW5nIGl0IHRvIGdldCBhIGdvb2QgcGF5***REDACTED-SUSPECT-TOKEN***I tried enumerating all the functionalities that the application has first and got a basic idea of how it works , what it does and what each user role is supposed to have access to.(This is really important)

Then I just tried checking IDOR/Access controls through Autorize(I’m really grateful to the people who built it) but couldn’t find any.

So I just went ahead and started testing for XSS. I tried testing all the inputs available for CSTI payload {{7*7}} since it’s AngularJS.

Strangely, When I first tested for it, I didn’t reflect as intended(49). After more testing, I found that the application has different parts and some parts weren’t based on AngularJS 1.5.9(remember the diff technologies I mentioned).

There was a search field which triggered the payload and got the result as 49. I was like

There was a problem though, the search was through post request so not a get parameter to edit.I thought of doing a POST based reflected xss too but there was a CSRF token so tried CSRF bypasses but didn’t work.

Get Harish’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was like what am I supposed to do now. Then I started finding inputs that were stored. I started first collecting all the places where I could store and started testing them out. I was like “I’ll have to give my 100%”

BTW, this was on a private program .And sorry that I can’t share any screenshots since it’s all private.

Getting back, the places where it stored didn’t reflect at first but after few steps(like second order ,input gets stored in one place and gets triggered in other). I was like hmm…Nice!. I edited the payload

{constructor.constructor(alert(1)}

to alert the cookie value and though it did have secure and httponly cookie. It had a duplicate of all these cookies without the flags set.

TIP: When you find a vulnerability in one endpoint try to find the same in all others endpoints too.

I found 5 places where it got triggered and reported all the endpoints for maximum coverage.

And I just didn’t wait for the qr to end to see other submission. Just went to sleep since it was too late already. I didn’t think much if it’ll be accepted or not. My thought was like to do my best in preparing report. I went to bed with a the feeling of all being rejected doubting my report quality.

Though I tried to sleep, the adrenaline rush didn’t let me sleep and I was checking my mobile for status of it every 2 hours in between naps. And In the morning like around 5 AM, I checked my mail and I was like

I too can do it. 4/5 reports competed and won the qr round and received $$$ each.The first person I shared this was my mom. I went to my mom and shared this waking her out of bed in half sleep. The happiness on my mother’s face made it worth all the effort.

Press enter or click to view image in full size

Timeline:
Hunt: 6pm-8pm
Report: 8pm –9pm
Accepted: 5 A.M

And now back to this feeling

Press enter or click to view image in full size

, till I find my next bug.

The bug might be simple but the process of finding it in all the places, writing the report a good quality report is not that easy. Thanks a lot for reading my article, hope it helped you in some way.
I’m currently looking for a full time job role as Red team/Web application Pentester, please reach out to me if you have any opening.
