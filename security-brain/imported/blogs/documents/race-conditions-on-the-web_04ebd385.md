---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2016-07-12_race-conditions-on-the-web.md
original_filename: 2016-07-12_race-conditions-on-the-web.md
title: Race conditions on the web
category: documents
detected_topics:
- api-security
- command-injection
- otp
- automation-abuse
- race-condition
tags:
- imported
- documents
- api-security
- command-injection
- otp
- automation-abuse
- race-condition
language: en
raw_sha256: 04ebd385f2032276c6d3b6b4060ce4613149896752055d48dc7ad12805c019c4
text_sha256: 55b0649349956cca5956a913c8d53d5c50baff49dbb91dbdc8a360bb08261714
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Race conditions on the web

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2016-07-12_race-conditions-on-the-web.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, otp, automation-abuse, race-condition
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `04ebd385f2032276c6d3b6b4060ce4613149896752055d48dc7ad12805c019c4`
- Text SHA256: `55b0649349956cca5956a913c8d53d5c50baff49dbb91dbdc8a360bb08261714`


## Content

---
title: "Race conditions on the web"
page_title: "Race conditions on the web -  Josip Franjković"
url: "https://www.josipfranjkovic.com/blog/race-conditions-on-web"
final_url: "https://www.josipfranjkovic.com/blog/race-conditions-on-web"
authors: ["Josip Franjkovic (@josipfranjkovic)"]
programs: ["Cobalt.io", "Meta / Facebook", "MEGA", "Keybase"]
bugs: ["Race condition"]
bounty: "8,450"
publication_date: "2016-07-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6282
---

#  [ Josip Franjković web security consultant ](/)

[Blog](/)

Bug bounties

##  Race conditions on the web 

written on July 12th, 2016

The goal of this blog post is to raise awareness about race condition attacks in both developers and security people, because I feel like not many know about this kind of bug - I have participated in CTFs whose points system was vulnerable to race conditions (even Facebook’s CTF platform [was](https://github.com/facebook/fbctf/commit/f706253fbcb1d81476c6ac642dd445b4214426f5)). All examples I wrote about were found in public bug bounty programs and are fixed. 

At the bottom of the page is a compilation of tools and posts for further reading. Enjoy!

### Stealing BitCoin from Cobalt.io

[Cobalt](https://cobalt.io) is a bug bounty platform that offers payouts in BitCoin and PayPal. Their BitCoin withdrawal flow was vulnerable to a race condition attack which could be used to withdraw one bounty multiple times. Check out the original report here:  
<https://cobalt.io/cobalt/cobalt/reports/587>

### Confirming any unused email address on Facebook

This was an unusual race condition which could be exploited to confirm any unused email address on Facebook. During February, I was testing the mobile registration flow on Facebook, and somehow succeeded to confirm a random email address. I reported this to Facebook hoping they’d be able to debug it, since I did not understand how it happened, and made ~5000 requests before realizing the email was confirmed. On April 20th I re-tested the flow and finally got reliable proof of concept:

  1. Register a new account, but do not confirm the email or phone

  2. Obtain a Facebook-issued access_token for the new account

  3. Create multiple requests at the same time toapi.facebook.com/method/user.editregistrationcontactpoint while changing the **add_contactpoint** POST parameter

  4. you should change **add_contactpoint** between an email you have access to, and one you do not, for example [[email protected]](/cdn-cgi/l/email-protection) and [[email protected]](/cdn-cgi/l/email-protection)

  5. On [[email protected]](/cdn-cgi/l/email-protection) you will receive a confirmation link that will look like this: /[[email protected]](/cdn-cgi/l/email-protection)&**c=** 13475&**code=** 84751

The GET parameter **“c”** is always the code for **your** email address, but the **“code”** parameter confirms the one you **do not** have acces to ([[email protected]](/cdn-cgi/l/email-protection)). After obtaining the code, you can go to Facebook settings and confirm the email.

The bug was fixed on May 10th, 2016, and is my favorite report to Facebook. 

### Adding multiple single-use coupons to one Facebook ad account

During the final three months of 2014, Facebook [announced](https://www.facebook.com/notes/protect-the-graph/doubling-up-on-ads-code-bounties/1519314984975314/) they’d be giving double bounties for any ads-related bugs, so I started poking around and found a (minor) bug in how they handled ad coupons. Some coupons can be used only once, and a single ads account should be able to redeem **only one** ad coupon. Using race conditions, I could add multiple ad coupons to a single account. Bear in mind that this bug did **not** enable me to re-use single coupon multiple times or on different accounts.  
To exploit this bug, you would need to buy a couple ad coupons, and try to redeem them at the same time on one account. Multiple coupons would then be available for you to spend, which obviously breaks the one coupon per account rule. 

The interesting thing about this report is the timeline:

  * **October 20, 2014:** Bug reported to Facebook

  * October 22, 2014: Facebook is looking into the issue

  * December 2014: Many messages back and forth between Facebook and me; they were not able to reproduce this issue.

I was at fault here, because the steps were not clearly explained in my report. Looking back, I should have attached my POST requests and server responses for easier analysis.

  * **February 13, 2015:** Update from Facebook, they still are not able to reproduce this, but have checked the code and believe vulnerability is present. Facebook apologizes for the high latency so far.

  * April 22, 2015: Facebook still not able to reproduce it. They ask me if the bug is still present. I have no way to buy coupon codes, and inform Facebook it is impossible for me to re-test it.

At this point I gave up on the report because there was no way for me to prove the vulnerability, and Facebook had no luck reproducing it. But…

  * **September 23, 2015:** Facebook informs me they have fixed the bug, and ask me to confirm it

  * September 24, 2015: After a lot of Googling I get my hands on a couple coupon codes, and try out the race condition. It is now **fixed.** A couple days later, Facebook closed the report:

![Facebook ads race condition reply](https://www.josipfranjkovic.com/resources/img/fb-ads-rc-1.png)

I think this bug is not worth $7500, so I asked Facebook for an explanation of the bounty. Their reply: 

![Facebook reply](https://www.josipfranjkovic.com/resources/img/fb-ads-rc-2.png)

### Mega.nz coupons and purchasing race conditions

Mega was vulnerable to a coupons reuse race condition, very similar to one I found in DigitalOcean ([writeup](https://josipfranjkovic.blogspot.com/2015/04/race-conditions-on-facebook.html)).

The other bug was present in the purchasing logic.  
When you purchase Mega premium, a request is made to their API server eu.api.mega.co.nz/cs, which lowers balance and adds premium time. By sending multiple requests you could buy the premium multiple times, while your balance would go to negative values - this was not an intended functionality.  
Mega rewarded me with a 250EUR bounty, which I told them to donate to LetsEncrypt.

### Cheating Keybase invites system

First bug was present when generating invites for different emails. Let us assume you have 1 invite on your Keybase account. You could bypass the invitation limit by sending a bunch of POST requests with different email values to an API endpoint. Original report with the steps:  
<https://hackerone.com/reports/115007>

Couple months later I saw Keybase re-designed the system, and tried the same attack. It did not work, but a new bug was introduced to the registration flow, using which you could register multiple users while redeeming one invite. Original report:  
<https://hackerone.com/reports/148609>

### Closing words and further reading

Here are some links if you want to read more about race conditions:

  * [@DefuseSec's blog post, includes theory and examples](https://defuse.ca/race-conditions-in-web-applications.htm)

  * [A tool to explot race conditions by @w3af](https://github.com/andresriancho/race-condition-exploit)

  * [Gift card reuse on Starbucks, by @homakov](http://sakurity.com/blog/2015/05/21/starbucks.html)

  * [Manipulating Medium's top stories, by Jack Cable](https://hackernoon.com/how-i-hacked-medium-s-top-stories-b0215da01bc9)

  * [My old post about bugs in Facebook, DigitalOcean, LastPass](https://josipfranjkovic.blogspot.com/2015/04/race-conditions-on-facebook.html)

  * [A writeup on an interesting CTF challenge, by @EdgarBoda of KITCTF team](https://kitctf.de/writeups/gits2015/aart/)

  * [Concurrency Attacks on Web Application, a video from BlueHat by @ScottStender and Alex Vidergar](https://www.youtube.com/watch?v=jTazZ8GXNpk)

A big thanks to all the companies listed for allowing me to write about those reports, and to you for reading!

##### Random blog post

Bug bounties 

####  Getting any Facebook user's friend list and partial payment card details 

written on March 9th, 2018

[ Read more ](/blog/facebook-friendlist-paymentcard-leak)

![Josip Franjković](/resources/img/josip-franjkovic.jpg)

##### Josip Franjković

###### web security consultant

I enjoy breaking websites and participating in various bug bounty programs. 

##### You can contact me using:

  * [@JosipFranjkovic](https://twitter.com/josipfranjkovic) (DM open to everyone) 
  * [[email protected]](/cdn-cgi/l/email-protection#ddb7b2aeb4adf3bbafbcb3b7b6b2abb4be9dbab0bcb4b1f3beb2b0)
  * [keybase.io/josipfranjkovic](https://keybase.io/josipfranjkovic)

All rights reserved © 2018.  
— Josip Franjković
