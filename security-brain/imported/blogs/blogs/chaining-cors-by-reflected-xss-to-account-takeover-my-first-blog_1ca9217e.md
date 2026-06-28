---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-26_chaining-cors-by-reflected-xss-to-account-takeover-my-first-blog.md
original_filename: 2020-12-26_chaining-cors-by-reflected-xss-to-account-takeover-my-first-blog.md
title: 'Chaining CORS by Reflected xss to Account takeover #My first Blog'
category: blogs
detected_topics:
- xss
- cors
- command-injection
tags:
- imported
- blogs
- xss
- cors
- command-injection
language: en
raw_sha256: 1ca9217eb413be18b98e3e8e18e605d23e917ae199d3801d736acf2681a84fdb
text_sha256: 3c935e5e81809f87fb267fbdb6dc1354111f5b3d22bc15bb0bda30005cb96e21
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Chaining CORS by Reflected xss to Account takeover #My first Blog

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-26_chaining-cors-by-reflected-xss-to-account-takeover-my-first-blog.md
- Source Type: markdown
- Detected Topics: xss, cors, command-injection
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `1ca9217eb413be18b98e3e8e18e605d23e917ae199d3801d736acf2681a84fdb`
- Text SHA256: `3c935e5e81809f87fb267fbdb6dc1354111f5b3d22bc15bb0bda30005cb96e21`


## Content

---
title: "Chaining CORS by Reflected xss to Account takeover #My first Blog"
page_title: "Chaining CORS by Reflected XSS to Account takeover #My first Blog | by Santosh Kumar Sha(@killmongar1996) | Medium"
url: "https://notifybugme.medium.com/chaining-cors-by-reflected-xss-to-account-takeover-my-first-blog-5b4f12b43c70"
authors: ["Santosh Kumar Sha (@killmongar1996)"]
bugs: ["CORS misconfiguration", "Reflected XSS", "Account takeover"]
publication_date: "2020-12-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4047
scraped_via: "browseros"
---

# Chaining CORS by Reflected xss to Account takeover #My first Blog

Top highlight

Member-only story

Chaining CORS by Reflected XSS to Account takeover #My first Blog
Santosh Kumar Sha(@killmongar1996)
Follow
3 min read
·
Dec 26, 2020

311

5

Hi, everyone

My name is Santosh Kumar Sha, I’m a security researcher from India(Assam). In this article, I will be describing how I was able to exploit a CORS misconfiguration by chaining it with Reflected xss to leak private information and ultimately taking over the account.

I am now offering 1:1 sessions to share my knowledge and expertise:

topmate.io/santosh_kumar_sha

TIP For looking for CORS bug:

Here is my workflow how i look for CORS bug.

First:

Spider the the host by Burpsuite. I like to used old version for burpsuite for spider .After spider the host copy all url and saved it in text file.

cat corstexturl.txt | CorsMe

OR

cat corstexturl.txt | soru -u | anew | xargs -n 1 -I{} curl -sk -H “Origin: test.com” | grep “Access-control-allow-origin: test.com”

cat corstexturl.txt | soru -u | anew |while read host do ; do curl -s — path-as-is — insecure -H “Origin: test.com” “$host” | grep -qs “Access-control-allow-origin: test.com” && echo “$host \033[0;31m” cors Vulnerable;done

Case#1
Vulnerable Endpoint

About a week ago, I was hacking this public bug bounty program, . After playing with the Origin header in the HTTP request, then…
