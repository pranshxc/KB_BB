---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-08_internet-safety-for-kids-families-trend-micro-bypass-dom-xss.md
original_filename: 2018-05-08_internet-safety-for-kids-families-trend-micro-bypass-dom-xss.md
title: Internet Safety for Kids & Families — Trend Micro Bypass DOM XSS
category: documents
detected_topics:
- xss
- command-injection
- mfa
tags:
- imported
- documents
- xss
- command-injection
- mfa
language: en
raw_sha256: 007523af6c62c3fb494c6dfe9a9aa6dddb8907c2ae4c906e7397cf0fabb3305d
text_sha256: cbcaf8b7d8611fed79e3bca312ab123e9585b28579e3918bf27d8087ee9f9222
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Internet Safety for Kids & Families — Trend Micro Bypass DOM XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-08_internet-safety-for-kids-families-trend-micro-bypass-dom-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, mfa
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `007523af6c62c3fb494c6dfe9a9aa6dddb8907c2ae4c906e7397cf0fabb3305d`
- Text SHA256: `cbcaf8b7d8611fed79e3bca312ab123e9585b28579e3918bf27d8087ee9f9222`


## Content

---
title: "Internet Safety for Kids & Families — Trend Micro Bypass DOM XSS"
url: "https://medium.com/@honcbb/internet-safety-for-kids-families-trend-micro-dom-xss-db34c9bbb120"
authors: ["Honc (@honcbb)"]
programs: ["Trend Micro"]
bugs: ["DOM XSS"]
publication_date: "2018-05-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5885
scraped_via: "browseros"
---

# Internet Safety for Kids & Families — Trend Micro Bypass DOM XSS

Internet Safety for Kids & Families — Trend Micro Bypass DOM XSS
Honc
Follow
3 min read
·
May 8, 2018

5

I was holding a cup of coffee, I want to say to practice a , find trend Micro loophole Policy project, want to say see can find some loopholes as one of the technical exercises

Press enter or click to view image in full size

Look at the trend technology loopholes policy, there is no need to pay special attention to the place, we try to maintain the same principle (find the vulnerability as soon as possible to submit a vulnerability recurrence method to the official security team)

A lot of people start for the application service, Web services penetration test, will first on the “subdomain” to try to crack

I try to use tools gradually, try (*. trendmicro.com) subdomain to do a lot of cracking

I began to be curious to move the target to: http://internetsafety.trendmicro.com/

Press enter or click to view image in full size

In general,

We will fuzzing and detect the parameter values or input boxes for the Web application service.

can also sniff the server

Because of my occupational disease,

First in the Input box list (type XSS POC): “><img src=x oneror:alert(1)/>

http://internetsafety.trendmicro.com/?s=%22%3E%3Cimg+src%3Dx+onerror%3Aalert%281%29%2F%3E

Press enter or click to view image in full size

Of course, my request was blocked. So it looks like there’s a firewall or WAF blocking the filter.

What I started to wonder was, what labels did he filter? is the “ > ” symbol or (img 、onerror) special letter?

At first I thought there might be no loopholes, but the results he gave me were so exciting.

So I’m trying to enter “>” To see if there are any filters for these strings. Unexpectedly, he did not filter …

Poc Payload:

Get Honc’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

http://internetsafety.trendmicro.com/?s=%22%3E%3C

Press enter or click to view image in full size

View Source code:

Press enter or click to view image in full size

Try to enter: Http://internetsafety.trendmicro.com/?s= “><img src=x

Press enter or click to view image in full size

he did not filter. Does it filter the onerror that executes the statement instructions?

Press enter or click to view image in full size

It is true that …

He filtered the (onerror)

We can see that this syntax is filtered and I try to use the HTML (a） value label to try

I combine the following syntax, and I like to encrypt it in the URL as an attempt:

http://internetsafety.trendmicro.com/?s="><a+href%3D"data%3Atext%2Fhtml%3Bbase64%2CPHN2Zy9vbmxvYWQ9YWxlcnQoMik%2B">click<%2Fa>

I try to input JS syntax in the URL, phn2zy9vbmxvywq9ywxlcnqomik decoding is: <svg/onload=alert (2)

Press enter or click to view image in full size
Press enter or click to view image in full size

Response results can be successful response!!

Prove that he only filtered some strings, rather than strictly filtering the strings that the client passed in. While it’s not difficult to bypass this application, it WAF me to learn skills.

Timeline
2018/02/11 03:52 Provide vulnerability details to Trend Micro Security Team
2018/02/11 05:53 Receive response from Trend Micro Automatic reply that inspection is in progress
2018/03/01 11:53 Yes, it fixes
2018/03/05 11:07 Trend Micro has posted me on the Acknowledgment（Hall Of Fame) page
