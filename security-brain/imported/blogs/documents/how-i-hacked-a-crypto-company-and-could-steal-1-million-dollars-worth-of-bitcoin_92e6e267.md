---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-05_how-i-hacked-a-crypto-company-and-could-steal-1-million-dollars-worth-of-bitcoin.md
original_filename: 2022-03-05_how-i-hacked-a-crypto-company-and-could-steal-1-million-dollars-worth-of-bitcoin.md
title: How I Hacked A Crypto Company And Could Steal 1 Million Dollars Worth of Bitcoin
category: documents
detected_topics:
- path-traversal
- xss
- command-injection
- otp
- rate-limit
- api-security
tags:
- imported
- documents
- path-traversal
- xss
- command-injection
- otp
- rate-limit
- api-security
language: en
raw_sha256: 92e6e267d7fb5b5e7d18b7fd871a7da1dbeb300286d2b1201524589e5c4eac00
text_sha256: 0fc44bead323be9620ea34e84fe7baada72a332bb8ffe731ea9cefcf475c8e3a
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# How I Hacked A Crypto Company And Could Steal 1 Million Dollars Worth of Bitcoin

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-05_how-i-hacked-a-crypto-company-and-could-steal-1-million-dollars-worth-of-bitcoin.md
- Source Type: markdown
- Detected Topics: path-traversal, xss, command-injection, otp, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `92e6e267d7fb5b5e7d18b7fd871a7da1dbeb300286d2b1201524589e5c4eac00`
- Text SHA256: `0fc44bead323be9620ea34e84fe7baada72a332bb8ffe731ea9cefcf475c8e3a`


## Content

---
title: "How I Hacked A Crypto Company And Could Steal 1 Million Dollars Worth of Bitcoin"
url: "https://zoidsec.medium.com/how-i-hacked-a-crypto-company-and-could-steal-1-million-dollars-worth-of-bitcoin-3174434b382c"
authors: ["zoid (@z0idsec)"]
bugs: ["Path traversal"]
bounty: "9,000"
publication_date: "2022-03-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2851
scraped_via: "browseros"
---

# How I Hacked A Crypto Company And Could Steal 1 Million Dollars Worth of Bitcoin

How I Hacked A Crypto Company And Could Steal 1 Million Dollars Worth of Bitcoin
zoid
Follow
4 min read
·
Mar 5, 2022

231

1

Press enter or click to view image in full size
Photo by Stillness InMotion on Unsplash

Breaking path normalisation has been my biggest interest in the past couple of years. Let me explain exactly why I have chosen to invest time in this attack vector, and how to exploit it. Firstly, let me introduce myself, my name is Blake, and I’m a part-time software engineer at Pentesterlab, an SRT member for Synack and a pentester for Cobalt.

Why Did I Invest Time In Path Normalisation?

Path normalization is one of those hit-and-miss vulnerabilities but to exploit it, it requires pure logical thinking. There are no real patterns to look for like XSS or other types of attacks where the payload is reflected, It’s just trial and error looking for nuances, and differences in the response. The post-adrenaline rush, once you hit something internal, is orgasmic; not just that, it generally always has a solid impact when you hit an internal path, think about it they are hiding these internal services/APIs because they don’t want the public to see the sensitive information, so they implement reverse proxies to shut them off from the public.

What is Path Normalization?

Normalizing a path involves modifying the string that identifies a path or file so that it conforms to a valid path on the target operating system. Normalization typically involves Canonicalizing components and directory separators.

Developers use this when they are writing reverse proxy rules to block certain internal paths from being passed through and upstreamed to internal services. This is what we are breaking, it involves path traversals and other bypass techniques.

Note: Don’t be confused with LFI though, we're not accessing internal files, we're accessing internal paths.

Here is a picture of a valid attack:

Press enter or click to view image in full size
AEM Dispatcher bypass, access to CRXDE | Lite
What Impact Can We Achieve?

Impact for path normalization can be a range of things such as:

Sensitive information leaks
Access to Internal Services like JBoss EAP, Tomcat, AEM and APIS + more
Some even have RCE by design.
Some allow you to write to the API for higher impact.

The impact is very high in most cases.

What tools do I use?

I keep it simple, KISS (Keep It Stupid Simple)

Get zoid’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Tools:

chrome dev tools
ffuf
Dirsearch
Burp
Assetnote Wordlists
Seclists

As I said, it requires pure logic to find these vulns. 🧠

What Did The Crypto Hack Look Like?

Okay, enough of the technical side of things, let’s talk about my hack and what the massive impact was. Before I get into details, the bug can not be disclosed at the moment, so everything will be redacted.

I started off using Chrome dev tools and was looking through the XHR requests and Documents, I noticed there was not much there so I decided to open up Burp and start crawling the in-scope assets. I generally test all paths with my pre-build wordlist and my brain, I noticed in one path I hit the internal root API, performed directory brute-forcing and could access the User Center API.

https://api.example.com/public/path/config/..;/..;/internal/path

Internal User Center API

This did not provide much impact, so I continued testing other paths.

FYI: Every path may contain a different backend service/API to access, the external attack surface is much higher with these types of attacks.

Upon investigation, I found another path, so I performed my usual tests with a combination of traversing and directory bruteforcing I could access the Internal Admin Balance API which leaked admin funds and I could perform various admin functions like:

Withdrawl Funds
View Token History
View Balance

This had some solid impact, if this was not reported on time the potential disaster is very high, if a malicious hacker found this before I did, they could clean out his account and send the company broke. I reported it 2 days later, It got triaged and fixed within 1 day and they paid me $9,000USD which is about $12,000 in my currency.

Press enter or click to view image in full size

If my content interests you, then you’ll want to check out Dirstrike, our latest SaaS built for high-scale directory brute-forcing without worrying about rate limits or IP bans. Join our Discord: https://discord.gg/4Q4WgNR5wg and help us make this platform even better. Your support is greatly appreciated!

Press enter or click to view image in full size
Dirstrike SaaS platform

I hope you enjoyed this story, feel free to follow me on Twitter and clap to this story, until next time.

https://twitter.com/z0idsec

Happy hacking.

Peace!✌️
