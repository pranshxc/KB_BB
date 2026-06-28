---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-16_how-i-was-able-to-buy-t-shirt-for-1-payment-price-manipulation.md
original_filename: 2020-06-16_how-i-was-able-to-buy-t-shirt-for-1-payment-price-manipulation.md
title: How I was able to buy t-shirt for €1 — Payment Price Manipulation
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 474ba96a1403bd7e2921c23c2d16859e02448a231447b26f03a5d2b1b025c185
text_sha256: f0fae18c9b687fac46211dd2513bcc0714bc1c8f3fe3d6b06d46df028f69481c
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to buy t-shirt for €1 — Payment Price Manipulation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-16_how-i-was-able-to-buy-t-shirt-for-1-payment-price-manipulation.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `474ba96a1403bd7e2921c23c2d16859e02448a231447b26f03a5d2b1b025c185`
- Text SHA256: `f0fae18c9b687fac46211dd2513bcc0714bc1c8f3fe3d6b06d46df028f69481c`


## Content

---
title: "How I was able to buy t-shirt for €1 — Payment Price Manipulation"
url: "https://medium.com/@muztahidultanim/how-i-was-able-to-buy-t-shirt-for-1-payment-price-manipulation-36b4d6a30034"
authors: ["Muztahidul Tanim (@TheMuztahidul)"]
bugs: ["Payment tampering"]
bounty: "2,000"
publication_date: "2020-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4492
scraped_via: "browseros"
---

# How I was able to buy t-shirt for €1 — Payment Price Manipulation

How I was able to buy t-shirt for €1 — Payment Price Manipulation
Muztahidul Tanim
Follow
2 min read
·
Jun 17, 2020

265

1

Today I am gonna share a simple but critical vulnerability with you guys. This vulnerability called payment price manipulation, by using this vulnerability, I was able to buy any product for just €1
So let’s see what was the whole vulnerability-

So firstly I added a product in the cart and captured the request in burp.

And captured this post request but nothing suspicious, so I moved forward and check for further, after that I got a page like this.

Press enter or click to view image in full size

But one thing caught my attention that is ‘QUANTITY’ If I increment One unit then what will be the Subtotal Price then I simply Increment a Unit and captured the request again.

Press enter or click to view image in full size

Then I found some parameters which were carrying the subtotal amount shipping amount and everything’s so I changed the all price parameters value to 0.00 except sub_total and total I changed those two parameters value to €1 And forwarded the request & redirected to Payment Page.

I made the payment and confirmed the order.

Get Muztahidul Tanim’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I hope you enjoyed this article. Let me know your thoughts on this one. Thanks for reading.

Bounty Rewarded: 2000€

Find me on twitter @TheMuztahidul
