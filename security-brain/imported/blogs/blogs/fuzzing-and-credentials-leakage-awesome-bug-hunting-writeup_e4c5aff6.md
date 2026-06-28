---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-04-25_fuzzing-and-credentials-leakageawesome-bug-hunting-writeup.md
original_filename: 2022-04-25_fuzzing-and-credentials-leakageawesome-bug-hunting-writeup.md
title: Fuzzing and credentials leakage..awesome bug hunting writeup
category: blogs
detected_topics:
- sqli
- command-injection
- otp
- information-disclosure
tags:
- imported
- blogs
- sqli
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: e4c5aff6f630982f991f2cb10788d3f774fa028d92b342adc91084d3b9811c50
text_sha256: 87d6d28ace16ca48d0304b4c4c2cce7517f643e556bb0affc3c7a277cbf0d327
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: true
---

# Fuzzing and credentials leakage..awesome bug hunting writeup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-04-25_fuzzing-and-credentials-leakageawesome-bug-hunting-writeup.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: True
- Raw SHA256: `e4c5aff6f630982f991f2cb10788d3f774fa028d92b342adc91084d3b9811c50`
- Text SHA256: `87d6d28ace16ca48d0304b4c4c2cce7517f643e556bb0affc3c7a277cbf0d327`


## Content

---
title: "Fuzzing and credentials leakage..awesome bug hunting writeup"
url: "https://medium.com/@abdalrahman.alshammas/fuzzing-and-credentials-leakage-nice-bug-hunting-writeup-38b2e774b300"
authors: ["Abdalrahman Alshammas"]
bugs: ["Hardcoded credentials", "Information disclosure"]
publication_date: "2022-04-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2685
scraped_via: "browseros"
---

# Fuzzing and credentials leakage..awesome bug hunting writeup

Fuzzing and credentials leakage..awesome bug hunting writeup
Abdalrahman Alshammas
Follow
2 min read
·
Apr 25, 2022

406

5

Here you find a beautiful write-up with useful tips :)

Let’s call the target: redact.com

While i look at in-scope domains,i ‘ve found manage.redact.com to be in scope

However when i try to navigate to ‘ manage.redact.com’ i get redirected to ‘login.redact.com’ which is the normal login page for this website.

But if i use wayback machine:

waybackurls manage.redact.com

i can see that there is a path: manage.redact.com/mange

Navigate to it,,but it also gives redirect to login.redact.com

Never give up,,use wfuzz to look for other sub-paths

wfuzz -w common.txt — hc 404,302 https://manage.redact.com/manage/FUZZ

And i’ve found this beautiful one: https://manage.redact.com/manage/m

Press enter or click to view image in full size

It gives 200 ok,,not a a redirect,and it looks like a manager login page

Get Abdalrahman Alshammas’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried default credentials,sqli,,none worked,,but when i looked for the source page i see!!

Press enter or click to view image in full size

the username and password(apitoken) are leaked in a script tag :)

remote-signup:UKy7mNY/***REDACTED-SUSPECT-TOKEN***and i am logged-in !!

I was able to send api calls to api.redact.com,,so i reported this and that’s it :)

Tips:

1-Even if you get 3xx redirect on some paths,this don’t mean all other paths are the same

1-look for forgotten endpoints using waybackurl machine and gau tool

2-keep fuzzing and fuzzing..

3-look for credentials leakage in log-in pages

Thanks for reading ❤

Follow me to keep in touch
