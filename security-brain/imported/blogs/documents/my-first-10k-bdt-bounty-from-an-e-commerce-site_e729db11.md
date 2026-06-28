---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-18_my-first-10k-bdt-bounty-from-an-e-commerce-site.md
original_filename: 2020-05-18_my-first-10k-bdt-bounty-from-an-e-commerce-site.md
title: My first 10k bdt bounty from an e-commerce site
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: e729db11609e188716747161220b3a515edfab6bc90d2a1c207d16bc0aafdeeb
text_sha256: 8fe7e57c0e4f2233ea213f2fa8ee23ed660d8bc88fb14a34d85e3fa6ed5d17e2
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# My first 10k bdt bounty from an e-commerce site

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-18_my-first-10k-bdt-bounty-from-an-e-commerce-site.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `e729db11609e188716747161220b3a515edfab6bc90d2a1c207d16bc0aafdeeb`
- Text SHA256: `8fe7e57c0e4f2233ea213f2fa8ee23ed660d8bc88fb14a34d85e3fa6ed5d17e2`


## Content

---
title: "My first 10k bdt bounty from an e-commerce site"
url: "https://medium.com/@0xh7ml.py/my-first-10k-bdt-bounty-from-an-e-commerce-site-cec9d58e1f55"
authors: ["Md Saikat"]
bugs: ["IDOR"]
bounty: "117"
publication_date: "2020-05-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4578
scraped_via: "browseros"
---

# My first 10k bdt bounty from an e-commerce site

My first 10k bdt bounty from an e-commerce site
Md Saikat
Follow
3 min read
·
May 18, 2020

211

2

Hello peps , Peace be upon on you.First of all that’s my 1st writeup so there maybe some lacking please avoid this silly mistakes.

So let’s dive to the journey of finding IDOR 😉. Normally that’s quarantine day I can’t go out to buy fish food for my lovely fishes.

Not exactly :3

That’s why I finding fish food on a well known e-commerce site of my country and ordered one packet of fish food.That’s appication was a function that after proceed an order it’s redirect to “Your Orders” page then suddenly I noticed the address bar and see the link it was

https://site.com/checkout/payment?orderId=xxxxxxx

my evil mind after see the param :3

Ah!!you see the param? 😁 I think you are thinking about the right thing what was I think.I fire up my Burp 🖤 and sent the intercept request to the Repeater.Then I change the value of param

https://site.com/checkout/payment?orderId=1111111

to

https://site.com/checkout/payment?orderId=1111112

But alas! It was showing 401 Unauthorized 😑.

Server be like -_-

So what! Should I give up or hunt deep? My evil mind was suggest me to hunt deep and I listen his words😉After digging more I came up to a process that “cancel orders” option. By using this option an authenticated user can cancel his / her orders.

Get Md Saikat’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I cancel my orders and intercept the request and the URL was

https://site.com/api-v4/Order/CancelOrder?orderId=xxxxxxx

I sent it to repeater tab and change the order id’s last value and I was shocked that the request’s response was come with 200 status code that’s mean I successfully canceled some user’s order without his / her account’s access

But I need to more confirm about this issue.So , I changed the last digit with another random integer but that time it shows 404 not found ! 🙄

Then I confirmed that If there is any order after canceling it shows 200 else 404 and through 200 response I was permitted to cancel any user’s order without any authenication.

I made a POC and reported this issue to authority.They fixed it and awarded me with 10,000 BDT.

Reported — Fri, May 8

Awarded -Thu, May 14

After all Thanks to my Allah for everything.Thanks to my PC , my parents , my friends and Specially someone 🖤 for their inspiration, helps and love.

Thanks for reading hope for a claps ;) pardon me for my mistakes.

Have a nice day. Be safe ❤

follow_me = [“Facebook”,”twitter”];
