---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-11_how-i-hacked-the-dutch-government-and-got-the-lousy-t-shirt.md
original_filename: 2022-12-11_how-i-hacked-the-dutch-government-and-got-the-lousy-t-shirt.md
title: How “I hacked the Dutch government and got the lousy t-shirt”
category: documents
detected_topics:
- xss
- command-injection
- otp
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- cloud-security
language: en
raw_sha256: 5aa5a3d8a14251a3e898065291de15d0e42a267bcc75fbdfd196243f5f79e81f
text_sha256: 69b09f73ecefe0a2235f44b22e0ac9379e6b72b2bf7c4c7549b4d560c66824d1
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: true
---

# How “I hacked the Dutch government and got the lousy t-shirt”

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-11_how-i-hacked-the-dutch-government-and-got-the-lousy-t-shirt.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, cloud-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: True
- Raw SHA256: `5aa5a3d8a14251a3e898065291de15d0e42a267bcc75fbdfd196243f5f79e81f`
- Text SHA256: `69b09f73ecefe0a2235f44b22e0ac9379e6b72b2bf7c4c7549b4d560c66824d1`


## Content

---
title: "How “I hacked the Dutch government and got the lousy t-shirt”"
page_title: "How I Hacked the Dutch Government | by IamDEAD | The Gray Area"
url: "https://medium.com/@Iam5345/how-i-hacked-the-dutch-government-and-got-the-lousy-t-shirt-81fd0a0dd84d"
authors: ["IamDEAD"]
programs: ["Dutch Government"]
bugs: ["XSS"]
publication_date: "2022-12-11"
added_date: "2022-12-12"
source: "pentester.land/writeups.json"
original_index: 1790
scraped_via: "browseros"
---

# How “I hacked the Dutch government and got the lousy t-shirt”

How I Hacked the Dutch Government
IamDEAD
Follow
3 min read
·
Dec 11, 2022

197

3

Press enter or click to view image in full size
Photo by Markus Spiske on Unsplash

Hello everyone! In this write-up, I will explain how I was able to find six vulnerabilities in the Dutch government, and how I was awarded cool swag for finding vulnerabilities on their website. In this write-up, I am going to share my experience hacking the Dutch government.

Motivation:

I went through a few blogs, and noticed this cool swag from the Dutch government. It was just mesmerizing to my eyes that the word “hacked the Dutch government” was cool, and I wanted it anyhow.

Scope:

After poking around the internet, I found some Github repositories on the penetration testing scope of the Dutch government. Here are a few of the ones I used →

https://gist.github.com/Zawadidone/***REDACTED-SUSPECT-TOKEN***https://gist.github.com/random-robbie/***REDACTED-SUSPECT-TOKEN***https://gist.github.com/R0X4R/***REDACTED-SUSPECT-TOKEN***GitHub - IamD345/Dutch-Government-Scope
You can't perform that action at this time. You signed in with another tab or window. You signed out in another tab or…

github.com

Reporting Findings:

You can report any findings on their official website HERE →

CVD-report form
In the event you find a technical vulnerability in one of the Dutch Central Government's systems, you can report the…

english.ncsc.nl

Tools I Used:

Aquatone

GitHub - michenriksen/aquatone: A Tool for Domain Flyovers
A Tool for Domain Flyovers. Contribute to michenriksen/aquatone development by creating an account on GitHub.

github.com

Gobuster

GitHub - OJ/gobuster: Directory/File, DNS and VHost busting tool written in Go
Directory/File, DNS and VHost busting tool written in Go - GitHub - OJ/gobuster: Directory/File, DNS and VHost busting…

github.com

Nmap

Nmap: the Network Mapper - Free Security Scanner
Get Nmap 7.93 here Nmap.org has been redesigned! Our new mobile-friendly layout is also on…

nmap.org

Waybackurl

GitHub - tomnomnom/waybackurls: Fetch all the URLs that the Wayback Machine knows about for a…
You can't perform that action at this time. You signed in with another tab or window. You signed out in another tab or…

github.com

The Process:

I had many domains to test, so I started with the Aquatone tool.

cat targets.txt | aquatone

Press enter or click to view image in full size

Then I selected some targets randomly, using Gobuster and Nmap on them. You can use some tools for the mass scans as well. No luck. Then I tried using Waybackurl and found some endpoints!

waybackurls example.nl > test.txt

cat test.txt | grep “query=”

Press enter or click to view image in full size

After this, I tried some XSS payload and bingo!

Press enter or click to view image in full size

I reported 3 RXSS 2 Information Leakage, and 1 Open Redirection. 4 others were duplicates or NA(static page). I was still happy with the 2 reports which got considered.

Press enter or click to view image in full size

Thanks for reading. I hope you enjoyed this blog. In the near future, I’ll write more blogs. That concludes the story of how I got my swag.

Get IamDEAD’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Gray Area is a collection of great cybersecurity and computer science posts. The best articles are highlighted in a weekly newsletter, sent out every Wednesday. To get updates whenever The Gray Area publishes an article, check out our Twitter page, @TGAonMedium.
