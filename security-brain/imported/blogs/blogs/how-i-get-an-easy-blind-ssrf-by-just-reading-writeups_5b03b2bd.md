---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-06-12_how-i-get-an-easy-blind-ssrf-by-just-reading-writeups.md
original_filename: 2024-06-12_how-i-get-an-easy-blind-ssrf-by-just-reading-writeups.md
title: How I get an easy Blind SSRF by just reading writeups
category: blogs
detected_topics:
- command-injection
- ssrf
tags:
- imported
- blogs
- command-injection
- ssrf
language: en
raw_sha256: 5b03b2bd3fcbe60ce115a80b406a3c290b865f4015e8afb062a2ec44dfcf1c8a
text_sha256: 67a77fe836d81fb839863bf22e97a67f2ea2114bb661ecf5b6b94fbeef68f015
ingested_at: '2026-06-28T07:32:34Z'
sensitivity: unknown
redactions_applied: false
---

# How I get an easy Blind SSRF by just reading writeups

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-06-12_how-i-get-an-easy-blind-ssrf-by-just-reading-writeups.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf
- Ingested At: 2026-06-28T07:32:34Z
- Redactions Applied: False
- Raw SHA256: `5b03b2bd3fcbe60ce115a80b406a3c290b865f4015e8afb062a2ec44dfcf1c8a`
- Text SHA256: `67a77fe836d81fb839863bf22e97a67f2ea2114bb661ecf5b6b94fbeef68f015`


## Content

---
title: "How I get an easy Blind SSRF by just reading writeups"
url: "https://medium.com/@mohamed0xmuslim/how-i-get-an-easy-blind-ssrf-by-just-reading-writeups-a5459bbdf96d"
authors: ["Muhammad Mostafa (@0xSekiro)"]
bugs: ["Blind SSRF"]
publication_date: "2024-06-12"
added_date: "2024-07-15"
source: "pentester.land/writeups.json"
original_index: 255
scraped_via: "browseros"
---

# How I get an easy Blind SSRF by just reading writeups

Top highlight

Muhammad_Mostafa
Follow
3 min read
·
Jun 13, 2024

535

6

How I get an easy Blind SSRF by just reading writeups

بسم الله الرحمن الرحيم

Don’t forget to pray for people in Gaza and Sudan 🤲🏻❤️

Introduction:

Reading writeups is one of the most important things in the world of bug bounty, It just makes you more experience hacker without even hacking

Story:

The story begans when I was exploring an external BBP program to hunt on it, After trying to find cache bugs (cache poisoning and cache deception) I found in one of the responses this url

https://www.target.com/about-us/xmlrpc.php

When I opened it on the browser I got this page

Press enter or click to view image in full size
The photo from Google not the target

So I immediately remember that I read writeups talk about this file and how to get bugs from it

Now I need you to leave my writeup and read this wrieup cause I am lazy to explain what is XML-RPC file and all those things ☺️

Writuep link:

https://ms-official5878.medium.com/xml-rpc-php-wordpress-vulnerabilities-9a7d66068bde

So after I found this page I reload the page and intercept the request and sent it to repeater

Get Muhammad_Mostafa’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After that I change request method to POST and write this on request body to list all functions

<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall>

Then I used pingback.ping method to make the server send external http request which means blind SSRF, So I sent this on request body

<methodCall>
<methodName>pingback.ping</methodName>
<params><param>
<value><string><-- burp collaborator link --></string></value>
</param><param><value><string>http://< Any valid page from the website ></string>
</value></param></params>
</methodCall>

And I get a response looks like that which faultCode 0 means that the request was sent successfully

So I go to burp collaborator and I found this

Press enter or click to view image in full size

Yeah exactly the server sent an http request which is enough to report the bug

What Is the impact of SSRF ?

The impact of exploiting a Server Side Request Forgery vulnerability mainly depends on how the web application uses the responses from the remote resource, such as:

scan ports and IP addresses
interact with some protocols such as Gopher
discover the IP addresses of servers running behind a reverse proxy
Denial of Services
In some situation potentially remote code execution
Reward :

So after I report the bug they accept it with medium severity and give me a voucher code with specific amount for some popular websites

Press enter or click to view image in full size

So thanks for reading and this is my social media if you want to contact with me

LinkedIn: https://www.linkedin.com/in/muhammad-mostafa-36a01a226

Twitter:

https://x.com/0xSekiro
