---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-06_watch-out-the-links-account-takeover.md
original_filename: 2022-04-06_watch-out-the-links-account-takeover.md
title: 'Watch out the links : Account takeover!'
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
raw_sha256: e03ac3236fbb7c08723fa352146b57feb416fc56ed012554dd285dfebf03e1c1
text_sha256: bbe8e749bb8dce6a5a2bb1e02ddc6e220bc883f01d9414e7791eeb7f4d5f870c
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# Watch out the links : Account takeover!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-06_watch-out-the-links-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `e03ac3236fbb7c08723fa352146b57feb416fc56ed012554dd285dfebf03e1c1`
- Text SHA256: `bbe8e749bb8dce6a5a2bb1e02ddc6e220bc883f01d9414e7791eeb7f4d5f870c`


## Content

---
title: "Watch out the links : Account takeover!"
url: "https://akashhamal0x01.medium.com/watch-out-the-links-account-takeover-32b9315390a7"
authors: ["Akash Hamal (@AkashHamal0x01)"]
bugs: ["Account takeover"]
publication_date: "2022-04-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2739
scraped_via: "browseros"
---

# Watch out the links : Account takeover!

Top highlight

Watch out the links : Account takeover!
Akash Hamal
Follow
3 min read
·
Apr 6, 2022

727

7

This is my second writeup here :), Hope you find enjoy it too!

Feedbacks, suggestions and your point of view are always appreciated!

Today we will discuss a case of what happens if there is poor session management. The worst is it can lead to account takeover!

It was months ago when i thought about this scene, which is what if a link which was meant to be clicked by a user to update something is clicked by another user and details are updated? Well it looks interesting , lets dive into it :D

But that’s just theory of mine and we need to find it in real targets to prove this method works in real world ;)

Its a manual approach and i checked about 10–15 public and private programs just to confirm this is really legit but only found one to be vulnerable and the second one was an external program!

Our main focus is ATO here so we will be playing around those functionalities. Whenever a user updates his/her email from profile settings, mostly a verification link is sent to the mail of user and once its clicked then the user mail is updated in website. Well that’s good because that’s how it was supposed to work but what if the email verification link instead of being clicked by intended user , is clicked by another user? Will it update other users mail? Let’s find out!

You need to create two accounts on let’s say vulnerable.com website, suppose those accounts are victim@gmail.com and attacker@gmail.com assuming them victim and attacker respectively! Secondly , go to attacker account and change mail to 123@gmail.com then a verification link will be sent to 123@gmail.com. Copy that link and paste it on web session of victim@gmail.com account , if it is vulnerable then the email of victim will be updated to 123@gmail.com

And yes :), the website was vulnerable and it indeed updated the email of victim upon clicking the email verification link. This happened because there was no session validation and whoever clicks that verification link, his/her account will be updated to new mail!

I will share the original report which is fairly simple as u see :

Press enter or click to view image in full size
POC of one of my private report!

Timeline:

Get Akash Hamal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

> Submitted report on October 24, 2021

> Triaged and paid instantly on October 26, 2021

Although it required single user click, the team decided to reward me as critical as it was first high severity vulnerability on their program :D.

Please note that this is just one case with maximum impact which is account takeover but in other cases the impact depends on the context. There might be links in website which when clicked changes something in your account. What u can do is identify them, use them into your other account and see if it changes something or not and depending on context severity changes accordingly.

So my theory was confirmed after i found at least one vulnerable instance and indeed i was happy cause never seen any report of such case and also i found similar issue in one of bitcoin website which was hosted externally and got rewarded

This tip was already shared on my twitter handle as you can also see in above POC image i have mentioned

Tweet link : https://twitter.com/AkashHamal0x01/status/1445867416412557317

Mostly am interested to look for common web functionalities and how they can be exploited! You just need to stay away from your PC sometimes and create scenes in your mind and ask yourself, is it really possible? Let’s find out :D.

As you can see i told you that i checked 10–15 programs or maybe more but found only one vulnerable and yes it was manual approach and took a bit more time but it was worth it ❤️

If you have any question/query regarding this writeup except disclosing private program name ofc 😂 , you can find me on twitter :

My twitter handle: https://twitter.com/AkashHamal0x01

That’s it for this writeup and stay tuned :) cause there are more writeups ahead :D and i hope you learnt something new from this writeup!
