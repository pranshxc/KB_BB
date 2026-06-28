---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-25_how-i-got-4000-from-visma-for-rce.md
original_filename: 2018-09-25_how-i-got-4000-from-visma-for-rce.md
title: How I got $4000 from Visma for RCE
category: documents
detected_topics:
- command-injection
- xss
- file-upload
- api-security
tags:
- imported
- documents
- command-injection
- xss
- file-upload
- api-security
language: en
raw_sha256: 364b386de69220ce9e9aa8afaf9c5b1f8e7a2720e955e4d8b7275348a23b36e3
text_sha256: 0cdca332528fbc29bb285b90546988b67738089f4b32b229aa3536812108af1a
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I got $4000 from Visma for RCE

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-25_how-i-got-4000-from-visma-for-rce.md
- Source Type: markdown
- Detected Topics: command-injection, xss, file-upload, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `364b386de69220ce9e9aa8afaf9c5b1f8e7a2720e955e4d8b7275348a23b36e3`
- Text SHA256: `0cdca332528fbc29bb285b90546988b67738089f4b32b229aa3536812108af1a`


## Content

---
title: "How I got $4000 from Visma for RCE"
url: "https://medium.com/@ratnadip1998/how-i-got-4000-from-visma-for-rce-d541e6042086"
authors: ["Ratnadip Gajbhiye (@scspcommunity)"]
programs: ["Visma"]
bugs: ["RCE"]
bounty: "4,000"
publication_date: "2018-09-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5680
scraped_via: "browseros"
---

# How I got $4000 from Visma for RCE

Ratnadip Gajbhiye
Follow
3 min read
·
Sep 25, 2018

461

7

How I got $4000 from Visma for RCE

Hello friends,
This is Ratnadip Gajbhiye.
This is my first article, so if there is any mistake in it forgive me.

I’m not telling any story about my life and I also know you don’t intrested to listen who am i..😋

I always believed that sharing is caring,
so i decided to share my findings with you as it might help others who started in the Bug Bounty journey.

As you already know We are seeing a lot of noise again regarding the Uploadify script vulnerabilities affecting some WordPress themes/plugins.

What is Uploadify :-
Uploadify allows anyone to upload anything they want to your site without any authentication.

First of all, I want to tell you that ... before entering a bug Bounty field, I was a black hat hacker and I hacked and defaced many websites ... so I have information about that How to upload shell in the website...

I always use black hat techniques for hunting bug like admin panel bypass etc... :V

I never Target a main domain, i always Target subdomain..😅

So one of my friend Ma*** gave me this site for security testing..
And I target subdomain of that site..

Ex.
https://visma.com
https://citrix.visma.com

So now here is the main Part of this article
how I detect site for RCE and upload a shell less than 10 minutes.

Get Ratnadip Gajbhiye’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I searched for admin panel
Ex:- https://citrix.visma.com/admin
And its redirect me to WordPress admin panel.. 😍
I have some idea about how to find a theme and plugins error using exploit-db ..🤗
So I tried to exploit the theme error using Dorks, I put 4 Dorks in the URL but I did not get success, then I filed the 5th Dork in the URL and I got the upload section.
Without wasting any time I upload a c99.php shell in website and I got access of hole server 😎

Proof of Concept :-
Remote Code Execution via Arbitrary File Upload

# Exploit Title : Wordpress Themes Konzept File Upload Vulnerability
# Author : Ratnadip Gajbhiye
# Google Dork: wp-content/themes/konzept
# Tested on: Lubuntu

# [!] Exploit : Upload section URL
https://citrix.visma.com//wp-content/themes/konzept/includes/uploadify/uploadify.php

# [!] File Location : C99 Shell URL
https://citrix.visma.com//wp-content/themes/konzept/includes/uploadify/uploads/c99_locus7s.php

Press enter or click to view image in full size

Day 1 :- After reporting this to site got their reply in 5 min. :p
Thank you for your report we have passed to your IT team for fixing it ASAP
and Vulnerability is fixed within 2 Hours.

Day 2 :- The hole has now been patched and the shell is removed, but it will probably require some more time to go through the server before declaring it properly secured again.😏

Day 3 :- discussing with their management department for cash reward. 🤨

Day 4 & 5 :- No reply 😐

Day 6 :- Thank you for your patience in this matter. I’m happy to tell you that we have awarded you a bounty of $4000 USD for this finding.. 🤑

Hope You liked this finding and i apologize for my weak English if there is any mistakes in this post.

Thanks for reading my article, have a great day . 🙂
