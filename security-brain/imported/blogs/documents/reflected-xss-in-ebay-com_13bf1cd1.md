---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-22_reflected-xss-in-ebaycom.md
original_filename: 2019-07-22_reflected-xss-in-ebaycom.md
title: Reflected XSS in Ebay.com
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
raw_sha256: 13bf1cd1bbadccf361d64cdd9816ac86a79ce3e61a471d1f7eb86f2d44fe6cb8
text_sha256: ee2599df774cb0b1ea9b64ff2bab363a58142102702ad9ced7a004220de03e90
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Reflected XSS in Ebay.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-22_reflected-xss-in-ebaycom.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `13bf1cd1bbadccf361d64cdd9816ac86a79ce3e61a471d1f7eb86f2d44fe6cb8`
- Text SHA256: `ee2599df774cb0b1ea9b64ff2bab363a58142102702ad9ced7a004220de03e90`


## Content

---
title: "Reflected XSS in Ebay.com"
url: "https://medium.com/@madguyyy/reflected-xss-in-ebay-com-60a9d61e26cd"
authors: ["Sukhmeet Singh (@MadGuyyy)"]
programs: ["Ebay"]
bugs: ["Reflected XSS"]
publication_date: "2019-07-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5129
scraped_via: "browseros"
---

# Reflected XSS in Ebay.com

Reflected XSS in Ebay.com
Sukhmeet Singh
Follow
3 min read
·
Jul 23, 2019

20

Press enter or click to view image in full size

In Sept. 2013 I found Reflected XSS in www.ebay.com. Why writing it up now? Because I didn’t want to “showoff” for reasons. Enough with the drama :D. Let’s get to the point.

So I was looking at all the names in Hall of fame of different sites. On Ebay’s Security Researcher page, I thought the list is long but I want my name in the list.

So I started playing with all the GET parameters and came to this possibly vulnerable page.

URL: http://www.ebay.in/sch/Coins-Notes-/11116/i.html

Vulnerable parameter: LH_SpecificSeller

Get Sukhmeet Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Reflected Code:

<span style="display:none">
<span title='XSS HERE'> XSS HERE </span>
</span>

List of hurdles:

< > and , are removed
Affected area lies within hidden span (display: none, no mouse events)

Because parent span had CSS style display: none , it was not possible to trigger event. Neither it was possible to make the affected span visible because of the same reason. Though I tried it by adding style attribute. I tried all other payload, say it be onload / onerror events or data: URI in style attribute. But after a little research; OK OK after 8 hours of research I came upon a CSS expression payload.

http://www.ebay.in/sch/Coins-Notes-/11116/i.html?LH_SpecificSeller=1..xss'+style="xss:expression(prompt(1))"+id='1
Press enter or click to view image in full size

Aaand it worked! Not in Firefox and Google Chrome, but in Internet Explorer. Yes I had to use Internet Explorer because of compulsion. But that was enough for me.

So I reported it and after a month they fixed it and I got a reply from them.

Press enter or click to view image in full size

and that’s how I got my name in the list. Here it is.
