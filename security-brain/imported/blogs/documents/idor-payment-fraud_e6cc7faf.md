---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-20_idor-payment-fraud.md
original_filename: 2019-06-20_idor-payment-fraud.md
title: 'IDOR: Payment Fraud'
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
raw_sha256: e6cc7fafba921eb1443b594a94af7354d4b13159f7e9417417a4937792959ac3
text_sha256: 01ea6ad6275f25d5d6d5d60b0c0092cd350dcbb335e336b1c159e8625e9b87c1
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# IDOR: Payment Fraud

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-20_idor-payment-fraud.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `e6cc7fafba921eb1443b594a94af7354d4b13159f7e9417417a4937792959ac3`
- Text SHA256: `01ea6ad6275f25d5d6d5d60b0c0092cd350dcbb335e336b1c159e8625e9b87c1`


## Content

---
title: "IDOR: Payment Fraud"
url: "https://medium.com/@Vibhurushi_Chotaliya/idor-payment-fraud-99d330879c0d"
authors: ["Vibhurushi Chotaliya (@_Vibhurushi_)"]
bugs: ["IDOR", "Payment tampering"]
publication_date: "2019-06-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5195
scraped_via: "browseros"
---

# IDOR: Payment Fraud

Top highlight

IDOR: Payment Fraud
Vibhurushi Chotaliya
Follow
3 min read
·
Jun 20, 2019

149

2

Hello guys

This is Vibhurushi Chotaliya. I hope you guys doing well…Today i want to share my cool finding on Bugcrowd Private Program.

I was found the IDOR vulnerability, through that i was able to do a big money fraud to company.

Let’s ROCK it…….

I got the Scope update mail from XYZ.com private program, then i start the hunting and observe the functionality of product and its transaction.

I add product into cart about the worth 100001 MXN (Maxican Peso) then go to the address tab then transaction tab.they have a Paypal payment gateway. I click on it and i got popup request like…

Press enter or click to view image in full size

You can see request have currency parameter.i change the currency to INR. but server block me and popup request closed.Then i thought that what about the USD so i try it, and yes it is accepted. then i also try with EUR and server accept the EUR.but this is not enough……

As i said early the currency is in MXN(Mexican Peso) so…

1 MXN = 0.053 USD

And server accept the USD currency so

100001 USD = 1892256.02 MXN

Now compare original amount and converted USD amount.

100001 MXN = 1892256.02 MXN

Omg!!!!! This difference is too much big.

Yes! I’m able to change currency but why i have to pay 100001 USD actually i need to pay 100001 MXN.

Now i got a thought that…I have to choose that currency which has lower rate then MXN. so i surfing lots of for that but i was fail to validate the currency.every time popup request is block me.

Now i got idea..this is a paypal gate way let me check which currency they are allow to transaction and between them which currency has lower rate then MXN.

Get Vibhurushi Chotaliya’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I got the currency list in paypal.

I Checked the rate of every currency with USD.

I got three currency which has lower rate then MXN

1 (THB)Thai Baht = 0.032 USD

1 (PHP)Philippine Peso= 0.019 USD

1 (THB)Czech Koruna = 0.044 USD

Again i click on payment with paypal and Change the currency parameter to PHP and Yes Paypal Accept this Currency.

Press enter or click to view image in full size

Now You compare the currency amount

100001 MXN = 5286.70 USD

100001 PHP = 1944.22 USD

User just have to pay 1944.22 USD against 5285.70

Now you can understand how much big fraud is possible with this IDOR.

But my hope is Fail.I got a duplicate

Press enter or click to view image in full size

After 1 month they reply again they change the status Unresolved and Reward me Nice bounty…

I hope guys you will learn something from this Write up…Thank you Bug Bounty Community…
