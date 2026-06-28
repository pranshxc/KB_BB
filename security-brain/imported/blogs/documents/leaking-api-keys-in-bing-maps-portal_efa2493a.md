---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2015-12-31_leaking-api-keys-in-bing-maps-portal.md
original_filename: 2015-12-31_leaking-api-keys-in-bing-maps-portal.md
title: Leaking API keys in Bing Maps Portal
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
raw_sha256: efa2493a0d0c742f56a6de4d2b29b43e0408fbb3b9671e842dd2e04eb899b796
text_sha256: a3eec05dc2d6624acc6ca409fcd95d4fd43614b623165cc7e3fd7a0b5e887d13
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Leaking API keys in Bing Maps Portal

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2015-12-31_leaking-api-keys-in-bing-maps-portal.md
- Source Type: markdown
- Detected Topics: idor, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `efa2493a0d0c742f56a6de4d2b29b43e0408fbb3b9671e842dd2e04eb899b796`
- Text SHA256: `a3eec05dc2d6624acc6ca409fcd95d4fd43614b623165cc7e3fd7a0b5e887d13`


## Content

---
title: "Leaking API keys in Bing Maps Portal"
url: "https://medium.com/bugbountywriteup/how-i-got-listed-in-microsoft-hall-of-fame-8f96ca4535c2"
authors: ["Sai Krishna Kothapalli (@kmskrishna)"]
programs: ["Microsoft"]
bugs: ["IDOR"]
publication_date: "2015-12-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6323
scraped_via: "browseros"
---

# Leaking API keys in Bing Maps Portal

Leaking API keys in Bing Maps Portal
Sai Krishna Kothapalli
Follow
4 min read
·
Jan 1, 2016

196

1

Since I promised to write about how I got listed in Microsoft Hall Of Fame. Here it is at last.

Some background info

This is my first time reporting a Security Vulnerability to a Major Company .
Yes, I had a little prior knowledge on Web Security.

Every year Microsoft conducts a Hackathon named code.fun.do in some IIT’s .The theme for the Hackathon was to build a web or mobile application using one of the Microsoft technologies.

We decided to participate and our Idea involved Bing maps. In order to use any API you need an API key.So does Bing maps . You can manage your applications and their keys for Bing maps at https://www.bingmapsportal.com/ . So I also registered

I was making myself familiar with the website and trying to create new API keys and use them.

(Don’t worry I deleted that Application and key :P)

Then there was this page where you could see the usage details of all the API keys

Well there were no statistics because I hadn’t used the key yet but have you noticed something ?

Press enter or click to view image in full size
URL

Look at the URL. While making the get request it is sending the Account ID as a parameter. So what I did next was to change the Account ID to 1418766 (Mine is 1418765) and pressed enter and then BOOM !! I got the API keys of that user.

Just Imagine !! I can get the API keys , Application Names, Usage details and Every damn statistics you can possibly imagine of every User ever registered.

There were even enterprise level API keys.

Get Sai Krishna Kothapalli’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If I hadn’t reported this bug, may be someday you would have seen that some hackers hacked Microsoft and posted API keys and some other details on pastebin or something 😛

Was that complicated ? Nope right. Anyone can change that Account ID . But in this case I was the one 😛 . In case you are wondering why I did that the answer is I am used to it although I never participated in any Bug bounties I practice a lot on our Institute websites and servers and so many other sites online.

My knowledge grew in this area because I practice in a lot of CTF’s (Capture The Flag contests) and once you do so many contests you get that instinct to check everything and you know where to look for finding bugs.

It’s not a special talent though and anyone with some dedication can master this art.

The guys at Microsoft fixed the bug, and the URL now look like this

and the vulnerability has been patched.

And that’s how I got into Microsoft Hall Of Fame for the month of November.

That’s it for now.

Timeline:-

10/11/2015 — Sent bug Report.

11/11/2015 — Got a mail saying that they are analysing the bug.

12/11/2015- They fixed it (I checked).

17/11/2015 — Got an official mail asking for my details.

Finally I got started with Bug Bounties while I was not looking for bugs.

We didn’t win the Hackathon but it’s still a win.

Thank you for reading.

Peace. :D

I reported another Vulnerability in the same website in the same month

Originally published at kmskrishna.wordpress.com on December 31, 2015.
