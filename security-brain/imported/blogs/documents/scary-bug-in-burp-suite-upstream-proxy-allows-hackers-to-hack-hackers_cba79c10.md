---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-06_scary-bug-in-burp-suite-upstream-proxy-allows-hackers-to-hack-hackers.md
original_filename: 2019-04-06_scary-bug-in-burp-suite-upstream-proxy-allows-hackers-to-hack-hackers.md
title: Scary Bug in Burp Suite Upstream Proxy Allows Hackers to Hack Hackers
category: documents
detected_topics:
- command-injection
- mobile-security
tags:
- imported
- documents
- command-injection
- mobile-security
language: en
raw_sha256: cba79c1025d9a5b25504bc4456f31f64332f4f5dae61d51ce89e78205715dbf6
text_sha256: 3f965b5b6b1324131755b85e052a32091b6f19ddd276a911cf9f9018b7936ac2
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Scary Bug in Burp Suite Upstream Proxy Allows Hackers to Hack Hackers

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-06_scary-bug-in-burp-suite-upstream-proxy-allows-hackers-to-hack-hackers.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `cba79c1025d9a5b25504bc4456f31f64332f4f5dae61d51ce89e78205715dbf6`
- Text SHA256: `3f965b5b6b1324131755b85e052a32091b6f19ddd276a911cf9f9018b7936ac2`


## Content

---
title: "Scary Bug in Burp Suite Upstream Proxy Allows Hackers to Hack Hackers"
url: "https://medium.com/@armaanpathan/scary-bug-in-burp-suite-upstream-proxy-allows-hackers-to-hack-hackers-e6fc9a8d60a"
authors: ["Armaan Pathan (@armaancrockroax)"]
programs: ["PortSwigger"]
bugs: ["MiTM"]
publication_date: "2019-04-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5326
scraped_via: "browseros"
---

# Scary Bug in Burp Suite Upstream Proxy Allows Hackers to Hack Hackers

Scary Bug in Burp Suite Upstream Proxy Allows Hackers to Hack Hackers
Armaan Pathan
Follow
3 min read
·
Apr 6, 2019

366

4

One day I was playing with a tool debookee (Network Traffic Interception) in the office, I noticed that the tool was intercepting facebook cookies in a plain text.

What is Debookee?

Debookee is able to intercept and monitor the traffic of any device in the same subnet, thanks to a Man-in-the-middle attack (MITM)It allows you to capture data from mobile devices on your Mac (iPhone, iPad, Android, BlackBerry…) or Printer, TV, Fridge (Internet of Things!) without the need of a proxy. This interception is done in 1 click and is totally transparent, without network interruption.

Now Getting facebook cookies in a plain text was not an intended behavior as Facebook uses SSL to transfer cookies and other data over HTTPS protocol. Again I tried If I get any other website’s cookies and I noticed that I was able to grab all website’s SSL traffic into plain text.

I asked my colleague and he said that he has configured burp proxy into a browser and he is surfing Facebook and other websites.

That's weird….

So I made a deep dive to understand the unexpected behavior and came to know that,

Get Armaan Pathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When any user uses a burp suite, the user installs CA-Certificate which trusts burp to intercept all the SSL Traffic into plain text. Once the user sets up a proxy, Browser sends all the traffic in the burp suite in plain text. now when I run Debookee, Burp Suites thinks that Debookee is an upstream proxy and by design, the burp suite does not force SSL Certificate into upstream proxy which means burp sends all the data to me/Debokee in a plain text.

Press enter or click to view image in full size
Configuring Burp Proxy in firefox
Press enter or click to view image in full size
Configuring Burp Proxy
Press enter or click to view image in full size
Getting cookies in a plain text
Video for better understanding

Which means If an attacker can get access into pen-testing consulting office’s wifi, then can probably hack all the pen testers, and what about live hacking events? most of all hackers/ Bug hunters use burp suite which means an attacker can hack all the hackers in live hacking events. and what if the company is sharing the same network as hackers then company triagers are exposed to the same risk as well which means the risk of getting hacked in live hacking events. :))

Isn’t it scary?
Reported this issue to port swigger and they replied

Burp doesn’t enforce upstream SSL trust by design but they will push a feature with a SSL enable toggle option in upstream proxy.

I hope you guys like it. Hit me up on twitter if you guys have any queries.
