---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-10_my-2nd-4digit-bug-bounty-from-facebook.md
original_filename: 2020-08-10_my-2nd-4digit-bug-bounty-from-facebook.md
title: My 2nd 4digit Bug Bounty From Facebook
category: documents
detected_topics:
- command-injection
- information-disclosure
- business-logic
tags:
- imported
- documents
- command-injection
- information-disclosure
- business-logic
language: en
raw_sha256: 8d9400b95d2834556ee56b733308aee7a571d737cee7149dc7018cf9458ffac6
text_sha256: db957ad08c159372cfca4caa8360ed2c6fb4acef9e77bc462d8c452331ab8f34
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# My 2nd 4digit Bug Bounty From Facebook

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-10_my-2nd-4digit-bug-bounty-from-facebook.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, business-logic
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `8d9400b95d2834556ee56b733308aee7a571d737cee7149dc7018cf9458ffac6`
- Text SHA256: `db957ad08c159372cfca4caa8360ed2c6fb4acef9e77bc462d8c452331ab8f34`


## Content

---
title: "My 2nd 4digit Bug Bounty From Facebook"
url: "https://medium.com/@sudipshah_66336/my-2nd-4digit-bug-bounty-from-facebook-99baa727ed02"
authors: ["Sudip Shah"]
programs: ["Meta / Facebook"]
bugs: ["Logic flaw", "Information disclosure"]
publication_date: "2020-08-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4337
scraped_via: "browseros"
---

# My 2nd 4digit Bug Bounty From Facebook

My 2nd 4digit Bug Bounty From Facebook
Sudip Shah
Follow
2 min read
·
Aug 10, 2020

250

I found an unintended behaviour in the FBLite app where the page admin could be easily exposed while adding a photo to his story . When the Page sends a photo message through FBLite then we can observe the Add to story options there . While clicking on it , the admin is getting disclosed . The usual behaviour should be that while clicking on the add to story options , the photo should be added to the page’s story but in this scenario the photo is being added to the page_admin’s personal id which leads to admin disclosure.

Impact
It leads to page admin disclosure which is a serious issue.
A page admin will post a story to their personal account instead of the Page when messaging from the Page inbox on FBLite and hitting “Add to Story”

Steps
1.UserA sends a photo to UserB through the page.
2. UserA clicks on Add to story option
3. The photo is added to the UserA’s story instead of Page’s story which is leading to page admin disclosure.

I don’t have a POC video available as I sent them the steps only and they were able to reproduce with that much of information only .

Get Sudip Shah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This writeup is a bit type of non technical but I hope you all are able to understand the bug and enjoy the writeup .

Press enter or click to view image in full size

I can’t describe my happiness that I got after receiving this awesome notification . I was finally able to buy an awesome Laptop with the help of this bounty from Facebook . So I thank Facebook Security team for this wonderful experience . I was like this to myself.

Finally I got Listed in the Hall Of Fame of Facebook too due to the bug reports that I sent to Facebook .

I still have a lot to learn in this journey of bug hunting and this motivated me to keep continuing the journey . :)

Thanks a lot to everyone and very special thanks to beloved Ashok dai .

#Bugbounty

Follow Infosec Writeups for more.
