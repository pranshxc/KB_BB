---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-04_bypass-waf-by-a-simple-trick-gained-1000-bounty.md
original_filename: 2023-09-04_bypass-waf-by-a-simple-trick-gained-1000-bounty.md
title: Bypass WAF by a simple trick gained $1000 bounty
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: 37b7efa0c216ad7f8c1f88822f5d779a2b0f96da002b10ee9cc837097eec0e86
text_sha256: 746c1bf235d70d14d1e18398317057b3bcd96d21a4f2f6270b0acdd6925e2b2e
ingested_at: '2026-06-28T07:32:25Z'
sensitivity: unknown
redactions_applied: false
---

# Bypass WAF by a simple trick gained $1000 bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-04_bypass-waf-by-a-simple-trick-gained-1000-bounty.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:32:25Z
- Redactions Applied: False
- Raw SHA256: `37b7efa0c216ad7f8c1f88822f5d779a2b0f96da002b10ee9cc837097eec0e86`
- Text SHA256: `746c1bf235d70d14d1e18398317057b3bcd96d21a4f2f6270b0acdd6925e2b2e`


## Content

---
title: "Bypass WAF by a simple trick gained $1000 bounty"
page_title: "Bypass WAF by a simple trick gained $1000 bounty | by 0xBartita | Medium"
url: "https://0xbartita.medium.com/bypass-waf-by-a-simple-trick-gained-1000-bounty-cfa0fa63779e"
authors: ["0xBartita (@0xBaRtiTa)"]
bugs: ["WAF bypass"]
bounty: "1,000"
publication_date: "2023-09-04"
added_date: "2023-09-05"
source: "pentester.land/writeups.json"
original_index: 815
scraped_via: "browseros"
---

# Bypass WAF by a simple trick gained $1000 bounty

Bypass WAF by a simple trick gained $1000 bounty
0xBartita
Follow
2 min read
·
Sep 3, 2023

221

2

Hi all….

My name is 0xbartita let’s get started>

Press enter or click to view image in full size

When I was hunting on a private program on hackerone I noticed that program use Cloudflare on all subdomain *.target.com , I usually going to securitytrails.com to search for origin IP of the web application

Press enter or click to view image in full size
Origin IP of amazon server

Maybe I found Original IP it’s 50.17.***.** When requested it it’t give me 404 Not found

Press enter or click to view image in full size
404 not found via origin ip

Most hunters see this error they think it’s not Origin IP of website.

Get 0xBartita’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This happens because host header set by default as IP that requested or it’s give you the default virtual host on the server

But when I changed HOST header to target domain it’s showed me the same response of domain target.com without “Server: CloudFlare” response header

Press enter or click to view image in full size

To make every reqeust to target.com going to Origin IP instead of cloudflare IP on my browser go to burp and change redirect to host option to original IP

Press enter or click to view image in full size
Proxy=>Options

Summary:

when you face 404 or any error when you want to bypass waf by origin IP try to change host header to target domain

My twitter → https://x.com/0xbartita
