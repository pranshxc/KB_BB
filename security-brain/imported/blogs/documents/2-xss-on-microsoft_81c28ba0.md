---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-04-20_2-xss-on-microsoft.md
original_filename: 2023-04-20_2-xss-on-microsoft.md
title: 2 XSS on Microsoft
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: 81c28ba0e8233835f47c95620b30e59d4eb8cbcfa72161e26f59abed103247ee
text_sha256: ec33857d430b641b288e16b569d2ee3c90e0084d5b41193b55a3bf34c98a3e86
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# 2 XSS on Microsoft

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-04-20_2-xss-on-microsoft.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `81c28ba0e8233835f47c95620b30e59d4eb8cbcfa72161e26f59abed103247ee`
- Text SHA256: `ec33857d430b641b288e16b569d2ee3c90e0084d5b41193b55a3bf34c98a3e86`


## Content

---
title: "2 XSS on Microsoft"
url: "https://medium.com/@nikouei_com/2-xss-on-microsoft-37b6a7efcc84"
authors: ["Mohammad Nikouei (@NikoueiMohammad)"]
programs: ["Microsoft"]
bugs: ["XSS"]
publication_date: "2023-04-20"
added_date: "2024-02-27"
source: "pentester.land/writeups.json"
original_index: 1236
scraped_via: "browseros"
---

# 2 XSS on Microsoft

2 XSS on Microsoft
Mohammad Nikouei
Follow
2 min read
·
Apr 20, 2023

223

6

The story begins that one day I was feeling funky and texted my friend that I feel like Microsoft has been escaping from my radar. I am gonna find something on it. Mission successful in 15 minutes :)

First finding begins with me use the power of google search engine to my advantage by dorking. As its commonly expected .aspx endpoint looks different in a hunter’s eyes :) So I began using the dork below:

site:*.microsoft.com ext:aspx

You can imagine the number of result here would be quite high. Therefore, it’s time for us to filter all the sites that doesn’t look suspicious to us using the filter below.

 -site:SAFE.microsoft.com

Don’t forget it’s a recursive filtering. Keep doing it till something catch your attention. And exact thing happened here, I found a subdomain that look interesting to me. Why you might ask? Due to the lack of fav icon and unfamiliarity with the language of the website, I was encouraged to poke further. Then when I opened it I found out that it has not been maintained or updated for a while. By looking at the UI, copy right 2014 and honestly; my 6th sense was telling me that there is something here, just gotta find it.

keep on Digging! The URL was already contained two parameters. So I started my testing wit those and sadly, got nothing! So, it’s time to fire up x8.

x8 -u XXS1.microsoft.com -w WORDLIST 

The result showed that the parameter “message” is being reflected. Alright, its time to test it out and BOOM! I popped the alert using payload below

message=xss%27-alert(origin)-%27

Am I done? Not quite!
As the first XSS payload was a bit straight forward and I was not ready to leave with a Duplicate; I decided to have a plan B.

Get Mohammad Nikouei’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Second XSS begins using the first subdomain as clue. How? I noticed that the first subdomain is using Japanese language thanks to google translate. Then I wondered what if I add the word “search” in Japanese in my dorks to see if any interesting result would show up! So I google translated the word “search” to Japanese and went back to dork some more and of course filter recursively.

site:*.microsoft.com 検索 -site:SAFE.microsoft.com

And after filtering for a while; one result caught my attention.

https://xss2.microsoft.com/

After many attempts here and there on this subdomain I was ready to move on, But said to myself, lets give the view-source another look. And indeed, it didn’t disappoint. I found this endpoint

xss2.microsoft.com/REDACTED/REDACTED?id=1&appid=22&uid=54

Although all these parameters here in this endpoint failed me, I dorked further to test my luck in any other path and so continued dorking.

site:xss2.microsoft.com/REDACTED/REDACTED

And the result was not going to be disappointing. I found an endpoint was similar looking to the one that I was working on. So the first thought in my mind was why not test the same parameters that were giving me a hard time in the last endpoint.

xss2.microsoft.com/REDACTED/REDACTED/REDACTED?id=1&appid=22&uid=54

And Voallah! The parameter ID being reflceted, and I managed to execute my JS!

Thank you for reading my finding and hope this helps out!
Peace out :)
