---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-25_my-first-bug-on-google.md
original_filename: 2020-10-25_my-first-bug-on-google.md
title: My first bug on Google
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
raw_sha256: 6f2b3919df45647438cba3f61aed38ba12bd411dc0a15d552bdb302cb95fea86
text_sha256: fb8d46605e1525954f00716c3e023ba4f56158f7532dbd9f81f461e650d7a60b
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# My first bug on Google

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-25_my-first-bug-on-google.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `6f2b3919df45647438cba3f61aed38ba12bd411dc0a15d552bdb302cb95fea86`
- Text SHA256: `fb8d46605e1525954f00716c3e023ba4f56158f7532dbd9f81f461e650d7a60b`


## Content

---
title: "My first bug on Google"
url: "https://medium.com/bugbountywriteup/my-first-bug-on-google-observation-wins-1a13d0ea54b0"
authors: ["Manas Harsh (@ManasH4rsh)"]
programs: ["Google"]
bugs: ["IDOR"]
publication_date: "2020-10-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4182
scraped_via: "browseros"
---

# My first bug on Google

My first bug on Google
The clearer you see, the better you win!
Manas Harsh
Follow
2 min read
·
Oct 25, 2020

530

3

Press enter or click to view image in full size

So, I was trying Google this time to see if I get something interseting in it. I spent like 20 days on an acquisition and finally I found some interesting stuffs over there. This is the tell about one of them:)

While I was testing almost everything, I saw a URI in burp which was providing some user data including thier user IDs and usernames. It was looking something like this:- redected.com/c/ask/20/l/latest.json. It got my attention so I started searching for some info where I could try other users’ user IDs or username as well.

Get Manas Harsh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Finally I found an endpoint where it was showing the data of my account. The Endpoint looked like this:- redected.com/u/yourusername.json. Well this was the endpoint which I was trying to find since a while and that’s all we need as a hacker! I changed the usernames to the ones which I found from another endpoint and BOOM! I was able to see the PII of other users as well. I have put some POCs of them below:-

Press enter or click to view image in full size
Press enter or click to view image in full size

That was an easy find once you get that endpoint. I took the time and it paid off. I would like to mention “no target is safe”. What you need to create is this mindset. Once you have it, go ahead and hack’em all! Also, it really matters how much time you are putting into your efforts. Big targets, actually huge targets need time to get exploited. Stick with it and you will find something eventually:)

I hope this helps people out there to observe targets better. With this, I will wrap up this write-up here. If you like this, follow me on twitter. Also, a clap will be highly appreciated:)

Keep your head high and your hacks higher!

Happy hacking! adios ❤

LinkedIn:- https://www.linkedin.com/in/manas-harsh-05636a154/
