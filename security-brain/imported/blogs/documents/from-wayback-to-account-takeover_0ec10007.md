---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-19_from-wayback-to-account-takeover.md
original_filename: 2022-05-19_from-wayback-to-account-takeover.md
title: From Wayback to Account Takeover
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: 0ec1000791d6922f565a3a267db95f6954a667faa921054966b29870f77e8532
text_sha256: 10981aa9bc4735b20e5682038ac69b695a0ea892dd7da3560830a9cbf6fef5f7
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# From Wayback to Account Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-19_from-wayback-to-account-takeover.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `0ec1000791d6922f565a3a267db95f6954a667faa921054966b29870f77e8532`
- Text SHA256: `10981aa9bc4735b20e5682038ac69b695a0ea892dd7da3560830a9cbf6fef5f7`


## Content

---
title: "From Wayback to Account Takeover"
url: "https://medium.com/@mohamedtaha_42562/from-wayback-to-account-takeover-ea7e80600188"
authors: ["Mohamed Taha (@Mohamed12742780)"]
programs: ["Plex"]
bugs: ["Information disclosure", "Account takeover"]
bounty: "120"
publication_date: "2022-05-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2629
scraped_via: "browseros"
---

# From Wayback to Account Takeover

From Wayback to Account Takeover
Mohamed Taha
Follow
2 min read
·
May 19, 2022

152

Press enter or click to view image in full size

Hi, I would like to share how Wayback Machine leads to limited Account Takeover.

What is Wayback:

WayBackMachine is an archive of websites which contains over 330 billion web pages, all indexed for you to search through! WayBackMachine scrapes websites and saves a copy of it and you are able to go back numerous amounts of years & view what they use to look like. From bugbountyhunter

I am always using waybackurl and gau for finding any information disclosure like invitation token or any endpoints that might lead to a vulnerability.

Get Mohamed Taha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The website that I was testing is plex.tv which is like Netflix. I Registered and started to see the features of the website while running burp in the background. I checked burp history and found this request:

Press enter or click to view image in full size

Notice the Plex-Token. This request is responsible for authentication with the website, meaning that if I intercepte this request while logging in to the website and change the Plex-Token to anyone else token, I will be logged in as this user. But how can I get this token? of course from above tools I searched for any archived links and surprisingly I found like 17 leaked tokens which I tested and I was able to login to these users which have premium accounts:)

The response from the program:

Press enter or click to view image in full size

120$ which is not bad as it is a limited account takeover.

Thank you for Reading.

Twitter:

twitter.com/mohamed12742780
