---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-10-22_xss-with-html-and-how-to-convert-the-html-into-charcode.md
original_filename: 2018-10-22_xss-with-html-and-how-to-convert-the-html-into-charcode.md
title: XSS with HTML and how to convert the HTML into charcode()
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
raw_sha256: 6a80c57371e9e9db5cbb4c330891575efcff30dea53d04b5596201d2b66b7eee
text_sha256: cbc07ce88bf020c69723f6553f6afa768b045ba811b69ab5b30810f99e5c9fd4
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# XSS with HTML and how to convert the HTML into charcode()

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-10-22_xss-with-html-and-how-to-convert-the-html-into-charcode.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `6a80c57371e9e9db5cbb4c330891575efcff30dea53d04b5596201d2b66b7eee`
- Text SHA256: `cbc07ce88bf020c69723f6553f6afa768b045ba811b69ab5b30810f99e5c9fd4`


## Content

---
title: "XSS with HTML and how to convert the HTML into charcode()"
page_title: "XSS WITH HTML AND HOW TO CONVERT THE HTML INTO CHARCODE() | by Arif-ITSEC111 | Medium"
url: "https://medium.com/@ariffadhlullah2310/xss-deface-with-html-and-how-to-convert-the-html-into-charcode-f0c62dd5ef3f"
authors: ["Arif-ITSEC111"]
programs: ["Purinar Logistics"]
bugs: ["XSS"]
publication_date: "2018-10-22"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5632
scraped_via: "browseros"
---

# XSS with HTML and how to convert the HTML into charcode()

XSS WITH HTML AND HOW TO CONVERT THE HTML INTO CHARCODE()
Arif-ITSEC111
Follow
3 min read
·
Oct 22, 2018

4

Hello, Back Again With Me

This time i want to try to do some inject XSS with HTML full page script. It can be called with “injecting xss then it will shows your HTML Page”

As usual, i do some check with this command input :

<script>alert(‘test’)</script>

If vuln, i try something different

My Target :

https://www.******.com/

2nd Open this Page :

Uncle Jim's Javascript Utilities: CharCode Translator
javascript examples with source code

jdstiles.com

Third, i try to convert my deface HTML web lol

do COPY all of my HTML script.

Then open uncle jim’s page

Get Arif-ITSEC111’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Paste into that part (zoom if you can’t see) :

Press enter or click to view image in full size
sebelah kiri charcodeat()

Then click the charcodeat() button

Press enter or click to view image in full size
sebelah kanan charcodeat()

After got the char result, i do Copy the charcode on my notepad

Then i do add some script :

<script>document.documentElement.innerHTML=(String.fromCharCode(*paste here your charcode*));<script>

It will looks this

<script> document.documentElement.innerHTML=(String.fromCharCode(60, 104, 116, 109, 108, 62, 32, 10, 60, 104, 101, 97, 100, 62, 32, 10, 60, 115, 99, 114, 105, 112, 116, 62, 32, 118, 97, 114, 32, 109, 101, 115, 115, 97, 103, 101, 61, 34, 84, 73, 77, 73, 84, 83, 69, 67, 45, 78, 88, 71, 71, 34, 59, 10, 47, 47, dst));</script>

Then back to your target page, paste into search column then do ENTER

TADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA …..

Press enter or click to view image in full size
injecting XSS full page

That;s it

Thank you

timeline
20/10/2018 (Submit Report)
21/10/2018 (Mitigation Bug)
22/10/2018 (Bug Closed)
