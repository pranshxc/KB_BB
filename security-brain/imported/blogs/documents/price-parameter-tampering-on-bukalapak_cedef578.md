---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-24_price-parameter-tampering-on-bukalapak.md
original_filename: 2019-07-24_price-parameter-tampering-on-bukalapak.md
title: Price Parameter Tampering On Bukalapak
category: documents
detected_topics:
- command-injection
- business-logic
- mobile-security
tags:
- imported
- documents
- command-injection
- business-logic
- mobile-security
language: en
raw_sha256: cedef578e80fa47ab8d98df8c78b8229bcb401a4067115176729912a2b61cf41
text_sha256: 597cd2ccb355ec018e08d390f1908a4e603848c3965ed3b45f2b1c2234e32396
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Price Parameter Tampering On Bukalapak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-24_price-parameter-tampering-on-bukalapak.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `cedef578e80fa47ab8d98df8c78b8229bcb401a4067115176729912a2b61cf41`
- Text SHA256: `597cd2ccb355ec018e08d390f1908a4e603848c3965ed3b45f2b1c2234e32396`


## Content

---
title: "Price Parameter Tampering On Bukalapak"
page_title: "Price Parameter Tampering On Bukalapak – Apapedulimu"
url: "https://apapedulimu.click/price-parameter-tampering-on-bukalapak/"
final_url: "https://apapedulimu.click/price-parameter-tampering-on-bukalapak/"
authors: ["apapedulimu / Nosa Shandy (@LocalHost31337)"]
programs: ["Bukalapak"]
bugs: ["Parameter tampering", "Payment tampering"]
bounty: "150"
publication_date: "2019-07-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5123
---

![Is this parameter tampering ?](https://apapedulimu.click/wp-content/uploads/2019/06/meme-is-this-680x510.png)

# Price Parameter Tampering On Bukalapak

On the Thursday night, I feel boring on my rooms and then I try to do something to make my time is more valuable. After that I’m thinking of “**How about I testing Bukalapak** ” . Not on the website application, But on their Mobile Application, although I’m not expert at all and just testing on their traffic from the Mobile Application to server.

I start hunt bug just trying to figured what’s the feature I should test, with the feeling of course. Long story short, I take a look on the feature called **“Buka Pengiriman”** In this feature, seller can pay the shipping fee on bukalapak and the shipping expedition will come to seller place to pick up the goods without request payment.

After now know the system work, I start thinking do this can be vulnerable on **Parameter Tampering,** Because I read a lot of the Parameter Tampering but have no luck to found one of them.

And then I start to launch the parameter tampering attack on the endpoint _**https://api.bukalapak.com/open-shipments/transactions ,**_ because I take a look on the system, this endpoint include the Price and the endpoint exist before system redirect to payment page.

![Vulnerable Endpoint Price Parameter Tampering](https://apapedulimu.click/wp-content/uploads/2019/06/parameter-tampering-copy.png)Vulnerable Endpoint Price Parameter Tampering

And then when I trice to change the value of **shipping** and **total** parameter to 10, the response is also turning to **10.** Hmmm, do this is really Vulnerable to Price Parameter Tampering ?

![Is this parameter tampering ?](https://apapedulimu.click/wp-content/uploads/2019/06/meme-is-this.png)Is this parameter tampering ?

Because I’m not sure, I take a look on the my payment page to see there’s a some invoice with the following price?

![Price on Payment page](https://apapedulimu.click/wp-content/uploads/2019/06/ss-parameter-tampering.jpg)Price on Payment page

Okay, this is on the payment page. But, I still not sure if this can be valid. So, I try to pay the invoice and the status is return to **SUCCESS.** And I was like :

[Asiap GIF](https://tenor.com/view/asiap-gif-13598855) from [Asiap GIFs](https://tenor.com/search/asiap-gifs)

And then after that, I start make some report to Bukalapak.

After long day no response, I ping up again to ask about the bounty, and they said it’s eligible for bounty and proceed the bounty soon. Long story short, the bounty of the Price parameter tampering on the Bukalapak is : **2.000.000 IDR** or around**150$**( Not include the tax).

### Timeline :

  * Reported – Mar 7, 2019
  * Validated Valid – Mar 12, 2019
  * Rewarded – May 13, 2019
  * Fixed – July 24, 2019

## Published by

![](https://secure.gravatar.com/avatar/4a2c0028ce53c37ad1d454a4dd5fb9ef9b89570464cdfbbc14e7e4914a284f17?s=56&d=mm&r=g)

### apapedulimu

Urip Kui Urup [ View all posts by apapedulimu ](https://apapedulimu.click/author/apapedulimu/)

Posted on [July 24, 2019February 12, 2020](https://apapedulimu.click/price-parameter-tampering-on-bukalapak/)Author [apapedulimu](https://apapedulimu.click/author/apapedulimu/)Tags [Parameter Tampering](https://apapedulimu.click/tag/parameter-tampering/)
