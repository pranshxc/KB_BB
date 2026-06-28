---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-24_session-expiration-bypass-in-facebook-creator-app.md
original_filename: 2019-10-24_session-expiration-bypass-in-facebook-creator-app.md
title: Session Expiration Bypass in Facebook Creator App
category: documents
detected_topics:
- command-injection
- automation-abuse
tags:
- imported
- documents
- command-injection
- automation-abuse
language: en
raw_sha256: 29832577cfbbf7bbf1f95e126eaac70fc60911284c0522a4b7c988e776232af1
text_sha256: 6c07be01100e80418ea20dc1e98156bd8e632764dc34eea7bd851adc009a04b2
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Session Expiration Bypass in Facebook Creator App

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-24_session-expiration-bypass-in-facebook-creator-app.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `29832577cfbbf7bbf1f95e126eaac70fc60911284c0522a4b7c988e776232af1`
- Text SHA256: `6c07be01100e80418ea20dc1e98156bd8e632764dc34eea7bd851adc009a04b2`


## Content

---
title: "Session Expiration Bypass in Facebook Creator App"
url: "https://medium.com/@evilboyajay/session-expiration-bypass-in-facebook-creator-app-b4f65cc64ce4"
authors: ["Ajay Gautam (@evilboyajay)"]
programs: ["Meta / Facebook"]
bugs: ["Session expiration issue"]
bounty: "1,500"
publication_date: "2019-10-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4973
scraped_via: "browseros"
---

# Session Expiration Bypass in Facebook Creator App

Session Expiration Bypass in Facebook Creator App
Ajay Gautam
Follow
3 min read
·
Oct 24, 2019

484

Hello everybody,

Welcome back to my medium after many days. Sorry for not publishing anything for a long time, these days I was busy with some personal work. Today am going to share one cool bug that I found in the facebook creator app which I had already shown in the Pentester Nepal Monthly meetup program.

So, first of all, let me elaborate some more about the facebook creator app.

“Facebook Creator Studio lets creators and publishers manage posts, insights and messages from all of your Facebook Pages in one place.”

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

So, talking more about the security issue that I found in the facebook creator app, I was able to publish a post or delete a post or do all the malicious activities that we can do from creator app even after the session has expired.

How I was able to bypass the session expiration?

When we log out all the logged-in devices from Security and Login then it shows session expired on facebook creator app but the session was not actually expired in the app. This is how the session expired message was shown.

but how I was able to post, delete or send a message after this too.

Get Ajay Gautam’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

For exploiting this vulnerability, I used two devices i.e my phone and my laptop.

I logged into both the devices
I logged out all the active sessions of the Facebook creator app from my laptop.
Session Expired message was shown on my phone.
I then turned my phone mobile data or wifi off.
I closed all the running app and reopened the Facebook Creator app.
I tried to create a post without turning on wifi or mobile data.
While clicking Publish post I turned on my wifi and Post was successfully created.
After Post was successfully created, Session Expired Message was Shown :)

For deleting posts and for other malicious activities same procedure could have helped me. I was awarded 1500$ for this vulnerability.

Press enter or click to view image in full size
Bounty Awarded From Facebook

Impact

Once I logged into someone's Facebook account then I could have used that account for a lifetime even after the victim log outs all the devices or change his password.

Now App has been removed from Facebook.

Timeline

Reported: Aug 1, 2018

Triaged: Aug 30, 2018

Patched: Feb 28, 2019

Bounty Awarded: Apr 10, 2019

Video POC:

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
