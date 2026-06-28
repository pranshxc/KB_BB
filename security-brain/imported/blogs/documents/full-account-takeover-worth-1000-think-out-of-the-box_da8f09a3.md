---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-15_full-account-takeover-worth-1000-think-out-of-the-box.md
original_filename: 2021-02-15_full-account-takeover-worth-1000-think-out-of-the-box.md
title: Full account takeover worth $1000 Think out of the box
category: documents
detected_topics:
- idor
- command-injection
- otp
- csrf
tags:
- imported
- documents
- idor
- command-injection
- otp
- csrf
language: en
raw_sha256: da8f09a3159c1971ea9dd63c7e4c46a76431fd97b5f173050636f1ce56e33705
text_sha256: 5fdd44b61a0cf68eea56590cd14fb53c526d638e29f6c05f80bc5dad80bc7c7c
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Full account takeover worth $1000 Think out of the box

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-15_full-account-takeover-worth-1000-think-out-of-the-box.md
- Source Type: markdown
- Detected Topics: idor, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `da8f09a3159c1971ea9dd63c7e4c46a76431fd97b5f173050636f1ce56e33705`
- Text SHA256: `5fdd44b61a0cf68eea56590cd14fb53c526d638e29f6c05f80bc5dad80bc7c7c`


## Content

---
title: "Full account takeover worth $1000 Think out of the box"
url: "https://mokhansec.medium.com/full-account-takeover-worth-1000-think-out-of-the-box-808f0bdd8ac7"
authors: ["Mohsin Khan (@tabaahi_)"]
bugs: ["Account takeover", "CSRF", "IDOR"]
bounty: "1,000"
publication_date: "2021-02-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3902
scraped_via: "browseros"
---

# Full account takeover worth $1000 Think out of the box

Top highlight

Full account takeover worth $1000 Think out of the box
Mohsin khan
Follow
5 min read
·
Feb 15, 2021

1.6K

9

Hi everyone how are you doing today? I hope you are doing great and scoring lots of bounties. Today's story is about a bug I found on public disclosure program which allows me to take over any user's account. It was a P4 issue but I didn’t report and chain it to P1. Without further ado let’s start

Press enter or click to view image in full size

I don’t have permission to disclosure target information so let’s call it example.com. It was a normal website. There is not so much functionality, You can create an account, log in, change password, etc.

As always I create 2 accounts. I first signup and login with the victim account and I checked every request & response in the burp suite. I found that website is using some kind of CSRF token to prevent CSRF attacks. In the view-page source, I found a website assigning userID to every user. It is 6 digit ID so we can guess ID easily.

Now I go to account settings and I change some of my information (still I am in the victim’s account) and I capture the request.

So now I signup and login with the attacker account. and I try to change the information of the victim on change username functionality (As you can see in the above screenshot) and BOOM nothing happened

Press enter or click to view image in full size

I checked on the change email page also but It looks like without the victim CSRF token you can’t change any information. I try to remove the CSRF token, change POST to GET, etc. but nothing happened.

Now I started looking into other website functionality. It’s time to check how the website implemented change password functionality. For changing the password you need to enter your current password and then the new password. I found that If I remove the current password parameter still I can change the user's password

Press enter or click to view image in full size

Without knowing the old password I can change my password. It’s a P4 issue sometimes P5. Don’t know. I didn’t report this. And I stopped hacking for few hours.

Whenever I don’t hack I talk to other hackers. I call my friend. He found a CSRF bug on his private program and he is able to turn on / off any other user's notifications. I asked him why not tried to change other user’s email or name etc. He said the website validating CSRF tokens on the change info page but not on turn on/off the notification. After talking to him, I start my laptop I now am checking if the change password page CSRF token is validating.

I found that If we remove the csrf_token token and instead of csrf token if we use null like this

Press enter or click to view image in full size

I can change my password. But still, this is P4 because If I want to change another user's password I must need to know their email (to login).

Get Mohsin khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If you can see the screenshot carefully you will found there is no userID. I tried to check for /api/user/userID/change_password, etc. But nothing happens and I was like

Press enter or click to view image in full size

It’s time to give it a last try. Now I am thinking if can use userID in JSON body. maybe will find something better. but I don’t know the parameter name so It’s time to use Param Miner

Param Miner
This extension identifies hidden, unlinked parameters. It's particularly useful for finding web cache poisoning…

portswigger.net

If you don’t know what is Param Miner is, It is a free burp suite extension by James ‘albinowax’ Kettle. This extension identifies hidden, unlinked parameters.

We want to find hidden param in the JSON body so will select Guess JSON parameter.

Press enter or click to view image in full size

A few minutes later I found uid parameter. Now you know what I am thinking to do. Yes, I use uid parameter in my change password JSON body and now I can change all user's passwords without the user's interaction.

Press enter or click to view image in full size

You may ask still you don’t know other user's email so you can change the password but you can’t log in to their account because you don’t know their email.

Yes, you are right but I reported and I mention in my report: I only tested my account but If you want me to show impact, I can change all the user’s passwords and can log in to admin@website.com.

Press enter or click to view image in full size

After reporting, the team reply to me and they fix the issue and reward me with $1000

Press enter or click to view image in full size

I hope you enjoy reading. If you have any question you can dm me on Twitter https://twitter.com/mokhansec
