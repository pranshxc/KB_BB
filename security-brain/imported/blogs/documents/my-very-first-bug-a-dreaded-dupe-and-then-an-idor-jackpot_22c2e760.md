---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-28_my-very-first-bug-a-dreaded-dupe-and-then-an-idor-jackpot.md
original_filename: 2019-03-28_my-very-first-bug-a-dreaded-dupe-and-then-an-idor-jackpot.md
title: 'My very first bug: a dreaded dupe and then an IDOR jackpot!'
category: documents
detected_topics:
- xss
- idor
- sqli
- command-injection
- api-security
tags:
- imported
- documents
- xss
- idor
- sqli
- command-injection
- api-security
language: en
raw_sha256: 22c2e760e840e36f49d035cbb8d8877479699b5c335ce31fa5127930496346fb
text_sha256: fc4d50f1858496e307a7553aa208db1e068ce33f8496ca9e8edddd1594fd34fb
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# My very first bug: a dreaded dupe and then an IDOR jackpot!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-28_my-very-first-bug-a-dreaded-dupe-and-then-an-idor-jackpot.md
- Source Type: markdown
- Detected Topics: xss, idor, sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `22c2e760e840e36f49d035cbb8d8877479699b5c335ce31fa5127930496346fb`
- Text SHA256: `fc4d50f1858496e307a7553aa208db1e068ce33f8496ca9e8edddd1594fd34fb`


## Content

---
title: "My very first bug: a dreaded dupe and then an IDOR jackpot!"
url: "https://medium.com/h4x00r/my-very-first-bug-a-dreaded-dupe-and-then-an-idor-jackpot-d01b69f6fbae"
authors: ["John H4X00R (@JohnH4X00R)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["IDOR"]
bounty: "5,000"
publication_date: "2019-03-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5341
scraped_via: "browseros"
---

# My very first bug: a dreaded dupe and then an IDOR jackpot!

Top highlight

My very first bug: a dreaded dupe and then an IDOR jackpot!
John H4X00R
Follow
6 min read
·
Mar 29, 2019

566

1

Hello fellow Hunter!,

I’m going to keep a log of most of my bugs I find on this journey of Bug Hunting. No matter how trivial it may be, as it was in my case, it may come of use to someone, somewhere, sometime!

This is about my very first bug I found, how I got duped and disappointed, and then I hit a jackpot in next two days!

How I got started

Disclaimer: Some blabbing, skip ahead if you don’t want to hear the damn thing.

I got into bug hunting and web security by accident, if I may call it that. May be not by accident when your client’s website gets hacked.

An SQL injection attack on my client’s website changed its entire DB to a malware junkyard in a day. As with most cases of a hack, that’s when we started looking for any backup left behind. I was very lucky to get the data back up and restored from a backup disk, taken just a few days before the hack.

Long story short, that’s when I really thought about web security, and how important it is to not just build applications, but to build applications upon security. As they say, “A chain is no stronger than it’s weakest link”, your application is no stronger than its weakest bug :-)

I started looking for writeup on security, and trying to learn on preventive measures, that’s when I came across blogs and writeup on security by this huge awesome community. This introduced me to the world of bug hunting!

With a little encouragement from fellow hacker writeups, I joined the HackerOne platform in 2016.

My First Bug

It was just after lunch time, I came back to my desk at office, opened up Burp Suite (not Larry_Lau but Community), and went through the proxy HTTP history.

As this was my very first time, I was just looking for anything that could really show up on my face.

I had Twitter open, and I was testing whatever little I knew from my learning. And literally, after a little while, lo and behold, I found my first bug. A reflected XSS on the main domain on Twitter.com!!

Twitter had just introduced Twitter Cards which allowed to attach rich media to tweets. On a parameter called scribe_context, the input was echoed unmodified in the application’s response.

I had hit jackpot! I thought, man this was easy, I love bug hunting. Prepared a POC link, opened up HackerOne.com and submitted my first report.

I was over the moon, or maybe mars! I could not sleep that day because of the excitement.

Until this happened the next day…

The Dreaded Dupe! Depression Level 1

My inner man told me, the report should be different, take courage and ask. Which I did…

Press enter or click to view image in full size

Then I was invited to the original report and this happened…

Press enter or click to view image in full size
This is the initial phase when more depression sets in :-) Depression Level 2
Depression Level 2

Yes depression has different levels, and I just got into level 2. I felt sick, betrayed and what not. I did not want to see the sun anymore. My first taste of a dupe, man it was sour.

Take courage, you are a lion within, my inner man told me, but I could not trust my inner man this time, as he had betrayed me a day ago. But I knew, I will live to fight another day.

Get John H4X00R’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I took a break for two days. I could not avoid the sun for long, so I had to wake up after a long sleep, and get myself back to office. After the short break, I made up my mind “Somehow, I have to find a damn bug today, to make up for the damn dupe.”

My Second Bug

I was back to office, and I got busy for most of the day. The day was getting over, and it was almost 5PM, with an hour left to leave home. I thought, why not open up Burp and check a new target today.

Back then, I used to use Yahoo Notepad to jot down some notes. I thought I could just go through this application. I opened up https://notepad.yahoo.com, to pull up my notes, in the mean time I was keeping an eye on the Proxy HTTP History tab in Burp.

When I opened up a specific note, I noticed a GET request being sent.

Press enter or click to view image in full size

GET /ws/v3/users/fziy4wzxr41k4qwsgumu2v2qymynzat6kclqpwmc/items?format=json&count=200&type=Journal&wssid=55mJmcMk3tg&rand=1478541308397&prog=aeon HTTP/1.1
Host: calendar.yahoo.com

I noticed the encrypted string fziy4wzxr41k4qwsgumu2v2qymynzat6kclqpwmc being sent next to users/.

I immediately knew it was my username, being encrypted and sent. I thought, why not change the encrypted string to my plain Yahoo username and send the request.

It would look so…
GET /ws/v3/users/yahoo-username/items?format=json&kw=test&count=200&type=Journal&wssid=55mJmcMk3tg&rand=1478541308397&prog=aeon HTTP/1.1
Host: calendar.yahoo.com

I changed the encrypted string to my Yahoo username and the response showed up my same notes as a JSON response.

Then, I tried to pass my secondary test Yahoo account (test_account_2222) to the same request, and lo and behold, it showed up my test account’s notes.

Press enter or click to view image in full size

The application was passing the username as an encrypted string, but entering any direct username in the request, was being passing through without any checks.

/ws/v3/users/fziy4wzxr41k4qwsgumu2v2qymynzat6kclqpwmc/items?

/ws/v3/users/user-name/items?

I knew I found a major bug, as I could just change the Username in the GET request to any other Yahoo user’s username and view the notes. I tried out few more test accounts to confirm the same.

Literally, I had found a major bug in just 15 minutes of checking the application. Again, I was over the Moon and beyond, but this time a little cautious not to be over confident on finding a bug. But, I was pretty sure this would be a unique bug, and could be found only if you think differently (out-of-the-box), with a sharp eye, and this time I somehow did.

I opened up HackerOne and submitted my very second bug. Luckily, this time it was not a dupe! Triaged in a day, and fixed in the next.

Press enter or click to view image in full size

Although the bug was fixed, it had failed to deploy on some hosts. I noticed this when I kept trying the same request, and with some hosts the fix did not work. The team was quick to fix the bug on all hosts and then issued my first bounty!!

Press enter or click to view image in full size

The bug was a weird case of IDOR. I feel, the developers tried to fool the eyes of the beholder by just encrypting the username, but really not doing anything with the encrypted string. Just say, encrypted for the eyes, but not for the application.

IDOR bugs are high paying bugs. It can be discovered if you start to look at the application differently, and testing how an application reacts on changing to different types of values. I have discovered many more weird types of IDORs, which I would be disclosing in my next posts.

I learnt to never get discouraged with a dupe. You can always live to fight another day.

Disclosure Timeline
2016–11–07 Report submitted to HackerOne.
2016–11–08 Team acknowledged and triaged the report
2016–11–11 Bug fixed
2016–11–17 $5,000 Bounty awarded
