---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-26_how-misconfigured-api-leaked-user-private-information.md
original_filename: 2018-10-26_how-misconfigured-api-leaked-user-private-information.md
title: How Misconfigured API leaked user private information?
category: documents
detected_topics:
- idor
- access-control
- command-injection
tags:
- imported
- documents
- idor
- access-control
- command-injection
language: en
raw_sha256: 9fa7285b380acca93246e42f118b82519ab7dd477a0178b9e45df6ada1efdd60
text_sha256: 3a75c5f812f97c854df8f054c39278b5f6404f81dd402610884567364418eeb1
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How Misconfigured API leaked user private information?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-26_how-misconfigured-api-leaked-user-private-information.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `9fa7285b380acca93246e42f118b82519ab7dd477a0178b9e45df6ada1efdd60`
- Text SHA256: `3a75c5f812f97c854df8f054c39278b5f6404f81dd402610884567364418eeb1`


## Content

---
title: "How Misconfigured API leaked user private information?"
url: "https://medium.com/@Skylinearafat/how-misconfigured-api-leaked-user-private-information-e3e8c13e52e4"
authors: ["Yeasir Arafat"]
bugs: ["IDOR", "Broken authorization"]
publication_date: "2018-10-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5625
scraped_via: "browseros"
---

# How Misconfigured API leaked user private information?

How Misconfigured API leaked user private information?
Yeasir Arafat
Follow
2 min read
·
Oct 26, 2018

131

H
ello folks, it’s been a long since I didn’t post an article about my findings, hence I was busy with my personal life.

I am here to share my recent finding on a private bug bounty program. I have got some experience on testing API sites. It’s more fun to play with them.

Let’s say the vulnerable site name is redact.io. The site is using API to fetching the user data from the server as such api.redact.io.

Before targeting on api.redact.io I try to understand how the site API was working. I read the full documentation from docs.redact.io. This is very important to know how your target site is working, you can make a right approach after gathering knowledge about your target.

Press enter or click to view image in full size

I came to know that the targeted domain redact.io is fetching user sensitive data using this endpoint https://api.redact.io/service/<userID>. Here the userID is the unique userID of a user of that site.

While I tried to catch the fetching data from the URL without authorization https://api.redact.io/service/<userID> it’s returning me an 404 error,,

Press enter or click to view image in full size

Hmm? What next?

Get Yeasir Arafat’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

It seems the site is working fine, No info leaking. I found a little trick here to exposed user sensitive information such as Email, userId, userName, scope etc.

Replacing the UserName on UserID field disclose the information of a user of redact.io without authorization. The site scope(service) is carrying user information behind the GET request in API.

Press enter or click to view image in full size

If you take a look at the UserName you can see it’s the same one above UserId I mentioned.

Basically, this flaw occurs via misconfigured or unsecured API. Which is not configured properly and allows an attacker to steal victims sensitive information.

09-Aug-2018 → Bug Reported

22-Aug-2018 → Bug Fixed

23-Aug-2018 →> Bounty Awarded

Thanks for reading! Yeasir Arafat
