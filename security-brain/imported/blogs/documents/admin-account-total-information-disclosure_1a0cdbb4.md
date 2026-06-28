---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-15_admin-account-total-information-disclosure.md
original_filename: 2019-06-15_admin-account-total-information-disclosure.md
title: Admin Account total Information Disclosure
category: documents
detected_topics:
- information-disclosure
- command-injection
tags:
- imported
- documents
- information-disclosure
- command-injection
language: en
raw_sha256: 1a0cdbb49564f0913f40ed837c4190ba6ff5fcd54073ae01b2d5a2195ccb04d1
text_sha256: 3cae5323eacd14af26da469886bce03d439943685b3d4c15e76eef697dfbec38
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Admin Account total Information Disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-15_admin-account-total-information-disclosure.md
- Source Type: markdown
- Detected Topics: information-disclosure, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `1a0cdbb49564f0913f40ed837c4190ba6ff5fcd54073ae01b2d5a2195ccb04d1`
- Text SHA256: `3cae5323eacd14af26da469886bce03d439943685b3d4c15e76eef697dfbec38`


## Content

---
title: "Admin Account total Information Disclosure"
url: "https://medium.com/@nishantrustlingup/admin-account-total-information-disclosure-72ec60da4a78"
authors: ["Nishant Saurav (@inishantsinha)"]
bugs: ["Source code disclosure", "Information disclosure"]
bounty: "200"
publication_date: "2019-06-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5216
scraped_via: "browseros"
---

# Admin Account total Information Disclosure

Admin Account total Information Disclosure
Nishant Saurav
Follow
2 min read
·
Jun 15, 2019

65

1

Hi Everyone, this is my 2nd writeup on the issue I found on one of India’s premier website for sharing Startup and Tech News.

I was actually hunting for the “Source Code Disclosure” Vulnerability. To do so, I only captured the request i.e. https://www.xyz.com/idnf.

where ‘idnf’ is the identifier which could be anything.

But when one by one I started checking the Payload results. I opened a request/ Payload/ File named as ‘1’ as shown in the screen capture below.

Press enter or click to view image in full size

The Vulnerability was pretty much straight forward. It was Information Disclosure and the Source Code Disclosure as well and that too at the admin level.

Get Nishant Saurav’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was like...

The website was based on the WordPress and all the content including IP of the DB, admin panel, and the Database’s name, id, and password was contained in this file in the plaintext as shown in the screenshots below.

Press enter or click to view image in full size
Press enter or click to view image in full size

As soon as I got these Pieces of information I tried connecting and I was successful. So, Informed the owner of the website and they patched the issue fucking quickly. ( by quickly I meant, they hardly took 4 hours to recheck the issue and respond back to them for the bounty). So, I checked and confirmed the mitigation and on Wednesday I received my Bounty of $200. Not Big though but quite a good amount looking at the size of the company.

Thanks for being here reading till now. Please mention in comments if you need more information in my writeups if I am missing out something because I am new to all these articulating stuff.

If you have any questions you can always find me on Twitter from the link below.

Twitter: https://twitter.com/inishantsinha

:D
