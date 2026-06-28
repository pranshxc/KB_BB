---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-29_1st-bounty-story-rewarded-300-idor.md
original_filename: 2019-07-29_1st-bounty-story-rewarded-300-idor.md
title: 1st Bounty Story | Rewarded 300$ (IDOR)
category: documents
detected_topics:
- idor
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- idor
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: f8ac213c763e5f1dff8b8049d9af8eeba0751780838510443f7d4b337c100b31
text_sha256: 03ea9c429fbf545c1eefcdb8014a12a587dc702144d25824a192152fe2e95edb
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# 1st Bounty Story | Rewarded 300$ (IDOR)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-29_1st-bounty-story-rewarded-300-idor.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `f8ac213c763e5f1dff8b8049d9af8eeba0751780838510443f7d4b337c100b31`
- Text SHA256: `03ea9c429fbf545c1eefcdb8014a12a587dc702144d25824a192152fe2e95edb`


## Content

---
title: "1st Bounty Story | Rewarded 300$ (IDOR)"
url: "https://medium.com/@mdhridoy_4607/1st-bounty-story-rewarded-300-idor-bc4e1708e8e0"
authors: ["Md Hridoy"]
bugs: ["IDOR"]
bounty: "300"
publication_date: "2019-07-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5115
scraped_via: "browseros"
---

# 1st Bounty Story | Rewarded 300$ (IDOR)

Top highlight

1st Bounty Story | Rewarded 300$ (IDOR)
Md Hridoy
Follow
3 min read
·
Jul 30, 2019

240

8

T
his is My 1st Bounty Rewarded Story and 1st Writeup.I am still learner not a pro man and week in english so ignor mistake spelling.My internet journey begin 2015. The first hacking word I could Found on My Facebook NewsFeed. From that moment on, hacking created a curiosity. After that I got to know about white hats and black hats. Then the interest in learning how to work white hats hacker.Then i am search on Google and Youtube.I am found many many resourcse.I hope Every Body already Know Google and Youtube World Best University For Everything Learning.One Day i am reading a blog post here i found 1 line here author write a line about Bug Bounty Programme.Then my curiosity jump Low level to High Level what is Bug Bounty Programme.Then I am again search google about Bug Bounty Programme Becasue i am already gather white hat hacking knowledge.Then i am found a interesting blog about Bug Bounty Programme to earn Money.Then i am setup my maind to learn about bug hunting,Then i am again search on google found many resource and start learning bug hunting method.Then i am join facebook,twitter bug bounty hunter group.I am skip many point in my bug bounty journy because its not possible to finished write 1 post.

L
ets start how i am found IDOR Vulnerability.Report status (Unresolved) so i am not mention site name.

after 1.5 year later i am login my bugcrowd account.Then i am choose a site.then i am find this sites subdomin using Sublist3r i am found many domain then i am check one bye one domain in my browser.

Then i am found a site and create a account here after i login dashboard i see here one 5 star review section.Like Below:

Press enter or click to view image in full size
Review Section

Then i am create 2 account and copy client id.Like Below:

user Profile (A)

test1@gmail.com > client id= 5d0687ab5568c800dc14aaae

Attacker Profile (B)

test2@gmail.com > client id= 5d068d935568c800df14aa97

Get Md Hridoy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then i am capture puting review request in bup suite.Like Below:

Press enter or click to view image in full size
Request Capture

Then i am replace user Profile (A) client id to Attacker Profile (B) client id and change 5 star to 2 star then forward request.Like Below:

Press enter or click to view image in full size

B
oom then i see user 5 star rating successfully change to 2 star rating.Like Below:

Press enter or click to view image in full size

My Feeling Below The Giphy Because Its My 1st Bounty />

Some Resource I Share Below.This Sites Writeup and poc i am follow many times:

List Of Bug Bounty Writeup
About IDOR
Bug Bounty Notes
Bugcrowd University

Thanks For Reading.Here My Facebook Profile feel free knock me any question about bug bounty.

Remember: I am not a pro man I am Still Learner In This Field.
