---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-24_three-microsoft-store-vulnerabilites.md
original_filename: 2021-06-24_three-microsoft-store-vulnerabilites.md
title: Three Microsoft Store vulnerabilites
category: documents
detected_topics:
- command-injection
- business-logic
- api-security
- cloud-security
- mobile-security
tags:
- imported
- documents
- command-injection
- business-logic
- api-security
- cloud-security
- mobile-security
language: en
raw_sha256: 841a2bac2a2b6898ab7e03f90e03387a727654ea831c6cfe3d7dfa42b578bcb9
text_sha256: aad81da1f1e04fb4f72b5ada8465ac5f433137ef0c669c795541791dfe725641
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Three Microsoft Store vulnerabilites

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-24_three-microsoft-store-vulnerabilites.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, api-security, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `841a2bac2a2b6898ab7e03f90e03387a727654ea831c6cfe3d7dfa42b578bcb9`
- Text SHA256: `aad81da1f1e04fb4f72b5ada8465ac5f433137ef0c669c795541791dfe725641`


## Content

---
title: "Three Microsoft Store vulnerabilites"
url: "https://gccybermonks.com/posts/msstore/"
final_url: "https://gccybermonks.com/posts/msstore/"
authors: ["Marlon Fabiano (@astrounder)"]
programs: ["Microsoft"]
bugs: ["Payment tampering", "Logic flaw"]
publication_date: "2021-06-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3551
---

# [Three Microsoft Store vulnerabilites](https://gccybermonks.com/posts/msstore/)

Author: Marlon Fabiano

Description of the 3 vulnerabilities: “Generating invoices in the Microsoft Store without making purchases”, “Adding money in the Microsoft Store Wallet” and “Buying Definitive / Deluxe / Ultimate games for the price of a standard game”.

The summary of the steps of the two Bypass (purchases of infinite games and subscriptions within Microsoft’s sandbox) can be found at the link: <https://github.com/smarlonfabiano/xbox_xpl>

# Vulnerability 1

Understanding the vulnerability that allows you to generate invoices for Xbox games without buying them and the possibility to profit through the Nota Fiscal Paulista.

After bypassing the payment methods the first time and subscribing to the Gamepass subscription services through the Microsoft developers’ Sandbox, I found 3 other logic flaws in Microsoft’s payment processes.

One of the bugs allows a malicious agent to generate invoices for Xbox games even if the purchase is not made. This vulnerability could be used by a scammer to make money through Microsoft’s financial losses. Because there is a possibility through of the program called “Nota Fiscal Paulista” of the consumer to redeem part of the amount paid in tax.

As the Microsoft Store generates NFs without any kind of control, it is possible to try to buy games in pre-sale without paying for them and even when the game licenses are revoked due to non-payment, the scammer will receive the game invoice as if he made the purchase. And with that the Xbox will pay the tax amount of the game sold and the scammer can profit up to 30% of the value of the ICMS.

## Reproducing the Vulnerability

First, we need to remember one of the first vulnerabilities that I reported to Microsoft, where it was possible to buy games from the Microsoft Store without paying for them:

Reproducing the first vulnerability:

1 - We have registered a valid card in our Xbox Live or MSA account.

2 - We cancel and block the credit card at the issuing bank. We can also use a paypal account with no credit card registered or a prepaid credit card.

3 - Now with an invalid card, paypal account or prepaid card we can buy the games in pre-order. Since the charge can also be made 10 days before launch, we were able to download the games without having the game fee charged.

4 - The attempted debit of the registered card will be made 10 days before the launch of the game and you may receive several notifications informing you about the payment failure.

5 - At that moment, the first fault was found, since the product license was not revoked. Now, with the vulnerability fixed and the license revoked, we will not have access to the product, but the rest of the financial processes will continue regardless of whether the payment is made or not.

So when Microsoft revokes the game license, we can go to our MSA account and note that we will receive the product invoice without paying for it.

### Now understanding how to make money from the flaw:

1 - The malicious agent uses the bug to obtain multiple invoices without paying for the games.

Example: the attacker buys R$ 10,000 worth of games using multiple MSA accounts.

2 - Microsoft will generate the Invoice and pay R$ 1,700 to São Paulo (the rate is between 17%.).

3 - Even if payment for the games is not made, the malicious agent receives the invoices after having the game licenses revoked by Microsoft.

4 - The scammer enters the website <https://www.nfp.fazenda.sp.gov.br/login.aspx> and redeems R$ 510 from his CPF or CPF of a victim.

With that in mind, we can create multiple accounts and thus buy the same game multiple times:

* * *

1 MSA account buying R$ 10,000 will redeem R$ 510 with the Nota Fiscal Paulista

10 MSA account buying R$ 10,000 will redeem R$ 5,100 with the Nota Fiscal Paulista

* * *

Note: the minimum wage in Brazil is R $ 1,100. The scammer can reach almost 5 times that amount by applying scams at Microsoft

### PoC:

![](https://lh6.googleusercontent.com/zD0FKDF2kZ_rBVaae26D5WFoTYdg026a9qjfhywmBLj9yZ5L06PvX81sJiAZxmN4aznxXOAcKuQ-dv8RztVLWQ34YDQErDdBfnD3hNxLnvITQV-9LtrMNIOacn0K2-nPKBEgrGLb)

![](https://lh6.googleusercontent.com/NKIPBGwqfqMsxQEdlQVfLgeD5MMOE-KCQ2uL1Uq06HQNJHFkEyP8LeINzBH0sSj_q8CXuTVwN5-85hMVdc9e9tofd27p-SGL40iFilutmn5_3hy8wLQVuufGyKix6exOAAqgAIrQ)

![](https://lh4.googleusercontent.com/tZ4LCg7hgH3HYIU6OSeITDq7rWQw4pO0qNSdidtVGBg1OQOrHtNMNeSlqsRJTJ5dp50WNUs-LB9905GwAhVuOa5tRLBeSutbCqbDtRNCct13I59L7UmZYtfFneLtsXNaEohX4zL-)

Supporting materials/ references:

<https://portal.fazenda.sp.gov.br/servicos/nfp>[  
](https://portal.fazenda.sp.gov.br/servicos/nfp)<https://portal.fazenda.sp.gov.br/servicos/nfp/Paginas/Como-%C3%A9-feito-o-c%C3%A1lculo-do-cr%C3%A9dito.aspx>[  
](https://portal.fazenda.sp.gov.br/servicos/nfp/Paginas/Como-%C3%A9-feito-o-c%C3%A1lculo-do-cr%C3%A9dito.aspx)<https://epocanegocios.globo.com/colunas/Financas-de-Bolso/noticia/2017/01/como-ganhar-dinheiro-com-nota-fiscal-paulista.html>

# Vulnerability 2

Understanding the vulnerability that allows you to add infinite money to the Microsoft Store wallet:

Continuing the same reproduction of the previous bug: when we received the invoices for the purchased games, but we did not receive the purchased game.  
There is a period of time in which you can play the games purchased with the bug, which is from 1 to 3 days after its release. After that, the game license will be revoked and you will not be able to play it anymore. With that, there is a process that does the validation to identify if the user who received the invoice also received the game. If the user, even after receiving the invoice, has not yet received the game, the purchase price will be refunded to the registered credit card. However, as we do not have a valid card for the refund, we do not receive a refund.

To ease all this confusion with the purchase and to please your customer, Microsoft sends a “gift” of R$ 27.00. But what happens if we reproduce this same bug several times in a row? Well, here’s the answer:

## PoC:

![](https://lh3.googleusercontent.com/gGOzrrMW_xc2U4RXJywCzT2Mf3ioI1tZS_i7gJlenHWQiM8ue7zegKHMLi1OpV1vMzwR2lF5xR5Ub5FR8Zu-0_EBuqvTYQR83kXJ3gCu---6P9qVezVbJT-wkJquqV_Dauo_eFhk)

![](https://lh4.googleusercontent.com/IUski3S11GFLWPl_KUZfQXFuqCWmEzwo6BxJsBpmW8CFNHrN61gGOzXNhhD9VycNIyAseSWg9SaLeqd2frg58jZHZyd4WjhIGs8yhy7C8Okd4VcNowumV9gSgvStMsKji_D_HHaW)

![](https://lh5.googleusercontent.com/RncAA6EAvbJhE6nDZmVc03IQYabrVsXzjAqidbG8WcjxHj8mBxerbxYLWS3d3SjsDob0m-xJoIlpTmB6QX-VdnNVuurpLMVB08Nc0WvIxhoKc8QbWZtOQnH8fI-EL5zFyvhY3dbh)

![](https://lh6.googleusercontent.com/e9odTi7XKEu0l6ssU1vFhZoKMikxbzDckkoIbMiC9d19Y0yhCCqwRl06afj9DU0p6AxcaorzUoX_CpPUOaJfWI8C8yoMJxd9msQhvc6LvDXtx6-Msr7uQAF2m7pcW6CasHkTak08)

![](https://lh3.googleusercontent.com/oxyyTNnIgopoqjtD9do1_cqtSBJBttLSODW0CvpIJK8AK6JpLNF04r6CapTw0YID6R4UzixFceIqy-MX7XgjN11PR3IQgvLI5iTc-gjgxGMgSVLSzmyCz1B1GUz0sKLhG8K-NCxK)

![](https://lh5.googleusercontent.com/VJoHSiKDR0kUqffrDQdVUCBvnlTem98eFog7vpKCiyyqcdcap5jSTIkloas3GY1kPnUSJt3I27Z7HixzW9htu8wONlysD73oK_lNh5_uvM_vlJ3asFgAijt-16hFR_W5NHXsRoL0)

So it is possible to patiently perform this process several times to receive refund money.

A malicious agent could create multiple accounts, add money to those accounts’ wallet, and resell the store’s games. Because there is an option to buy the game as a gift, the games could be sent or sold to any Xbox Live user.

Another important point is that there is no segregation in Microsoft Store and Xbox stores. Therefore, if a good value is added to the user’s account, in addition to games, this user will be able to purchase licenses of Windows, Office 365, keyboard, mouse, notebooks, etc.

# Vulnerability 3

Understanding the vulnerability that allows you to buy Ultimate/Deluxe/Definitive games and pay only for the price of a Standard game:

Still following the same logic as the Bug. In addition to the two vulnerabilities above, I reported the vulnerability that allows me to buy Standard Edition games and enjoy the Ultimate Edition. How would it be?

## Reproducing the flaw

1 - Follow the same steps we used to generate invoices without paying for the game. The difference is that in this case we must choose the most expensive version of the game (remembering that this bug will work for pre-order games).

2 - Performing the test in the Watch Dogs Legion game in which the Standard edition costs R$ 279.95 and the Ultimate edition costs R$ 459.95.

![](https://lh6.googleusercontent.com/a6iQghgEuixP3WDE2UMlTVZTOuytVUxED3GtytnRUKiMF3i-1D88F1Q4tT3MrXKTFTh7_ZJVaKo2W08M38lsvLnJJZn1u-wQskefWY1SZaw2HsXWAPC3NNQ2ch5wDNmmnQ3-Z-WG)

![](https://lh3.googleusercontent.com/QRcfV46kvmJXINNL3GNqWCXCPEFDe0gbeSY9ZsAtc9I-iSDYKINVKo6j0POR6u_afdNQi4xAseRbwgYHIPTxS_sD4is9Xa5_SCovadHyYuZHWPZ0D1UbxGmddqavmZSJeJ0s12mw)

3 - We bought the Ultimate edition game with an invalid card and when this game is released we will have the license revoked. And if we try to play it after its release we will get the message that the game must be purchased again.

The problem is that Xbox revokes only the game license and not the license for premium content, Season Pass, DLCs, etc. So in this case, although we no longer have the base game license, we still have the license for all the rest of the premium content.

Now to enjoy the Ultimate edition game (R$ 459.95 value), we only need to buy the standard version of the game paying R$ 279.95. This gives us savings and losses for Microsoft/Ubisoft of R$ 180.00.

Posted on 24\. June 2021
