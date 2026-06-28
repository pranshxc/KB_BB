---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-12_open-redirect-developers-are-lazyor-maybe-busy.md
original_filename: 2018-12-12_open-redirect-developers-are-lazyor-maybe-busy.md
title: '[Open redirect] Developers are lazy(or maybe busy)'
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: efbe97cbf466c231b9174b3652de1aaafdc2b9f214c59cf420cdba8097de4101
text_sha256: 68e4a042919178fe5f49437b400146b810778f6618bf894342f74e1df0c4cf8a
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# [Open redirect] Developers are lazy(or maybe busy)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-12_open-redirect-developers-are-lazyor-maybe-busy.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `efbe97cbf466c231b9174b3652de1aaafdc2b9f214c59cf420cdba8097de4101`
- Text SHA256: `68e4a042919178fe5f49437b400146b810778f6618bf894342f74e1df0c4cf8a`


## Content

---
title: "[Open redirect] Developers are lazy(or maybe busy)"
url: "https://medium.com/bugbountywriteup/open-redirect-developers-are-lazy-or-maybe-busy-6c51718b10e4"
authors: ["KatsuragiCSL (@ZuuitterE)"]
bugs: ["Open redirect"]
bounty: "150"
publication_date: "2018-12-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5529
scraped_via: "browseros"
---

# [Open redirect] Developers are lazy(or maybe busy)

[Open redirect] Developers are lazy(or maybe busy)
KatsuragiCSL
Follow
3 min read
·
Dec 12, 2018

401

4

This time I am going to write up an open redirect bug I found in a private program. The bug itself was a low-hanging fruit, but the process of reporting it is funny enough.

First, lets’ talk about the bug itself. 🙂

Let’s call the domain example.com. I got myself started by registering an account and poking around. Then I found an URL :

https://www.example.com/account/login?next=https%3A%2F%2Fwww.example.com

“Time to test for open redirect.” I told myself.

First I tried the most straightforward payload: https://www.example.com/account/login?next=https%3A%2F%2Fgoogle.com . Didn’t work. Then I tried next=https://example.com@google.com , //google.com , javascript:alert(1) (turning an open redirect to XSS) etc. but none of these worked. Then HPP (HTTP parameter pollution) came to my mind:

https://www.example.com/account/login?next=https%3A%2F%2Fwww.example.com&next=https%3A%2F%2Fgoogle.com

I didn’t expect anything, instead I just gave it a try and see what would happen. Then my url bar became

https://example.com%2Cwww.google.com

and my browser throws error message to me.

That was the moment I knew that I can exploit it. The value of the second next parameter was not filtered as the first one did. %2C is just a comma, so the mechanism of example.com handling this request is basically joining two next with a comma without filtering the second one.

Get KatsuragiCSL’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So what if I do it in this way?

https://www.example.com/account/login?next=https%3A%2F%2Fwww.example.com&next=@google.com

Note that there is a “@” in the second parameter now. So ends up example.com will redirect me to https://example.com,@google.com, which is in fact going to google.com. So a successful open redirect for me to report now. (I have tried to dig deeper and leverage it to more severe bug, bug I failed 😦 )

Press enter or click to view image in full size

On the second day, I was told that it was a duplicate and the bug was fixed. 😦 . But a thought came into my mind: Why don’t you check if they have TOTALLY fixed it ? Maybe they have made some other mistakes during fixing!

So I go for a check. I tried a lots of payloads on the login URL as above, but I could not exploit it anymore. I started to convince myself that they have fixed it well and no more open redirect bugs for me.

Wait, “no more open redirect bugs”? I can check other endpoints for open redirect bugs!

So, instead of the login page (which is fixed), I tried on the signup page like:

https://www.example.com/account/signup?next=https%3A%2F%2Fwww.example.com&next=@google.com

and I succeed!

Press enter or click to view image in full size

So the conclusion is, their developers forgot the signup page when they were fixing the login page.

Then I got the bounty. Developers are lazy, or maybe just busy.

Bounty rewarded : $150

*Remarks: The bug bounty hunter who found the login page bug before me, he forgot to check for the same bug on the signup page too. LOLLL. Hunters are lazy too!
