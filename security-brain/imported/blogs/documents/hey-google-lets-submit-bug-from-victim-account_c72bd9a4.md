---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-18_hey-google-lets-submit-bug-from-victim-account-.md
original_filename: 2022-07-18_hey-google-lets-submit-bug-from-victim-account-.md
title: Hey Google Lets submit bug from Victim Account !
category: documents
detected_topics:
- idor
- access-control
- command-injection
tags:
- imported
- documents
- idor
- access-control
- command-injection
language: en
raw_sha256: c72bd9a49eac9b73929d27dee75b58d0cc073ad8878f22dea7ae2e6cbc57175a
text_sha256: ff944ad6d8471549c052c233a4f193b601ccfd5de8211acb5eea3d66b275e594
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Hey Google Lets submit bug from Victim Account !

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-18_hey-google-lets-submit-bug-from-victim-account-.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `c72bd9a49eac9b73929d27dee75b58d0cc073ad8878f22dea7ae2e6cbc57175a`
- Text SHA256: `ff944ad6d8471549c052c233a4f193b601ccfd5de8211acb5eea3d66b275e594`


## Content

---
title: "Hey Google Lets submit bug from Victim Account !"
url: "https://virtuvil.medium.com/hey-google-lets-submit-bug-from-victim-account-af6a25d390e1"
authors: ["Prasanth Elangovan"]
programs: ["Google"]
bugs: ["IDOR"]
publication_date: "2022-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2435
scraped_via: "browseros"
---

# Hey Google Lets submit bug from Victim Account !

Hey Google Lets submit bug from Victim Account !
Virtuvil
Follow
4 min read
·
Jul 18, 2022

275

3

Introduction

Hello friends, This is Prasanth Elangovan (aka Virtuvil) , a security researcher & an ethical hacker from India. This is the story of how my bug bounty journey helped me to pay for my college fees.

Let’s get started by explaining how I can submit a bug report using another user’s account without their authentication on bughunters.google.com.

Press enter or click to view image in full size

While scrolling through LinkedIn, I noticed numerous posts about people receiving Huge Google rewards for their findings. So I decided to hunt on Google.

After spending 7–8 hours, I discovered privilege escalation on a Google domain, and I made a report to submit via bughunters.google.com.

The thought “Harey bhai, Why you didn’t check the bughunter.google.com?” suddenly occurs as I type the report on bughunter.google.com.

Press enter or click to view image in full size

What if we discovered a bug during the submission process? Come on! Simply give it a shot.

Let’s Fired up the burp and then submit the privilege escalation bug. After submitting the report, I review each and every request and response from the burp that we captured from bughunters.google.com.

One of those requests caught my attention. That is what follows.

Press enter or click to view image in full size

What if we changed the mail address?

Press enter or click to view image in full size

Its time to give a shot! So I sent that request to repeater and changed the email address to victim@mail.com. In this case, I used my secondary email address.

Press enter or click to view image in full size

Guess what ? I received 200 OK responses. And the bug was submitted to Google using the victim’s account.

Press enter or click to view image in full size

I got more excited !😁

And here, HTML, content, and text injection are also possible by modifying the request’s other details. So quickly, I submitted the bug and am waiting for a response.

Get Virtuvil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The status was updated three-seven days later. Yes ! My report was triaged by Google.

Like everyone else, I am also excepting the reward.😁

I received the update from Google after a few days. :(

Not again!
I got another duplicate from Google.

Press enter or click to view image in full size

Story behind the this bug :)

I was studying M.Sc. cybersecurity in October 2021. On one Thursday, I received notice that I needed to pay third semester fees. There are only two months left to pay fees. I have some knowledge of networking and cloud-related technologies so I started looking for different freelance jobs , the day after I got the notification. :(

Even though I was a noob in the security field at the time, I was still doing bug bounties. At the initial time I got 100+ duplicates. 😌

Press enter or click to view image in full size

At the time, I received a duplicate from Google as well. It is common for me to receive duplicates and informative messages.😐

Press enter or click to view image in full size

But, luckily, I received $400 from another program for discovering a privilege escalation bug and I paid my college fees without Any delay. :)

Thank you for reading this far. Please DM if you have any questions.

I’ve written other articles as well. I will describe how I discovered complete account takeover without user interaction (how I paid my final semester fees) and other bugs as well.

Always Thanks to NithishKumar M and Vasanth GN

Contact : Linkedin
