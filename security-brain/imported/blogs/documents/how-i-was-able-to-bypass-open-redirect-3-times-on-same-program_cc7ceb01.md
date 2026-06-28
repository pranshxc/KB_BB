---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-19_how-i-was-able-to-bypass-open-redirect-3-times-on-same-program.md
original_filename: 2022-07-19_how-i-was-able-to-bypass-open-redirect-3-times-on-same-program.md
title: How i was able to bypass Open Redirect 3 times on same program.
category: documents
detected_topics:
- command-injection
- graphql
- api-security
tags:
- imported
- documents
- command-injection
- graphql
- api-security
language: en
raw_sha256: cc7ceb01d117678ac9a786e849ad38bfc7def891d369497d6f1a9d3bca153bf8
text_sha256: 23c4c98425a8fb4e0b2531e1ed8b90f9f8c16006a0557693d889183a0e96c19f
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# How i was able to bypass Open Redirect 3 times on same program.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-19_how-i-was-able-to-bypass-open-redirect-3-times-on-same-program.md
- Source Type: markdown
- Detected Topics: command-injection, graphql, api-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `cc7ceb01d117678ac9a786e849ad38bfc7def891d369497d6f1a9d3bca153bf8`
- Text SHA256: `23c4c98425a8fb4e0b2531e1ed8b90f9f8c16006a0557693d889183a0e96c19f`


## Content

---
title: "How i was able to bypass Open Redirect 3 times on same program."
url: "https://hunter-55.medium.com/how-i-was-able-to-bypass-open-redirect-3-times-on-same-program-d78f9d2443f6"
authors: ["himanshu pdy (@himanshu_pdy)"]
bugs: ["Open redirect"]
bounty: "300"
publication_date: "2022-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2430
scraped_via: "browseros"
---

# How i was able to bypass Open Redirect 3 times on same program.

How i was able to bypass Open Redirect 3 times on same program.
himanshu pdy
Follow
3 min read
·
Jul 19, 2022

190

2

Hello Security folks, Here is interesting finding which I want to share. As you know i only write if it’s unique finding or if my approach gives some better result. Here is my Twitter and Linkedin.

So The Story started 6 months ago when i got private invite to hackerone program. Its has very less scope. The website was already tested by multiple hackers. 100+ reports already resolved and 65,000+ bounty already awarded.

So this story is about my approach, how i found simple issue within 10 minutes even if the program was heavily tested. And got 3X reward for same issue, just by giving attention to tiny detail.

Main Story :-

On Signup, user gets verification link to verify his/her account.

Now i started playing with the verification link and i observed that it was having “redirect_after” parameter which is empty by-default. But the verification request was not containing any “redirect_after” field.

It was weird!!!

As you can guess, i started entering “redirect_after” everywhere but it was throwing error, request malformed.

Then something clicked in my mind and i used it in the signup url link.

For example :- https://private-site.com/singup?redirect_after=https://evil.com.

And guess what, successful redirect to evil.com happened.

So I reported it. After 1 month they patched it and marked it as closed without asking me to retest.

Press enter or click to view image in full size
Story Continues…..

I thought lets see if they fixed it or not :

I did same steps to reproduce the issue and it seemed that issue was fixed.

After sign up, it didn’t took me to evil.com, the application just stopped.

Get himanshu pdy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I thought maybe it is getting filtered or something since they patched it.

But when i clicked verification link then it redirected me to evil.com !!!

It was successful attack again.

I reported it 2nd time and they triaged it and again patched it and marked it as resolved.

Press enter or click to view image in full size
The End….Just kidding!!!! The issue was still in play.

Recently i tested it again.

Now i noticed they were using POST request while signup and it was a graphql request, actually i was searching for different issue but luckily got bypass for previous fix.

Now the verification link was getting encoded and they were using third party to shorten the url.

I decoded it and guess what i again found the same hidden paramter in the verification link.

So this time i intercepted the POST request for singup and added the hidden paramter (POST /graphql?redirect_after=https://evil.com)

And guess what the verification link redirected the user to evil.com.

I again reported it !!!!

Press enter or click to view image in full size

So For 1 Low issue, i got 3X Reward.

The main thing that you should do while doing bug bounty is to see the tiny details. And study every request and its response. Even if the application is heavily tested, treat the application as new. You will be Surprised !!!

Hope it will helps you to grow.

Thank you for your time, milte hai next writeup mai …. Happy Hacking.
