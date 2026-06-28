---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-12_discovering-a-hidden-security-loophole-rent-luxury-cars-for-a-single-dollar.md
original_filename: 2023-05-12_discovering-a-hidden-security-loophole-rent-luxury-cars-for-a-single-dollar.md
title: 'Discovering a Hidden Security Loophole: Rent luxury Cars for a Single Dollar'
category: documents
detected_topics:
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 33b0439b2fee607c29a8f2bf04f824a637375ddf84f42faedf57b28231bca9f3
text_sha256: 86dc3ca43a4a17d319b4567e780245b6388fdd9ff13aa458a463f8960e7a2e43
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Discovering a Hidden Security Loophole: Rent luxury Cars for a Single Dollar

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-12_discovering-a-hidden-security-loophole-rent-luxury-cars-for-a-single-dollar.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `33b0439b2fee607c29a8f2bf04f824a637375ddf84f42faedf57b28231bca9f3`
- Text SHA256: `86dc3ca43a4a17d319b4567e780245b6388fdd9ff13aa458a463f8960e7a2e43`


## Content

---
title: "Discovering a Hidden Security Loophole: Rent luxury Cars for a Single Dollar"
url: "https://medium.com/@yashsancheti24/discovering-a-hidden-security-loophole-rent-luxury-cars-for-a-single-dollar-706b4a7bf101"
authors: ["Yash Sancheti"]
bugs: ["Payment tampering"]
publication_date: "2023-05-12"
added_date: "2023-05-15"
source: "pentester.land/writeups.json"
original_index: 1163
scraped_via: "browseros"
---

# Discovering a Hidden Security Loophole: Rent luxury Cars for a Single Dollar

Yash Sancheti
Follow
2 min read
·
May 12, 2023

3

Discovering a Hidden Security Loophole: Rent luxury Cars for a Single Dollar

I am excited to share an intriguing security vulnerability that I discovered in a car rental service a few months ago. Leveraging this loophole allowed me to rent any vehicle, for any duration, at a mere cost of 1 inr. In essence, I was able to manipulate the pricing in my shopping cart.

Initially, my primary focus was to understand the operation of the “add to cart” function and what pathway led to the final payment page, subsequently leading to the payment gateway.

Get Yash Sancheti’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The vulnerability was tucked away in a request sent while booking a car. Here’s what the request looked like:

Press enter or click to view image in full size

Interestingly, the parameters used encoded strings as values. Despite multiple attempts using various decoders, I was unable to decipher these strings to ascertain their actual content.

A breakthrough came when I thought of replicating a similar request for a product of lesser value, and then using those encoded values corresponding to lower prices for a product of higher value. Essentially, this was an attempt at price parameter tampering.

To my surprise, the approach succeeded. I could manipulate the price with the encoded strings derived from the product with lower prices. The adjusted price was reflected on the payment page, and I managed to book the ride for a nominal fee of just 1 inr. In this case, I used an encoded string that corresponded to an amount of 1 inr.

Pro Tip: Whenever you encounter encoded values, delve deeper into analyzing them and attempt to escalate them. You might stumble upon something fascinating.
