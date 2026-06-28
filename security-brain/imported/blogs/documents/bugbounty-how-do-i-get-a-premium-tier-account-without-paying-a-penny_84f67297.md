---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-06-29_bugbounty-how-do-i-get-a-premium-tier-account-without-paying-a-penny.md
original_filename: 2022-06-29_bugbounty-how-do-i-get-a-premium-tier-account-without-paying-a-penny.md
title: '[BugBounty] how do I get a premium tier account without paying a penny'
category: documents
detected_topics:
- idor
- access-control
- command-injection
- rate-limit
- api-security
- cloud-security
tags:
- imported
- documents
- idor
- access-control
- command-injection
- rate-limit
- api-security
- cloud-security
language: en
raw_sha256: 84f67297969d5c3d5a06f9132f4f7466a4268ddec12b3af70265bf48fdd66223
text_sha256: 1d07af5a110606047152b7bd989f9b9dd19349e42c7219a2f7732e136b51fef8
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# [BugBounty] how do I get a premium tier account without paying a penny

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-06-29_bugbounty-how-do-i-get-a-premium-tier-account-without-paying-a-penny.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, rate-limit, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `84f67297969d5c3d5a06f9132f4f7466a4268ddec12b3af70265bf48fdd66223`
- Text SHA256: `1d07af5a110606047152b7bd989f9b9dd19349e42c7219a2f7732e136b51fef8`


## Content

---
title: "[BugBounty] how do I get a premium tier account without paying a penny"
url: "https://iamnoob.medium.com/bugbounty-how-do-i-get-a-premium-tier-account-without-paying-a-penny-767921a6c4e4"
authors: ["Marzuki (@aizack_ma)"]
bugs: ["Mass assignment", "Payment bypass"]
publication_date: "2022-06-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2501
scraped_via: "browseros"
---

# [BugBounty] how do I get a premium tier account without paying a penny

[BugBounty] how do I get a premium tier account without paying a penny
Marzuki
Follow
2 min read
·
Jun 29, 2022

84

1

Hello, after a long time of not writing, I wanted to write something unique. what I found here is privilege escalation, wherein attackers can get premium tier accounts without paying. I found a bug in a private program on bugcrowd. For the convenience of program privacy and easy understanding of readers, I will call it marzuki.com

marzuki.com has two account tiers, free and premium, and there is no trial here. Users must purchase a subscription for $50 per month to become premium. A few weeks ago, I tested marzuki.com but missed the endpoint of registration, and this bug occurred when registering. there is a vulnerable parameter that causes an attacker to be able to get a premium account without paying

OK, let’s go to the enumeration step to find the parameters. you can use param miner (now supports for POST json parameters).

Press enter or click to view image in full size

you can see progress with Logger++ burp plugin.

you can also use arjun or other tools for parameter discovery.

good article to find hidden parameters https://medium.com/geekculture/params-discovering-hidden-treasure-in-webapps-b4a78509290f

Get Marzuki’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

non-vulnerable request

request after I run param miner and found hidden parameter and this upgrade account to premium without paying a penny

the report is sent and within three days the bounty is given

Press enter or click to view image in full size

Summary
when you test a program, don’t miss any features, I previously tested this program a few weeks ago but missed the signup feature. Try to browse like a regular user, go through all the available features, and then think about what shouldn’t happen. Try fuzzing with any request GET/POST/PATCH/PUT. Finding hidden parameters is a good way because many hackers may miss it. And burp suite is a great tool.

Thanks.
