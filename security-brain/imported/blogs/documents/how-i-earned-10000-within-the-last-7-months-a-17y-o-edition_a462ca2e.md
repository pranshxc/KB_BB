---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-01_how-i-earned-10000-within-the-last-7-months-a-17yo-edition.md
original_filename: 2022-08-01_how-i-earned-10000-within-the-last-7-months-a-17yo-edition.md
title: How I earned $10,000 within the last 7 months — a 17y/o Edition
category: documents
detected_topics:
- idor
- access-control
- xss
- command-injection
- mfa
- race-condition
tags:
- imported
- documents
- idor
- access-control
- xss
- command-injection
- mfa
- race-condition
language: en
raw_sha256: a462ca2ebb4e6670674be432625339c20b87d1fe7e4d61c6507aa92ec3369ab4
text_sha256: 3edd92789e451cbca364592b0c0e272562526fe63a13497c23aeefb364c3f456
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# How I earned $10,000 within the last 7 months — a 17y/o Edition

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-01_how-i-earned-10000-within-the-last-7-months-a-17yo-edition.md
- Source Type: markdown
- Detected Topics: idor, access-control, xss, command-injection, mfa, race-condition
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `a462ca2ebb4e6670674be432625339c20b87d1fe7e4d61c6507aa92ec3369ab4`
- Text SHA256: `3edd92789e451cbca364592b0c0e272562526fe63a13497c23aeefb364c3f456`


## Content

---
title: "How I earned $10,000 within the last 7 months — a 17y/o Edition"
url: "https://gowtham-naidu.medium.com/how-i-earned-10-000-within-the-last-7-months-17y-o-edition-f566651cef82"
authors: ["Gowtham Naidu Ponnana (@gowtham_ponnana)"]
bugs: ["Broken authorization"]
bounty: "10,000"
publication_date: "2022-08-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2375
scraped_via: "browseros"
---

# How I earned $10,000 within the last 7 months — a 17y/o Edition

How I earned $10,000 within the last 7 months — a 17y/o Edition
Gowtham_Naidu
Follow
6 min read
·
Aug 1, 2022

917

16

“It’s been a long day without you, my friend
And I’ll tell you all about it when I see you again
We’ve come a long way from where we began
Oh, I’ll tell you all about it when I see you again
When I see you again”

~ See You Again [ One Of My Favourite Song ]

Press enter or click to view image in full size

I know, I know, It’s been 3months and I procrastinated a lot🥲 But Believe Me, This Blog will give you the best insights and it will make you stick till the End! And I sincerely thank each and everyone for your continued support. I will try to write blogs consistently🙂(I’m not Lying Bro!)

* Introduction *

Hello InfoSec people, This is Gowtham, a 17y/o Security Researcher from India who loves to dive deep into technologies all the time😁😅. and currently, I am focusing on Blockchain and Smart Contract Security as it makes me struggle a lot.

Coming to the original story, If you are following me on social media you would know that “I earned more than $10,000 within the last 7 months” and it’s still counting. This Blog is all about My Approach and My Methodology [Including writing perfect reports ] and Finally closing with some FAQs’.

What’s so special about me?

Well, If you are familiar with my tweets on Twitter or stories on Instagram, you know that I mostly earn bounties in Cryptocurrencies and this leads to the answer → I mostly hunt on Immunefi, Special invites from Web3 Companies, and some targets using google Dorking. That’s the answer, Bye :)

I won’t leave you here. To Be Honest, I won’t hunt on every random site that I see on Platforms like Immuenfi, Hackerone, Bugcrowd etc... I specifically choose programs where there is less competition with huge rewards [referring to Private Programs ]along with more functionalities and I constantly look for new targets every 24hrs. I play a lot with google dorks to get the best target. Usually, it takes hours to days [ It depends!! ].

What’s the area you mostly look into?

If you ask me personally, I love playing with functionalities where there will be some kind of authorizations. 90% of my bugs were purely reported on Authorization Issues in some way or the other.

I know what you are thinking right now🙂, How the heck I can find authorization vulnerabilities in Crypto-Platforms where they usually log in with wallets? “Connect Wallet”.

Yeah, you are right. 95% of the time we can’t find authorization bugs while logging in with our wallets. But still, you can spend your time looking for those kinds of bugs where you can end up getting some sensitive data leaks.

I don’t care whether they are using normal SignUp/SignIn or Connect-Wallet, All I do is just log in and check all the functionalities that need some kind of authorization. And I will start playing with functionalities. My only best tip here is ~ Just don’t leave upon seeing Connect Wallet Feature on any target.

What kind of bugs you will love to find though? XSS? — Definitely not :)

I think, I should start teaching about some vulnerabilities such as “Rate-Limiting issues at Authentication End-Points, Bypassing 2FA, IDOR etc…” Ummm, I left something and my most favourite vulnerability — Race Conditions. But this is not that kind of blog, so I apologize.

Reverting to your question, I mostly use these kinds of vulnerabilities to get my desired result of Authorization Issues. I can simply say that 70–80% of my reports were mostly on Race-Condition Issues and Rate-Limitings at Authentication End-Points including some IDORs at some places.

So these are the areas and vulnerabilities I mostly look into, upon starting on a program. It may depend from person to person but I prefer this. So no worries :)

We are about to End! Please bear with me my lovely readers🥰. Now Let’s jump into our FAQs.

Why aren’t you replying to our DMs? You are a moron.

There’s a reason why I am not replying, you are either saying just “Hii” or else asking the questions that are stated here below.

How to get started into Cyber Security? Please Help Bro.

Ans: The Best Answer I can give you is, that I can’t. To Be Honest, I don’t know your current understanding of computers and technologies, so the roadmap will be different for everyone. So Blindly don’t follow the roadmaps that pop up on your screen. [Common Roadmap is at the End ]

Get Gowtham_Naidu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2. How do I find good programs to hunt? There is a lot of competition in Public programs.

Ans: Ok, I recommend you to hunt on VDPs until you get some confidence in your skills and meanwhile based on your performance you will start getting Private Programs. In Meantime, Use googling dorking techniques to find programs. Also, Hunt is on the same programs where people post about them on Social-Media.

3. It’s been X months and still I can’t able to find bugs or earn bounties. What should I do?

Ans: Umm, Nice question. I will still say you to continue. If not now, you will find one day. All you need is consistency and look for things that people generally tend to forget. Maybe Like ……., Don’t expect the answer from me🤣

4. What are the best ways to find bugs or to keep updated?

Ans: Just read as many blogs as you can along with Hackerone disclosed reports. It helps you to understand the vulnerability and you can copy-paste things sometimes. And please talk with more people during Conferences, Meetups, Twitter Spaces, Live Discussions and so on.

5. How can I learn Smart Contract Security?

Ans: If you saw one of my tweets, I found some bugs in Smart Contracts which are not super critical but still yeah, I am good enough. So Basically, This space is less for now and people are showing interest in it. But, there is no clear roadmap and I will be hitting soon on “How to get started into Smart Contract Security”. Let’s see how it goes.

So, This is How I earned $10,000 within the last 7months. The simple answer is, that I am consistent enough and I look for some unique bugs. This is all about my approach and methodology. Before Ending the blogs, let me give a quick roadmap for everyone.

Press enter or click to view image in full size
My Recent Bounty😁[Check on Twitter for more INFO]

Roadmap in Common ~

Learn about Computers [such as RAM, Ports, OS, etc] → Learn about basic Network Topologies like IP, NAT, etc → Complete Network+ course → start learning about Security from Security+ material → Now, It’s time to learn about Linux and other OS’s as well. → Learning programming helps you but you can skip it if you want. I recommend doing it [Any Language but go with Python/Go] → Choose a Course [PEH by TCM Academy or some] → Practice, Practice and Practice [TryHackMe, HackTheBox etc] → Google a lot

Ending Note 🥹

This is what all you are waiting for. And I apologize if it’s too lengthy or makes you boring. I wrote it to keep it clean and simple for newbies. I will be there for you again with another awesome blog on

“Race-Conditions” — How I earned $7000+ Only from this vulnerability

If you wanna talk personally with me, drop a mail regarding your situation and your details to my mail below ~

✉️ — gowtham.official45@gmail.com

Follow Me on: [These are my Official Accounts]

Twitter —@ Gowtham_Ponnana
LinkedIn — @Gowtham-Ponnana
Instagram — @Gowtham_Ponnana
Discord — MountXLover#3269
Press enter or click to view image in full size
Photo by Howie R on Unsplash
