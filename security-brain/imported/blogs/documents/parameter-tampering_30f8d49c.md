---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-09-26_parameter-tampering-.md
original_filename: 2020-09-26_parameter-tampering-.md
title: Parameter Tampering ₹→$
category: documents
detected_topics:
- command-injection
- business-logic
tags:
- imported
- documents
- command-injection
- business-logic
language: en
raw_sha256: 30f8d49c6afbaa0f891b5869b207f7198fac79a1dfb4f8644bbe249909d4c642
text_sha256: 73d340675f4ccd1b19a2cf90af517d16a2630e6a0f4e4242f2e2ef04a6535983
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Parameter Tampering ₹→$

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-09-26_parameter-tampering-.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `30f8d49c6afbaa0f891b5869b207f7198fac79a1dfb4f8644bbe249909d4c642`
- Text SHA256: `73d340675f4ccd1b19a2cf90af517d16a2630e6a0f4e4242f2e2ef04a6535983`


## Content

---
title: "Parameter Tampering ₹→$"
page_title: "Parameter Tampering medium Vulnerability bug bounty | Medium"
url: "https://medium.com/@suneets1ngh/parameter-tampering-ddd9b3de0da8"
authors: ["SuneetSingh"]
bugs: ["Parameter tampering"]
publication_date: "2020-09-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4237
scraped_via: "browseros"
---

# Parameter Tampering ₹→$

Parameter Tampering ₹→$
Suneet Singh
Follow
2 min read
·
Sep 26, 2020

130

Hell0 W0rld,

First, What is the Parameter Tampering?

As the name suggests Parameter Tampering is the tampering or manipulation of a parameter that is exchanged between the client and server through HTTP requests and responses, parameters carry information such as currency type, country code, price, permission, etc. which are used to increase the functionality of a website and to modify application data.

Simply put parameters carry specific data to-and-fro client and server and if a manipulated data is sent to the server and the server did not verify that data or process it securely it can cause an application to be manipulated in a malicious manner, this is known as Parameter Tampering Attack.

Now straight to the vulnerability,

I was specifically looking for parameter tampering vulnerabilities on a sports-based e-commerce website using burp suite. I was trying basic amount manipulation by changing the amount of money, but it didn’t work as there were some verifications at the backend which keep correcting the amount on checkout.

Get Suneet Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I tried changing the currency parameter from INR to USD which changed the checkout amount from INR(Indian Rupees) to its USD(US dollar) equivalent but -

-it did not changed the currency-type from INR to USD at checkout i.e., on checkout it was still showing ₹ INR instead of $ USD but with the manipulated USD equivalent price of that product and I was able to check out with manipulated price.

Parameter
Original Prices
Manipulated Amount

I reported this bug they fixed it and it got accepted under P3. Hope you people find this writeup informative any feedback is welcomed.

🙏
