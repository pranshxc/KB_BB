---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-18_xss-through-swf-file.md
original_filename: 2019-01-18_xss-through-swf-file.md
title: XSS Through SWF file!
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
raw_sha256: 1d945c0a99f705b886d8c33c6f7ea63606bd9eb2a990d324de87288a5f599dd0
text_sha256: 913fc24655ef11ce698a039280478bd3873e2c7d1b4155e771bc57e3c53d59cf
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# XSS Through SWF file!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-18_xss-through-swf-file.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `1d945c0a99f705b886d8c33c6f7ea63606bd9eb2a990d324de87288a5f599dd0`
- Text SHA256: `913fc24655ef11ce698a039280478bd3873e2c7d1b4155e771bc57e3c53d59cf`


## Content

---
title: "XSS Through SWF file!"
url: "https://medium.com/@friendly_/xss-through-swf-file-4f04af7b0f59"
authors: ["Friendly (@SkeletorKeys)"]
bugs: ["Flash XSS"]
bounty: "200"
publication_date: "2019-01-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5471
scraped_via: "browseros"
---

# XSS Through SWF file!

XSS Through SWF file!
Friendly
Follow
2 min read
·
Jan 18, 2019

91

1

First off, I’d like to say thank you to everyone who’s followed and helped me learn different target points and attacks for web testing.

In this story, I will be telling how a flash file led me to an XSS — however, I will not be disclosing the website due to their privacy and respect. 😊

Let’s start.

You will need an XSS swf. That XSS swf file can be obtained through: https://github.com/evilcos/xss.swf — download the file and then upload to the server you’re testing on for Bounty Hunting!!

Once you see the file is on the server and doesn’t ask you to download/reflects on the server, that’s when you put your XSS code.

Get Friendly’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Simply add ?js=alert(document.domain); at the end of your .swf and it should display the XSS.

Screenshots:
Press enter or click to view image in full size
As you can see, the x.swf file stays on the server.
Press enter or click to view image in full size
Adding ?js=alert(document.domain); triggered my XSS.
Time and date for payout:
Mon, Oct 29, 2018 10:51 AM - XSS found and reported the same day.
Wed, Oct 31, 2018, 9:56 AM - An investigation was done by their security team.
Nov 19, 2018, 8:18 AM - Payout of $200 USD was sent to my PayPal.

Thank you for all reading and hope this helps you in your quest for bounty hunting. 😎

If you have any questions or comments, feel free to message me on Twitter @Skeletorkeys
