---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-02-11_bugbounty-how-i-was-able-to-shop-for-free-payment-price-manipulation.md
original_filename: 2018-02-11_bugbounty-how-i-was-able-to-shop-for-free-payment-price-manipulation.md
title: '#BugBounty — “How I was able to shop for free!”- Payment Price Manipulation'
category: documents
detected_topics:
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 4346284cb07de68fa336abd2165e74de561a41bd3884e237b8b9943f6ca68951
text_sha256: 8388c5c90e06f6a01858a643e56a33c4944cda603033eb2fda1edfe36db1c571
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# #BugBounty — “How I was able to shop for free!”- Payment Price Manipulation

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-02-11_bugbounty-how-i-was-able-to-shop-for-free-payment-price-manipulation.md
- Source Type: markdown
- Detected Topics: command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `4346284cb07de68fa336abd2165e74de561a41bd3884e237b8b9943f6ca68951`
- Text SHA256: `8388c5c90e06f6a01858a643e56a33c4944cda603033eb2fda1edfe36db1c571`


## Content

---
title: "#BugBounty — “How I was able to shop for free!”- Payment Price Manipulation"
page_title: "#BugBounty — “How I was able to shop for free!”- Payment Price Manipulation | by Avinash Jain (@logicbomb) | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/bugbounty-how-i-was-able-to-shop-for-free-payment-price-manipulation-b29355a8e68e"
authors: ["Avinash Jain (@logicbomb_1)"]
bugs: ["Parameter tampering", "Payment tampering"]
publication_date: "2018-02-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5977
scraped_via: "browseros"
---

# #BugBounty — “How I was able to shop for free!”- Payment Price Manipulation

#BugBounty — “How I was able to shop for free!”- Payment Price Manipulation
Avinash Jain (@logicbomb)
Follow
2 min read
·
Feb 11, 2018

781

4

Hi Guys,

During my recent bug bounty hunt, I came across a critical and yet simple vulnerability.It was payment price manipulation through which I could buy any product at the minimal cost. So, lets see what was the whole vulnerability-

Get Avinash Jain (@logicbomb)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I had to buy a wedding suit to attend a wedding ceremony so I went over internet where I came across a popular Indian shopping site and started my hunt. For some days, I was looking to find some bug in payment gateways and this came at the exact right time. So I captured the request before it hit the payment gateway —

Press enter or click to view image in full size

Note the amount parameter carrying the amount to be paid which is here as “Rs. 1104.00” (INR) and without any hesitation, I tampered the price value , entered “119” which means 1.19 (INR) and forwarded the HTTP request. Next, I was redirected to bank payment page as you can see below -

Press enter or click to view image in full size

Whoaa! The final prize is “1.19” , I had a huge smile on my face and then I proceed further to get this —

Press enter or click to view image in full size
Order Successfully Placed

Order was placed successfully and I paid just 1.19 INR for 1104.00 INR :D. So simple yet so critical vulnerability and this happens when the prize is not validated back by the server. It was a surprise that still such simple loopholes exists and developers misses the validation of prize. Some secure steps that can be taken to prevent against such kind of attacks —

Always validate the prize back by the server.

Pull the prize from db and check whether it’s the same prize.

Refrain from sending amount in http request rather send only product id.

Thanks for reading!
This is all about this interesting finding. ☺

~Logicbomb ( https://twitter.com/logicbomb_1)(https://www.reddit.com/user/logicbomb_1/)
