---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-15_how-i-hacked-worldwide-tiktok-users.md
original_filename: 2021-09-15_how-i-hacked-worldwide-tiktok-users.md
title: How I hacked worldwide Tiktok users
category: documents
detected_topics:
- idor
- command-injection
- api-security
tags:
- imported
- documents
- idor
- command-injection
- api-security
language: en
raw_sha256: 05507e77a209ddaa93c63918c0c7d3752a2daf91099671145c9634a04ab89b0b
text_sha256: b278896f7ef589b66954fbf2094e705b613b80403a972cb40140c4ece0cfe7ba
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked worldwide Tiktok users

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-15_how-i-hacked-worldwide-tiktok-users.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `05507e77a209ddaa93c63918c0c7d3752a2daf91099671145c9634a04ab89b0b`
- Text SHA256: `b278896f7ef589b66954fbf2094e705b613b80403a972cb40140c4ece0cfe7ba`


## Content

---
title: "How I hacked worldwide Tiktok users"
url: "https://s3c.medium.com/how-i-hacked-world-wide-tiktok-users-24e794d310d2"
authors: ["s3c (@s3c_krd)"]
programs: ["TikTok"]
bugs: ["IDOR"]
bounty: "7500"
publication_date: "2021-09-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3315
scraped_via: "browseros"
---

# How I hacked worldwide Tiktok users

Top highlight

s3c
 highlighted

How I hacked worldwide Tiktok users
s3c
Follow
2 min read
·
Sep 14, 2021

641

7

Press enter or click to view image in full size

Hello everyone,

In this write up I am sharing a TikTok vulnerability reported via TikTok’s bug bounty program

While I was testing the Tiktok app to find a vulnerability I saw a part called family pairing and it’s let parents control account their younger users like turn off/on the search bar and turn off/on account to private/public and many more things like the direct message, comments, liked videos….

I thought it’s a good position for testing because these functions are complex in the backend app so I start testing in this part

I created 2 accounts 1 for parents 1 for children and then linked it, and I was turn on my burp suite to catch the requests,

In the parent account, I tried to change my children account from public to private so once I clicked the turn on button private I catch the request in the burp suite

Let’s see what’s happening in this request,
I saw there are some parameters each of them does different actions like

restriction_type and restriction_value and child_user_id

Type is for parts like
Number 1 for direct message
Number 2 for liked videos
Number 3 for comments
Number 4 for public/private account

And Value for if this turn on/off/noone
Like 1 or 2 or 3 or 0

Get s3c’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And child_user_id for your children account id

So i thought what happens if i change the child_user_id to another user id so i changed it and i see BoOM it worked😱

Now I can change sensitive settings of any account just by user id of the account 😳

proof of content

impact
an attacker would have potentially been able to collect all users id of Tiktok and change all users from public to private accounts and stop all lives and videos on the ForYou page and all comments…etc

So I quickly reported it to Tiktok and they resolved the issue quickly.

Timeline:

Reported — Aug 2nd

Awarded $$$$— Aug 6th

Resolved — Aug 13th

Thank you for reading.

Twitter: @s3c_krd
