---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-06_how-i-was-able-to-spoof-any-instagram-username-on-instagram-shop.md
original_filename: 2022-01-06_how-i-was-able-to-spoof-any-instagram-username-on-instagram-shop.md
title: How I was able to spoof any Instagram username on Instagram shop
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
raw_sha256: af806efdc92c84ff1543ba66c6d2e5c5d1d43e2d172432f2ed354fbeb1ffbde2
text_sha256: 41ea572b9756e9e7a4d4f9ef33656bfd6051a2d4795b53fa8d54da9199d6bf16
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to spoof any Instagram username on Instagram shop

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-06_how-i-was-able-to-spoof-any-instagram-username-on-instagram-shop.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `af806efdc92c84ff1543ba66c6d2e5c5d1d43e2d172432f2ed354fbeb1ffbde2`
- Text SHA256: `41ea572b9756e9e7a4d4f9ef33656bfd6051a2d4795b53fa8d54da9199d6bf16`


## Content

---
title: "How I was able to spoof any Instagram username on Instagram shop"
url: "https://medium.com/@nvmeeet/how-i-was-able-to-spoof-any-instagram-username-on-instagram-shop-b4d6abdb474a"
authors: ["Nawaf Alkhaldi (@nvmeeet)"]
programs: ["Meta / Facebook"]
bugs: ["IDOR"]
bounty: "1,050"
publication_date: "2022-01-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3026
scraped_via: "browseros"
---

# How I was able to spoof any Instagram username on Instagram shop

How I was able to spoof any Instagram username on Instagram shop
Nawaf Alkhaldi
Follow
2 min read
·
Jan 5, 2022

156

3

Summary: i discovered that i can spoof any Instagram username on Instagram shop, with this bug scammers can trick people into thinking they made purchases to verified accounts and so on.

— — — — — — — — — — — — — —

Hi, This is a write up about a bug which I found on Instagram.

Get Nawaf Alkhaldi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Enjoy!

Description

19/11/2021: i found a new feature in Instagram direct messages that allowed shops to send invoices to customers

As you can see in the second image in the top left corner there is the seller username and seller’s avatar with order status of “Placed” even if you didn’t order anything

the problem was in the HTTP Request data there is a “merchant_id” parameter that determines the Seller’s username/avatar as shown in the previous image.

Press enter or click to view image in full size

After i saw “merchant_id” parameter i went and tried again and intercepted the HTTP request then switched the “merchant_id” parameter to another Instagram account’s user id and guess what.. It worked!

Conclusion:

when you replace the merchant id with any Instagram user’s id the receiver will get the order with the spoofed username in the top left corner even though the order came from the attacker’s account

( victim receives order confirmation from @attacker.1 opens the order and sees that the seller’s name is @Instagram with the verified badge!)

and seeing the order coming from a verified account could help the victim believe the scam

Report timeline:

19 Nov 2021: Report sent

30 Nov 2021: Facebook asked for more info

11 Dec 2021: Bug patched

31 Dec 2021: Facebook awarded me 1000$ + 50$ for the delay

Press enter or click to view image in full size
