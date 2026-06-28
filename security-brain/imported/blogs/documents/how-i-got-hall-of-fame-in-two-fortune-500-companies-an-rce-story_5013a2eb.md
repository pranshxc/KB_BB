---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-29_how-i-got-hall-of-fame-in-two-fortune-500-companies-an-rce-story.md
original_filename: 2018-05-29_how-i-got-hall-of-fame-in-two-fortune-500-companies-an-rce-story.md
title: How I got hall of fame in two fortune 500 companies — An RCE story…
category: documents
detected_topics:
- command-injection
- path-traversal
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- path-traversal
- automation-abuse
- api-security
language: en
raw_sha256: 5013a2eb142a784a8a56625d7ac84aeb37eb6c4d81f953e63be497e71087f02e
text_sha256: 2cecc6b7a9b99f50223e33f2b3aec15e42a49fed5c95c93f9af1da1a20b67136
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I got hall of fame in two fortune 500 companies — An RCE story…

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-29_how-i-got-hall-of-fame-in-two-fortune-500-companies-an-rce-story.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `5013a2eb142a784a8a56625d7ac84aeb37eb6c4d81f953e63be497e71087f02e`
- Text SHA256: `2cecc6b7a9b99f50223e33f2b3aec15e42a49fed5c95c93f9af1da1a20b67136`


## Content

---
title: "How I got hall of fame in two fortune 500 companies — An RCE story…"
url: "https://medium.com/@emenalf/how-i-got-hall-of-fame-in-two-fortune-500-companies-an-rce-story-9c89cead81ff"
authors: ["Alfie (@emenalf)"]
bugs: ["RCE"]
publication_date: "2018-05-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5865
scraped_via: "browseros"
---

# How I got hall of fame in two fortune 500 companies — An RCE story…

How I got hall of fame in two fortune 500 companies — An RCE story…
Alfie
Follow
2 min read
·
May 30, 2018

46

2

After doing some recon from the target company’s IPs using shodan, I narrowed my attack vector to focus on exploiting some jenkins applications which did not seem to need credentials.Using the shodan dork below, I was able to get a list of unrestricted jenkins instances

Shodan dork for jenkins instances on port 8081 (Web GUI)

From the original target list I had, I was able to enumerate a few candidates for exploitation.I could see the unrestricted instances, where one could get the code that was being pushed by the company’s development team and one could also change the configuration. This could be enough to report and get bounty — due to lack of confidentiality. But, as they say..try harder!

From experience I have come to appreciate that the objective in bug bounty is to simulate a bigger impact as long as you are within the program’s bug bounty guidelines.

Get Alfie’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

On closer inspection, some nodes had the jenkin instance with the ‘manage jenkins’ configuration option. I was fortunate enough to find 2 hosts with this configuration option.

Press enter or click to view image in full size
ManageJenkins config option

I chose to install the terminal plugin on both and hence could exhibit that remote code execution was possible!

I quickly sent in my responsible disclosure email, and I got quick response; bounty and HoF followed :-)

A couple of weeks later, I replicated the same issue on another fortune 500 company — another one!

Further reading:

https://the-infosec.com/2017/06/22/from-shodan-to-remote-code-execution-1-hacking-jenkins/

Twitter: Alfie
