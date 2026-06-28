---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-24_microsoft-store-free-purschase-vulnerabilites.md
original_filename: 2021-06-24_microsoft-store-free-purschase-vulnerabilites.md
title: Microsoft Store free purschase vulnerabilites
category: documents
detected_topics:
- sso
- access-control
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- sso
- access-control
- command-injection
- business-logic
- api-security
language: en
raw_sha256: e52135c1642cce8771c4bda4f068f33c1929e620535693468efe0feeab5a55f7
text_sha256: b8bb864a140a42232e60570d440b7aaa05a2a9721f92233866aa05b26aa30ba3
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Microsoft Store free purschase vulnerabilites

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-24_microsoft-store-free-purschase-vulnerabilites.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `e52135c1642cce8771c4bda4f068f33c1929e620535693468efe0feeab5a55f7`
- Text SHA256: `b8bb864a140a42232e60570d440b7aaa05a2a9721f92233866aa05b26aa30ba3`


## Content

---
title: "Microsoft Store free purschase vulnerabilites"
url: "https://gccybermonks.com/posts/msstorebypass/"
final_url: "https://gccybermonks.com/posts/msstorebypass/"
authors: ["Marlon Fabiano (@astrounder)"]
programs: ["Microsoft"]
bugs: ["Payment tampering", "Logic flaw"]
publication_date: "2021-06-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3550
---

# [Microsoft Store free purschase vulnerabilites](https://gccybermonks.com/posts/msstorebypass/)

Author: Marlon Fabiano

## First bypass - Free Vulnerability Purchases

Microsoft has an extensive BugBounty program. I have already participated a few times and received some acknowledgements on the MSRC (Microsoft Security Response Center) portal, so I identified a great bug in Microsoft’s payment method. A failure that allowed me to buy products from the store and not paying anything for it.

It is important to mention that when I reported the failure to the MSRC it was not that simple, because the triage team ended up discrediting even with the PoCs (Proof Of Concept) of someone who said: “Hey Microsoft, I can subscribe to Xbox Live for free.”

I had my ticket at the MSRC closed, but I continued to improve the vulnerability and after a while I opened a new ticket saying: “Hey Microsoft, in addition to subscribing to your services, now I can buy your products without paying anything”.

After much discredit by the MSRC and after many purchases (about US$ 5k in products) they replied: “Hey, stay with us, as we will continue to reproduce your bug”.

### To start understanding the bug we need to understand Microsoft’s purchase flow:

1 - The customer, being logged in to the Xbox or microsoft store, searches for and selects the products he is interested in and at the end of the purchase requests to close the cart, initiating the payment process.

2 - Microsoft receives the purchase request for the selected items and the payment details.

3 - The Microsoft Payment Host makes a request to the responsible Payment Gateway

4 - The payment gateway consults the acquirer so that he can settle the transaction

5 - The acquirerconsults the financial institution to find out if the customer has sufficient credit for the transaction

6 - The Bank submits the transaction to its validation rules, which among other things checks whether the customer has credit to complete the transaction and returns the answer to the acquirer

7 - The inverse process takes place so that the purchase approval is completed

Understanding the purchase flow, we also need to know that Microsoft has two product categories:

### Release products (games that have already been released)

### Pre-order products (games to be released)

## About the logic of billing product

Release products - For products in release, the validation (checkout performed by the gateway) occurs at the time of credit card registration and at the time of purchase.

Pre-order products - For pre-order products, validation (checkout performed by the gateway) occurs at the time of registration and purchase. However, there is a small difference.

The charge for a pre-order product occurs at the time of purchase, but if there is no limit available, it will occur at another time. In this case, if the first charge fails, the second charge happens 10 days before the product is launched. Therefore, steps 2 to 7 of the flowchart will be performed exactly 10 days before the product becomes a release.

### In this case we have the following timeline:

1 - Credit card registration - A query to the payment gateway is carried out to confirm that the data entered is a valid credit card

2 - Product purchase - The second consultation is made at the payment gateway, however, as it is a pre-order product, there is no obligation to pay at the time of purchase and we have an implicit option of being “charged” 10 days before of the release

3 - Product delivery - The product is sent to the buyer.

In this case, the attempt to break the payment logic is to gain access to the product and not paying before 10 days of its release.

In order to bypass the payment we have to make our credit card a valid card at the time of registering the payment method and an invalid card at the time of debiting the product value.

## Reproducing a failure

1 - We registered a valid card in our Xbox Live account (first payment gateway consultation is performed).

2 - We cancel and block the credit card at the issuing bank.

3 - Now with an invalid card, we can buy the products in pre-sale. - The second consultation with the gateway is carried out, however, as the collection can be made 10 days before the release, we can access the products without being charged.

4 - The attempted debit of the registered card will be made 10 days before the launch of the product and you will be able to receive several notifications informing you about the payment failure (Keep Calm and Bypass).

5 - At that moment, we found the flaw and it is in the purchase refund, because the product license is not revoked.

When the product is released you normally have the license and will be able to enjoy the games.

After a while I realized that in some cases it is not necessary to cancel a valid credit card. But we can also use a prepaid card or paypal account without sufficient funds.

Interestingly, at the time of this report, there was no program for Xbox One assets. However after the MSRC accepted the bug, they created a private program in which I was invited and recently launched a public program.

This bug has already been fixed, but there are other e-commerce and game platforms that can be tested in the same way.

I contacted MS through the reward program and they rewarded me with a great bounty.

### PoC:

![](https://lh6.googleusercontent.com/BbHk0JCNaen6p76Gi9cJ4KcAcYz7OT0XQGYf_LVgW_LZQlhp9Lmzx67qPbVQccNhkggfAJobIWtj51EMJK6VcVNGS_PZxa3Rt0BwSkMH0sDE6hzrjrdjB0NK8A3prW0B1h0kG8uw)

![](https://lh5.googleusercontent.com/yrB4jTfKS6E85JL86c4ZIdDx1D4ePhsj3-z8CYwY4UEhUtHeHgjSHp8WCLaxjlugKm8TC19GPHFQcUNVX0uDf0ln2wXfDi1WeCbrhhCSsLkq5wZjHF-kzjm21oqCmksIzi4UnTiy)

# Second Bypass

Accessing Sandbox from Microsoft developers and subscribing to XboxLive and Xbox Game Pass services

## Step by step for the second bypass

exploitation was possible through change and lack of control in the sandbox. XboxOne has a developer mode that allows for some different interactions than consoles in Retail. When a console is in Dev Mode it is possible to change the current sandbox to interact with some features that should only be available to the owners of those sandboxes. With the “Developer Mode activation” application it is possible to change the console sandboxes or in some cases it is also possible to go to the Xbox menu at Settings> System> Console Information and press the LB + RB + LT + RT keys. However, the second mode does not work on all sandboxes after some updates from Microsoft.

The vulnerability occurs within some sandboxes from Microsoft developers, where there is an option to purchase service subscriptions (XboxLive, GamePass PC, GamePass Console and GamePass Ultimate). However, as it is a development environment, there is no charge for it. Failure is only possible because there is no segmentation of what was purchased within the development environment and what was purchased in retail. Thus purchases within the development environment appear in purchases made at MSA as if it were a real purchase. A fact that was confirmed by contacting Xbox support who did not know how I owned the GamePass Ultimate subscription without paying a cent.

To correct this vulnerability, it would be necessary to segment retail and development purchases. In addition to implementing an authentication and authorization control to validate that the user who is typing the sandbox, really has permission to do so. At the time of the report it was possible to enter the sandbox just by knowing your ID.

The known sandboxes are:

* * *

RETAIL (Retail ID)

XDKS.1 (Dev ID)

MSFT.XDK (Dev ID)

MSFT.1 (Dev ID)

MSFT.PRERELEASE (Dev ID)

MSFT.Dogfood (Dev ID)

MSFT.99 (Dev ID)

MSFT.88 (Dev ID)

TURN.99 (Turn 10’s App Debugging ID)

RKTR.99 (Dev ID)

BNGE.99 (Destiny’s App Debugging ID)

* * *

The vulnerability has been reported to the MSRC. They reported that there was no such crossover of subscriptions for the Retail and Dev environments, but they did not know how to explain how I had logged into the listed sandboxes. Even so, they reported that the vulnerability was not a security breach and closed the case.

After the vulnerability was published on twitter at <https://twitter.com/astrounder/status/1284109107922968577> the vulnerability has been fixed, but Microsoft has not contacted us to mention the incident.

### PoC:

![](https://lh4.googleusercontent.com/CNE5IMRBcgpUqG19eLGNb7jUAJhVbINHeE-P704KHLKrKuS34FvIybSt2sRnLs7T8ce5NqZzVylpMDbxZrgD6kFAwrM5DjeEcYSz4wD4Dp7Wsk9hLQEybGHBHq5PweDogqklxJSE)

![](https://lh3.googleusercontent.com/8lBlFXDMqIVD36lmMHauYcW0kMBJ_ei9Xd6VlNuB9G5hUTUg7-RbpXeKgHQb65W0lzd306m5XRU_zTYOAVsDXPI7RnVmRS1FFEVQgTp621sdXsih-AzPro9HO_C4FfdnjZGLVtXh)

![](https://lh6.googleusercontent.com/BoCNPGldylIDtfiZimxlL7Ar0QOic4kmWSRUXceMSvuAkOOIBezVUQAcbnEbRo2K66pomwSj5UZj_F0KW8GbtCxtgk_0sJFwyTsE20pbRof0kkzrnfL7X9ddIU45mzggOmYXttTT)

![](https://lh5.googleusercontent.com/phfelk3muuZTPQ9tgsgT9ig09LfgQlfS9oJFnlKm33AYK1F7yiWVpgmZtQ8Y_s1zo8_e0PfggUGzJwM24Xwmw9C8FkoNrsYk1z5ip5ognLyFWU4NDkKT9Do7JK0q_qyXj5YWyON4)

![](https://lh4.googleusercontent.com/XocI-D86LAbpgHuJ7y_FdcobwCOex6GJ-nAOgmOIFjagw2Kgc2zVAkjoEK5SjlqyArKFeImsrTdMfpGQ1DLZ9znqhxibjtS5LOLgTK4Zno7PA5kX4LAGmCv9zbak5_bET7FqCmLl)

Posted on 24\. June 2021
