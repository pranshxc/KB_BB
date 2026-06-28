---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-11-17_transforming-a-domain-into-the-matrix-an-open-redirect-story.md
original_filename: 2017-11-17_transforming-a-domain-into-the-matrix-an-open-redirect-story.md
title: Transforming a Domain into the Matrix (an open redirect story)
category: documents
detected_topics:
- oauth
- command-injection
- cors
- api-security
- mobile-security
tags:
- imported
- documents
- oauth
- command-injection
- cors
- api-security
- mobile-security
language: en
raw_sha256: 1ab45db4f3044f791a88f548f7a59f2fe2f99cdfa84043724073cb567b3b2ac9
text_sha256: 2886857ce0b137bdb54d7c1af856e8c254ad4bbb5c794ec882dd0fb5ea62936a
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Transforming a Domain into the Matrix (an open redirect story)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-11-17_transforming-a-domain-into-the-matrix-an-open-redirect-story.md
- Source Type: markdown
- Detected Topics: oauth, command-injection, cors, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `1ab45db4f3044f791a88f548f7a59f2fe2f99cdfa84043724073cb567b3b2ac9`
- Text SHA256: `2886857ce0b137bdb54d7c1af856e8c254ad4bbb5c794ec882dd0fb5ea62936a`


## Content

---
title: "Transforming a Domain into the Matrix (an open redirect story)"
url: "https://medium.com/bugbountywriteup/transforming-a-domain-into-the-matrix-an-open-redirect-story-4bd87c3a8caa"
authors: ["Ak1T4 (@akita_zen)"]
bugs: ["Open redirect"]
publication_date: "2017-11-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6048
scraped_via: "browseros"
---

# Transforming a Domain into the Matrix (an open redirect story)

Ak1T4
 highlighted

Ak1T4
 highlighted

Ak1T4
 highlighted

Ak1T4
 highlighted

Ak1T4
 highlighted

Transforming a Domain into the Matrix (an open redirect story)
Ak1T4
Follow
3 min read
·
Nov 18, 2017

292

4

Hey, what’s up community? hope you are good, today i share a very strange and non-common behavior that i found a year ago when i start with bounties. We keep private the program so we can call it from now [redacted.com].

So I found this normal endpoint which is:

https://[redacted.com]/login?return_to=[url]

Interesting huh? so i decide to try some Open Redirect payloads:

return_to=http://evil.com -> rejected

return_to=http://[redacted.com].evil.com -> rejected

return_to=//google.com -> rejected

return_to=//redacted.com@evil.com -> rejected

return_to=//google.com/redacted.com -> rejected

… well the list of payloads is quite large.. but with all attemps failed :(

And my feels are:

The truth sometimes hurts :(

But.. during this actions i notice an strange behaviour.. (here is where the Twilight’s Zone Music comes.. )

So the inspiration down from the heaven with this message directly to me:

I try the next weird thing:

Get Ak1T4’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If i put any string on /login?return_to=anythinghere (when the user is logged) the domain becomes on https://redacted.comanythinghere

Press enter or click to view image in full size
(shit happens)

Well well well , whats going on here? So a little trick comes to my mind and i ask myself: what happens if i do the next request?

https://[redacted.com]/login?return_to=pany

When the user is logged, is redirected directly to https://[redacted.company]

So i look if this domain is available.. and for my surprise:

Press enter or click to view image in full size
YES! AVAILABLE!

At this moment i feel like:

This same trick can be used in a lot of scenarios when we handle a whitelisted URL or domains over CORS, OAuth, etc
I hope you enjoy the reading as i do writing this post :)

Nice resources about Open Redirect are:

zseano | UK Security Researcher
Open url redirects are simply urls like https://www.example.com/?go=https://www.google.com/, which when visited will go…

zseano.com

Evolution of Open Redirect Vulnerability.
TL;DR ///host.com is parsed as relative-path URL by server side libraries, but Chrome and Firefox violate RFC and load…

homakov.blogspot.com.ar

And remember: relax and just some things comes to you: it’s inevitable

Press enter or click to view image in full size

HAPPY HACKING!

HackerOne profile - ak1t4
Whiteh4t Hack3r & Zen Monk & bounty hunter - https://twitter.com/knowledge_2014

hackerone.com

ak1t4 z3n (@knowledge_2014) | Twitter
The latest Tweets from ak1t4 z3n (@knowledge_2014). Bug Bounty Hunter - HoF : Google - Mozilla - PayPal - Microsoft …

twitter.com
