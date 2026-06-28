---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-12-19_how-one-bug-scored-me-double-rewards.md
original_filename: 2023-12-19_how-one-bug-scored-me-double-rewards.md
title: How One Bug Scored Me Double Rewards!
category: documents
detected_topics:
- idor
- command-injection
- information-disclosure
- api-security
- cloud-security
tags:
- imported
- documents
- idor
- command-injection
- information-disclosure
- api-security
- cloud-security
language: en
raw_sha256: 5b382763b360f0b1b2a5f33a3426a1427398963c25a16708cff63c698e4b3056
text_sha256: 1b550905d7a904d72ff77b0a263903240dabc79eed8d09b00d5c3a5d1905eedf
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# How One Bug Scored Me Double Rewards!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-12-19_how-one-bug-scored-me-double-rewards.md
- Source Type: markdown
- Detected Topics: idor, command-injection, information-disclosure, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `5b382763b360f0b1b2a5f33a3426a1427398963c25a16708cff63c698e4b3056`
- Text SHA256: `1b550905d7a904d72ff77b0a263903240dabc79eed8d09b00d5c3a5d1905eedf`


## Content

---
title: "How One Bug Scored Me Double Rewards!"
url: "https://anasbetis023.medium.com/how-one-bug-scored-me-double-rewards-355b8d02cdbf"
authors: ["Anas H Hmaidy"]
bugs: ["Information disclosure", "IDOR"]
bounty: "300"
publication_date: "2023-12-19"
added_date: "2024-02-01"
source: "pentester.land/writeups.json"
original_index: 607
scraped_via: "browseros"
---

# How One Bug Scored Me Double Rewards!

Anas H Hmaidy
 highlighted

Anas H Hmaidy
Follow
4 min read
·
Dec 19, 2023

838

5

How One Bug Scored Me Double Rewards!
Press enter or click to view image in full size
https://www.pexels.com/photo/security-logo-60504/

Good day!

I hope you are well. As this is my first write-up here, I hope you like it. I’ll get straight into the bugs I found a while ago in a private program at HackerOne. Let’s call it redacted.com :)

The program I am hunting on is resolving any subdomain “anything.redacted.com” to the main website login page “redacted.com/login”, That behavior is new to me so I thought it is kind of useless to use subdomain gathering tools.

Press enter or click to view image in full size
Hide the pain

I started with a simple Shodan dork:

ssl:redacted.com

A lot of results come out until I found an IP address going to the subdomain “z2007.redacted.com” — interesting! You can look at “z2007”; it seems like it is some old forgotten server!

The main website services are like making video sessions and screenshare between others. After searching, I found a test page at “z2007.redacted.com/agv/sampleAgent.html”.

Press enter or click to view image in full size
The test page
Request body of the test page

OK. Let us send a request and intercept it. You can see the PUT /offer request body above. I tried to change everything to see the response, and it was the same one response. Except when changing the “groupid” param, there was a little difference in the response; you give the groupid, and the server responds with the group name.

Server responds

At first, this changing was not interesting for me. But after thinking about the website services and functions, that group name was a new thing I hadn’t seen before. So I reported it as “Information Disclosure [Group Name Manipulation],” and Alhamdulillah, the program accepted it as the group name should not be disclosed without authentication, and I got a bounty of 100$ :)

Get Anas H Hmaidy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

OK, should we stop here? I don’t think so. As we found a bug at one subdomain, it might be the same bug there on another one! Just visit every possible subdomain and make a PUT request to see the response.

With some Google dorking, I gathered some subdomains and started to send the same PUT /offer request above to each subdomain. Unfortunately, I got nothing, and I stopped here :(

Surely, no, just don’t stop. The bug is there; you just need to search harder. Luckily, I found a subdomain “video.redacted.com” allows the previous PUT requests! After searching, I found that the server accepts three params “groupid, isAnonymous, and a new param called personid.”

Now, access: https://video.redacted.net/offer?groupid=21582&isAnonymous=true&personid=1990018
Intercept the request and change the method to PUT and click forward to see results in the browser. And WOW! A lot of results came out!!

video.redacted.com responds

By this, I was able to register a video session for anyone in any group. If you modify the groupid and personid parameters, you will get new session data.
I reported it as “IDOR Leads to Unauthorized Access to Sensitive Users Session Data” and Alhamdulillah, the program accepted it and rewarded me with 200$.

At the end, things didn’t go well with HackerOne support. They banned me from the reward I got because I live in Syria, and so I am not applicable for any rewards due to some US laws.

feel the pain

But it doesn’t matter. Money will come sooner or later. As they say, you are only responsible for the effort, not the outcome.

I hope you enjoyed it; please don’t forget to give it a like :)

Join my telegram channel: anas_hmaidy

Follow me on LinkedIn: anas_hmaidy

Best Regards :)
