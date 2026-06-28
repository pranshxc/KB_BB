---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-07_the-bug-that-kept-on-giving-paymentbypass-qr-code.md
original_filename: 2023-01-07_the-bug-that-kept-on-giving-paymentbypass-qr-code.md
title: 'The Bug That Kept On Giving :: PaymentBypass :: QR CODE'
category: documents
detected_topics:
- sso
- command-injection
- api-security
tags:
- imported
- documents
- sso
- command-injection
- api-security
language: en
raw_sha256: 1c39b5846d0848523f4ddb2f250755f2e2f4f8c22c623796e990de33a20634ab
text_sha256: f14076d2444889ad32fc179c245695e89f9620c1405b2d2a267c8910524d60bc
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# The Bug That Kept On Giving :: PaymentBypass :: QR CODE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-07_the-bug-that-kept-on-giving-paymentbypass-qr-code.md
- Source Type: markdown
- Detected Topics: sso, command-injection, api-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `1c39b5846d0848523f4ddb2f250755f2e2f4f8c22c623796e990de33a20634ab`
- Text SHA256: `f14076d2444889ad32fc179c245695e89f9620c1405b2d2a267c8910524d60bc`


## Content

---
title: "The Bug That Kept On Giving :: PaymentBypass :: QR CODE"
page_title: "The Bug That Kept On Giving :: PaymentBypass :: QR CODE | crypt0g30rgy.github.io"
url: "https://crypt0g30rgy.github.io/post/PaymentBypassOne"
final_url: "https://crypt0g30rgy.github.io/post/PaymentBypassOne"
authors: ["g30rgy th3 d4rk (@Crypt0g30rgy)"]
bugs: ["Payment bypass"]
publication_date: "2023-01-07"
added_date: "2023-01-18"
source: "pentester.land/writeups.json"
original_index: 1694
---

# [crypt0g30rgy.github.io](https://crypt0g30rgy.github.io/)

# The Bug That Kept On Giving :: PaymentBypass :: QR CODE

## How we got there

A story of a bug i found through QR code Response Manipulation.

I was scrolling my [twitter](https://twitter.com/crypt0g30rgy) feed when i can across a [tweet](https://twitter.com/intigriti/status/1467111453945733139) from [@intigriti](https://twitter.com/intigriti) about paywall bypass, and i remembered i had a target that had payment bypass inscope.

I went a head and visted the program jij0 [(why)](/post/why). jij0 had a website offering an option to buy e-giftcards. <https://jij0.be/nl/jij0-gift> that would redirect you to <https://gifts.jij0.be> This process contains a flow like;

> select gift card -> get taken to cart -> fill in all the details -> Verify info -> Select payment (By QR Code) -> get qr code -> scan qr to pay (Vulnerable area)

## Reproduction steps

  1. Visit <https://gifts.jij0.be>
  2. Select a gift card
  3. get taken to cart -> fill in all the details -> Verify info -> Select payment (QR code) -> get qr code -> scan qr to payment
  4. Open burp and intercept request with the payment info `"POST /rest/Payment/v1/status?"` and json data `{"paymentData": "DATAAAA"}`
  5. Select burps do intercept response option.
  6. Intercept response which should contain a json parmeter with `{"payload": "","resultCode":"pending","type":"complete"} .Change the response from {"payload": "","resultCode":"pending","type":"complete"}` to `{"payload": "","resultCode":"complete","type":"complete"}`
  7. Now you should recieve a green check to show payment complete and get redirected to
  8. After several minutes you should recieve email confirmation of your purchase.

I made a report and sent it to the program and after a few days it got accepted as a high severity and Bounty €500 awarded.

![basic](/images/poc/accepted.png)

## Contacts

### @[github](https://github.com/crypt0g30rgy) @[twitter](https://twitter.com/crypt0g30rgy) @[LinkedIn](https://www.linkedin.com/in/george-maina-waithaka-95a465214/) @[Intigriti](https://app.intigriti.com/profile/g30rgyth3d4rk) @[hackerone_old](https://hackerone.com/crypt0p3n3tr4t0r?type=user)
