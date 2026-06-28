---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-29_how-i-found-my-first-idor-in-hackerone.md
original_filename: 2021-07-29_how-i-found-my-first-idor-in-hackerone.md
title: How I found my first IDOR in HackerOne
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- automation-abuse
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- automation-abuse
language: en
raw_sha256: 44f7ff85d4ee439cb2d650f70963c7f47c850b071e65e05a3e953ea02467b206
text_sha256: 9a60e02f1ef50aca965c358f8944cef849d7eac00b0d2bfb8059840d6c1e9151
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I found my first IDOR in HackerOne

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-29_how-i-found-my-first-idor-in-hackerone.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `44f7ff85d4ee439cb2d650f70963c7f47c850b071e65e05a3e953ea02467b206`
- Text SHA256: `9a60e02f1ef50aca965c358f8944cef849d7eac00b0d2bfb8059840d6c1e9151`


## Content

---
title: "How I found my first IDOR in HackerOne"
url: "https://n1ghtmar3.medium.com/how-i-found-my-first-idor-in-hackerone-5d5f17bb431"
authors: ["N1GHTMAR3 (@n1ghtmar3_2421)"]
bugs: ["IDOR"]
publication_date: "2021-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3466
scraped_via: "browseros"
---

# How I found my first IDOR in HackerOne

How I found my first IDOR in HackerOne
N1GHTMAR3
Follow
2 min read
·
Jul 28, 2021

230

In the name of Almighty, Allah, i begin. This write up is about how I found my first IDOR in HackerOne and got my first swag.

Get N1GHTMAR3’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Recently I got BugBountyHunter subscription and so I tried to test what I learnt from there in h1 programs. Normally, I create two account while testing and passing everything through Burp suite. And try to create both of them with same username using Null byte at the end. But in this case nothing worked. So now I searched every request which had my user-id using the HTTP History tab and used Match and Replace from the option and changed my first account user-id with second account user-id to check if I got any 200 OK response back(easy way to find IDOR I suppose)

Press enter or click to view image in full size
Burp Suite Match and Replace

But unfortunately this method didn’t work as well. Then I tried looking for upload vulnerabilities and there was an option where an user needed to upload payment receipt to verify he is legit customer. So I checked the url of the uploaded image and there was an id value which was in simple numerical value looking like this https://target.com/attachments/registrations/{numerical_value}/proof_of_purchases/view/original . So I immediately uploaded another picture from the 2nd account and tried to view the 2nd account’s url with the 1st one and BoOm! So now to show more impact I brute force the ‘numerical_value’ in intruder and all the 200 response contained customer signature, paypal address,home address etc. Then I tried to check if image metadata was handled properly as recently I read this report https://hackerone.com/reports/906907. So I downloaded picture from this repository https://github.com/ianare/exif-samples/tree/master/jpg/gps and uploaded it. Now downloaded my uploaded picture from the url and used exiftool to check the metadata was stripped but to my surprise it didn’t stripped anything as you can see GPS location is still present

Press enter or click to view image in full size

So I chained the IDOR with exif-metadata and it got triaged as High Severity. And got my first swag. It was uncommon for me as normally I look for IDOR where only my user-id is used. But in this case IDOR was in image id. So, don’t forget to check every endpoint. Happy Hacking
