---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-09-24_filter-bypass-to-reflected-xss-on-httpsfinanceyahoocom-mobile-version.md
original_filename: 2017-09-24_filter-bypass-to-reflected-xss-on-httpsfinanceyahoocom-mobile-version.md
title: Filter Bypass to Reflected XSS on https://finance.yahoo.com (mobile version)
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 41fda787332b419ba64c6859874c4c9bf5fc338d9b48f644a033343fc19146f0
text_sha256: 60de37cf394b4ffb2954de2dd19546fd38e50c6af9efad1b37a56438f1823a3e
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Filter Bypass to Reflected XSS on https://finance.yahoo.com (mobile version)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-09-24_filter-bypass-to-reflected-xss-on-httpsfinanceyahoocom-mobile-version.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `41fda787332b419ba64c6859874c4c9bf5fc338d9b48f644a033343fc19146f0`
- Text SHA256: `60de37cf394b4ffb2954de2dd19546fd38e50c6af9efad1b37a56438f1823a3e`


## Content

---
title: "Filter Bypass to Reflected XSS on https://finance.yahoo.com (mobile version)"
url: "https://medium.com/@saamux/filter-bypass-to-reflected-xss-on-https-finance-yahoo-com-mobile-version-22b854327b27"
authors: ["Samuel (@saamux)"]
programs: ["Yahoo! / Verizon Media"]
bugs: ["Reflected XSS"]
publication_date: "2017-09-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6090
scraped_via: "browseros"
---

# Filter Bypass to Reflected XSS on https://finance.yahoo.com (mobile version)

Filter Bypass to Reflected XSS on https://finance.yahoo.com (mobile version)
Samuel
Follow
3 min read
·
Sep 25, 2017

726

2

Today I‘ll share with you a interesting XSS in Yahoo. My favorite target is Yahoo, because they have a big scope, so let’s start.

In the hunting process, I detected some websites that are responsive in a mobile way. Not always the vulnerabilities that are detected in a website are reflected in the mobile version. I tried to find any bug on the website https://finance.yahoo.com, but I didn’t find anything :(, so, I decided to find bugs in the mobile version of this website.

Press enter or click to view image in full size
Mobile Version Finance Yahoo

Until I found a very interesting endpoint

https://finance.yahoo.com/quote/xxxxxxxxyyyyzzzzzz

Press enter or click to view image in full size

In this endpoint, everything I wrote using the URL was reflected in the website, although through this, I could have done a Content Spoffing, I didn’t do it since this has no impact for Yahoo and it is also out scope, so my other option was to test an XSS, which I did with the next payload

https://finance.yahoo.com/quote/"><svg onload=alert(1)>

Press enter or click to view image in full size

For my luck in the source code I realized that the characters “>< were processed, then I could execute an XSS, however I did not understand at first, why XSS did not work, being that the attack vector was correct. Well, then I understood, that I had to close the </script> tag so that the XSS would work. and then…

Press enter or click to view image in full size

Not running :(

Get Samuel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Well, I started to study the behavior of this XSS, and I realized that the payload was processed in capital letters, and well, I noticed that a payload in capital letters does not work. I just needed the word “alert” to be processed in lowercase. Then I came up with an HTML character encoding.

Lowercase Coding

alert

Coding

&#97;&#108;&#101;&#114;&#116;

New Payload XSS

https://finance.yahoo.com/quote/"></script><svg onload=%26%2397%3B%26%23108%3B%26%23101%3B%26%23114%3B%26%23116%3B(document.domain)>

Press enter or click to view image in full size

: O: O: O and happiness came into my life :D.

Thanks

Twitter: @saamux
