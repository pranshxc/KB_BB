---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-28_an-attempt-to-escalate-a-low-impact-hidden-input-xss.md
original_filename: 2020-06-28_an-attempt-to-escalate-a-low-impact-hidden-input-xss.md
title: An attempt to escalate a low-impact hidden input XSS
category: documents
detected_topics:
- xss
- command-injection
- otp
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- command-injection
- otp
- clickjacking
- api-security
language: en
raw_sha256: 26cd1afa134a933a3d903c56626911e830756188bf77887486c8c70b13f51429
text_sha256: 0ddb65b209c8c565613c7a61c027094320cd079e9840e62ed0d47afb7f68dba2
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# An attempt to escalate a low-impact hidden input XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-28_an-attempt-to-escalate-a-low-impact-hidden-input-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, otp, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `26cd1afa134a933a3d903c56626911e830756188bf77887486c8c70b13f51429`
- Text SHA256: `0ddb65b209c8c565613c7a61c027094320cd079e9840e62ed0d47afb7f68dba2`


## Content

---
title: "An attempt to escalate a low-impact hidden input XSS"
url: "https://officialaimm.medium.com/an-attempt-to-escalate-a-low-impact-hidden-input-xss-9f4b9c88f19c"
authors: ["Ayush Ojha (@officialaimm)"]
bugs: ["XSS"]
publication_date: "2020-06-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4467
scraped_via: "browseros"
---

# An attempt to escalate a low-impact hidden input XSS

An attempt to escalate a low-impact hidden input XSS
Ayush
Follow
3 min read
·
Jun 28, 2021

129

Introduction

A few months ago when I was hacking on one of the websites, I came across a page where one of the get parameters was reflected into the value-attribute without quotes enclosing it(any angle brackets in the payload was sanitized though).

Press enter or click to view image in full size
Attribute injection on a hidden input(angle bracket sanitized)

This was obviously prone to an XSS attack via arbitrary html-attribute injection, since simply adding white-space could add a new attribute. It only had a “small” problem: the input tag where the injection occurred was hidden.

In this article, I will take you through my journey to know more about hidden input XSS and an attempt to escalate this low-impact bug I found. I only received thanks(totally understandable because of the low-impact) for this btw, but I think this was an interesting topic to wander about so am writing this.

Note:

Due to disclosure policies, I have recreated the vulnerability on a new website for this article:

Vulnerable site: https://hiddeninputxss.bunch777.repl.co

Exploit/Attacker’s site: https://hiddeninputxssattacker.bunch777.repl.co

Problem with hidden input XSS

The way we trigger XSS via html-attribute injection is that we take advantage of javascript event-handlers like onload, onfocus, etc. Since the input tag we can inject into is hidden, there is not much way to trigger such events. This special type of vulnerability has also been explained by Gareth Heyes at PortSwigger’s website: https://portswigger.net/research/xss-in-hidden-input-fields.

User-interaction definitely can cause XSS in Firefox

Gareth’s article mentions how the accesskey feature can lead to XSS in Firefox requiring user interaction. In our case, the malicious URL is:

https://hiddeninputxss.bunch777.repl.co/?token=fdf%20accesskey%3da%20onclick%3dalert(document.domain)

which had this corresponding reflection:

<input name="token" type="hidden" value="fdf" accesskey="a" onclick="alert(document.domain)">

The XSS fires when the user presses ALT+SHIFT+A.

Press enter or click to view image in full size
XSS when victim presses ALT+SHIFT+A

This worked but the exploitability was pretty much zero; I mean what are the chances a victim first visits the malicious link and then press ALT+SHIFT+A for no reason?

Get Ayush’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I then started searching if there was any way to achieve an XSS without any user interaction for this case. And I got to Masato Kinugawa’s article on exactly that: https://translate.google.com/translate?sl=auto&tl=en&u=https://masatokinugawa.l0.cm/2016/04/hidden-input-xss.html. However, the no-interaction XSS was only for IE10 and IE11 which are now not considered to be modern browsers. Although Masato hinted he had one for Firefox as well and that he would talk about it in upcoming articles, I couldn’t find the article whatsoever.

Escalation attempt via iframe

It seemed there wasn’t any easy way to escalate the bug in anyway, since no-interaction XSS seemed almost impossible. Then I noticed that there was no X-Frame-Options directives at all in the response of the vulnerable site, so I wondered what if I iframe the vulnerable page on another website and see if the XSS still fired?

I then schemed an exploit scenario:

Victim is made to visit the attacker’s site framing the vulnerable site (with the user-interaction XSS payload) hidden from user’s sight.
The site asks the victim to press ALT+SHIFT+A.
An XSS fires but at the vulnerable site’s domain.

It worked, the XSS fired! The attacker’s website looked something this:

<iframe width="1" height="1" src="https://hiddeninputxss.bunch777.repl.co/?token=fdf accesskey=a onclick=alert(document.domain)">
</iframe>
You have been selected for a prize of $10000. Press alt+shift+a to start the receival process
Press enter or click to view image in full size
XSS on another domain, when victim interacts with attacker’s site

I think this attack was pretty realistic because the user is interacting with the attacker’s and not the target website. Thus we, in a way, were able to escalate this weird low impact XSS bug.
