---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-12_how-i-bought-vps-hosting-domain-only-001.md
original_filename: 2019-11-12_how-i-bought-vps-hosting-domain-only-001.md
title: How i Bought VPS, Hosting, Domain only $0.01
category: documents
detected_topics:
- sso
- command-injection
tags:
- imported
- documents
- sso
- command-injection
language: en
raw_sha256: 0aafe1097e2ee5b4f4412772c92f73b5fd3cd896f2f6de8faa640de64bb28d83
text_sha256: 367e9ff6993eb5e060958ac096ac0fb560c1f6c6114ce997c78abcc1ac2b5599
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How i Bought VPS, Hosting, Domain only $0.01

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-12_how-i-bought-vps-hosting-domain-only-001.md
- Source Type: markdown
- Detected Topics: sso, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `0aafe1097e2ee5b4f4412772c92f73b5fd3cd896f2f6de8faa640de64bb28d83`
- Text SHA256: `367e9ff6993eb5e060958ac096ac0fb560c1f6c6114ce997c78abcc1ac2b5599`


## Content

---
title: "How i Bought VPS, Hosting, Domain only $0.01"
page_title: "Got VPS, Hosting, Domain only $0.01 | Bug Bounty | by zer | Medium"
url: "https://medium.com/@androgaming1912/got-vps-hosting-domain-only-0-01-bug-bounty-edeea1a7d5e6"
authors: ["Zerb0a"]
bugs: ["Payment tampering"]
bounty: "500"
publication_date: "2019-11-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4950
scraped_via: "browseros"
---

# How i Bought VPS, Hosting, Domain only $0.01

zer
 highlighted

zer
Follow
2 min read
·
Nov 12, 2019

68

1

How i Bought VPS, Hosting, Domain only $0.01 | Bug Bounty

Helo Guys My Name is Rafli Pasya.
So This Story gonna Tell you how i Found the Simple Vulnerability with Huge Impact .
So okay let’s start My Story.

btw Guys i found this kind of vulnerability on 2 different Local Site.
1. redaced.net ( Online Store )
2. redaced.com ( Web Hosting Service )

That day I wanted to buy RDP for Recon. I visited the redacted.net website, there I saw the “Paypal Checkout” button. Usually Online Store only sends POST data to Paypal(/cgi-bin/webscr) including the amount that needs to be paid, I definitely can change the price.

Note: It’s Sometime Work with Braintrees Payments if there is no Filter / Validator After / Before Transaction.

The redacted.net send POST request to Paypal like this :

….&amount=1321&tax=12&….

if any hacker finds this request they will change the price and tax amount like this :
….&amount=0.01&tax=0&….

Get zer’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After Paid $0.01 I got an email from redacted.net that I paid the payment

I clicked The “Confirm My Payment” button then i saw my Order Changed To “Paid”.

The Seconds Bug I found at Hosting Service Provider.
This Website Didn’t Check Total Amout i have been Paid.
They Just Checking The Trx ID. if success they will Activate my Hosting…

Note: This Vulnerability Fixed on WHMCS, any Hosting provider using WHMCS is not vuln anymore because they check the Amount i paid.
if less than the total bill I have to pay off again.

I paid $0.01 For Rp 1.226.954 ( around $90-&95 )

I immediately Report This issue To Them, I Got Nice Bounty From Hosting Provider, the Online Store Give Me less xD ( Better Then not )

Timeline:
1 Nov 2019 = Found This Issue on redacted.net & then Report it.
2 Nov 2019 = Found This Issue on redacted.com & then Report it.
3 Nov 2019 = Bug Fixed & Awarded $500 from redacted.com
4 Now 2019 = Bug Fixed & Awarded Rupiah 1 Million from redacted.net

Thx For Reading this Write Up Guys !
Remember ! Always Read any Bug Bounty Write up on Pentester land . it’s usefull to help you
