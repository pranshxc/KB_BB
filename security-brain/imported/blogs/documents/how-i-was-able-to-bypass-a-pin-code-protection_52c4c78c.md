---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-03_how-i-was-able-to-bypass-a-pin-code-protection.md
original_filename: 2022-01-03_how-i-was-able-to-bypass-a-pin-code-protection.md
title: How i was able to bypass a Pin code Protection
category: documents
detected_topics:
- rate-limit
- access-control
- command-injection
- api-security
tags:
- imported
- documents
- rate-limit
- access-control
- command-injection
- api-security
language: en
raw_sha256: 52c4c78ca75def9f128fedde895273ba190588bcb86708089f463b91667aec34
text_sha256: 900d8eef24f068e37aa3a7306096c5999811e317ff1c5ef0cff3e76385ed883b
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How i was able to bypass a Pin code Protection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-03_how-i-was-able-to-bypass-a-pin-code-protection.md
- Source Type: markdown
- Detected Topics: rate-limit, access-control, command-injection, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `52c4c78ca75def9f128fedde895273ba190588bcb86708089f463b91667aec34`
- Text SHA256: `900d8eef24f068e37aa3a7306096c5999811e317ff1c5ef0cff3e76385ed883b`


## Content

---
title: "How i was able to bypass a Pin code Protection"
url: "https://xko2x.medium.com/how-i-was-able-to-bypass-a-pin-code-protection-8352295bb4fb"
authors: ["Kerolos sameh (@xko2xx)"]
bugs: ["Broken authorization"]
publication_date: "2022-01-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3036
scraped_via: "browseros"
---

# How i was able to bypass a Pin code Protection

How i was able to bypass a Pin code Protection
Kerolos sameh (xko2x)
Follow
3 min read
·
Jan 3, 2022

90

2

Hello guys,
I Hope all are doing good. my name is kerolos sameh(AKA xko2x), I’m 17 years old bug hunter in HackerOne.

I found an interesting bug in private program I would like to share with y’all and I hope you find this write-up is helpful

so let’s get started!

Info about the target

it’s a financial company that provides virtual and physical cards

full story

so I after some recon and understanding the target well I found a function for creating the virtual and the physical card and I found that’s when you create a virtual card you can read card details without any other steps

overwise the physical card is different you need the pin code behind the card and you can’t do this without getting the card delivered and it costs 5$ too :)

so let’s take a look in pin code request

and response looked like this

so basically there is a rate limit so it’s not brute-forceable

i tried to bypass the rate limit but no luck :(

so I totally forget about it and when I was analyzing javascript

Get Kerolos sameh (xko2x)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

if found endpoint that activates the card with the card UUID only!

original one:

as you can see the difference is the truncated_pan(pin code)
so I tried this endpoint and I was shocked!

request

response:

Press enter or click to view image in full size

and it worked successfully!

so I was still wondering what this request is for ???

and after some investigation, I found this for activating the virtual card if the user disabled it manually!

Recap

so basically bypass the PIN code protection by using the virtual card activate request in the physical card by replacing the card uuid!

Tips for Pentester

always read js files and analyze it.
and literally, click on every button/ function you can find and read the requests and think what you can do with this, this is how you can build a hacker mindset :)

and that’s it I hope you liked my first write-up and I hope you learned something new :)

see you in the next write-up , bye
