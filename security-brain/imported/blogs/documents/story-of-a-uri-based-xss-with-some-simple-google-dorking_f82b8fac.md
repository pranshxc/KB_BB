---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-02_story-of-a-uri-based-xss-with-some-simple-google-dorking.md
original_filename: 2019-06-02_story-of-a-uri-based-xss-with-some-simple-google-dorking.md
title: Story of a uri based xss with some simple google dorking
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- api-security
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- api-security
language: en
raw_sha256: f82b8facec916ee26876975e26c7f79b8777261f951c049bc493c3aa79fb2af6
text_sha256: 38229b81ae429bcfb8e2bbf23d487cfdcbaa6ef7d5b4b65fb42598ef5e1df9b6
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Story of a uri based xss with some simple google dorking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-02_story-of-a-uri-based-xss-with-some-simple-google-dorking.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `f82b8facec916ee26876975e26c7f79b8777261f951c049bc493c3aa79fb2af6`
- Text SHA256: `38229b81ae429bcfb8e2bbf23d487cfdcbaa6ef7d5b4b65fb42598ef5e1df9b6`


## Content

---
title: "Story of a uri based xss with some simple google dorking"
url: "https://medium.com/@nandwanajatin25/story-of-a-uri-based-xss-with-some-simple-google-dorking-e1999254aa55"
authors: ["Jatin Aesthetic (@techyfreakk)"]
bugs: ["XSS"]
publication_date: "2019-06-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5236
scraped_via: "browseros"
---

# Story of a uri based xss with some simple google dorking

Jatin Nandwana
Follow
2 min read
·
Jun 3, 2019

102

1

Story of a uri based xss with some simple google dorking

Hey everyone,

This is a old xss bug which I found in a private program on hackerone by doing some google recon. Because it was a private program I will the name the site as www.example.com everywhere.

So lets start,

The program seemed to be quite old but its scope was wide with a bunch of domains.I thought that many people might have already tested the main domain. So I thought of exploring other domains in the list first. During the initial testing I did’nt find anything useful.Then I thought of doing some google dorking using

Site:*.example.com inurl:redirect

and appending various things like intext: ../index, admin , sql , url , redirect etc. After using redirect in inurl parameter I got an interesting endpoint like this

example.com/social?redirect=/somewhere

It suddenly took my interest and I started looking for bugs in it. First I tried redirecting it to google.com and it worked. Then I thought of javascript uri parsers which can lead to xss. And added this simple javascript uri in redirect parameter

example.com/social?redirect=javascript://alert(1)

And now the site took me to the login page as I was not logged in to the site. I logged in and alert popped up. There was also no protection on logout so user can be logged out of his account and then again be sent to this malicious url and when he enters the creds xss executes and the attacker can do whatever he want like phishing, cookie stealing, keylogging, etc. Unfortunately the same endpoint was also on some other domains of that program so they were also vulnerable.

Get Jatin Nandwana’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The program responded very fastly and gave a good reward.

THINGS TO CONSIDER FROM THIS BUG:

If you are lost in a program and dont find anything, always look for other things like google dorking, reading source code for some other endpoints which are not seen in main app and might be many hunters have missed them.

QUICK TIP

I will add a small list of dorks you can use to find these kind of bugs.

inurl: redirect,url,next,redirect_to,page,site

These can even lead to ssrf if there is not proper sanitization in code.So keep digging on these. You can also try other dorks for finding hidden gems. You can find the latest updated dorks here https://www.exploit-db.com/google-hacking-database . Google dorking is great to find some sensitive endpoints,parameters, always give it a try during your testing :)

I will post some of my more findings here in the upcoming weeks. Till then keep hacking and sharing. This community is great and we should learn from each other and share. #TogetherWeHitHarder

Thanks,

Jatin

Twitter : https://twitter.com/techyfreakk
