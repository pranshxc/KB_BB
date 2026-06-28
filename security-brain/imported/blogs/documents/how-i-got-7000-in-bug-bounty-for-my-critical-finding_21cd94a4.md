---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-31_how-i-got-7000-in-bug-bounty-for-my-critical-finding.md
original_filename: 2020-10-31_how-i-got-7000-in-bug-bounty-for-my-critical-finding.md
title: How i got 7000$ in Bug-Bounty for my Critical Finding.
category: documents
detected_topics:
- mobile-security
- api-security
- command-injection
- information-disclosure
- cloud-security
tags:
- imported
- documents
- mobile-security
- api-security
- command-injection
- information-disclosure
- cloud-security
language: en
raw_sha256: 21cd94a4de65b58fc56d82699e40bf33b706c182d0df6d65be9acbbe1e244b49
text_sha256: 593f7b6ffbdfb959c189ad11023bf5213e91b6f439849d633867a6f796c352d2
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How i got 7000$ in Bug-Bounty for my Critical Finding.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-31_how-i-got-7000-in-bug-bounty-for-my-critical-finding.md
- Source Type: markdown
- Detected Topics: mobile-security, api-security, command-injection, information-disclosure, cloud-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `21cd94a4de65b58fc56d82699e40bf33b706c182d0df6d65be9acbbe1e244b49`
- Text SHA256: `593f7b6ffbdfb959c189ad11023bf5213e91b6f439849d633867a6f796c352d2`


## Content

---
title: "How i got 7000$ in Bug-Bounty for my Critical Finding."
url: "https://medium.com/@noobieboy1337/how-i-got-7000-in-bug-bounty-for-my-critical-finding-99326d2cc1ce"
authors: ["Kishan Kumar / Noobie BoY (@hst_kishan)"]
bugs: ["Information disclosure"]
bounty: "7,000"
publication_date: "2020-10-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4166
scraped_via: "browseros"
---

# How i got 7000$ in Bug-Bounty for my Critical Finding.

How i got 7000$ in Bug-Bounty for my Critical Finding.
noobie-boy
Follow
2 min read
·
Oct 31, 2020

441

2

Image Credit >> computerworld.com
WHOAMI:

@Kishan Kumar (noobie-boy) > Independent Web/Mobile security researcher, bugs hunter and App-Sec Trainer

Hi this is my 2nd Write-up about my Android Hunting and I’m going to share my finding how we can find most critical information inside the APK file I saw most of the hunters like to do dynamic testing using Burp Suite but I want to suggest you something sometimes we have to focus in static testing for finding better flaws.

To keep this write up effective and time-friendly I’ll keep it as short as possible and informative.

Summary:

The program was about a news agency and their web app and their mobile application. I had managed to get their PII data which is very sensitive by nature including their banking details like bank transactions info, API Keys and much more which were stored in an excel file. I found these excel files via admin panel of the company which were found in their android application through static analysis.

Attacking Steps:

1: Firstly I had downloaded the target apk file.

Get noobie-boy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2: Used Dex2jar tool to change apk into jar.

3: Opened jar file in JD-Gui

4: Then I checked com/target/global/Constants.java file and I got the admin URL from here and the admin panel was having default credentials admin:admin after authentication I used dirbuster for content discovery and I got the below file which were having lots of information and some excel files including banking details.

Press enter or click to view image in full size
Got the file via dirbuster after authentication in admin panel
Press enter or click to view image in full size
This one is the first excel file which is having users’ details.

These are all I can share and the rest are sensitive enough that I can’t share it.

Press enter or click to view image in full size
I got 7000$ bounty for PII details from the company after few days.

If you have any question or need any help regarding Bug Hunting in Mobile /Web/API

please reach me without any hesitation.
#Happy_hunting #happy_hacking

https://www.linkedin.com/in/kishan-kishan-3896a013a/
