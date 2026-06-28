---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-12_facebook-bug-bounty-page-admin-disclose-bug-facebook-android-app.md
original_filename: 2019-07-12_facebook-bug-bounty-page-admin-disclose-bug-facebook-android-app.md
title: Facebook Bug bounty page admin disclose bug {Facebook Android app}
category: documents
detected_topics:
- mobile-security
- command-injection
- information-disclosure
tags:
- imported
- documents
- mobile-security
- command-injection
- information-disclosure
language: en
raw_sha256: f665d507222273a322d3ae5fa778aed95fbe60313235f3e582345eefc5e5d3e7
text_sha256: 472f4d6c3f48dec868866052d4c9313d4bea4cebd9ce192538881395a16abc55
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Bug bounty page admin disclose bug {Facebook Android app}

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-12_facebook-bug-bounty-page-admin-disclose-bug-facebook-android-app.md
- Source Type: markdown
- Detected Topics: mobile-security, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `f665d507222273a322d3ae5fa778aed95fbe60313235f3e582345eefc5e5d3e7`
- Text SHA256: `472f4d6c3f48dec868866052d4c9313d4bea4cebd9ce192538881395a16abc55`


## Content

---
title: "Facebook Bug bounty page admin disclose bug {Facebook Android app}"
url: "https://medium.com/@yusuffurkan/facebook-bug-bounty-page-admin-disclose-bug-facebook-android-app-c0fa50459177"
authors: ["Yusuf Furkan (@h1_yusuf)"]
programs: ["Meta / Facebook"]
bugs: ["Information disclosure"]
bounty: "500"
publication_date: "2019-07-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5155
scraped_via: "browseros"
---

# Facebook Bug bounty page admin disclose bug {Facebook Android app}

Facebook Bug bounty page admin disclose bug {Facebook Android app}
Yusuf
Follow
1 min read
·
Jul 12, 2019

229

1

Hello community! my name is Yusuf Aydın

I found a vulnerability on 1 july 2019

I tried this steps:

Create an event from a page [facebook android Mobile app]
Add another account (be sure he/she is not admin of the page) as a co-host in the event.

3. Open another account and click the notification about the co-host.

Get Yusuf’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4.You will see the name of the admin that has added you as a co-host like this

5.two notifications come at the same time and explain the admin of this page.

Press enter or click to view image in full size

PoC Video:

https://youtu.be/HdZb0t8BysM

Timeline:
jul. 1, 2019 — Report sent
jul. 4, 2019 — Report Triaged
jul. 8, 2019 — Issue Fixed
jul. 11, 2019— Bounty of $500 Awarded

Follow me on Twitter: https://twitter.com/h1_yusuf
