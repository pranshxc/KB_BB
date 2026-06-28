---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-03-21_google-adwords-31337-stored-xss.md
original_filename: 2018-03-21_google-adwords-31337-stored-xss.md
title: Google adwords 3133.7$ Stored XSS
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
raw_sha256: bae367f51622da8770dfbb04a9a8bb54988463575b851f0240a93b8ceaa26209
text_sha256: e7055c2dc3c9c0560655cd5d05df07a751fd17e701d6a1ac9fffa76eab4be5ea
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# Google adwords 3133.7$ Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-03-21_google-adwords-31337-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `bae367f51622da8770dfbb04a9a8bb54988463575b851f0240a93b8ceaa26209`
- Text SHA256: `e7055c2dc3c9c0560655cd5d05df07a751fd17e701d6a1ac9fffa76eab4be5ea`


## Content

---
title: "Google adwords 3133.7$ Stored XSS"
url: "https://medium.com/@Alra3ees/google-adwords-3133-7-stored-xss-27bb083b8d27"
authors: ["Emad Shanab (@Alra3ees)"]
programs: ["Google"]
bugs: ["Stored XSS"]
bounty: "3,133.7"
publication_date: "2018-03-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5946
scraped_via: "browseros"
---

# Google adwords 3133.7$ Stored XSS

Top highlight

Google adwords 3133.7$ Stored XSS
Emad Shanab
Follow
4 min read
·
Mar 21, 2018

2.3K

20

welcome my brothers and friends.

I would love to thank you for your support and wish success to all.

There was a dream called Google and its HOF without thinking about reward or anything else.

This vulnerability was the easiest vulnerability and more vulnerability has been rewarded so far.

In 17/02/2018 I posted a post on Facebook.

I think it’s the time to get Google HOF

Because I always choose my target and do not go to another without ending it completely.

My work as a lawyer also takes all my time and I only have 6 hours daily to do my hobby.

On 08/03/2018 while browsing my gmail I clicked on even more from Google . You will find it in the up right side.

Even more from Google
Press enter or click to view image in full size
Google products page

After browsing the entire page I chose my target which is Google adwords.

I logged in and started the test and moved from page to another and in fact I

was playing didn't expect to find anything.

I was added many payloads hoping that the magic alert would appear.

I went to this page:-

https://adwords.google.com/aw/conversions

Press enter or click to view image in full size
conversions

I added a new conversation and in the conversation name i put this payload.

“><svg/onload=alert(document.domain)>”@x.y

Press enter or click to view image in full size
conversation name

After added the payload it pupped up many times and I thought it might be a

self XSS so i clicked on prevent this message to continue and complete it.

After completion i have clicked on Save Conversation.

And the payload didn't pupped up any more because i chooses to prevent the XSS alert.

I copied the entire URL and paste it into the browser in a new tab and this time I got shocked.

Get Emad Shanab’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The payload was stored on the page and works on all the latest versions of browsers.

Press enter or click to view image in full size
XSS pupped up in latest version of Firefox for Kali Linux

And worked on Firefox in windows.

Press enter or click to view image in full size
XSS pupped up in latest version of Firefox for windows

I made a cup of coffee and lit a cigarette and wrote the report and I made a

video to explain the vulnerability and report it to Google and waited for the

reply hoping not to be duplicated.

I received a message from Google accepting the vulnerability

and nice catch ( i loved it ).

Press enter or click to view image in full size
nice catch ( i loved it )

A very easy vulnerability and I got A good bounty from Google Vulnerability Reward Program and HOF.

Press enter or click to view image in full size
Rewarded $ 3133.7

Finally my name added to Google HOF.

Press enter or click to view image in full size
Google HOF

Time line:-

08/03/2018 I have found the vulnerability and Email sent to Google

08/03/2018 Got automatically replay confirms they’ve received my message

08/03/2018 I received a message from Google accepting the vulnerability

08/03/2018 I received a message from Google nice catch ( i loved it )

20/03/2018 closed the report and changed the status to Resolved

20/03/2018 Rewarded $ 3133.7 for Stored XSS in google adwords

I would love to thank you all for your patience in reading my write up and for

your continued support.

specially :-

@ak1t4 z3n @Brute and @IfrahIman_

I'm very happy to unlock this achievement and my goal for this year is perfect so far.

sorry for my bad English but just i wanted to share this with you as always i doing.

The POC video hope you will like it:-

Security XSS Knoxss Emad Shanab Cross Site Scripting Google Bug bounty
