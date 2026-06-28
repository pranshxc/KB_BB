---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-02_design-flaw-a-tale-of-permanent-dos-informative-triaged.md
original_filename: 2022-04-02_design-flaw-a-tale-of-permanent-dos-informative-triaged.md
title: 'Design Flaw : A Tale of Permanent DOS (Informative -> Triaged)'
category: documents
detected_topics:
- command-injection
- rate-limit
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- rate-limit
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 4b4dac13c8600c4724964f14be426316e16853900d2657a5db9401726d5a3bfc
text_sha256: 2007f15b3ebdb877660d74c41bbc1b79b6cd2fcefdc5886b8a2073d7049f8b6a
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Design Flaw : A Tale of Permanent DOS (Informative -> Triaged)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-02_design-flaw-a-tale-of-permanent-dos-informative-triaged.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `4b4dac13c8600c4724964f14be426316e16853900d2657a5db9401726d5a3bfc`
- Text SHA256: `2007f15b3ebdb877660d74c41bbc1b79b6cd2fcefdc5886b8a2073d7049f8b6a`


## Content

---
title: "Design Flaw : A Tale of Permanent DOS (Informative -> Triaged)"
url: "https://akashhamal0x01.medium.com/design-flaw-a-tale-of-permanent-dos-a9ef05181083"
authors: ["Akash Hamal (@AkashHamal0x01)"]
bugs: ["DoS"]
publication_date: "2022-04-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2760
scraped_via: "browseros"
---

# Design Flaw : A Tale of Permanent DOS (Informative -> Triaged)

Design Flaw : A Tale of Permanent DOS (Informative -> Triaged)
Akash Hamal
Follow
4 min read
·
Apr 2, 2022

359

5

This is my first writeup here on medium. Hope you enjoy it :). Feedbacks are always appreciated!

This was indeed an interesting find, while testing a web application i found a design flaw which could have led to permanent DOS to any user account or even mass DOS at once

As usual i started with testing every functionality i came across. So i checked rate limit on login request but i found that there was rate limit implemented and my account was locked out after some unsuccessful attempts but when i tried to refresh my account on browser i was logged out, interesting!!

So what came in my mind first is how to abuse it? but we have to verify some things first, like was it IP based lockout or account based?

To verify it, i logged into my account on andriod on different network and bruteforced my account password and yes i was logged out(logged in session was destroyed) from website on andriod which means it was account based lockout not IP based but if you noticed , the weird thing here is i was logged out once i exceeded my account login tries so what it means is any attacker can bruteforce victim account with wrong password and trigger account lockout which will also logout victim from the website!

The issue here is only one thing which is the user was logged out once account was locked out which shouldn’t happen because of following reasons :

The attacker has not gained access to account because it was prevented by locking out user account
The victim won’t ever bruteforce his/her own password as we the victim has got options to reset password

So i got pretty good bounties from this method but it wasn’t easy as it looks. Your report must be clear and concise if you want to save time on both side. Meanwhile mine report was understandable but the developers of that program doesn’t seem to understand the risk. The timeline for my one of similar issue report was :

> Report Sent: Apr 1, 2021

> Got Reply : Apr 9 2021, status => informative with below reasoning :

Press enter or click to view image in full size

As you can clearly see the internal team thought it involves MiTM which isn’t true and also it takes time to digest new attack vector or try to get what the hacker is trying to point out and also the program was very old and i know i was the first to discover such scene so i knew its going to happen so i was ready with the reply to make them a more brief explanation:

>Reply sent : Apr 9, 2021

Press enter or click to view image in full size

Then after this reply there was silence from the program team for nearly about 3 months but the wait was going to be over as i received reply from them after about 3 months:

Get Akash Hamal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

> Got Reply: July 29, 2021

Press enter or click to view image in full size

The severity was set to HIGH because it can lead to Permanent DOS of single user account or mass accounts once the process is automated!

I got few more bounties from this method and i shared this method on twitter on October 10, 2021 :

Press enter or click to view image in full size

Tweet link: https://twitter.com/AkashHamal0x01/status/1446927311161331712

So if you find any website which locks user account after unsuccessful login attempts then you can try this and see if it works. If it does you can report it as MEDIUM-HIGH severity issue.

This is mostly acceptable because this is application level DOS which occured due to design flaw

I hope you learnt following things from this writeup:

How implementation in design can lead to high severity issues/flaws like this
Always be patient and if the triager is not understanding, tell about what you found more briefly and in detail from attacker point of view like ease of exploitation and how it can be exploited, etc

That’s it for today and i hope you enjoyed it! If you got any questions you can find me on:

Twitter: https://twitter.com/AkashHamal0x01

Update as of Apr 11, a friend of mine got rewarded because of this writeup:

Press enter or click to view image in full size

tweet link: https://twitter.com/tabaahi_/status/1513450589765570567

Don’t just learn, apply it too. Don’t just watch a tip, retweet and like and finally ignore it , rather apply it to learn !

Stay tuned for more writeups ahead! Stay Tuned!
