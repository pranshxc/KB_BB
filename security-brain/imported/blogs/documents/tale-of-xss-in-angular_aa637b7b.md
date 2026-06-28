---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-02_tale-of-xss-in-angular.md
original_filename: 2021-08-02_tale-of-xss-in-angular.md
title: Tale of XSS in Angular
category: documents
detected_topics:
- xss
- automation-abuse
- command-injection
- supply-chain
tags:
- imported
- documents
- xss
- automation-abuse
- command-injection
- supply-chain
language: en
raw_sha256: aa637b7b58fce314df2a1bc0a915bdefa28b83d35ed7b3efbf4885a592c30d2b
text_sha256: 56d979e3f927d0288661106cd6b4db15b28169fb0569e9cfa25922a1b84d88ff
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Tale of XSS in Angular

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-02_tale-of-xss-in-angular.md
- Source Type: markdown
- Detected Topics: xss, automation-abuse, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `aa637b7b58fce314df2a1bc0a915bdefa28b83d35ed7b3efbf4885a592c30d2b`
- Text SHA256: `56d979e3f927d0288661106cd6b4db15b28169fb0569e9cfa25922a1b84d88ff`


## Content

---
title: "Tale of XSS in Angular"
url: "https://medium.com/@sicks3c/tale-of-xss-in-angular-c5c057a56156"
authors: ["Sicksec (@OriginalSicksec)"]
bugs: ["Reflected XSS"]
publication_date: "2021-08-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3451
scraped_via: "browseros"
---

# Tale of XSS in Angular

Member-only story

Tale of XSS in Angular
Automation helps get easy $$$ rXSS
Sicksec
Follow
2 min read
·
Aug 1, 2021

119

Press enter or click to view image in full size
Photo by Ferenc Almasi on Unsplash

Hello Security Researcher and Hackers

In this writeup I will explain how I was able to get 2 rXSS in Angular using automation and simple payloads in Github

First of all I will explain my recon automation and how I was able to detect the XSS in those 2 subdomains , I’m currently a subscriber to Findomain Maintained and created by Ed who originally created Findomain Public

His service allows you to add targets you want and perform a lot of cool stuff on the finding subdomains that looks as follows

Press enter or click to view image in full size

and many more you can head over his website to check the packages his offers and you may ended up getting one for yourself

I was looking at my Telegram where I set up the incoming recently found subdomains and I saw 2 newly discovered ones and I wanted to take a small look at them, with Wappalyzer plugins saw the both assets are using Angular 1.6 where I previously saw that it has an XSS payload that works in Github

I tried to log in and I received an error since my email is not in the authorized organization…
