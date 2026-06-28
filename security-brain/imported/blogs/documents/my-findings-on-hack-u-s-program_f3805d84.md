---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-08-30_my-findings-on-hack-us-program.md
original_filename: 2022-08-30_my-findings-on-hack-us-program.md
title: My findings on Hack U.S Program
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: f3805d844b621c30508f7b2054da768b2f44cc2e16f111ada4210ac3d1344366
text_sha256: 365e4497525d0e71fb7026e5dd89f83c854faaccb689291b43db3b3a996cb02a
ingested_at: '2026-06-28T07:32:13Z'
sensitivity: unknown
redactions_applied: false
---

# My findings on Hack U.S Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-08-30_my-findings-on-hack-us-program.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:13Z
- Redactions Applied: False
- Raw SHA256: `f3805d844b621c30508f7b2054da768b2f44cc2e16f111ada4210ac3d1344366`
- Text SHA256: `365e4497525d0e71fb7026e5dd89f83c854faaccb689291b43db3b3a996cb02a`


## Content

---
title: "My findings on Hack U.S Program"
url: "https://falcon319.medium.com/my-findings-on-hack-u-s-program-43b692a5c057"
authors: ["Charansai"]
programs: ["U.S. Dept Of Defense"]
bugs: ["Missing authentication", ".git folder disclosure", "Information disclosure"]
bounty: "500"
publication_date: "2022-08-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2241
scraped_via: "browseros"
---

# My findings on Hack U.S Program

My findings on Hack U.S Program
Charansai
Follow
3 min read
·
Aug 30, 2022

111

Greetings, everyone! I’m Charan, also known as 0xcharan, in the bug bounty community. I dabble in bug bounty hunting while pursuing my studies in agriculture. Today, I’m thrilled to share my insights and experiences from participating in the Hack U.S program.

Before delving into the details, let me briefly share how my hacking journey started. I stumbled upon the Hack U.S program on Twitter, and like many others, I was eager to dive into the challenges it presented. Despite facing time constraints due to university commitments and health issues, I powered up my laptop and headed to the extensive scope page. What awaited me was a vast scope, and that’s when the real excitement and adventure began.

So, without further ado, let’s embark on this journey together.

1)Publicly accessible GIT directory https://redacted/.git/ [Duplicate]

Given the enormity of the DoD program, I found myself a bit overwhelmed, uncertain of where to commence within the expansive scope. Undeterred, I resolved to streamline my approach by extracting all subdomain IPs from Shodan. My strategy involved fuzzing for endpoints and scrutinizing for sensitive files. To initiate this process, I employed the following Shodan command:

ssl:"target.com" 200

During the process of fuzzing for IPs, I stumbled upon the presence of the /.git/ directory. Recognizing the potential significance of this discovery, I promptly reported my findings. Regrettably, it appears that my enthusiasm led to a duplicate submission. Despite this setback, I remain committed to contributing positively to the security of the program and learning from every experience along the way.

Press enter or click to view image in full size
2)unauthenticated access to Redacted leads to attacker can create frameworks or delete them [accepted].

In the course of fuzzing through the Shodan obtained IPs, I stumbled upon a significant endpoint: https://redacted/#/frameworks. To my surprise, this endpoint lacked any authentication measures, granting me unrestricted access to create or delete frameworks. Recognizing the potential security implications, I promptly reported my findings.

Get Charansai’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Fortunately, the security team acknowledged the severity of the issue, categorizing it as high risk. As a result, I was rewarded with a bounty of 500 USD for my responsible disclosure.

there is also one endpoint https://redacted/#/configuration where i was able to change configuration details

3)sensitive information disclosure on open public repo which leads to access to [redacted] [accepted]

While exploring the scope section, I considered the possibility of finding potential vulnerabilities through GitHub leaks. Although my initial attempts at GitHub reconnaissance didn’t yield significant results, I persisted in my efforts. Employing the dork “target.com” password, I sifted through numerous subdomains, encountering many protected by login portals.

After 30 minutes of diligent searching, I stumbled upon a GitHub repository that stored passwords in clear text, along with the corresponding URLs for access. Recognizing the potential risk, I promptly tested the credentials and, to my fortune, gained access. Despite the sensitivity of the finding, it was classified as a medium severity issue upon reporting.

In the end, I received payment for the unauthenticated access to frameworks

Press enter or click to view image in full size

Thanks for reading :)
