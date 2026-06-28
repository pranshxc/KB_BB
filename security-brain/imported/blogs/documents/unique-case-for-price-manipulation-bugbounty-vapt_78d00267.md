---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-18_unique-case-for-price-manipulation-bugbounty-vapt.md
original_filename: 2020-07-18_unique-case-for-price-manipulation-bugbounty-vapt.md
title: Unique Case for Price Manipulation | BugBounty | VAPT
category: documents
detected_topics:
- command-injection
- otp
tags:
- imported
- documents
- command-injection
- otp
language: en
raw_sha256: 78d002675927d70b2e4bab657e00e7414129ebfa5878f870ef7570964f4fc5f9
text_sha256: 9b460aae6b65ffe4dfd17ed1026b20fb8b416fcb706b6d0c11d130720d7211ee
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Unique Case for Price Manipulation | BugBounty | VAPT

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-18_unique-case-for-price-manipulation-bugbounty-vapt.md
- Source Type: markdown
- Detected Topics: command-injection, otp
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `78d002675927d70b2e4bab657e00e7414129ebfa5878f870ef7570964f4fc5f9`
- Text SHA256: `9b460aae6b65ffe4dfd17ed1026b20fb8b416fcb706b6d0c11d130720d7211ee`


## Content

---
title: "Unique Case for Price Manipulation | BugBounty | VAPT"
url: "https://medium.com/bugbountywriteup/unique-case-for-price-manipulation-bugbounty-vapt-df57637769cd"
authors: ["Harshit Sengar (@sengarharshit1)"]
bugs: ["Payment tampering"]
publication_date: "2020-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4400
scraped_via: "browseros"
---

# Unique Case for Price Manipulation | BugBounty | VAPT

Unique Case for Price Manipulation | BugBounty | VAPT
Harshit Sengar
Follow
3 min read
·
Jul 18, 2020

200

1

Press enter or click to view image in full size

Price Manipulation is a test case for Price Tampering. Generally, Penetration testers change the amount value of the product (i.e., shoes, tshirt, flight ticket, etc) from Rs.XXXX (or $XXXX) to Rs1 (or $1) in price tampering . And Sometimes, Penetration Testers change the Currency format means from Dollar to INR or others.

So, Here I am not gonna talk about above cases here. I found a unique case for price manipulation. I am not gonna paste here any POCs, Requests and Response. If you will have a doubt then contact me on Twitter or Linkedin.

I tested an E-Commerce web application. I tried all cases for price manipulation but got no success like I tried to change the product’s original amount value to 1 but it gave me error and I tried to change the currency format like Dollar to INR but got no success.

Then, I took my coffee and enjoyed it. Suddenly, I got an idea and tried over that application.

A product has some price and it’s 3 digit value like $999. when the request was going from burp suite and I changed it’s value to $100. Then, the request forwarded to payment gateway and Payment gateway was showing $100 that I had to be pay. But It was no successful attempt then I used my card and I got an OTP for paying $100. Then I realised that It was a successful attempt. but I didn’t pay $100 because It was too much amount if there was price manipulation vulnerability.

Get Harshit Sengar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now, I tried once again but this time, I changed the value 999 to 001 then Payment gateway was showing $1 and I used my card to pay then I got an OTP for paying $1.

Similarly, I bought 4digit dollar’s product at $1. How? It was so easy now.

I changed the amount value from 9999 to 0001.

So, the scenerio was that there was validation at server side and It validated the number of digit of the amount, not the amount value.

If you like it then do clap and share it.

Thanks guys! Hope, you enjoyed it.

You can Follow me on Twitter, Linkedin.
