---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-17_accessing-deleted-comment-for-a-bug-bounty-writeup.md
original_filename: 2024-01-17_accessing-deleted-comment-for-a-bug-bounty-writeup.md
title: 'Accessing deleted comment for $$: A Bug Bounty Writeup'
category: blogs
detected_topics:
- idor
- command-injection
- rate-limit
- automation-abuse
- business-logic
tags:
- imported
- blogs
- idor
- command-injection
- rate-limit
- automation-abuse
- business-logic
language: en
raw_sha256: 9e147d79cc69955f11c2d7c0c65620af2cc0be23b643616db74bd3f09df559b8
text_sha256: 01e6e556be852e437e863716e3ada053c602c840520c5331215bae0be6841582
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Accessing deleted comment for $$: A Bug Bounty Writeup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-17_accessing-deleted-comment-for-a-bug-bounty-writeup.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, automation-abuse, business-logic
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `9e147d79cc69955f11c2d7c0c65620af2cc0be23b643616db74bd3f09df559b8`
- Text SHA256: `01e6e556be852e437e863716e3ada053c602c840520c5331215bae0be6841582`


## Content

---
title: "Accessing deleted comment for $$: A Bug Bounty Writeup"
url: "https://vijetareigns.medium.com/accessing-deleted-comment-for-a-bug-bounty-writeup-95d56662d209"
authors: ["the_unluck_guy (@7he_unlucky_guy)"]
bugs: ["Logic flaw"]
publication_date: "2024-01-17"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 537
scraped_via: "browseros"
---

# Accessing deleted comment for $$: A Bug Bounty Writeup

Accessing deleted comment for $$: A Bug Bounty Writeup
the_unlucky_guy
Follow
3 min read
·
Jan 17, 2024

426

3

Hello hackers, I am back with a new bug bounty write-up. In this blog, I am going to show how I was able to access deleted comments on a community thread of a website. I will be using redacted.com as the main domain.

*.redacted.com is in the scope. As usual, I started with subdomain enumeration and found 500+ live subdomains. I took screenshots of all subdomains using tool aquatone and started reviewing them. One of the screenshot having subdomain name community.redacted.com caught my eyes.

Community website at community.redacted.com where authenticated user can create a thread, interact with other thread and can interact with other users. I started exploring the website and capturing every request in the proxy tool burp suite.

After exploring the website, I started reviewing all the requests and responses from the community.redacted.com. There is one GET endpoint https://community.redacted.com/ajax/ugc/frontend/comment/getComment?id=comment_id&tid=thread_id which is used to fetch comment from the thread based on the parameter id=comment_id&tid=thread_id . Both comment_id and thread_id is long numeric string. I open the GET endpoint https://community.redacted.com/ajax/ugc/frontend/comment/getComment?id=comment_id&tid=thread_id in the browser and found that all the comment from my thread is visible in the JSON response.

What i did next is I deleted the comment from my community thread and in UI no comment is visible in my thread as i deleted it.

Press enter or click to view image in full size

I reopened the same GET endpoint https://community.redacted.com/ajax/ugc/frontend/comment/getComment?id=comment_id&tid=thread_id in the browser and found that the deleted comment is still visible in JSON response. Thread comment is only deleted from the UI but not actually deleted from the backend/database so anyone or thread owner can access the deleted comment of the thread.

Press enter or click to view image in full size

The bug is not having too much of impact because of long numeric comment_id and thread_id. Anyone can access the deleted comment if comment_id is know or they captured the comment_id of a thread before deletion of comment. I sent report to the security team as this is violation of privacy of the user. Security team accepted the report as Low and fixed it.

Security Team to Me

Timeline:

Get the_unlucky_guy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Nov 09, 2021 — Reported

Nov 24, 2021 — Triaged

Dec 8, 2021 —$$ Rewarded

Dec 24, 2021 — Fixed.

To schedule a one-on-one session with me, please make a booking through the Topmate platform.

Thanks for reading, hope you learned something new. Do clap and share if you like it. Happy Hacking and Try Harder!.

Twitter: 7he_unlucky_guy
Linkedin: Vijeta
Topmate: Vijeta
