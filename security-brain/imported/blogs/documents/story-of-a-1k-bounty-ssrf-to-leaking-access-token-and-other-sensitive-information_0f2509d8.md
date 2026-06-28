---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-05_story-of-a-1k-bounty-ssrf-to-leaking-access-token-and-other-sensitive-informatio.md
original_filename: 2022-11-05_story-of-a-1k-bounty-ssrf-to-leaking-access-token-and-other-sensitive-informatio.md
title: Story of a $1k bounty — SSRF to leaking access token and other sensitive information
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- mfa
- otp
- automation-abuse
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- mfa
- otp
- automation-abuse
language: en
raw_sha256: 0f2509d830576ae6ffae23ec0e7f0907e5b6c8a661c24f1b4ee803ac2d39e28a
text_sha256: 5e7723930bf6d0ce2a719fbb78e3501361f72da75cf0a6820e175eac02168e71
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Story of a $1k bounty — SSRF to leaking access token and other sensitive information

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-05_story-of-a-1k-bounty-ssrf-to-leaking-access-token-and-other-sensitive-informatio.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, mfa, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `0f2509d830576ae6ffae23ec0e7f0907e5b6c8a661c24f1b4ee803ac2d39e28a`
- Text SHA256: `5e7723930bf6d0ce2a719fbb78e3501361f72da75cf0a6820e175eac02168e71`


## Content

---
title: "Story of a $1k bounty — SSRF to leaking access token and other sensitive information"
url: "https://infosecwriteups.com/story-of-a-1k-bounty-ssrf-d5c4868680f5"
authors: ["Faique (@imfaiqu3)"]
bugs: ["SSRF"]
bounty: "1,000"
publication_date: "2022-11-05"
added_date: "2022-11-08"
source: "pentester.land/writeups.json"
original_index: 1946
scraped_via: "browseros"
---

# Story of a $1k bounty — SSRF to leaking access token and other sensitive information

Story of a $1k bounty — SSRF to leaking access token and other sensitive information
Faique
Follow
4 min read
·
Nov 5, 2022

538

7

Press enter or click to view image in full size

Hello and welcome everyone to my story of how I got my first bounty on HackerOne by exploiting an SSRF that leaked Google cloud access token and other sensitive data, Before moving forward I would like to thank this sweet community that has helped me in my overall journey.

I chose the target from my HackerOne’s private invitation list, therefore I cannot the disclose the target and so I’ll call it redacted.com. I started with recon, I created an automation tool that do my recon process like gathering subdomains, getting live hosts, running nuclei , directory brute forcing, nmap and getting waybackurls etc. After my automation was done i analyzed all the data like waybackurls and others.

The waybackurls seemed interesting so I quickly used gf patterns to get all ssrf endpoints that could be vulnerable

cat waybackurl | gf ssrf
Press enter or click to view image in full size

As the __host field fetches some kind of data from the github, I tried testing ssrf, So I quickly opened my Burpsuite and put the burp collaborator link in the __host field and send the request, I clicked on poll now button and yes I got an HTTP interaction and the burp collaborator response was reflected on the screen.

Press enter or click to view image in full size

I tried XSS with it by firing up an Apache server and uploading alert JavaScript payload

Press enter or click to view image in full size

But i stopped because XSS won’t be so impactful and started to look for ssrf, In the __host parameter I put 169.254.169.254 and in the url I added /latest/meta-data/iam/security-credentials/

https://redacted.redacted.com/latest/meta-data/iam/security-credentials/?__host=169.254.169.254&__proto=https

and sent the request. But it returned 502 BAD Gateway I then changed __proto value to http but it didn’t either worked.

Then I though of why not try other endpoints like google, digital ocean one’s, I took a help of a pdf that has all ssrf endpoints that I will provide down and finally google cloud endpoint gave a response other than 502.

Get Faique’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The response contained

Missing required header: Metadata-Flavour
Press enter or click to view image in full size

So I quickly added this header and set the value of it to Google(took help from pdf) and send the request and yesss!! it did work

Press enter or click to view image in full size

I then tried to get access token using

GET /computeMetadata/v1/instance/service-accounts/default/token?__host=169.254.169.254&__proto=http

I screamed woah!! I got it, SSRF achieved :)

Press enter or click to view image in full size

I tried and got other details like scopes, emails, region and id etc.

Reporting

I reported the vulnerability with all the Pocs and waited until next day, they responded & acknowledged it as a cool finding and rewarded me with $1000 bounty

Press enter or click to view image in full size

PDF: SSRF.pdf

Thank you for reading till here, I hope you guys learned something new from the write up. If you enjoyed make sure to give a clap and follow me on:

Twitter: https://twitter.com/imfaiqu3
Instagram: https://www.instagram.com/faique.exe
LinkedIn: https://www.linkedin.com/in/faiqu3/
From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!
