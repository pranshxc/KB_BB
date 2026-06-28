---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-13_disclose-private-attachments-in-facebook-messenger-infrastructure-15000.md
original_filename: 2019-02-13_disclose-private-attachments-in-facebook-messenger-infrastructure-15000.md
title: Disclose private attachments in Facebook Messenger Infrastructure - 15,000$
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: c5323b7b0fcd96227df1bb3f641ec4f15ed014a0cfe3295ad9710f06986f9b17
text_sha256: 40f313bca0fc359ed3459718c31ef18a64f634505e27c8894f0997bc51dcc799
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Disclose private attachments in Facebook Messenger Infrastructure - 15,000$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-13_disclose-private-attachments-in-facebook-messenger-infrastructure-15000.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `c5323b7b0fcd96227df1bb3f641ec4f15ed014a0cfe3295ad9710f06986f9b17`
- Text SHA256: `40f313bca0fc359ed3459718c31ef18a64f634505e27c8894f0997bc51dcc799`


## Content

---
title: "Disclose private attachments in Facebook Messenger Infrastructure - 15,000$"
url: "https://medium.com/bugbountywriteup/disclose-private-attachments-in-facebook-messenger-infrastructure-15-000-ae13602aa486"
authors: ["Sarmad Hassan (@JubaBaghdad)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "15,000"
publication_date: "2019-02-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5417
scraped_via: "browseros"
---

# Disclose private attachments in Facebook Messenger Infrastructure - 15,000$

Disclose private attachments in Facebook Messenger Infrastructure - 15,000$
Sarmad Hassan (Juba Baghdad)
Follow
3 min read
·
Feb 13, 2019

1.3K

9

Press enter or click to view image in full size

Hello community, today I would like to share with you my most critical bug that I found in Facebook so far, so let’s get started :)

In 22 Jan. 2019 I was smoking my cigarette at 4:00 AM and suddenly Portal Facebook came to my mind.

What is Portal Facebook

Facebook Portal is a video communication device from Facebook. for more details see this link

I already tested portal.facebook.com before and didn’t find anything in it, but when I opened the site again and switched to Account Setting, I saw something new to me that didn’t saw before, see the below image:

Press enter or click to view image in full size
Support Bot chat in portal Facebook

Then I noticed that you can upload attachments like, images, videos and files, once I saw that I said I need to test this upload feature, so I uploaded normal image and intercepted the request with Burpsuite to see what kind of parameters in the post request and I saw this:

POST /messaging/send/ HTTP/1.1
Host: www.facebook.com

client=mercury&action_type=ma-type:user-generated-message&body=&ephemeral_ttl_mode=0&has_attachment=true&image_ids[0]=123&message_id=111&offline_threading_id=123

as you can see in the above request there is an interesting parameter called image_ids[0] which refers to the image that I uploaded in portal Facebook chat, I said what if I changed this ID to other user image ID, can I disclose his image!!!?? what about other attachments (files, videos and audio messages) !! after testing a lot in portal chat I noticed below things:

I can disclose any attachment for other users that been sent through the chat, those attachments includes ( images, files, videos and audio messages)
It works in all Facebook chat infrastructure (Facebook main chat, messenger, portal chat and workplace chat)
I was able reproduce the bug from any chat (Facebook main chat, messenger, workplace and portal chat) it doesn't matter since its the same
I had to keep the request live in the proxy tab in Burpsuite to reproduce the bug successfully , sending it to repeater was giving me an error ( till now don’t know why)
My thoughts:

Imagine if a malicious hacker found this bug and create a tool to brute force other users ID’s (Images IDs, video IDs, files IDs and audio messages IDs), not to mentioned we’re talking about millions of users who use Facebook chat every day, imagine if he disclose a very VIP persons audio messages, photos or videos …etc as an example, it’s really dangerous if we’re talking about Privacy.

Get Sarmad Hassan (Juba Baghdad)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I reported this directly to Facebook Security Team and they rewarded me with awesome bounty 15k, so thank you so much guys for this bounty :)

Also I would like to thanks my brothers Kassem Bazzoun,張啟元 and Max Pasqua for their great support :)

Timeline:
Jan. 22, 2019 — Initial Report
Feb. 04, 2019 — Report Triaged
Feb. 13, 2019 — Bug Fixed
Feb. 13, 2019 — Fixed confirmed
Feb. 13, 2019– 15k bounty awarded

PoC Video:

Takeways:

1- Try to test your target from time to time, sometimes you will see something that you never saw before just like I did.

2- Don’t trust the response , getting an error doesn’t mean it’s the end :)

Thank you

Sarmad Hassan (JubaBaghdad)

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
