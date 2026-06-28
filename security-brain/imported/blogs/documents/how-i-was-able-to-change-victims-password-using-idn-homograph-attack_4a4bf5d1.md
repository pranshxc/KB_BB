---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-11_how-i-was-able-to-change-victims-password-using-idn-homograph-attack.md
original_filename: 2020-07-11_how-i-was-able-to-change-victims-password-using-idn-homograph-attack.md
title: How I was able to change victim’s password using IDN Homograph Attack
category: documents
detected_topics:
- command-injection
- password-reset
- api-security
tags:
- imported
- documents
- command-injection
- password-reset
- api-security
language: en
raw_sha256: 4a4bf5d125da0a91afb84d63e0a3897cb391c861afd83aa06efb4a1fed31ce4b
text_sha256: 785dbf585606f10b9ca94a405c14f70d3ca0e6aeb9fa5270d1f4a78eb02d3238
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to change victim’s password using IDN Homograph Attack

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-11_how-i-was-able-to-change-victims-password-using-idn-homograph-attack.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `4a4bf5d125da0a91afb84d63e0a3897cb391c861afd83aa06efb4a1fed31ce4b`
- Text SHA256: `785dbf585606f10b9ca94a405c14f70d3ca0e6aeb9fa5270d1f4a78eb02d3238`


## Content

---
title: "How I was able to change victim’s password using IDN Homograph Attack"
url: "https://medium.com/bugbountywriteup/how-i-was-able-to-change-victims-password-using-idn-homograph-attack-587111843aff"
authors: ["Abhishek Karle (@AbhishekKarle3)"]
bugs: ["IDN homograph attack"]
bounty: "600"
publication_date: "2020-07-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4415
scraped_via: "browseros"
---

# How I was able to change victim’s password using IDN Homograph Attack

1

·

Abhishek Karle
 highlighted

1

·

Abhishek Karle
 highlighted

Abhishek Karle
 highlighted

How I was able to change victim’s password using IDN Homograph Attack
Abhishek Karle
Follow
3 min read
·
Jul 11, 2020

877

13

Hey guys Abhishek this side. This is my first writeup. This article is about a vulnerability I was able to find in the BugCrowd private program.

What is IDN homograph attack?

The internationalized domain name (IDN) homograph attack is a way a malicious party may deceive computer users about what remote system they are communicating with, by exploiting the fact that many different characters look alike (i.e., they are homographs, hence the term for the attack, although technically homograph is the more accurate term for different characters that look alike). For example, a regular user of example.com may be lured to click a link where the Latin character “a” is replaced with the Cyrillic character “а”.

One day I saw interesting #bugbountytips post on twitter https://twitter.com/musiclouderlml/status/1276987908340232193?s=19

Then I thought why not give a try. I started hunting for this bug on Bugcrowd private program. Let’s call target.com .

Tha web application “https://target.com/forgot-password?email=" fails to properly validate the value of “email” which was used to takeover the user’s account by changing his password using IDN homograph attack.

IDN homograph attack exploits the fact that many different charachters look like a is different from á Because in that we used a acute accent which looks like exactly a, Suppose the victim’s account is abc@gmail.com , attacker ask password reset link for abc@gmáil.com, target.com’s mail system send password reset link of victim- abc@gmail.com to the attacler mail- abc@xn — gmil-6na.com, To perform this attack , attacker have to buy domain xn — gmil-6na.com

How to test without buying domain ?

The answer is using burp collaborator client.

We have to create a account on target.com with email- abc@gmail.com.burpcollaboratorpayloadhere

Get Abhishek Karle’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So when we ask password reset link for abc@gmáil.com.burpcollaboratorpayloadhere , target.com’s send password reset link of user- abc@gmail.com.burpcollaboratorpayloadhere to the mail- abc@xn — gmil-6na.com.burpcollaboratorpayloadhere , the password reset link received on Burp collaborator client. Make sure to check in burp collaborator client , received email details: To- abc@xn — gmil-6na.com.burpcollaboratorpayloadhere.

Press enter or click to view image in full size

Steps to reproduce-

Open the burp collaborator client > Generate Collaborator payload .
Go to the sign up page of target.com and create a new account with email- abc@gmail.com.burpcollaboratorpayloadhere
Now if the target.com has email confirmation > you will receive the email confirmation link in burp collaborator client > verify the email.
Go to password reset page of target.com > enter email as abc@gmáil.com.burpcollaboratorpayloadhere
If the target.com is vulnerable then it will send password reset link to the mail- abc@xn — gmil-6na.com.burpcollaboratorpayloadhere and you will receive password reset link in burp collaborator client. Make sure to check in burp collaborator client -received email details: To- abc@xn — gmil-6na.com.burpcollaboratorpayloadhere.
Now you can change the password and access the victim’s account.

Result-

Press enter or click to view image in full size

Special thanks to https://twitter.com/musiclouderlml for sharing #bugbountytips.

Hope you guys enjoyed. Thanks for reading.
