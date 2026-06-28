---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-09-05_facebook-bug-bounty-permission-bug.md
original_filename: 2018-09-05_facebook-bug-bounty-permission-bug.md
title: Facebook Bug Bounty! {Permission Bug}
category: documents
detected_topics:
- access-control
- command-injection
- business-logic
tags:
- imported
- documents
- access-control
- command-injection
- business-logic
language: en
raw_sha256: 864bbd228c99036b7a8cc94d2ec6fb94204a248636ac49573c77d19a88e76516
text_sha256: d8e49678394d7bcf097d626d8eb4fa8b6a49c4716587e517a8ad15506c69b038
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Facebook Bug Bounty! {Permission Bug}

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-09-05_facebook-bug-bounty-permission-bug.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, business-logic
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `864bbd228c99036b7a8cc94d2ec6fb94204a248636ac49573c77d19a88e76516`
- Text SHA256: `d8e49678394d7bcf097d626d8eb4fa8b6a49c4716587e517a8ad15506c69b038`


## Content

---
title: "Facebook Bug Bounty! {Permission Bug}"
url: "https://medium.com/@alicanact60/facebook-bug-bounty-permission-bug-19c9358d2297"
authors: ["Ali Tütüncü (@alicanact60)"]
programs: ["Meta / Facebook"]
bugs: ["Broken authorization", "Logic flaw"]
bounty: "750"
publication_date: "2018-09-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5724
scraped_via: "browseros"
---

# Facebook Bug Bounty! {Permission Bug}

Ali TÜTÜNCÜ
 highlighted

Top highlight

Facebook Bug Bounty! {Permission Bug}
Ali TÜTÜNCÜ
Follow
2 min read
·
Sep 5, 2018

508

5

Press enter or click to view image in full size

Hi guys! My name is Ali Tütüncü and I am a security researcher. When I started to bug bounty, I said “I will find a vulnerability on Facebook. This is my goal.”. And I found a vulnerability on 12 Aug 2018.

This is my first write up.

12 Aug 2018

I was searching vulns on facebook 4 days ago. Then, I was bored and started watch “proof of concept videos”. I watched a video and It gave me an idea.

Get Ali TÜTÜNCÜ’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I went to App’s roles, I saw this permissions:

Press enter or click to view image in full size

Tester can’t access app’s insights. Really?

I tried this steps:

Go to http://developers.facebook.com/apps and create a app.
Go to https://developers.facebook.com/apps/{App Id}/roles/roles/
Add a tester.
Login with your tester account.
Go to https://www.facebook.com/insights. But I saw nothing. What the?

After a thought, i went to https://facebook.com/analytics/{App Id} and YES! I saw all anaytcis and and I could have edited them.

PoC Video:

Timeline:
Aug. 12, 2018 - Report Triaged
Aug. 15, 2018 - Report Triaged
Aug. 28, 2018 - Issue Fixed
Sept. 05, 2018 - Bounty of $750 Awarded

Follow me on Twitter: https://twitter.com/alicanact60
