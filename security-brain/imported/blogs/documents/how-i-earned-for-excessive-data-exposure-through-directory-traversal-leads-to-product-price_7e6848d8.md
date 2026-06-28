---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-03_how-i-earned-for-excessive-data-exposure-through-directory-traversal-leads-to-pr.md
original_filename: 2023-03-03_how-i-earned-for-excessive-data-exposure-through-directory-traversal-leads-to-pr.md
title: How I Earned $$$ for Excessive Data Exposure Through Directory Traversal Leads
  to Product Price Manipulation
category: documents
detected_topics:
- path-traversal
- idor
- command-injection
- rate-limit
- information-disclosure
- api-security
tags:
- imported
- documents
- path-traversal
- idor
- command-injection
- rate-limit
- information-disclosure
- api-security
language: en
raw_sha256: 7e6848d88b58a3ecf96f442e25c014628ba5db126b04281e4b80687600f5c942
text_sha256: 27d640e2e66c72c823f09dc8e71981849427f2f263fb44188d2b6b3ae2297bfe
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# How I Earned $$$ for Excessive Data Exposure Through Directory Traversal Leads to Product Price Manipulation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-03_how-i-earned-for-excessive-data-exposure-through-directory-traversal-leads-to-pr.md
- Source Type: markdown
- Detected Topics: path-traversal, idor, command-injection, rate-limit, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `7e6848d88b58a3ecf96f442e25c014628ba5db126b04281e4b80687600f5c942`
- Text SHA256: `27d640e2e66c72c823f09dc8e71981849427f2f263fb44188d2b6b3ae2297bfe`


## Content

---
title: "How I Earned $$$ for Excessive Data Exposure Through Directory Traversal Leads to Product Price Manipulation"
url: "https://mshibilmp.medium.com/how-i-earned-for-excessive-data-exposure-through-directory-traversal-leads-to-product-price-4582e5371774"
authors: ["Mohamed Shibil"]
bugs: ["Path traversal", "Information disclosure", "Payment bypass"]
bounty: "500"
publication_date: "2023-03-03"
added_date: "2023-03-06"
source: "pentester.land/writeups.json"
original_index: 1439
scraped_via: "browseros"
---

# How I Earned $$$ for Excessive Data Exposure Through Directory Traversal Leads to Product Price Manipulation

Top highlight

How I Earned $$$ for Excessive Data Exposure Through Directory Traversal Leads to Product Price Manipulation
Mohamed Shibil
Follow
3 min read
·
Mar 3, 2023

171

2

Hi Folks 👋,

This is my second small write-up✍️. This time I am writing about the first bounty I received from a private program. Let’s say our domain name called Redact.com

API3:Excessive Data Exposure

Excessive data exposure is a vulnerability that occurs when sensitive data is exposed to an unauthorized user or application. This can include data such as passwords, credit card numbers, social security numbers, and other personal information. This type of vulnerability can occur when an application is not properly configured to limit access to sensitive data, or when an application does not properly encrypt the data before it is stored or transmitted. This can allow malicious actors to gain access to data that should be kept private.

Press enter or click to view image in full size

Since Redact.com having Medium scope, I started with subdomain enumeration and among them only a few was in scope and rest belongs to third party domains.

Coming to the main application, I went through the each functionality to get an idea how the application works.

Attack Scenario: 🛠

They have couple of products in the application which is used to organize the documents. So I thought of checking their Product Purchasing Flow.

First I fire up Burp suite then select a product and added to cart by intercepting the cart requests. I checked each request’s responses but didn’t find anything interesting. After going through all the requests I am done for that day 🌃 !

Very next day with a fresh mind again I focused on the same scenario carefully. Then I noticed one of the requests among adding to cart has a parameter base

base=https://www.redact.com

and another parameter next in the URL !

next=https://www.redact.com/cart?sku=0000000

Then I was started to playing with these parameters one after another to find something special. Interestingly the base parameter was unlocked by throwing at “ /../../../../../../ ” payload via simple Directory Traversal !!

Get Mohamed Shibil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This landed us to another subdomain which exposed the Sensitive Information in JSON format 🔎

https://api.redact.com/numericalvalue/cart/list.ext?id=

Here goes the Magic Spell ! !

Press enter or click to view image in full size
Excessive Data Exposed

I checked its response and found 👾 Excessive data including the product’s distinct coupon codes, id, Clients who received personalized discount was exposed.

Then what I did was, just copied one of the Coupon code and entered the same code during check out and I got the discount to purchase the product. I tried each and every coupon code and finally got a Coupon code which 👾 “offers 100% discount” and I applied that code in the coupon code. Instantly the price changed to 000.00 for their Pro Product. So I can able to purchase it Free of cost!

Press enter or click to view image in full size
After Applying the 100% Coupon code for purchasing pro edition

For reporting this vulnerability, I’ve been 🎯 awarded with $500 💰 and got the appreciation from the client as well !

Bounty Received !

Happy to secure !

Thank you 🙏🏻
