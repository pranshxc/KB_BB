---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-29_part-2.md
original_filename: 2022-01-29_part-2.md
title: Part 2
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
raw_sha256: cea7656cc3622c6c9e074fef3f9426b410de968ec32dc8591d349e058b39a72f
text_sha256: 65f01e9f1b2c8b39e1a45faabfb0b305bf13899e2eb2aaba963a5f8e03be8299
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Part 2

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-29_part-2.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `cea7656cc3622c6c9e074fef3f9426b410de968ec32dc8591d349e058b39a72f`
- Text SHA256: `65f01e9f1b2c8b39e1a45faabfb0b305bf13899e2eb2aaba963a5f8e03be8299`


## Content

---
title: "Part 2"
page_title: "How I Made $16,500 Hacking CDN Caching Servers — Part 2 | by bombon | InfoSec Write-ups"
url: "https://bxmbn.medium.com/how-i-made-16-500-hacking-cdn-caching-servers-part-2-4995ece4c6e6"
authors: ["Kevin (@bxmbn)"]
bugs: ["Web cache poisoning", "Stored XSS", "Web cache deception"]
bounty: "16,500"
publication_date: "2022-01-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2967
scraped_via: "browseros"
---

# Part 2

Top highlight

How I Made $16,500 Hacking CDN Caching Servers — Part 2
@bxmbn
bombon
Follow
2 min read
·
Jan 29, 2022

539

3

A Nice Way To Hide XSS

Bounty: $2,000

While Google Dorking, i found a particular URL, but this time, was not being cached, but if i added an cacheable extension file (.js , .css) at the end of URL, it would cache the response.

Now, all i needed was to found a XSS. I found an injection point on a Cookie, but WAF would trigger when i added anything after %20

Cookie: cookiename=xss</script%20

While trying to bypass the WAF, I realized that my IP was also being reflected on that same script..

guid="</script ","24.99.19.20"

Since my IP was being reflected, I tried “X-Forwarded-For” Headers, this way i can close the <script> and avoid WAF, as it would trigger if it detected <[anything]>

Get bombon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This is why you will see 3 “X-Forwarded-For” Headers

Request:
GET /xxx/xx/xxx.xx/x.js?t=2021111121 HTTP/2 
Host: Redacted
X-Forwarded-For: xss 
X-Forwarded-For: xss><svg/onload=globalThis[`al`+/ert/.source]`1`// X-Forwarded-For: > 
Cookie: gdId=xss</script%20
Response:
...
guid="</script ","24.99.19.20","xss","xss><svg/onload=globalThis[`al`+/ert/.source]`1`//,">
...

After Poisoned an URL with an XSS, an attacker just needed to send it to the victim

redacted.com/xxx/xx/xxx.xx/x.js?t=2021111121

A nice way to hide XSS :D

This was my favorite Cache Poisoning, and it was found on a Public Program

https://hackerone.com/reports/1424094

Timeline:

Reported → December 11, 2021

Triaged → December 14, 2021

Bounty Awarded → January 7, 2022

Fixed → March 7, 2022

Next:

Part 3: Cache Poisoning DoS Via X-Forwarded-Scheme Header

🔈 🔈 Infosec Writeups is organizing its first-ever virtual conference and networking event. If you’re into Infosec, this is the coolest place to be, with 16 incredible speakers and 10+ hours of power-packed discussion sessions. Check more details and register here.
IWCon2022 - Infosec WriteUps Virtual Conference
Network With World's Best Infosec Professionals. Find How Cybersecurity Pros Achieved Success. Add New Skills to Your…

iwcon.live
