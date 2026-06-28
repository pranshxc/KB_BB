---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-11-29_price-manipulation-bypass-using-integer-overflow-method.md
original_filename: 2021-11-29_price-manipulation-bypass-using-integer-overflow-method.md
title: Price Manipulation Bypass Using Integer Overflow Method
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 1e2c2ad6dd69cc151c6946ecd3e9ae1f84ccea46f2ac1615b6e71f93c892429b
text_sha256: 727cbd2467a171061c186571099c267a0b236081cb312395618b437157264762
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Price Manipulation Bypass Using Integer Overflow Method

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-11-29_price-manipulation-bypass-using-integer-overflow-method.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `1e2c2ad6dd69cc151c6946ecd3e9ae1f84ccea46f2ac1615b6e71f93c892429b`
- Text SHA256: `727cbd2467a171061c186571099c267a0b236081cb312395618b437157264762`


## Content

---
title: "Price Manipulation Bypass Using Integer Overflow Method"
url: "https://marxchryz.medium.com/price-manipulation-bypass-using-integer-overflow-method-36ff23ebe91d"
authors: ["Marx Chryz"]
bugs: ["Payment tampering", "Memory corruption"]
publication_date: "2021-11-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3134
scraped_via: "browseros"
---

# Price Manipulation Bypass Using Integer Overflow Method

Price Manipulation Bypass Using Integer Overflow Method
Marx Chryz Del Mundo
Follow
2 min read
·
Nov 29, 2021

296

3

Hello everyone, I am Marx Chryz and I do bug bounty hunting for about a year now. It’s also been two and a half years since I started doing web penetration testing.

Introduction

The website that I am doing bug bounty is private so let’s just call it redacted.com. Redacted.com is an e-commerce website that allows users to buy items from redacted.com

Integer Overflow

During my recon, I noticed that wappalyzer says that redacted.com is using PHP as its programming language. In PHP, there are several data types such as String, Integer, Float, etc. Signed integers in PHP has limits on how big the number it can store. This limit depends on the system itself (32-bit or 64-bit).

In 64-bit systems, signed ints can store only from -2⁶³ up to 2⁶³-1 . So what will happen if we store here a very large number such as 9223372036854775808 (2⁶³)? Since 2⁶³ is higher than the max limit of PHP, PHP forces the number to go back to the lowest possible number which is -2⁶³. Think of it as a clock, that when the number passes 2⁶³-1 (23:59) it goes back to -2⁶³ (00:00).

Here’s a reference about integer overflow. Here’s also a post from MITRE about CWE-190.

In redacted.com, I thought of adding negative items in my cart. I ordered -10 items of Item A. But of course, before trying integer overflow, I tried first inputting negative numbers directly. There are 2 APIs (adding and editing items in cart), the first API forces the quantity to be positive (if I input -10, the quantity becomes 10), while in the second API if I input negative numbers, there is an error message saying that negative numbers are not allowed.

Get Marx Chryz Del Mundo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Due to these restrictions, I thought of trying integer overflow.

Exploitation

Let’s say Item A is 10$ each and Item B is 80$ each.

I ordered 9223372036854775808 of item A.
Upon submitting, the quantity becomes -9223372036854775808, proving the existence of the integer overflow bug.
I ordered again 9223372036854775800 of item A so I will have -8 items of Item A in total.
Now, my cart total is -80$
I ordered 1 item of Item B (80$)
Now, my cart total is $0.00
At first, I thought that this was just a visual bug, and probably there is another checking in the server for negative quantities. To be sure that this is not a visual bug, I checked out my cart and paid using paypal. To my surprise, the bug worked and I paid my items for FREE.
