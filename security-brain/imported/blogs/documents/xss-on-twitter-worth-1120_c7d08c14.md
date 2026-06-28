---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-22_xss-on-twitter-worth-1120.md
original_filename: 2019-07-22_xss-on-twitter-worth-1120.md
title: XSS On Twitter [Worth 1120$]
category: documents
detected_topics:
- xss
- command-injection
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- command-injection
- clickjacking
- api-security
language: en
raw_sha256: c7d08c1438b98238c5a6fa02f30a1a1094253ed5335ca0a6da656e0df9ece264
text_sha256: 0b76e0445a9c73c5cb403a777dfeeaa29e6c36f9f093646872c38bda3f57d5ab
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# XSS On Twitter [Worth 1120$]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-22_xss-on-twitter-worth-1120.md
- Source Type: markdown
- Detected Topics: xss, command-injection, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `c7d08c1438b98238c5a6fa02f30a1a1094253ed5335ca0a6da656e0df9ece264`
- Text SHA256: `0b76e0445a9c73c5cb403a777dfeeaa29e6c36f9f093646872c38bda3f57d5ab`


## Content

---
title: "XSS On Twitter [Worth 1120$]"
url: "https://medium.com/@bywalks/xss-on-twitter-worth-1120-914dcd28ee18"
authors: ["Bywalks (@bywalkss)"]
bugs: ["XSS"]
bounty: "1,120"
publication_date: "2019-07-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5128
scraped_via: "browseros"
---

# XSS On Twitter [Worth 1120$]

Bywalks
 highlighted

XSS On Twitter [Worth 1120$]
Bywalks
Follow
3 min read
·
Jul 22, 2019

273

2

Hi guys, this is the first writeup about my vulnerability bounty program,a process about how I discovered a Twitter XSS vulnerability.

I think that in the process of finding the vulnerability, there are some interesting knowledge points, I hope you can get some from my writeup.

If you want to know more details, you need to visit bobrov’s blog, my discovery is due to reading his writeup, and thanks bobrov very much,I have a lot of gains from his blog.

Maybe you don’t want to spend more time. Here I will give a brief explanation of his article. When you visit some addresses, the server returns 302, which is similar to the following picture.

Press enter or click to view image in full size

In the returned Body, location will choose how to populate according to the requested URL,and the requested URI will be placed in the href event.

What do you think of next? Can we try it with dev.twiiter.com//javascript:alert(‘1’);/

indeed, as you might expect, <a href=”javascript:alert(‘1’);/”> Xxx</a> will be in the return body,but the returned location is location:javascript:alert(‘1’);/ ,The browser does not play the box

So, bobrov did a lot of fuzz, trying to get around the limitations here, amazing, he did, his Fuzz process is as follows (taken from his blog)

Press enter or click to view image in full size

So, his final Payload is

https://dev.twitter.com//x:1/:///%01javascript:alert(document.cookie)

and the response from the server is as follows.Location header = //aa :1/:/dev.twitter.com/%01xxx . returned body = <a Href=”javascript:alert(document.cookie)”>xxx</a>.

Get Bywalks’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Seeing this, you may be wondering, is this a problem?Javascript only works when the a tag is clicked,and the location header is http:////aa:1/:/dev.twitter.com/%01xxx,does the browser not jump?

There is a key point in this.When you visit a website, usually, the port you access is 80 or 8080,if you enter the port address as 1, the browser will not jump.Here, it is the a tag. The click was made possible, so we can combine the issue via Clickjacking,let the victim trigger this XSS vulnerability

After introducing his findings, let me talk about how I found this problem again.Honestly, I have been paying attention to Twitter security for a while,but I have gained very little,so I put my eye on Twitter’s past vulnerability report to see if there are some problems in the Twitter fix.

When I saw bobrov writeup about the problem,I immediately visited dev.twtter.com to try to find out if there were some problems.When I collected information through Google, I found an extremely interesting link.

https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/basics/adding-international-support-to-your-apps

Look closely, do you find it interesting? My feeling tells me that there may be problems here.So I tried to go to Fuzz to confirm my guess.After a period of testing, I found that when I added a / at the end of the URL,a miracle happened, for example,when I visited https://dev.twitter.com/web/sign-inhttps://dev.twitter.com/http://www.bywalks.com/,

location=http://www.bywalks.com,href=http://www.bywalks.com

Yes,Twitter’s fix for this issue no longer exists. Finally,after a period of Fuzz, my final Payload was https://dev.twitter.com//web%2f:1/:///%01javascript:alert(1)/ and I got Twitter 1120$ rewards

My gains in the process:

1: Don’t give up on the exploitation of a large company’s loopholes, insist that there will always be gains

2: When accessing a 302 jump page, location header and link on page extracting Url in different ways, there may be problems here.

3: When the browser tries to access a website with a port of 1, it will not jump

I hope that you can make some gains from my writing and sorry I m a non English speaker

best wishes,
Bywalks
