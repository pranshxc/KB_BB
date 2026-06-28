---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-16_how-i-managed-to-create-unauthorized-comments-on-facebook-live-stream.md
original_filename: 2018-11-16_how-i-managed-to-create-unauthorized-comments-on-facebook-live-stream.md
title: How I Managed to Create Unauthorized Comments on Facebook Live Stream
category: documents
detected_topics:
- access-control
- command-injection
- path-traversal
- automation-abuse
- mobile-security
tags:
- imported
- documents
- access-control
- command-injection
- path-traversal
- automation-abuse
- mobile-security
language: en
raw_sha256: 421987b77e7663f308c56336ca07e4ba6c2873cbe4e3c37ba9fee01d1a95a602
text_sha256: b39c8eca42c29e1994523c9ba52fe0ff1a6fc9bfe51060b4a793985f21ba27cf
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I Managed to Create Unauthorized Comments on Facebook Live Stream

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-16_how-i-managed-to-create-unauthorized-comments-on-facebook-live-stream.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, path-traversal, automation-abuse, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `421987b77e7663f308c56336ca07e4ba6c2873cbe4e3c37ba9fee01d1a95a602`
- Text SHA256: `b39c8eca42c29e1994523c9ba52fe0ff1a6fc9bfe51060b4a793985f21ba27cf`


## Content

---
title: "How I Managed to Create Unauthorized Comments on Facebook Live Stream"
page_title: "How I Managed to Create Unauthorized Comments on Facebook Live Stream - Ask Buddie"
url: "https://www.askbuddie.com/blog/unauthorized-comments-on-facebook-live-stream/"
final_url: "https://www.askbuddie.com/blog/unauthorized-comments-on-facebook-live-stream"
authors: ["Binit Ghimire (@WHOISbinit)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization"]
bounty: "750"
publication_date: "2018-11-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5580
---

[![logo](/images/logo/ask-buddie.svg)![logo](/images/logo/ask-buddie-white.svg)](/)

  * [Home](/)
  * [Blog](/blog)
  * [Events](/events)
  * [Contact](/contact)

[](https://github.com/askbuddie)

## How I Managed to Create Unauthorized Comments on Facebook Live Stream

By @binit

2018-11-16

bug-bounty

![image](/blogs/unauthorized-comments-on-facebook-live-stream/images/How-I-Managed-to-Create-Unauthorized-Comments-in-Facebook-Live-Stream.png)

How's it going on, guys? Today, I will be showing you what exactly I did to get the bug that I discovered qualify for the Facebook Bug Bounty Program which made me earn $750 as a reward from the Facebook Security Team.

This article consists of detailed information regarding the bug, my bug report to Facebook along with the embedded Proof-of-Concept video. The bug could have let a malicious Facebook user to add a comment on any live stream even though the streamer allows only friends to comment on his/her live stream.

## How did I manage to get the Bounty?

Everything started out on October 4, 2018. A friend of mine had shared a live stream of a person who was kicked out from a reality television show for misbehaving with the main judge of the show. I decided to watch the live stream. I wanted to comment something on it such as _Hello!_ , but it didn't display the comment box at the bottom of my Android screen since the live streamer wasn't a friend of mine. The only thing I could do was to share or react to the live stream. However, I found a way to comment _Hello!_ in the live stream.

Then, I decided to create a bug report and submit it to Facebook. Before and after submitting, I asked if the bug would qualify or not for the Facebook Bug Bounty Program to some of my friends who were working in the technical field as well-established bug hunters and web/software developers. I was 99% sure that the bug wouldn't qualify for the bug bounty program both before and after submitting the bug report. However, after nearly a month of submitting the vulnerability report to Facebook, the chances of getting rewarded from Facebook Security Team started getting higher when they replied back to me mentioning that they resolved the issue and they would get back to me when they are finalized with their bug bounty decisions.

## What exactly did I do?

I just commented on a live stream of a person who isn't my friend and doesn't allow anyone except friends to comment in his/her live stream.

## What I needed to reproduce the bug?

  * My Facebook account
  * An account which isn't a friend of mine and allows only Friends to comment on posts
  * A running or an ended live stream on that non-friend's account

## How did I comment?

### Step 1

I visited the profile of the person who isn't my friend and allows only friends to comment on his/her posts.

### Step 2

I scrolled down until I found a live stream on his/her profile and opened the live stream.

### Step 3

Facebook had launched a new feature which allows people to create quick comments in live streams without having to type general text like _Hello_ , thumbs up and other emojis. This quick comment area appears in every live stream and you just have to press on one of the quick comment buttons and it gets commented in the live stream.

[caption id="attachment_43" align="aligncenter" width="600"]![Quick Comment buttons in Facebook Live Stream](/blogs/unauthorized-comments-on-facebook-live-stream/images/photo1.jpg) Quick Comment buttons in Facebook Live Stream[/caption]

Similarly, I saw this area in the live stream of the non-friend Facebook user. I decided to press on any of the quick comment buttons and it got commented in the live stream. It didn't even display an error or any limitation message. To be sure, I tried again and it got commented again and when I checked the comments list later on, I found my comment there.

[caption id="attachment_45" align="aligncenter" width="600"]![Unauthorized Comment in Facebook Live Stream](/blogs/unauthorized-comments-on-facebook-live-stream/images/photo2.jpg) My comment on a live stream of a non-friend who allows only friends to comment in her live stream[/caption]

## What I reported to Facebook? [the entire Facebook Bug Report]

I went to the Facebook's **Report Vulnerability Form** in the **Facebook Whitehat** webpage and reported the vulnerability to Facebook on October 5, 2018.

**Title** : Unauthorized Comments on Facebook Live Streams

**Vulnerability Type** : Privilege Escalation

**Product Area** : Facebook - Android

**Description/Impact** :

> Hello, sir! I am Binit Ghimire. I found a bug on Facebook.
> 
> Here's how I discovered the vulnerability. Suppose there is a person who isn't a friend of mine on Facebook. That person allows only "Friends" to comment in posts, pictures and videos. When that person goes live on Facebook and I watch the live stream, there appears "Share" button and reaction buttons. Just above the reaction and "Share" buttons, there appear text like "Hello", tears-of-joy emoji, heart emoji, etc. in the live stream. When I click on any of those, it gets commented, even though it wasn't meant to be commented there.
> 
> I have submitted 2 screenshots regarding this bug along with this report.
> 
> I hope this bug gets resolved soon.
> 
> My Facebook Profile: https://www.facebook.com/InternetHeroBINIT My Email: [[email protected]](/cdn-cgi/l/email-protection)

**Reproduction Steps** :

> Setup ===== 1. An account which isn't your friend and allows only Friends to comment on posts. 2. Your Facebook account 3. The person who isn't your friend and allows only Friends to comment on posts needs to start a live stream.
> 
> Reproduction Steps ================== 1. Open the live stream. 2. You will see Share button, reactions button and above these, you will see some text like "Hello", tears-of-joy emoji, heart emoji, etc. as shown in "photo1.jpg". What you need to do here is, click on these text for commenting.
> 
> It will be commented on the live stream with your Facebook account even though the live streamer doesn't allow outsiders to comment on his/her posts.

**Attachments** :

  * photo2.jpg
  * photo1.jpg

The two screenshots which I kept earlier in this article are the exact same photos that I submitted to Facebook.

After submitting this bug report, I got a reply immediately from Facebook on October 5, 2018 which is an automatic response for every bug report upon submission mentioning the report number along with a message that says they require certain time to investigate and mitigate the issue as well as their right to publish my bug report.

## Further Information regarding the Vulnerability

Later, on October 9, they replied back to me with the following text:

> Hi Binit,
> 
> Can you provide a video showing how you a "non-friend" of the user who posted their Live Stream got access to see it to be able to click on these options?
> 
> Thanks,
> 
> Hatice Security

Then, I responded back in the same bug report with a Proof-of-Concept video regarding the vulnerability on the same day (October 9).

This is what my response looked like:

> Here's a video (attached with this response) where I am showing how I became able to click on these options to comment on a live stream of a user who isn't my friend and allows only friends to comment.
> 
> **Attachments**
> 
> _🔗_ Unauthorized Comments on Facebook Live Streams.mp4

I have uploaded the exact same video file "**Unauthorized Comments on Facebook Live Streams.mp4** " on YouTube which you can watch it here:

[youtube https://www.youtube.com/watch?v=Zgyno1mIPVU]

After responding back with the video, the Facebook Security Team member **Hatice** replied with the following text on October 12:

> Hi Binit,
> 
> Thank you for your submission.
> 
> We've managed to reproduce your report and will get back to you once we have had a chance to investigate.
> 
> Thanks,
> 
> Hatice Security

Along with this response, another Facebook Security Team member **Aaron** also responded with the following text right after the response from **Hatice** :

> Hi Binit,
> 
> To be clear, you are only clicking on the emoji or "Hello" buttons and cannot make arbitrary comments on the Live Stream right?
> 
> Thanks,
> 
> Aaron Security

After getting these two responses, I replied back to the Facebook Security Team with the following information on the same day (i.e. October 12):

> Yes, I am able to comment only the "Hello" text and the other emojis displayed next to it.

I offered a follow-up response to Facebook right after this response with the following text on October 12:

> I can't add my custom comments like I do in friend's posts. Just the "Hello" text and the other emojis.

## Vulnerability Mitigation

After responding back to Facebook with these information, I had to wait till November 10, 2018 for the next response from the Facebook Security Team. I was 99.9% sure that my bug report wouldn't qualify for the Facebook Bug Bounty Program until I got a response from Facebook on November 10. This is what the response looked like:

> Hi Binit,
> 
> We have looked into this issue and believe that the vulnerability has been patched. Please let us know if you believe that the patch does not resolve this issue. We will follow up regarding any bounty decisions soon.
> 
> Thanks,
> 
> Aaron Security

They mentioned that they have patched the issue and requested me to notify them if the patch still doesn't resolve the issue along with a message that tells they will respond back to me if they are finalized with any bounty decisions.

When I got this response back from Facebook, my hopes to get my first ever bounty started increasing. But, I was still 99% sure about not getting the bounty.

I checked if the issue still persists or not on Facebook and found out that the issue has been resolved. So, I responded back to Facebook with the following information on November 10:

> Yes, I checked it again and now the vulnerability has been found to be patched. The patch also resolves the issue.
> 
> Thank you!

## Getting my first ever Bounty from Facebook

After I responded back with this information, I waited until November 14, 2018 to witness the best moment in my entire life. Finally, at around 8:49pm (+5:45 GMT, i.e. Nepal's Time) on November 14, The Facebook Security Team decided to award me a bounty of $750 for letting them know about the issue on their system. Here's how the final response from Facebook looked like on November 14, 2018:

> Hi Binit Ghimire,
> 
> After reviewing this issue, we have decided to award you a bounty of $750. Below is an explanation of the bounty amount. Facebook fulfills its bounty awards through Bugcrowd.
> 
> This could have let a malicious user to add a comment on any live stream even if it has a friends only privacy. The comment text was limited to a given set of quick comments.
> 
> Thank you again for your report. We look forward to receiving more reports from you in the future!
> 
> [_This part of the response from the Facebook Security Team included the URL to claim the bounty amount through Bugcrowd along with the information on how I can claim the bounty and whether I would like to donate my bounty amount to a recognized charitable organization or not. They also mentioned the URL to the webpage containing some frequently asked questions regarding the bug bounty._]
> 
> Thanks, The Facebook Security Team

After getting this response from Facebook, I didn't even click on the claim URL for around 3-4 hours. I was so happy that I had totally lost everything from my mind to express my happiness on getting my first ever bounty from Facebook. I didn't even know what I need to do next. I spammed the inbox of some of my good friends on Facebook with a lot of messages regarding the bounty. Finally, I logged in to my Bugcrowd account at around 11:04pm on November 14, 2018 and then clicked on the URL to claim the bounty amount.

[caption id="attachment_48" align="aligncenter" width="820"]![The Time I visited the URL to Claim the Bounty](/blogs/unauthorized-comments-on-facebook-live-stream/images/Bounty-Claiming-URL.png) The Time I visited the URL to Claim the Bounty[/caption]

With this applicable vulnerability report to Facebook, 38 points were added to my Facebook Whitehat Score to boost up my rankings in their **Thanks** page.

The Payout FAQ webpage on Facebook mentions that if I wish to be added to the Facebook's Thanks page, I need to reply to the bounty award notification message that I received from Facebook along with the name I'd like to be mentioned in the Thanks page.

I was totally unknown about this information until an experienced security researcher who had his name mentioned in the Thanks page on Facebook let me know about it. When I came to find out about this information, I submitted a response back to the Facebook Security Team thanking them along with a request to mention my name in the Thanks page on November 14, 2018.

When I get my name mentioned in the Thanks page on Facebook, I would be updating this article to let you know about the update to the Thanks page. (_Finally, I made it to the list as per the update to the**Thanks** page on November 27, 2018. See below for more information!_)

* * *

### UPDATE: November 27, 2018

I checked the Thanks page on Facebook at the first hour of the day (+5:45 GMT; i.e. Nepal's Time on November 27, 2018) and found out that my name has been included in the list of security researchers who submitted applicable vulnerability reports to Facebook in the year 2018.

At the moment, my name is at the one-hundred and twenty-third position of the list. The rankings depend upon the points researchers have secured in the Facebook Whitehat vulnerability reporting area. So, my position isn't currently fixed at the one-hundred and twenty-third position of the 2018's list since there's still a month left for the year to end.

You will be able to see the entire list of security researchers who have agreed to have their names included in the Thanks page on Facebook here: <https://www.facebook.com/whitehat/thanks/>.

* * *

I hope you had a great time going through this article where I mentioned about the vulnerability that existed on Facebook along with my overall bug report and the responses from the Facebook Security Team from October 5, 2018 to November 14, 2018.

#### Popular Tags :

bug-bountysecurity

  * [Privacy Policy](/privacy-policy)
  * [Terms of Service](/terms-of-service)
  * [Cookies](/cookies)
  * [Contact Us](/contact)

Ask Buddie © 2026

We use cookies to improve your experience on our website. By continuing to use this website, you agree to our use of cookies.

[learn more](/cookies)I understand
