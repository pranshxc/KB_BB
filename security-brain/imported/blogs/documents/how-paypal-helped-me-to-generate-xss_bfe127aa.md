---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-20_how-paypal-helped-me-to-generate-xss.md
original_filename: 2019-10-20_how-paypal-helped-me-to-generate-xss.md
title: How PayPal helped me to generate XSS
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: bfe127aa0b5215b5ac7d282363c0c3978ca085237637d5672a7a941befa391e2
text_sha256: 7dbb0375a6e7b30a549f52f52c4dd99ea120877d58fc8b78fa545e39679642bd
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How PayPal helped me to generate XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-20_how-paypal-helped-me-to-generate-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `bfe127aa0b5215b5ac7d282363c0c3978ca085237637d5672a7a941befa391e2`
- Text SHA256: `7dbb0375a6e7b30a549f52f52c4dd99ea120877d58fc8b78fa545e39679642bd`


## Content

---
title: "How PayPal helped me to generate XSS"
url: "https://medium.com/@pflash0x0punk/how-paypal-helped-me-to-generate-xss-9408c0931add"
authors: ["Pflash Punk (@PflashPunk)"]
programs: ["Paypal"]
bugs: ["Reflected XSS"]
bounty: "250"
publication_date: "2019-10-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4980
scraped_via: "browseros"
---

# How PayPal helped me to generate XSS

How PayPal helped me to generate XSS
Pflash Punk
Follow
2 min read
·
Oct 20, 2019

167

2

Hi ,

I was on break for a year because of my dad’s health issue :(
But now I’am back :D

This is my first write up on medium.com , its a old finding but may help you ;)

Ok. So one day I was doing some work with my friend and visited PayPal to get a Pay with PayPal button.

I logged in to PayPal and moved to tools section and clicked on PayPal buttons. After clicking PayPal redirected me to https://financing.paypal.com/ppfinportal/adGenerator

Here we can create buttons.

While generating a button I looked on the URL bar and got excited.

Get Pflash Punk’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The URL was some thing like this https://financing.paypal.com/ppfinportal/adGenerator/emailCopy?size=320x200

The banner size was in url .So i decided to test it.

I’ve changed the size to LOL

and got surprised , the width size in embed code changed to LOL

Now what :P
I’ve changed LOL string to a XSS payload and the size became “><img src=x onerror=prompt(1)>

Now the size in embed code became “><img src=x onerror=prompt(1)> . Which means if you’ll use the infected embed code you’ll be greeted by XSS popup :P

Press enter or click to view image in full size

Look at the embed code carefully :P

So this accidental XSS gave me 250$ :D
