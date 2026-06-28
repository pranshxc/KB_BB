---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-23_my-first-valid-bug-bypass-the-admin-panel.md
original_filename: 2022-09-23_my-first-valid-bug-bypass-the-admin-panel.md
title: My First Valid Bug “Bypass the Admin Panel”
category: documents
detected_topics:
- sso
- access-control
- command-injection
tags:
- imported
- documents
- sso
- access-control
- command-injection
language: en
raw_sha256: 977111fffc321cf2580b9027b2767eccb41d4131edaaa0a861a4d2ecbf6ac357
text_sha256: 41ad90a499eefa0254969f361ed199b73721ced84ca69415e1d03ce513c43d39
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# My First Valid Bug “Bypass the Admin Panel”

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-23_my-first-valid-bug-bypass-the-admin-panel.md
- Source Type: markdown
- Detected Topics: sso, access-control, command-injection
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `977111fffc321cf2580b9027b2767eccb41d4131edaaa0a861a4d2ecbf6ac357`
- Text SHA256: `41ad90a499eefa0254969f361ed199b73721ced84ca69415e1d03ce513c43d39`


## Content

---
title: "My First Valid Bug “Bypass the Admin Panel”"
url: "https://medium.com/@digant_15/my-first-valid-bug-bypass-the-admin-panel-e859e72a1b7d"
authors: ["Digant Prajapati"]
bugs: ["Authentication bypass"]
publication_date: "2022-09-23"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2129
scraped_via: "browseros"
---

# My First Valid Bug “Bypass the Admin Panel”

My First Valid Bug “Bypass the Admin Panel”
Digant Prajapati
Follow
3 min read
·
Sep 23, 2022

209

5

Hey everyone, I am Digant Prajapati. Cyber Security Enthusiast and currently focusing on bug bounty💸.

This is my first write-up on the first valid bug that I have found which is “Bypass the admin panel” in just 5 minutes 😎. Without wasting any more time, let’s start !!

PS: I love cats😻 very much So, I invited them for contribution.🤗

I love to check education sites and specially universities sites because they have some juicy information about internal information and sometimes they have all the record of professors and students including their private email-id, contact number, department and others.

During pandemic time, I was searching about Cyber Security and in that i was so curious to know that how hackers hack the system and earn money with that. So, I reached to one video named “ A Day with a Hacker”. After that I saw the video and my mind was surprised.

I searched all things about cyber security and I came up with new term “Bug Bounty” and gathered all resources which will helpful to me to do bug hunting.

One day I was searching about education site with google dork portal.target.com. I will call target “redacted.com” due to privacy concerns and everyone is naming that so…🙄👀

I quickly open that domain and it redirects me to the login panel.
https://portal.redacted.com/example/(filename*).jsp

Press enter or click to view image in full size

So, first I searched for default credentials but it didn’t work. After that I tried SQL Payload but didn’t work. After getting tired I searched about innovative process — Recon. I used this google dork site:”portal.target.com” -www . In just few seconds I got results of some URLs.

Get Digant Prajapati’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I opened all the URLs in New Tab but it redirects me to login page. I was confused about that why every time i redirect to login page.

One thing I noticed here, all the URLs are authenticated so it redirects me directly to the login page. Without wasting time I copied all authenticated URLs into my notepad.

Eg. — https://portal.redacted.com/example/(secret*)ServAuthorization.jsp and https://portal.redacted.com/example/(secret*)PersonList.jsp

Now I search domain with no redirect extention and enter the domain name like this :- “https://portal.redacted.com" and this time it does not redirect so it means I bypass the admin panel.

Press enter or click to view image in full size

Now I able to access all the information like Name, E-mail ID, Number and other informations. I am not only access these informations but also I was able to add myself as s student of that university. After knowing that I was like:

I quickly made a Proof of Concept (POC) video and reported to security team of that university. They took more than 2 months to saw my mail and after 2 months suddenly at one night I got mail from security team and they appreciate my report and decided to give me $50 as a bounty and that time I was overwhelmed with joy just because I received my first bounty.

Credit: https://medium.com/@ratnadip1998

I hope this will helpful for you :)
