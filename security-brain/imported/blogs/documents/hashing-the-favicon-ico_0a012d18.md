---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-21_hashing-the-faviconico.md
original_filename: 2022-01-21_hashing-the-faviconico.md
title: Hashing the Favicon.ico
category: documents
detected_topics:
- command-injection
- information-disclosure
tags:
- imported
- documents
- command-injection
- information-disclosure
language: en
raw_sha256: 0a012d18f4467e7d830ad0b9a70a88e96a0b8ad1d0e905a111588a8938c7be06
text_sha256: a623c766e2466a7fb2fea0b089efcb29f329605f8b5effa6f1d22dd3433fc832
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# Hashing the Favicon.ico

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-21_hashing-the-faviconico.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `0a012d18f4467e7d830ad0b9a70a88e96a0b8ad1d0e905a111588a8938c7be06`
- Text SHA256: `a623c766e2466a7fb2fea0b089efcb29f329605f8b5effa6f1d22dd3433fc832`


## Content

---
title: "Hashing the Favicon.ico"
url: "https://medium.com/@SkiMask0/hashing-the-favicon-ico-a498fc3d665b"
authors: ["Ski Mask (@Ski_Mask0)"]
bugs: ["Information disclosure"]
bounty: "100"
publication_date: "2022-01-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2992
scraped_via: "browseros"
---

# Hashing the Favicon.ico

Hashing the Favicon.ico
Ski Mask
Follow
2 min read
·
Jan 21, 2022

71

1

Hey Folks, I am Ski Mask and I recently started bug bounty. in this Write-up, I will tell you about one of my findings!!

So I was Hunting on this Private Program on Bugcrowd let's call it Test.com

I recently read this blog about how you can calculate favicon.ico hash to find a company’s internal assets and IP Address you can find the blog here.

What is Favicon.ico ??

The little icon you find from the endpoint test.com/favicon.ico

How to calculate favicon.ico ??

Get Ski Mask’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

There are many ways to calculate it you can refer to the blog I mentioned above or you can also use this website that can calculate the favicon hash.

Favicon Hash Calculator
Free tool to calculate favicon hashes. Favicon hashes can be used to find results on shodan.io with specific favicons.

faviconhash.com

Press enter or click to view image in full size

After you have successfully calculated the favicon hash you need to find the company’s assets and IP Addresses using shodan

Use a Query like this: HTTP.favicon.hash: the hash

Add 200 to search for all 200 OK Pages !!

So I found this one IP Address using this method after that it is just simple directory fuzzing I Found a /.backup file that was leaking MySQL credentials

Press enter or click to view image in full size

unluckily the credentials were not valid anymore so they changed the status to P4 and rewarded 100$

That’s all for the writeup

Hit me up on my Twitter!!

Twitter
