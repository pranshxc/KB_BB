---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-16_how-i-was-able-to-find-100-xss-in-united-nations-bug-bounty-program.md
original_filename: 2021-09-16_how-i-was-able-to-find-100-xss-in-united-nations-bug-bounty-program.md
title: How I was able to find 100+ XSS in United nations Bug Bounty Program
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- cloud-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- cloud-security
- supply-chain
language: en
raw_sha256: d762c184e3f31aed2b37ca3f2f172a61ce9d643c0b086bddfe0b847a32f2efcf
text_sha256: 26e7066defb2f37f80be05a83973c816a1e98d9f017c11636035e9559e47d0cd
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to find 100+ XSS in United nations Bug Bounty Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-16_how-i-was-able-to-find-100-xss-in-united-nations-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `d762c184e3f31aed2b37ca3f2f172a61ce9d643c0b086bddfe0b847a32f2efcf`
- Text SHA256: `26e7066defb2f37f80be05a83973c816a1e98d9f017c11636035e9559e47d0cd`


## Content

---
title: "How I was able to find 100+ XSS in United nations Bug Bounty Program"
url: "https://mrpentestguy.medium.com/how-i-was-able-to-find-100-xss-in-united-nations-bug-bounty-program-a675573c006d"
authors: ["mrpentestguy (@MR_iambatman)"]
programs: ["United Nations"]
bugs: ["XSS"]
publication_date: "2021-09-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3311
scraped_via: "browseros"
---

# How I was able to find 100+ XSS in United nations Bug Bounty Program

How I was able to find 100+ XSS in the United nations Bug Bounty Program
mrpentestguy
Follow
3 min read
·
Sep 16, 2021

201

2

Hey, Guys so this is my first blog. so I thought maybe give it try to show people how you could find bugs in an easy way

So let's get started

First After my recon for 4 days. I started to look for URLs. URLs of your choice may be from Wayback or live URLs from the website by crawling. so first I started for archive ones

For that, you could any tools of your choice. but for me, I used 2 two tools. Those are waybackurls and gau. I choose these two tools both combined like I would take URLs from both of them because of the fact. when I did my recon and send those subs to these tools. I have found out that both of these tools would give me new or different URLs and it kind of differs from the number of URLs found. Sometimes I would be getting more URLs from waybackurls tool written by tomnomnom other times i would be getting from gau. So yeah I kinda mix them and use them together.

So After i got all my urls i started for hunting XSS . My methology is different. I would look for only one type of bug for a long period of time . So I found a wooping of 1700000 urls at the end .

Now what Since I got my urls . I started using kxss this also amazing tool which was written by tomnomnom and I stored all the urls which were reflecting certain Unfiltered special characters . Now I picked those urls from it and started using dalfox .

You could use it as

Get mrpentestguy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

cat urls.txt | kxss | awk ‘{print $4}’| sort -u >> xss_list.txt

or you can pipe it to dalfox directly as well which is up to you

cat urls.txt | kxss | awk ‘{print $4}’| sort -u | dalfox pipe -b <you blind xss> — custom-payload <your payload> -w 300 — multicast — mass — only-poc -o xss_vulns.txt

Here I found a xss with my custom payloads list i have created on my own .But one thing that striked me that the end parameter “lng” called language was found in 300+ urls from one domain lets say reacted.com and when i started to find if all the lng parameter were vulnerable or not . To me Only 179 urls were vulnerable since those urls exits . The reset of the urls didn’t exist or return 404 .

The Funny thing was i able to find xss in 404 pages as well since it would not be vulnerable because there is nothing to exploit on the page .

Finally submitted to them in March -5th .

Was given hall of fame in April 22nd

Press enter or click to view image in full size
Press enter or click to view image in full size

Thank you for reading
