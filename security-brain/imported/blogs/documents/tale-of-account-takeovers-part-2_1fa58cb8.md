---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-17_tale-of-account-takeovers-part-2.md
original_filename: 2020-05-17_tale-of-account-takeovers-part-2.md
title: Tale of Account Takeovers (Part-2)
category: documents
detected_topics:
- rate-limit
- password-reset
- xss
- command-injection
- otp
- api-security
tags:
- imported
- documents
- rate-limit
- password-reset
- xss
- command-injection
- otp
- api-security
language: en
raw_sha256: 1fa58cb83c954b34fc6de247060ba40d74643bfe95ba4c019b9011643fa5ce8b
text_sha256: 612c8f0c04a31153558b9fcd7bd74726789ab4e0d33fa0dde4420744db1f6fc1
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Tale of Account Takeovers (Part-2)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-17_tale-of-account-takeovers-part-2.md
- Source Type: markdown
- Detected Topics: rate-limit, password-reset, xss, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `1fa58cb83c954b34fc6de247060ba40d74643bfe95ba4c019b9011643fa5ce8b`
- Text SHA256: `612c8f0c04a31153558b9fcd7bd74726789ab4e0d33fa0dde4420744db1f6fc1`


## Content

---
title: "Tale of Account Takeovers (Part-2)"
url: "https://medium.com/@bathinivijaysimhareddy/tale-of-account-takeovers-part-2-9abf62de4ca3"
authors: ["Vijaysimha Reddy Bathini (@fatratfatrat)"]
bugs: ["Account takeover"]
publication_date: "2020-05-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4581
scraped_via: "browseros"
---

# Tale of Account Takeovers (Part-2)

Tale of Account Takeovers (Part-2)
Vijaysimha Reddy Bathini
Follow
5 min read
·
May 18, 2020

426

3

Hello guys, It’s my birthday today and on the occasion of my birthday, I’m here with the next part of Tale of Account Takeovers. It’s been a long time since I have released my part 1 of Tale of Account Takeovers so I thought of giving some time from my busy schedule and start working on this part. I got a good response from the community and compliments for the first part which I haven’t expected and I have got quite a few messages about when the second part will be released. I’d like to contribute little more for the community which will help them learn something new from a different perspective. Thanks to all who are constantly supporting me in my journey as a Bug Bounty Hunter.

In the last part, I have described two of my account takeover scenarios and in this blog post, I wanted to describe three account takeover scenarios which I thought were interesting than the others.

So without wasting time will get straight to the point. Account takeover scenarios 1 and 2 were present in the previous blog post if you haven’t read my first part of Tale of Account Takeovers go check it out.

Account Takeover Scenario 3:

There was a signup feature in this target so as usual, I created an account with fatrat@gmail.com and I logged in. As soon as I have created an account there was no verification email functionality. I have taken note of this in my notes and I have started checking for other functionalities. I have opened another browser and I tried to create an account with the same email as above. I was shocked that it created my account without any error. Then I created an account with testing@gmail.com and added info like credit card details, shipping address and I went to another browser and created an account with testing@gmail.com and to my surprise, the details which I kept were reflected in the new account and BOOM I got Account takeover.

Exploit Scenario:

An attacker gets the victim’s email.
He creates an account with victim email and as the server is accepting to create an account with already existing email without any error.
We have successfully overridden the victim’s password.
This leads to ACCOUNT TAKEOVER

Account Takeover Scenario #4:

I have created a new account and start playing with the requests. After logged in I have found a parameter(ZXlKMWMyVnlibUZ0WlNJNkltWmhkSEpoZERFME15SXNJbkJoYzNOM2IzSmtJam9pZG1scVlYbHliMk5yZWlKOT09) value in the cookies.

Request

Whenever I see such values I always sent them to burp decoder and check whether they have used any encryption. As usual, I have tested for base64 decoding I got the output starting with ey… (If a value is starting with ey I assume it to be base64 encoded value). So I again decoded it.

Press enter or click to view image in full size
Burp decoder output

You can see that they are storing usernames and passwords in cookies which is a bad implementation. To grab the cookies we need an XSS vulnerability. I have already reported an XSS vulnerability two days ago on the same domain and the same I have chained it now which leads to ACCOUNT TAKEOVER.

Get Vijaysimha Reddy Bathini’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Exploit Scenario:

The attacker sends the XSS payload link to the victim and grabs the cookies of the victim.
The attacker double decodes the cookie parameter value and gets the username and password.

Account Takeover Scenario #5:

In this scenario, I will explain how I chained 2 low hanging bugs to Account takeover. There was a forgotten password functionality that sends a 5 digit code to your email. When we enter OTP I found that there is no rate limit protection on that endpoint so I have reported it to the company about this. This program was an external program not on Bugcrowd and HackerOne or any other platforms. After two days I got a reply from them stating that we know about this and you need to fire actually 1,00,000 to brute force the OTP from 00000 to 99999. So I started hunting for other bugs and I found that when we issue 10 forgot password requests only the last OTP code should be valid but I found that previous codes are not expiring even after issuing a new OTP. So I combined two rate limit bugs to chain it to P1 without any user interaction. I have made an assumption that the probability of OTP starting with 50XXX will be more than others. So the scenario we will be using no rate limit bug on forgot password endpoint and issue 1000 password reset emails. I have received 1000 emails and I have made an assumption like there might be a possibility that in all 1000 OTP codes there might be an OTP code starting with 50XXX. I didn’t check the OTP codes but I went on to enter the OTP and captured the request and started to brute-force the OTP from 50000 to 50999. After completion of the attack, I was able to get the correct code and login to the account. Previously we need to brute force it 1Lakh times to crack the code but now we just need to issue 1000 password reset codes and 1000 payloads to brute force the OTP. I have decreased the attack from 100000 to 2000. Reported it to the company and they triaged it by saying this was a clever finding😍😍.

Exploitation Scenario:

An attacker sends 1000 password reset codes to the victim’s email.
After that, the attacker starts to brute force from 50000 to 50999 he gets logged in.

There were more scenarios but I thought these scenarios were best among remaining so even though they are in triage state I have just made a writeup to let all know about it and the remaining will be writing in the next part.

Stay tuned…

If you have liked this article do click on the clap button and do follow me on Twitter and Linkedin.

LinkedIn==>https://www.linkedin.com/in/vijaysimha-reddy/

Twitter ==> https://twitter.com/fatrat_v2

~Vijaysimha Reddy (a.k.a fatrat)

Buy me a coffee here=>>https://www.buymeacoffee.com/fatrat
