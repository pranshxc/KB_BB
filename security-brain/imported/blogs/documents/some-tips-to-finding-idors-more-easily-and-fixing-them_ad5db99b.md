---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-08_some-tips-to-finding-idors-more-easily-and-fixing-them.md
original_filename: 2022-11-08_some-tips-to-finding-idors-more-easily-and-fixing-them.md
title: Some Tips to Finding IDORs more easily and Fixing them
category: documents
detected_topics:
- idor
- access-control
- sso
- command-injection
tags:
- imported
- documents
- idor
- access-control
- sso
- command-injection
language: en
raw_sha256: ad5db99bfbc9a61be84e6b05bcc3d855ef3d12ee663608d4a6d93dd2725f269f
text_sha256: 21f708b2a6c2e28b003bec3f84fcee1ccf5788fcb0a3ec71cf1b7b52375805aa
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Some Tips to Finding IDORs more easily and Fixing them

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-08_some-tips-to-finding-idors-more-easily-and-fixing-them.md
- Source Type: markdown
- Detected Topics: idor, access-control, sso, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `ad5db99bfbc9a61be84e6b05bcc3d855ef3d12ee663608d4a6d93dd2725f269f`
- Text SHA256: `21f708b2a6c2e28b003bec3f84fcee1ccf5788fcb0a3ec71cf1b7b52375805aa`


## Content

---
title: "Some Tips to Finding IDORs more easily and Fixing them"
url: "https://medium.com/@nxenon/some-tips-to-finding-idors-more-easily-and-fixing-them-2c9d0c58bb4a"
authors: ["Xenon"]
bugs: ["IDOR"]
publication_date: "2022-11-08"
added_date: "2022-11-18"
source: "pentester.land/writeups.json"
original_index: 1937
scraped_via: "browseros"
---

# Some Tips to Finding IDORs more easily and Fixing them

Some Tips to Finding IDORs more easily and Fixing them
Amin Nasiri
Follow
3 min read
·
Nov 8, 2022

43

This time I want to talk about IDOR blinkers which are the keys for finding IDORs faster and some tips for programmers who want to have a general knowledge of IDORs and maybe fix them. First I’m going to say what IDOR is.

According to Portswigger:

“Insecure direct object references (IDOR) are a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly. IDOR vulnerabilities are most commonly associated with horizontal privilege escalation (which means changing your access to a user with the same privileges as yours), but they can also arise in relation to vertical privilege escalation(which means changing your access to a higher privileged user, like an admin user).”

Generally, when we see an ID in a request or anything which is an object in the back-end or concept of an object, we should test it for IDOR vulnerability. There are always things that I pay attention to them that are kind of blinkers showing themselves.

Time Objects:

M
ostly, when I say the object in this article, I mean a parameter in a request. In this case, I mean a parameter that has time in itself. First I tell why you as a penetration tester or a bug bounty hunter should pay attention to time objects. After some years of back-end programming experience, I know that many programmers who want to make something unchangeable that had a deadline in the past, use time inputs, and I have seen many times when they get time from the user and they did not implement the access control properly.

Wait what? Why do they get time from the user?

Get Amin Nasiri’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So it depends on the functionality of the application, but as an example when we have repeated items and different timelines, we need to get the time from the user, and doing this is kind of OK if the controls are implemented correctly.

So what if we have different Object IDs and different timelines?

Press enter or click to view image in full size
Two different cases for accessing objects

So in Case 1, the programmer has to get the time from the user so the user can change or add items based on the time. However, I just want to tell you about Case 2.

So in Case 2:

Web application may just check the time and after passing the time checking level, does not compare IDs with the specified time, then the hacker can easily change or add items that occurred in the past.

Press enter or click to view image in full size
Vulnerable way and secure way of accessing and checking objects

This is an IDOR example on one of the programs which I can not show the details right now:

Press enter or click to view image in full size
Request with Past Time

So everything you have to do for a successful attack is to change the time to a day after that time because you have permission to change the items in the future, but the web application does not check the IDs with time in the request.

Press enter or click to view image in full size
Change the Request Time to Future
The Process is not Correct (for Programmers):

When you have specific IDs for each item, you don’t have to get time from the user. you have to calculate and compare time yourself in the web application back-end based on request time (the arrival time of request).
