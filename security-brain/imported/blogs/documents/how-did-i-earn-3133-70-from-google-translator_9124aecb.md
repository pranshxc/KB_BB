---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-30_how-did-i-earn-313370-from-google-translator.md
original_filename: 2019-12-30_how-did-i-earn-313370-from-google-translator.md
title: How did I earn $3133.70 from Google Translator?
category: documents
detected_topics:
- xss
- command-injection
- graphql
tags:
- imported
- documents
- xss
- command-injection
- graphql
language: en
raw_sha256: 9124aecb3a126b74ef1e8706dfb32a6f2c03691f934b6d45230a5931c7ac3177
text_sha256: e0218a940fcfdbbc688a3dab075c4e161d944a365b6dbbfef451d4124df87eb0
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How did I earn $3133.70 from Google Translator?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-30_how-did-i-earn-313370-from-google-translator.md
- Source Type: markdown
- Detected Topics: xss, command-injection, graphql
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `9124aecb3a126b74ef1e8706dfb32a6f2c03691f934b6d45230a5931c7ac3177`
- Text SHA256: `e0218a940fcfdbbc688a3dab075c4e161d944a365b6dbbfef451d4124df87eb0`


## Content

---
title: "How did I earn $3133.70 from Google Translator?"
url: "https://medium.com/monetary/how-did-i-earn-3133-70-from-google-translator-9becf942dbdc"
authors: ["Beri Bey (@uppmen)"]
programs: ["Google"]
bugs: ["XSS"]
bounty: "3,133.70"
publication_date: "2019-12-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4855
scraped_via: "browseros"
---

# How did I earn $3133.70 from Google Translator?

How did I earn $3133.70 from Google Translator?
Beri Bey
Follow
4 min read
·
Dec 30, 2019

142

A bug may seem simple but not at all simple when you need to be … Vietnamese.

Press enter or click to view image in full size
How did I earn $3133.70 from Google?

You’ve probably read through the write-up series about a company X’s bug through Prisma GraphQL.

Then today I will continue the series scattered with bug Cross-Site Scripting (XSS) on the domain translate.google.com of Google. (See details about XSS on https://en.wikipedia.org/wiki/Cross-site_scripting)

2am along with the winter weather in Hanoi when everyone was asleep, I was still fascinated with my daily work, after finishing the job, it was also 2:45.
Decided to “entertain” a little before I went to sleep, but I had language problems when searching for movies. While translating the title of the movie from Vietnamese into English on translate.google.com, I accidentally discovered a problem that the “Translator” (in Vietnamese main language) feature of Google Translator was caught (See figure 2).

Press enter or click to view image in full size
figure 2

Now I try F12 in the browser to open the DevTools tool and check, I discovered that the HTML I inserted above is being executed. (See picture 3)

Press enter or click to view image in full size
picture 3

Well, Google does not filter and encode HTML tags in this feature. So I can exploit XSS here already.
I tried changing the main language to another language but it was not possible, because the HTML tags were coded and filtered out. This error appears when you select the primary language as Vietnamese.

Get Beri Bey’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Continue with other HTML snippets to create a bulletin board to display the domain name and session of the user.
(The difficulty of doing this is to keep the length and the characters properly aligned so that the Translator displays “word suggestions”).
And finally, I got a look at the XSS (see Figure 4 when the xss was executed to create a message box):

<iframe onload=”javascript:prompt(document.domain, document.cookie)” id=”xss” role=”xss”>hello xss

Figure 4

PoC (Proof of Concept) Video on Chrome and Firefox latest version: https://youtu.be/Q3AUguoreyU

But will Google accept this vulnerability?

If Google uses the POST method instead of GET to get the suggested results, is it not allowed? Because that code you have to send to the victim to execute it, but whether you send the victim the code, they will also execute it?

Address URL displayed on browser:
https://translate.google.com/?hl=en#view=home&op=translate&sl=vi&tl=en&text=%3Ciframe%20onload=%22javascript:alert(document.domain)%22%20id=%22xss%22%20role=%22xss%22%3Ehello%20xss

Now look at the url address in the browser, then pay attention to the parameters passed.

& sl = en => Primary language
& tl = en => Language after translation
& text => Paragraphs

So I thought it would definitely work, I just need to encode the XSS executable and then pass the TEXT parameter above and send the link to the victim.
After I had enough facts about the bug and I submitted a report to Google.
But then it got a response from Google not to think it was a bug because the domain name was in the “sandbox domains” and they thought it was invalid, so they changed the status to “Won’t Fix (Intended Behavior). “(See picture 5).

Press enter or click to view image in full size
picture 5).

I was quite sad at the moment, but I did not read it again to look for information about the domain name “sandbox” (See Figure 6).

Press enter or click to view image in full size
Figure 6

I would like to briefly talk about “sandbox domains”.
Sandbox domains — Often used to contain all content including viruses, malware, trojans, etc., and it does not affect other servers. It is separate from the main server that contains the user’s data. Hence it is safe.
But strangely, the domain “translate.google.com” is not on the list, and I am sure it is valid. I have sent 2 feedbacks to prove their mistake.
After 7 days of sending me 2 replies I didn’t see them respond, so I kept responding again, and as a result, they reviewed my status change and accepted it as bug and team meeting to assess the level and offer bonuses for this bug.
Lastly, I would like to thank some of you and some members of the “Bounty hunting community”, during the feedback process to prove this mistake and facilitate me. have more motivation to prove.

Timeline:

14/11/2019 14:05 — I send the report
14/11/2019 20:29 — Received a response from Google, but was responded to “Won’t Fix (Intended Behavior)”.
14/11/2019 21:29 — I provided more information
11/15/2019 00:36 — I prove that the domain name is valid.
21/11/2019 23:23 — I continue to prove the domain name is valid and enclose a PoC video.
11/22/2019 00:12 — Google changes that status and confirms that and re-evaluates the bug.
November 28, 2019 01:20 — Google announced a bonus of $ 3133.70
23/12/2019 03:47 — Google feedback has fixed the bug.
