---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-14_united-nations-bug-bountywriteup.md
original_filename: 2022-04-14_united-nations-bug-bountywriteup.md
title: United Nations bug bounty[writeup]
category: blogs
detected_topics:
- api-security
- command-injection
- information-disclosure
tags:
- imported
- blogs
- api-security
- command-injection
- information-disclosure
language: en
raw_sha256: 3592e778f0bc7a7dba1645d6658d11292bd65e52f51d6d62a90ba4925ead6e9a
text_sha256: e7df0a8f6842a4eedf394b92809028746b244ea00ef82ce972c8d605b19968b1
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# United Nations bug bounty[writeup]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-14_united-nations-bug-bountywriteup.md
- Source Type: markdown
- Detected Topics: api-security, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `3592e778f0bc7a7dba1645d6658d11292bd65e52f51d6d62a90ba4925ead6e9a`
- Text SHA256: `e7df0a8f6842a4eedf394b92809028746b244ea00ef82ce972c8d605b19968b1`


## Content

---
title: "United Nations bug bounty[writeup]"
url: "https://debprasadbanerjee502.medium.com/united-nations-bug-bounty-writeup-4bcfdefbb8d3"
authors: ["Debprasad Banerjee"]
programs: ["United Nations"]
bugs: ["Information disclosure"]
publication_date: "2022-04-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2711
scraped_via: "browseros"
---

# United Nations bug bounty[writeup]

United Nations bug bounty[writeup]
Ravaan
Follow
2 min read
·
Apr 15, 2022

61

5

Let’s get to the point, how can you hack the UN and get your name featured in the prestigious hall of fame? Lemme show you a guaranteed method to do the following and I hope you benefit from it.

Intro:

So a few days back I was scrolling through Twitter and I see this guy writing something regarding UN bug bounty people in the comments were very pessimistic about this program since most of the vulnerabilities are fixed. So I thought to myself lemme check it out. I'm nowhere near as great as the hunters listed in the program. So I first went and checked the hall of fame listing. Few mentions were recent so I'm sure bugs still exist.

Subdomains:

So recently I'm using this tool called subdomainer which hunts for almost all places and runs httpx to sort them into live subdomains. Note i did not want to actually use all the subdomain enum like mentioned in my previous post.

FUZZING AND FFUF:

So i tried file bruting, now the most common mistake people make is not having a good wordlist. I have discovered 20 subdomains with almost same misconfiguration, and ill mention the list i use which will guarantee get you bugs. Its an extensive wordlist by albusec, now the command which i use, its for multiple subdomains where i use FFUF. If you do not know about FFUF, it's a fuzzing tool that is very fast.

Installation:go install github.com/ffuf/ffuf@latest

Download the wordlist: WORDLIST, git clone it

Get Ravaan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

COMMAND:

For multiple targets:

ffuf -w Infodisclosure_Sensitive-list-1.txt:FUZZ -w subdomain.txt:URL -u URLFUZZ -mc 200 -of csv -o ffuf-result.txt

See The Result: cat ffuf-result.txt | awk -F ‘,’ ‘{print $3}’

For single target

ffuf -w Infodisclosure_Sensitive-list-1.txt -mc 200 -u un.org/FUZZ

If you have chosen the target well, you will have several leaked files such files on visiting might have ID numbers, leaked API keys, and even exact software version with internal IP. The wordlist is the magic, use it and get bounties and once you try a few you should report it and get your name featured.

I discovered a file with internal usernames and emails. I have not reported 19 others that I found. There are several so I want you to do it and enjoy it. Do follow the steps and i can guarantee you will find several bugs:) -Ravaan

Press enter or click to view image in full size
FLEX TIME

UPDATE 1: I tried to reproduce the bug, all are fixed:( In, in future ill try to bring in more bugs but try this method with other targets. Maybe the dutch has some swags for you;)
