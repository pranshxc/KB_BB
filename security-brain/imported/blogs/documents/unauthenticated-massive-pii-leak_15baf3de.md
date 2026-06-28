---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-13_unauthenticated-massive-pii-leak.md
original_filename: 2023-09-13_unauthenticated-massive-pii-leak.md
title: Unauthenticated Massive PII Leak
category: documents
detected_topics:
- rate-limit
- command-injection
tags:
- imported
- documents
- rate-limit
- command-injection
language: en
raw_sha256: 15baf3debd618f7d41da9d560fe9668bf0d70e563f43743ff477e311de78b90c
text_sha256: a0c175580a91b282915cb3ad3cb087dfd930be76b61f425040c39cc5e0fb2307
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated Massive PII Leak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-13_unauthenticated-massive-pii-leak.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: False
- Raw SHA256: `15baf3debd618f7d41da9d560fe9668bf0d70e563f43743ff477e311de78b90c`
- Text SHA256: `a0c175580a91b282915cb3ad3cb087dfd930be76b61f425040c39cc5e0fb2307`


## Content

---
title: "Unauthenticated Massive PII Leak"
url: "https://cristivlad.medium.com/unauthenticated-massive-pii-leak-d182ad3f7553"
authors: ["Cristi Vlad (@CristiVlad25)"]
bugs: ["Rate limiting bypass", "Bruteforce"]
publication_date: "2023-09-13"
added_date: "2023-10-03"
source: "pentester.land/writeups.json"
original_index: 781
scraped_via: "browseros"
---

# Unauthenticated Massive PII Leak

Unauthenticated Massive PII Leak
Cristi Vlad
Follow
4 min read
·
Sep 13, 2023

297

4

Press enter or click to view image in full size

This is probably the report that I’m most proud of. On top of that, it was the lengthiest I’ve ever written.

I think I said it in the past, I’m not big into bug bounty hunting. But there are a handful of programs and platforms that I enjoy playing with. And this one isn’t among them, after the way they handled my report.

Anyway, here’s what I did. The real endpoints, parameters, and communication are different (to protect the identity of the company).

1. I found an endpoint that retrieves user data without authentication. The endpoint accepts a GET request to /id/XXXX123456789?birthday=dd-mm-yyyy and it responds with: id, first name, last name, date of birth, and a few other pieces of personal information.

So, we need two pieces of information (the 13-digit ID and the birthday) to receive a valid response.

2. What I did next was to see how the server responds to an invalid ID and an invalid birthday. For the invalid ID it simply responded with something along the lines of: “We don’t know this ID”.

Now, for a valid ID but an invalid birthday, it responded with something along the lines: “The birthday we have for this ID does not match the one you provided”. Alright, game on!

3. Let’s first bruteforce for a valid ID. Using Intruder, I simply added a payload for the last 5 remaining digits and hit “Start Attack”. After not even 5 attempts, rate limiting kicked and I was stopped. I believe it took 30 to 60 minutes until I was able to hit the API again.

Obviously, I didn’t see that coming. But for this first hurdle, simply adding an “X-Forwarded-Host” header to the request, using a “Battering Ram” attack did the trick.

4. After a few minutes, I had a few valid IDs. Now, for the fun part. How do I bruteforce the birthday? Remember, this is an unauthenticated request and I need a valid ID and a valid birthday to retrieve user information.

Get Cristi Vlad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

5. The birthday is in the format dd-mm-yyyy. How should I go about it? Here’s my rationale:

This is a company with this type/profile of user.
The most probable age range would be 20 to 40 years (in reality this wasn’t the case but I’m protecting the company’s identity).
I need a list of all the birthdays starting January 1st, 1983 to maybe get a few hits. Where can I find this type of list?
The answer is: probably nowhere in this exact format, so I should just do it myself. I’ll use Python.
Ok, how can I do it faster? I know! Instead of coding it myself, I’ll just use GPT4 and have it done for me in seconds.
I’m decent with Python but I don’t need to reinvent the wheel. Let the AI do it, better and faster. The first few lines of the script the AI came up with:

A few seconds later, the list was ready for me to download as txt file from ChatGPT4’s Code Interpreter (now Advanced Data Analysis).

Next, I used Intruder with another Battering Ram attack, with payloads for the birthday and also the X-Forwarded-Host header.

So to recap, the first use of Intruder gave me valid IDs. Now, using one of those IDs and Intruder, I bruteforced for valid passwords.

The beauty of it is that it worked like a charm, it took a couple of minutes for Intruder to run through all the birthdays to find the correct one:

What does a (reckless/careless) company do when presented with this sort of information?

Bruteforcing/Rate Limit Bypass => OOS.

I knew this was not fair but I was not upset at all. Instead, I was really proud of myself for going this far to put up with this attack scenario (I worked some hefty hours to pull it through) and actually succeeded.

And I reply to them something along these lines:

This is probably the lengthiest and most comprehensive report I ever sent. I did it because it shares characteristics of personal data that usually appears in data breaches (full names, birthdays, IDs, and, with a bit of stretch, emails could also be extracted). I did it because despite rate limiting being out of scope I was easily able to bypass it and collect personal information.

If you decide to keep this out of scope, please at least choose to fix it, out of respect for the personal data of the hundreds of thousands of users (or more) that is exposed via this security issue.

And I moved on. This company has already rewarded me for other serious severity vulnerabilities and I decided not to actively engage with them in the future.
