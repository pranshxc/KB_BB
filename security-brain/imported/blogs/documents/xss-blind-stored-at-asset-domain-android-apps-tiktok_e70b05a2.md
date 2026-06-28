---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-16_xss-blind-stored-at-asset-domain-android-apps-tiktok.md
original_filename: 2022-06-16_xss-blind-stored-at-asset-domain-android-apps-tiktok.md
title: XSS Blind Stored at Asset Domain Android Apps TikTok
category: documents
detected_topics:
- xss
- command-injection
- mobile-security
tags:
- imported
- documents
- xss
- command-injection
- mobile-security
language: en
raw_sha256: e70b05a2b40ee9422ce0e314c5ad2e20f849c37bbb11ebd9cfc6e771334523d6
text_sha256: 3feebb7456f30af22a24742e3f49c654c7d2efc5287d76dccc17019b12226152
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# XSS Blind Stored at Asset Domain Android Apps TikTok

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-16_xss-blind-stored-at-asset-domain-android-apps-tiktok.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mobile-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `e70b05a2b40ee9422ce0e314c5ad2e20f849c37bbb11ebd9cfc6e771334523d6`
- Text SHA256: `3feebb7456f30af22a24742e3f49c654c7d2efc5287d76dccc17019b12226152`


## Content

---
title: "XSS Blind Stored at Asset Domain Android Apps TikTok"
url: "https://aidilarf.medium.com/xss-blind-stored-at-asset-domain-android-apps-tiktok-ae2f4c2dbc07"
authors: ["Aidil Arief"]
programs: ["TikTok"]
bugs: ["Stored XSS"]
bounty: "1,500"
publication_date: "2022-06-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2544
scraped_via: "browseros"
---

# XSS Blind Stored at Asset Domain Android Apps TikTok

XSS Blind Stored at Asset Domain Android Apps TikTok
Aidil Arief
Follow
3 min read
·
Jun 16, 2022

107

1

Hi everyone

First, let me introduce a little background, I am a young teenager graduated from Senior High School and IT Security Enthusiast from Indonesia. Now, I am 21 years old.

I once had a dream that I wanted to find a valid vulnerability on some Tech Giant Site, and I thought it wasn’t easy and I had to fight. Exactly today I made a Write Up about the findings of Vulnerabilities on TikTok.

Press enter or click to view image in full size

The vulnerability I found was XSS Blind Stored at https://webcast.tiktokv.com/

When I try to find XSS from Android Apps TikTok to get new Coverage URLs and I do that to minimize Duplicate findings from Other Research. And I found a feature in TikTok’s Android Apps, namely the Create Live Event Feature.

Press enter or click to view image in full size

Then I tried to enter the XSS payload in all the forms.

“><img src=x onerror=write(document.domain)>

A little information, why don’t I use alert(document.domain)?

I think if I use alert() inside Android Apps, and it doesn’t work. For that I tried to use write() so I can see whether XSS is working or not in Android Apss, and it turns out that the XSS payload I input is triggered in TikTok Asset Domain.

XSS trigger

And the Live Event I created triggers XSS. Then I pause and see, is XSS triggered for myself or can it be triggered for other users?

Get Aidil Arief’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then, it turned out that the Live Event that I created had to wait for a review by the TikTok team so that it could be accessed by the public, and of course that made me feel that my findings were only SELF XSS. And it’s not good for me :(

Press enter or click to view image in full size

And I try to be patient and wait until my Live Event has been reviewed by the TikTok team. And I didn’t report this finding to TikTok at that time because the XSS I got was only SELF XSS.

And after waiting 30 minutes, finally the Live Event that I created has been approved by the TikTok Review team. And I tried to see if I could use XSS there for other users, and of course I found something unique here, namely that I can promote my Live Event by posting a Video to my TikTok account, and of course it will reach other users : )

And this is the result of the video post:

And I managed to leverage Self XSS to Blind Stored XSS :)

Report :

https://hackerone.com/reports/1542703

Timeline :

Report : Apr 16th

Triaged : Apr 21st

Fix : May 11th
