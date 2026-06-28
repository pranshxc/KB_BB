---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-03-28_hundreds-of-hundreds-sub-secdomains-hack3d-including-hacker0ne.md
original_filename: 2017-03-28_hundreds-of-hundreds-sub-secdomains-hack3d-including-hacker0ne.md
title: Hundreds of hundreds sub-secdomains hack3d! (including Hacker0ne)
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 5261422c4ddfe0eaad19ee99b7e8ba68188c9505a8215bb59ecee67a5031ef7a
text_sha256: 07f03ab36a5cc0d94172e1d451d06e85ee14c88d60c3f3e1ede1fb8dc595de69
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Hundreds of hundreds sub-secdomains hack3d! (including Hacker0ne)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-03-28_hundreds-of-hundreds-sub-secdomains-hack3d-including-hacker0ne.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `5261422c4ddfe0eaad19ee99b7e8ba68188c9505a8215bb59ecee67a5031ef7a`
- Text SHA256: `07f03ab36a5cc0d94172e1d451d06e85ee14c88d60c3f3e1ede1fb8dc595de69`


## Content

---
title: "Hundreds of hundreds sub-secdomains hack3d! (including Hacker0ne)"
url: "https://medium.com/bugbountywriteup/hundreds-of-hundreds-subdomains-hack3d-including-hacker0ne-ad3acd1c0a44"
authors: ["Ak1T4 (@akita_zen)"]
programs: ["HackerOne"]
bugs: ["Subdomain takeover"]
bounty: "1,000"
publication_date: "2017-03-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6204
scraped_via: "browseros"
---

# Hundreds of hundreds sub-secdomains hack3d! (including Hacker0ne)

Hundreds of hundreds sub-secdomains hack3d! (including Hacker0ne)
Ak1T4
Follow
2 min read
·
Mar 28, 2017

409

9

The last month was something interesting, looking to takeover some subdomains at HackerOne i found one that took my attention, was info.hacker.one . The dns was pointing to unbouncespages.com a landing pages app services. Looking at the API i try to add the hackerone domain, but when i try the output was: “domain is already claimed”.

Well.. i try to find another way to bypass this, for hours looking enpoints, trying with different requests and changing some params, i could hack & bypass the filter domain, this hack gives me the power to add any domain managed by the dns of unbouncepages.com.

Well.. at this time info.hacker.one was hacked!

Looking unbouncepages servers i decide to do a Reverse Dns to 54.225.142.127 and see which others domains could be compromised with this bypass.. For my surprise hundreds of subdomains appears! some of few domains are list here:

(With some google dorks i’veen able to locate more domains under this service)

Get Ak1T4’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

(In the complete list are domains like payoneer.com, fiverr and others important companies compromised)

The bounty:
Press enter or click to view image in full size

Details of HackerOne Report here: https://hackerone.com/reports/202767

Thanks to HackerOne for the awesome plattform and special thanks to all tha amazing hackers who inspire me to improve every day:

Peter Yaworsky
Nahamsec
Yassine aboukir
Zseano
Frans Rosen

HAPPY HACKING! by ak1t4

HackerOne profile - ak1t4
Whiteh4t Hack3r & Zen Monk & bounty hunter - https://twitter.com/knowledge_2014

hackerone.com

ak1t4 z3n (@knowledge_2014) | Twitter
The latest Tweets from ak1t4 z3n (@knowledge_2014). Bounty Hunter. Hacker & Zen Monk

twitter.com
