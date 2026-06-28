---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-16_how-i-could-get-the-instagram-username-of-anyone-on-tinder.md
original_filename: 2019-07-16_how-i-could-get-the-instagram-username-of-anyone-on-tinder.md
title: How I Could Get The Instagram Username of Anyone on Tinder
category: documents
detected_topics:
- sso
- idor
- xss
- command-injection
- automation-abuse
- csrf
tags:
- imported
- documents
- sso
- idor
- xss
- command-injection
- automation-abuse
- csrf
language: en
raw_sha256: 0aea33f6d527248246909d4fb70ed32a1a7e29c0b5318faa6eab51ffa76b4a9f
text_sha256: 7a4b6c3818c5cddb4608d655e3034b0156682672bbdce534b537b6eeb32f2f7e
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# How I Could Get The Instagram Username of Anyone on Tinder

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-16_how-i-could-get-the-instagram-username-of-anyone-on-tinder.md
- Source Type: markdown
- Detected Topics: sso, idor, xss, command-injection, automation-abuse, csrf
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `0aea33f6d527248246909d4fb70ed32a1a7e29c0b5318faa6eab51ffa76b4a9f`
- Text SHA256: `7a4b6c3818c5cddb4608d655e3034b0156682672bbdce534b537b6eeb32f2f7e`


## Content

---
title: "How I Could Get The Instagram Username of Anyone on Tinder"
url: "https://medium.com/bugbountywriteup/wrong-swipe-tinder-29fe1eb0203c"
authors: ["Shahar Albeck"]
programs: ["Tinder"]
bugs: ["Information disclosure"]
publication_date: "2019-07-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5146
scraped_via: "browseros"
---

# How I Could Get The Instagram Username of Anyone on Tinder

How I Could Get The Instagram Username of Anyone on Tinder
Shahar Albeck
Follow
4 min read
·
Jul 16, 2019

76

1

Note: The following article was published on 16/07/2019 on https://FogMarks.com

Press enter or click to view image in full size

T

oday’s case-study does not involve any vulnerability at all.
Yes — you heard me. No XSSes, no open redirects, no CSRFs or IDORs. Nothing. Nada.

We’ll only learn about a wrong implementation that was used by Tinder in order to integrate their users Instagram accounts on their platform.

While joking with (Ok, more like on) a friend about that the only way he’ll get a match on Tinder is if he’ll find a vulnerability for it, I have started to read about recent security vulnerabilities Tinder has suffered.
So AppSecure has found a way to take over Tinder accounts using Facebook’s Account Kit, which is awesome, and Checkmarx has found that some information on Tinder is being transferred over HTTP, again, god-knows-why.
But the vulnerability I have found most funny and interesting was the one discovered by IncludeSecurity about how Tinder users location was disclosed using Triangulation.
A fascinating article about a creative way to disclose users location using a very-accurate location parameter that was returned to any regular request to their server. Basically, Tinder handed over a vulnerability for free.

And I was amazed by the simplicity of that

After reading IncludeSecurity’s article I was amazed by how simple that was. No IDOR was needed, no complex CSRF or an XSS. The information was right there, for free, for everyone to take and abuse.

And that’s when I’ve started to think

I’ve spent a few hours researching Tinder’s website and Android app.
Really, on 2019 and especially after Facebook’s Cambridge Analytica crisis, Tinder did some damn good job securing themselves from the typical, OWASP TOP 10 vulnerabilities.

This is also the place and the time to say that on paid platforms, it is really difficult to conduct a quality security research. A lot of the actions on Tinder requires a premium account, and repeating those actions as a premium user costs even more.
Companies who want their platforms to be researched by the security community should allow full access to their platform, for free.
I know that a lot of security companies can afford funding the research, but it is not fair for small and individual young security researchers. Think about it.

I thought to myself that its over

During those few research hours I have devoted that evening after joking with (OK- on) my friend, I could not find any interesting lead to a vulnerability on Tinder. I was (and I am) so flooded in work, and I couldn’t devote anymore time for researching Tinder.
I had to message my friend that he will have to get himself that auto-swiper from AliExpress in hope for a match.

Press enter or click to view image in full size
credit: https://odditymall.com/tinda-finger-robot

And then IncludeSecurity’s article has popped in my head. I thought to myself: “If Tinder’s logic on that case was not very privacy-oriented, what other sensitive information do they pass ‘out in the wild’, while it should have been kept private?”

3rd party integrations is the name of the game

Tinder, like many other social platforms, has several integrations with some very popular companies and platforms — Spotify, Facebook and even with some universities.

Get Shahar Albeck’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While simply going through all the responses that came back from regular Android API calls of the application, I have noticed that when a user connects his Instagram account with Tinder, his Instagram photos are being showed on his profile page.

After tapping the ‘Share X’s Profile’ button, I’ve noticed that a unique share-identifier has been generated to that profile, which looked like this:
https://go.tinder.com/~<UNIQUE_SHARE_ID>-<USER_FIRST_NAME>

When I have accessed this URL from the web version of Tinder, nothing happend — I was redirected to https://tinder.com

But when I have accessed it from an Android phone’s browser, the Tinder app was launched and a GET request to https://api.gotinder.com/user/share/~<UNIQUE_SHARE_ID> was initiated.
The response to that request contained a lot of details about the user, including his/her Instagram username.

Finale

It is the first time in the history of my case-studies that I don’t have something smart to say or teach. This vulnerability (which has been patched, of course) and the one IncludeSecurity found could have been easily prevented by simply going through the returned data of all the supported API calls, and making sure that non-private information is being handed over.

In the end, I believe that a QA team has gone through the returned data of the API calls, but for the wrong purposes — they probably just made sure that the returned data is exactly what the front-end UI expects.

I think that the most important lesson here is that the QA stage before version releases is not enough, as large and comprehensive it may be.
Having a Red-team is crucial for the safety of the about-to-be-released product and its users.

Cheers!
