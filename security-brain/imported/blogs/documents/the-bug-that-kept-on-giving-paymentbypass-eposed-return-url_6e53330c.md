---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-05_the-bug-that-kept-on-giving-paymentbypass-eposed-return-url.md
original_filename: 2022-04-05_the-bug-that-kept-on-giving-paymentbypass-eposed-return-url.md
title: 'The Bug That Kept On Giving :: PaymentBypass :: Eposed Return Url'
category: documents
detected_topics:
- sso
- command-injection
- business-logic
- webhooks
tags:
- imported
- documents
- sso
- command-injection
- business-logic
- webhooks
language: en
raw_sha256: 6e53330cb579af846886fb1e0da7ed66f2d7f8c8b5d4ee27fa61773829396e0c
text_sha256: d2f1d9d5255fc34ddad2dce5ed87c6feba383160b2cd3c7717becb067d0d4bd7
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# The Bug That Kept On Giving :: PaymentBypass :: Eposed Return Url

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-05_the-bug-that-kept-on-giving-paymentbypass-eposed-return-url.md
- Source Type: markdown
- Detected Topics: sso, command-injection, business-logic, webhooks
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `6e53330cb579af846886fb1e0da7ed66f2d7f8c8b5d4ee27fa61773829396e0c`
- Text SHA256: `d2f1d9d5255fc34ddad2dce5ed87c6feba383160b2cd3c7717becb067d0d4bd7`


## Content

---
title: "The Bug That Kept On Giving :: PaymentBypass :: Eposed Return Url"
page_title: "The Bug That Kept On Giving :: PaymentBypass :: Eposed Return Url | crypt0g30rgy.github.io"
url: "https://crypt0g30rgy.github.io/post/PaymentBypassThree"
final_url: "https://crypt0g30rgy.github.io/post/PaymentBypassThree"
authors: ["g30rgy th3 d4rk (@Crypt0g30rgy)"]
bugs: ["Payment bypass", "Logic flaw"]
bounty: "500"
publication_date: "2022-04-05"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 2741
---

# [crypt0g30rgy.github.io](https://crypt0g30rgy.github.io/)

# The Bug That Kept On Giving :: PaymentBypass :: Eposed Return Url

## How we got there

A story of the second bug i found after my Initial payment bypass via the [QR CODE](/post/PaymentBypassOne).

It was the same program jij0 [(why)](/post/why). jij0 had a website offering an option to buy e-giftcards. <https://jij0.be/jij0-gift> that would redirect you to <https://gifts.jij0.be>

This process contains a flow like; select ticket -> get taken to cart -> fill in all the details -> Verify info -> Select payment (QR Code) -> get qr code -> scan qr to pay (Vulnerable area)

The issue that arised and caused this bug was that the server lacked validation and relied on the return url that when the payment provider would use when the payment was successful. The backend didn’t validate this url to make sure that the order has been paid.

The issues were as follows;

  1. gifts.jij0.me didn’t validate that we indeed have paid the order.
  2. The payment provider returned the onSuccess payment redirect url, in the json response `not an issue for the payment provider `
  3. gifts.jij0.me relied on this returned url to validate successful payment.

> The best option here would be using webhooks to validate orders have been paid.

## Reproduction steps

  1. Visit gifts.jij0.be
  2. Select a ticket
  3. get taken to cart -> fill in all the details -> Verify info -> Select payment (QR Code) -> get qr code -> scan qr to payment
  4. Open burp and intercept request with the payment info `GET /v1/status?authorisation=[id here]&transaction=[id here]` and empty body
  5. Select burps do intercept response option.
  6. Intercept response which should contain a json parmeter with

`{"Response":[{"IssuerTransaction":{"uuid":"[uuid]","created":"[time stamp]","updated":"time stamp","name":"jij0","description":"1291","amount":{"currency":"USD","value":"13.37"},"status":"CREATED","transaction_id":"[id]","purchase_id":"[alphanumeric id]","return_url":"https://gifts.jij0.be/complete.shtml?sessionId=id&pspEchoData=[data]&ec=[data]","qr":{"qr_data":"[base64 image data]","qr_content_type":"image/png"}}}]}`

  1. Extract return_url

`["return_url":"https://gifts.jij0.be/complete.shtml?sessionId=id&pspEchoData=[data]"]`

  1. Now you should recieve a green check to show payment complete
  2. After several minutes you should recieve email confirmation of your purchase

I made a report and sent it to the program and after a few days it got accepted as a high severity and Bounty €500 awarded.

![basic](/images/poc/accepted2.png)

## Contacts

### @[github](https://github.com/crypt0g30rgy) @[twitter](https://twitter.com/crypt0g30rgy) @[LinkedIn](https://www.linkedin.com/in/george-maina-waithaka-95a465214/) @[Intigriti](https://app.intigriti.com/profile/g30rgyth3d4rk) @[hackerone_old](https://hackerone.com/crypt0p3n3tr4t0r?type=user)
