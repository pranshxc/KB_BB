---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-31_bug-bounty-how-i-booked-a-rental-house-for-just-100-inr-price-manipulation-in-ci.md
original_filename: 2018-05-31_bug-bounty-how-i-booked-a-rental-house-for-just-100-inr-price-manipulation-in-ci.md
title: '#Bug Bounty — How I booked a rental house for just 1.00 INR — Price Manipulation
  in Citrus Pay'
category: documents
detected_topics:
- command-injection
- otp
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- otp
- business-logic
- api-security
language: en
raw_sha256: 953295df328277f3d25badb564d2e9cbdb0ab9062095dc9348b3403a9db49e84
text_sha256: 9e7e727c11f4a98eb504761de6e4466d0f47013b82a93205e3d058f4c123471a
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# #Bug Bounty — How I booked a rental house for just 1.00 INR — Price Manipulation in Citrus Pay

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-31_bug-bounty-how-i-booked-a-rental-house-for-just-100-inr-price-manipulation-in-ci.md
- Source Type: markdown
- Detected Topics: command-injection, otp, business-logic, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `953295df328277f3d25badb564d2e9cbdb0ab9062095dc9348b3403a9db49e84`
- Text SHA256: `9e7e727c11f4a98eb504761de6e4466d0f47013b82a93205e3d058f4c123471a`


## Content

---
title: "#Bug Bounty — How I booked a rental house for just 1.00 INR — Price Manipulation in Citrus Pay"
page_title: "#Bug Bounty — How I booked a rental house for just 1.00 INR — Price Manipulation in Citrus Pay | by Raghavendra | Medium"
url: "https://medium.com/@raghav2039/bug-bounty-how-i-booked-a-rental-house-for-just-1-00-inr-price-manipulation-in-citrus-pay-318ff6e0d8a8"
authors: ["Raghavendra Reddy"]
bugs: ["Parameter tampering"]
publication_date: "2018-05-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5860
scraped_via: "browseros"
---

# #Bug Bounty — How I booked a rental house for just 1.00 INR — Price Manipulation in Citrus Pay

#Bug Bounty — How I booked a rental house for just 1.00 INR — Price Manipulation in Citrus Pay
Raghavendra
Follow
3 min read
·
May 31, 2018

210

4

Hey Guys,

During my recent bug bounty hunt, I came across a very critical and yet simple vulnerability. It was payment price manipulation through which I could book a furnished home with one of the famous home rental app in India at the minimal cost (Rs.1.00).

So, let’s see what the whole vulnerability was.

I had to move to a service apartment from a paying guest accommodation. So I went over the internet and searched for a sharing apartment in a home rental site. I loved a house and thought of paying the advance. I was desperately hunting for a Payment gateway vulnerabilities from past few weeks, so I thought of giving a try on this site. I captured the request using a proxy tool before it hit the Payment Gateway.

Press enter or click to view image in full size

The order amount parameter was carrying the amount to be paid, which is “7291.0” INR. Immediately I changed the value to “1.0” INR.

Press enter or click to view image in full size

After manipulating the order amount value, I have forwarded the HTTP request and it redirected me to the below Payment gateway (Citrus Pay) page.

Press enter or click to view image in full size

After clicking on Pay Now button I captured the request and used trial and error technique. I changed many parameter values from “False” to “True”, but no luck. After so many unsuccessful attempts I got the right one. I changed the “Retry count” from 0(zero) to “positive value”.

Press enter or click to view image in full size

Hurray…. It took me to the next page successfully.

Press enter or click to view image in full size

There it asked me for my contact details and my credit card details (I selected this payment method) to pay the amount of 1.00 INR. I enter all my details and clicked on Pay. I got an OTP for paying 1.00. After entering OTP, it showed me the success page displayed below.

Press enter or click to view image in full size

BHOOM…..I have received the rent receipts for the payment of 7291.0 to my email. And there is one more important thing. I have cancelled the house which I booked and I got the refund of 7291.0 INR instead of 1.0 INR which I actually paid.

Get Raghavendra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Here it is the retry count value manipulation that bypassed the payment checksum validation logic of Citrus Pay. So never ever ignore any parameter, you should validate each and everything which is going to the server from client.

This is simple yet a critical vulnerability and this happens when the price or checksum is not validated back by the server.

Always validate the amount back by the server.

Pull the amount from database and check whether it’s the same value or not.

Create a payment checksum and validate it at server side.

This is all about this interesting finding.

Thanks for reading.

— Raghavendra
