---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-16_password-reset-poisoning-leading-to-account-takeover.md
original_filename: 2020-05-16_password-reset-poisoning-leading-to-account-takeover.md
title: Password Reset Poisoning leading to Account Takeover
category: documents
detected_topics:
- password-reset
- idor
- command-injection
- otp
tags:
- imported
- documents
- password-reset
- idor
- command-injection
- otp
language: en
raw_sha256: 1caf29b9b1c8cacbccc624526ea8d2cdcc49424b2e24a124583ee48e6cb3fd1b
text_sha256: 44559e1e16cbb60a070e69936c6220a3a22c77f4434a6927c693d57663364224
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Password Reset Poisoning leading to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-16_password-reset-poisoning-leading-to-account-takeover.md
- Source Type: markdown
- Detected Topics: password-reset, idor, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `1caf29b9b1c8cacbccc624526ea8d2cdcc49424b2e24a124583ee48e6cb3fd1b`
- Text SHA256: `44559e1e16cbb60a070e69936c6220a3a22c77f4434a6927c693d57663364224`


## Content

---
title: "Password Reset Poisoning leading to Account Takeover"
url: "https://medium.com/@swapmaurya20/password-reset-poisoning-leading-to-account-takeover-f178f5f1de87"
authors: ["Swapnil Maurya (@swapmaurya20)"]
bugs: ["Password reset", "Account takeover"]
publication_date: "2020-05-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4587
scraped_via: "browseros"
---

# Password Reset Poisoning leading to Account Takeover

Password Reset Poisoning leading to Account Takeover
Swapmaurya
Follow
3 min read
·
May 16, 2020

428

As mentioned in my previous blog here is my another blog on Account Takeover which is unique from the previous one.

So getting started with it, after achieving my 1st P1 on Bugcrowd which was for IDOR to Account Takeover the next day I got a private program invite with a wildcard domain as assets and I just opened the main domain and looked at the whole web application and its working, the first thing I tried was reset password function that I have done in my previous blog but there was no such workflow for that so I logged off for the day and took a break for some days.

And after 2 days I received and Email saying that the program is being paused for some days. Next as usual I was going for college and while we were discussing about the recent tweets on the bug bounty tips Pratik gave me an idea on Host Header injection bypass, so after college I went back and tried the same on the private program and luckily it executed as expected. This Vulnerability was marked as P2 by Bugcrowd since it required one click user interaction.

Press enter or click to view image in full size

Comming to the Proof of Concept:- For this attack I used Burpsuite and Ngrok.

Get Swapmaurya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First I tried requesting the reset password for the victim account and captured the same request in the Burp and edited the request before Forwarding it. And in the same request I added another Host Header with the Ngrok url in the request below the original Host.

Press enter or click to view image in full size
Request having attacker Host

So after sending the edited POST Request the Victim will receive a reset password link which will have ngrok domain in the URL(attacker controlled domain).

Press enter or click to view image in full size
Reset password containing attacker URL received by Victim

And as soon as the Victim visits the link received the Reset token will be leaked on the attacker controlled server.

Press enter or click to view image in full size
Ngrok server controlled by attacker

As you can see in the above image the the Victim’s Password reset Token is Leaked on the attacker controlled server which now he will use it to change the Password and thus Takeover the whole Account of the victim.

Stay updated with me on Twitter

Hope you may have liked it!
Thank you for reading.
