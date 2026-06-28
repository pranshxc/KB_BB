---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-29_xss-blind-stored-at-2-assets-tiktok.md
original_filename: 2022-06-29_xss-blind-stored-at-2-assets-tiktok.md
title: XSS Blind Stored at 2 Assets TikTok
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: 76ea7c4b639048108d4bf6c64fc6f90f77dd5974e289bf4d15165b741d13f926
text_sha256: 33c22ab741bbd38735607902a2d6662c0ee90d2d31aaf75b1fda29206945add0
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# XSS Blind Stored at 2 Assets TikTok

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-29_xss-blind-stored-at-2-assets-tiktok.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `76ea7c4b639048108d4bf6c64fc6f90f77dd5974e289bf4d15165b741d13f926`
- Text SHA256: `33c22ab741bbd38735607902a2d6662c0ee90d2d31aaf75b1fda29206945add0`


## Content

---
title: "XSS Blind Stored at 2 Assets TikTok"
url: "https://aidilarf.medium.com/xss-blind-stored-at-2-assets-tiktok-f32829f11e58"
authors: ["Aidil Arief"]
programs: ["TikTok"]
bugs: ["XSS"]
bounty: "1,000"
publication_date: "2022-06-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2499
scraped_via: "browseros"
---

# XSS Blind Stored at 2 Assets TikTok

XSS Blind Stored at 2 Assets TikTok
Aidil Arief
Follow
3 min read
·
Jun 29, 2022

160

Hi everyone,

In this article, I share the findings of XSS Blind Stored at 2 TikTok Assets.

Press enter or click to view image in full size

When I decided to hunt for bugs in the TikTok program, and I spent 1 month looking for this XSS.

This XSS finding started when I created a product on a TikTok seller account (https://seller-id.tiktok.com/)

I entered the XSS payload in the product name in the seller’s account.

Press enter or click to view image in full size

And the result is that there is no XSS on https://seller-id.tiktok.com/ that I get. And I decided not to continue looking for XSS there.

And the next day, when I continued testing on TikTok Android Apps assets, and I discovered the features of my product.

I tried to see the Product URL Location from the **Share** feature above.

And I get a URL of the form :

https://oec-api.tiktokv.com/view/product/1231414124124124

Press enter or click to view image in full size

And it turns out to be the same, there is no XSS here :(

I was silent for a moment and tried to see the view source of the page.

And apparently I found a vulnerable XSS snippet there in the form of:

<meta name='keywords' content='["><img src=x onerror=alert()>], TikTok, TokTok Shop' />

And that’s what made me give up, but after I know the snippet of the responses, I tried to change my product name from the TikTok seller account (https://seller-id.tiktok.com/).

Get Aidil Arief’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now I’m using an XSS payload with a single quote ( ‘ ) prefix :

‘><img src=x onerror=alert()>

And finally a pop up appears :)

Press enter or click to view image in full size

Let’s see the responses from view source:

<meta name=’keywords’ content=’[’><img src=x onerror=alert()>], TikTok, TokTok Shop’ />

And yes, there the ‘> prefix is ​​used to close the input value in the META TAG. And I got the XSS Blind Stored here.

I was overjoyed and immediately reported it to the TikTok team.

After I finished reporting the issue, I continued my testing, and it turned out that I found URLs for other TikTok assets that were affected by XSS in my initial findings.

The affected assets are https://shop.tiktok.com/

Press enter or click to view image in full size

I also reported this finding to the TikTok Team.

Report :

https://hackerone.com/reports/1554048

Affected Assets :

https://oec-api.tiktokv.com/

https://shop.tiktok.com/

Timeline :

Report : Apr, 29th

Fix & Resolved : May, 13th
