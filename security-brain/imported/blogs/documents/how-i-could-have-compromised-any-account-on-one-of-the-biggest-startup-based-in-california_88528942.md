---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-01-28_how-i-could-have-compromised-any-account-on-one-of-the-biggest-startup-based-in-_2.md
original_filename: 2017-01-28_how-i-could-have-compromised-any-account-on-one-of-the-biggest-startup-based-in-_2.md
title: How I could have compromised any account on one of the biggest startup based
  in California
category: documents
detected_topics:
- otp
- idor
- command-injection
- password-reset
tags:
- imported
- documents
- otp
- idor
- command-injection
- password-reset
language: en
raw_sha256: 8852894298e37e5b87c3eafa5b592110c06adaa08d2e7c102fc908fb0f6a4b50
text_sha256: b49da192f90b6b90fe6cfbe95a432a4e3519cab5a4d7550764e19a7f53992ab9
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# How I could have compromised any account on one of the biggest startup based in California

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-01-28_how-i-could-have-compromised-any-account-on-one-of-the-biggest-startup-based-in-_2.md
- Source Type: markdown
- Detected Topics: otp, idor, command-injection, password-reset
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `8852894298e37e5b87c3eafa5b592110c06adaa08d2e7c102fc908fb0f6a4b50`
- Text SHA256: `b49da192f90b6b90fe6cfbe95a432a4e3519cab5a4d7550764e19a7f53992ab9`


## Content

---
title: "How I could have compromised any account on one of the biggest startup based in California"
page_title: "How I Could Have Compromised Any Account On One Of The Biggest STARTUP Based In California | by Prateek Tiwari | Medium"
url: "https://medium.com/@prateek_0490/how-i-could-have-compromised-any-account-on-one-of-the-biggest-startup-based-in-california-3ebc8c6844b5"
authors: ["Prateek Tiwari (@prateek_0490)"]
bugs: ["Account takeover", "IDOR", "Password reset"]
publication_date: "2017-01-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6233
scraped_via: "browseros"
---

# How I could have compromised any account on one of the biggest startup based in California

How I Could Have Compromised Any Account On One Of The Biggest STARTUP Based In California
Prateek Tiwari
Follow
6 min read
·
Jan 28, 2017

122

1

Summary:

This blog is about a severe vulnerability which was being discovered on one of the biggest startup based in California. Since I’m not authorized to reveal the companies name so I’ll just try and keep the name as Private Company here!

I wouldn’t have gone to their website and found this vulnerability if Facebook would have stopped showing me their ads, every now and then Facebook was displaying their ad on my timeline, for the fifth consecutive day when I saw the ad then a thought came into my mind, why not let’s check them out once! And one thing was for sure, they were paying heavily to Facebook to get that ad popped up again and again! So, a BIG Thanks to Facebook from myself and from that Private Company.

So, I started looking at their web application, signed up and after 10–15 mins of browsing I thought it’s not worth investing much of a time when they don’t run a bug bounty program. I signed out and was about to close the application when my eyes suddenly went at a so-called reset-password link, I was like let’s take a look at this and if that works well then, I’ll just close it and get back to what I was doing. Most of the companies become victim of these type of vulnerabilities because they do not set up a proper mechanism for Password recovery. Password recovery functionalities can result in vulnerabilities in the same application they are intended to protect.

Using reset password feature I was able to compromise any user’s account easily without any user interaction. This could have also given me full access of another users account which has all the confidential data even stored payment details, private messages, etc. The most severe issue to notice was once the password was being reset then there was a feature inside the app to change the email, so what more do you want! Change the email and that was it, when victim will try to reset the password from his/her email the app will say sorry you’re not there in our database anymore because someone has hacked your account BECAUSE we were not able to set up a proper reset password mechanism. [the app actually didn’t said this, it just said sorry wrong username]!

Let’s take a look at how this was achieved.

Description of the Vulnerability:

Whenever a user Forgets his password, he has an option to reset the password by entering his email address on https://www.domain.com/forgotpassword, Application will then send an email with a link to set up a new password which would be like — https://www.domain.com/authentication/resetpas/userID?key=<token>&auth=<token>

When I saw the link, my initial reaction was like WOWW, userID in the reset link? I mean I just need to change the userID to Victim ID (any other userID) and would it be done?

As the rules says in our community we should not do any harm on any other users account, so I created another account and obtained an userID, obtaining userID, emails weren’t that difficult because –

FIRST — they were not encrypted

SECOND — they were passed in the GET request, so if you visit any other users profile, you would easily obtain the userID as well as the email address!

So, now what? I have another userID, let’s modify the userID of reset-password link and see if we get success! After changing the userID in the URL param and sending the request for the new password, the message was SUCCESS! I was like ohh WTF? Was it so simple that too with this biggest startup Giant, I said to myself, calm down, yeah we will report the issue for sure now, but let’s just check it out first if it did changed the password of another user? NOOOOO!!! I was like whattt then why was it Success, then I tried to login with this new pass of that old account on which we actually tried to reset the password, ohh I see now, it got changed here though we changed the userID in the URL param.

Get Prateek Tiwari’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So, my next reaction was like they were simply generating the userID but not actually using it! I thought before ending a mission let’s try some different route, so close yet so far!

Okay, so now I was trying to play with the tokens key=<token>, I tried decrypting this a lot with no success, it was 16 chars! My initial reaction was that it might be a base64 string but I was wrong. And another token which was auth=<token> was of 16 char string, but since the first one didn’t work I didn’t try to play with this one because I was an idiot (you’ll discover later, why)!

So, by now, I was pretty sure that it’s not that easy as it was looking in the initial observation, but I had my thoughts clear, I was just trying to think why the hell is userID in there in URL param for reset password? I thought to poke a bit more now, I again requested a password reset link but this time with a newly created account and this time the auth=<token> caught my attention just because it ended with an equal to sign (base64), now you know why I was idiot in not trying to play with auth=<token> at first place!

I immediately decrypted the auth key and VOILA, the decrypted value came as *****@gmail.com, goodness me! So this email was an email of the person who requested the reset password feature. BUT still we had to decrypt the key=<token> value, but that wasn’t happening so what I did was I tried using the same key<token> and replaced the auth=<token> with an encrypted value of a newly created account and changed the userID as well. Now, it failed no Success! Let’s give another shot, let’s remove the key=<token> value from the post request, again no Success.

Something was wrong for sure, the hopes were there but success was not too far either, I thought let’s try and observe these key=<token> values, I requested 4–5 password reset, each time the char strings were different but in a same format, then I thought why not create one of our own in similar format, I created very similar 16 char string, so now I have everything, let’s go for the kill and the Final Blow, and that was it, the message was SUCCESS and this time it changed the password of the Victim Account, WHOOOP!

Adding more insult to injury was after changing the password, an attacker can immediately login into the system and change the email, so the victim would never be able to login back neither he would be able to reset the password, full compromise. Now, attacker can have access to all the data starting from all basic details to the payment/bank details, private chats!

Special Thanks:

I would like to thank all my family members, friends, and everyone around me who plays an important role in motivating me each and every day.

Always TRUST in your abilities.

Disclosure Timeline:

January 25th, 2017: Report sent to Private Company

January 25th, 2017: Company responds within 20 mins, Bug reproduced from their end. They immediately took down the passwordreset feature!

January 27th, 2017: Bug Fixed, and asked to verify the FIX. I confirmed.

The most annoying part was even after responsibly working with their team they said the max they would be able to reward is only $$$ (min value).

Feel free to connect with me here — Tweet me! , LinkedIn
