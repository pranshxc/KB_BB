---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-10_how-i-found-3-rare-security-bug-in-a-day.md
original_filename: 2022-09-10_how-i-found-3-rare-security-bug-in-a-day.md
title: How I found 3 rare security bug in a day
category: documents
detected_topics:
- rate-limit
- command-injection
- mobile-security
tags:
- imported
- documents
- rate-limit
- command-injection
- mobile-security
language: en
raw_sha256: bd844f3aef39b6cfd30ca639b373f9622fff31588a6f146254921faabadd72e5
text_sha256: a2439d91988288b486030febae10d24628a286ef39951c262e57168813c80a05
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# How I found 3 rare security bug in a day

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-10_how-i-found-3-rare-security-bug-in-a-day.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `bd844f3aef39b6cfd30ca639b373f9622fff31588a6f146254921faabadd72e5`
- Text SHA256: `a2439d91988288b486030febae10d24628a286ef39951c262e57168813c80a05`


## Content

---
title: "How I found 3 rare security bug in a day"
url: "https://medium.com/@zer0d/how-i-found-3-bug-bounties-in-a-day-c82fe023716e"
authors: ["zer0d"]
bugs: ["Session expiration issue", "Payment bypass", "Lack of rate limiting"]
publication_date: "2022-09-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2182
scraped_via: "browseros"
---

# How I found 3 rare security bug in a day

1

How I found 3 rare security bugs in a day
zer0dac
Follow
4 min read
·
Sep 10, 2022

286

3

Hello everyone,

Last week, I was waiting for test accounts to pentest a mobile application. So at this time, I decided to look for a bug bounty. I choose a program from Hackerone and started to hack it. It was about travel and trip website. I have found 3 vulnerabilities. Even if one of them was a duplicate and two were accepted as informative, I decided to explain them to you, because they were unusual vulnerabilities. Even if those vulnerabilities didn’t help me with bounties, they may help you to find new bugs.

1- Bypassed one-time usage on the sign-in link:

When I review the website login logic, If I choose e-mail login It was asking for your e-mail as expected. :D

And when I enter my e-mail, it is sending me an e-mail with a sign-in link.

Press enter or click to view image in full size

It says this link can be used only one time and in 10 minutes it will expire. So, I clicked the link and sign-in successfully.

Press enter or click to view image in full size

After then, that link should be expired, right? But, is it? I have copied the link and opened a private tab to check it.

Press enter or click to view image in full size

It says there is an error, you can send a new link to your e-mail. However, when we examine the URL, we see there is a parameter “success=false”

What happens if we write true to this input?

Press enter or click to view image in full size

BOOM!☠️

Press enter or click to view image in full size

So, we can use the same sign-in link forever in order to log in.

Get zer0dac’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2- The credit card checker bypass:

I will explain that shortly, even if you bypass some of the security functions of the company, they can say it is informative.

Press enter or click to view image in full size

There is a credit card checker function on the website, so with that, customers can not enter random numbers as credit card no.

The function was that:

Press enter or click to view image in full size

So it was checking card length and the first six digits.

I tried 454545 as a VISA card’s first six digits and I changed the length from request via burp proxy.

Press enter or click to view image in full size

So it accepted 454545 as a card.

3- E-mail bombing and Rate limit

There was a button on the website about “do you want a notification if there is cheap travel?”. I click it and it was asking for an e-mail.

Press enter or click to view image in full size

After then I enter my e-mail. It sent me an apply mail in order to be sure that’s my e-mail and if I really want notifications. However even though I didn’t apply it, it started sending notifications. Then I started to review the request and I realize that there is no rate limit if you enter different mails.

Press enter or click to view image in full size

So if an attacker has e-mail DB, btw all hackers have :), an attacker can send all of them notifications from the website, without their approval. Firstly it sends apply mail but without applying it, it starts to sending cheap travel mails…

So that was the last vulnerability. Hope you enjoy it while reading. See you until the next vulnerability.

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!
