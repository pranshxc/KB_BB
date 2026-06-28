---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-16_the-bug-that-kept-on-giving-paymentbypass-response-manipulation.md
original_filename: 2022-12-16_the-bug-that-kept-on-giving-paymentbypass-response-manipulation.md
title: 'The Bug That Kept On Giving :: PaymentBypass :: Response Manipulation'
category: documents
detected_topics:
- sso
- command-injection
- business-logic
tags:
- imported
- documents
- sso
- command-injection
- business-logic
language: en
raw_sha256: 3d3f20fbd1cc2776bd194c92f009937b8c5d90013c8b326050ea170c85495d52
text_sha256: 4c07e7194e5ebb78625964aba39f3467a612c700471d43b9634cb9f0d68956e5
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# The Bug That Kept On Giving :: PaymentBypass :: Response Manipulation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-16_the-bug-that-kept-on-giving-paymentbypass-response-manipulation.md
- Source Type: markdown
- Detected Topics: sso, command-injection, business-logic
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `3d3f20fbd1cc2776bd194c92f009937b8c5d90013c8b326050ea170c85495d52`
- Text SHA256: `4c07e7194e5ebb78625964aba39f3467a612c700471d43b9634cb9f0d68956e5`


## Content

---
title: "The Bug That Kept On Giving :: PaymentBypass :: Response Manipulation"
page_title: "The Bug That Kept On Giving :: PaymentBypass :: Response Manipulation | crypt0g30rgy.github.io"
url: "https://crypt0g30rgy.github.io/post/PaymentBypassTwo"
final_url: "https://crypt0g30rgy.github.io/post/PaymentBypassTwo"
authors: ["g30rgy th3 d4rk (@Crypt0g30rgy)"]
bugs: ["Payment bypass", "Logic flaw"]
bounty: "500"
publication_date: "2022-12-16"
added_date: "2023-02-26"
source: "pentester.land/writeups.json"
original_index: 1768
---

# [crypt0g30rgy.github.io](https://crypt0g30rgy.github.io/)

# The Bug That Kept On Giving :: PaymentBypass :: Response Manipulation

## How we got there

A story of the third bug i found after the one for [QR CODE](/post/PaymentBypassOne) And the Next [Exposed Return URL](/post/PaymentBypassThree)

It was the same program jij0 [(why)](/post/why). jij0 had a website offering an option to buy e-giftcards. <https://jij0.be/jij0-gift> that would redirect you to <https://gifts.jij0.be>

This payment bypass is brought by the reliance of JavaSript to validate transactions.
  
  
  function makePayment(data) {
  data['paymentMethod'] = $('.checkout__payment').html();
  $.ajax({
  method: "POST",
  url: "/v1/Payment",
  data: {paymentData: data},
  dataType: "JSON",
  success: function(response) {
  },
  error: function () {
  alert('Ooops...');
  }
  }).then(action => {
  if (action == "Authorised") {
  dropin.setStatus("success")
  $.ajax({
  method: "POST",
  url: "/v1/HandleResponse",
  data: {responseData: action},
  dataType: "JSON",
  success: function(response) {
  window.location = response;
  },
  error: function (response) {
  window.location = response;
  }
  });
  } else if (action == "Refused" || action == "Error") {
  dropin.setStatus("error");
  $.ajax({
  method: "POST",
  url: "/v1/HandleResponse",
  data: {responseData: action},
  dataType: "JSON",
  success: function(response) {
  window.location = response;
  },
  error: function (response) {
  window.location = response;
  }
  });
  

if you read and analyze the above code you would find the vulnerability easy as i eventually did;

> In the above snippet the developer assummed that server responses should be trusted, because a user had no control over what response the server would return but using a tool like burpsuite we can manipulate even server responses hence we would be able to control `action == & .setStatus`

The one is handled by gifts.jij0.be following the below procedure;

item added to cart == user info filled and goes to checkout == user select pay with card == user enters card == transaction performed == gifts.jij0.be checks server responses {The issue lies here} == User either get redirected to cart if transaction failed or confirmation page if transaction is successful

Successful Transaction

`GET /v1/cart == POST /v1/Payment == [Response: 200 OK Data:"Authorised"] == POST /v1/HandleResponse == GET /confirmation`

Unsuccessful Transaction

`GET /nl/cart == POST /v1/Payment == [Response: 200 OK Data:"Refused"] == POST /nl/checkout/HandleResponse == GET /cart`

## Reproduction Steps:

  1. connect burp with your prefered browser
  2. go to https://gifts.jij0.be/ and add an item to your cart
  3. proceed to https://gifts.jij0.be/cart and select checkout
  4. follow the prompts to fill in all the required details and proceed to payment page.
  5. select pay with card and add the test card “1337 1337 1337 1337” expiry data “03/30”
  6. checkout first for camparisons sake and observe the failed checkout that redirected you to https://gifts.jij0.be/cart
  7. go to payment again and do step 5 again but don’t send request yet
  8. Head over to burp and turn intercept on. send request now and make sure [POST /v1/Payment] request is captured by burp
  9. right click and select intercept response to this request and forward request
  10. observe the 200 OK response with the data “Refused” in the body.
  11. Change “Refused” to “Authorised” and forward request, turn off intercept to
  12. You should now recieve confirmation in mail

I made a report and sent it to the program and after a few days it got accepted as a high severity and Bounty €500 awarded.

![basic](/images/poc/accepted1.png)

## Contacts

### @[github](https://github.com/crypt0g30rgy) @[twitter](https://twitter.com/crypt0g30rgy) @[LinkedIn](https://www.linkedin.com/in/george-maina-waithaka-95a465214/) @[Intigriti](https://app.intigriti.com/profile/g30rgyth3d4rk) @[hackerone_old](https://hackerone.com/crypt0p3n3tr4t0r?type=user)
