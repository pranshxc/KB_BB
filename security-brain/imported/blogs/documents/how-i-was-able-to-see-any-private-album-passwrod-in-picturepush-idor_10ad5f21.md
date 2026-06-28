---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-05-23_how-i-was-able-to-see-any-private-album-passwrod-in-picturepush-idor.md
original_filename: 2018-05-23_how-i-was-able-to-see-any-private-album-passwrod-in-picturepush-idor.md
title: How I was able to see any private album passwrod in Picturepush — IDOR
category: documents
detected_topics:
- idor
- command-injection
tags:
- imported
- documents
- idor
- command-injection
language: en
raw_sha256: 10ad5f21ce2d7cedddb40f2187be73773965f8fc1691f1bac041162d4913dc9c
text_sha256: 0f6db26a303ecaad76ab981df14d346ecf0b15056b73eeeb3c0af265ae1ba01a
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to see any private album passwrod in Picturepush — IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-05-23_how-i-was-able-to-see-any-private-album-passwrod-in-picturepush-idor.md
- Source Type: markdown
- Detected Topics: idor, command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `10ad5f21ce2d7cedddb40f2187be73773965f8fc1691f1bac041162d4913dc9c`
- Text SHA256: `0f6db26a303ecaad76ab981df14d346ecf0b15056b73eeeb3c0af265ae1ba01a`


## Content

---
title: "How I was able to see any private album passwrod in Picturepush — IDOR"
url: "https://medium.com/@r99tiq/idor-how-i-was-able-to-see-any-private-album-passwrod-in-picturepush-264913f45e10"
authors: ["Murtada Kamil"]
programs: ["PicturePush"]
bugs: ["IDOR"]
publication_date: "2018-05-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5869
scraped_via: "browseros"
---

# How I was able to see any private album passwrod in Picturepush — IDOR

How I was able to see any private album in Picturepush — IDOR
Murtada Kamil
2 min read
·
May 23, 2018

--

--

Hi Guys,

My Name is Murtada Kamil, I am a bug hunter from Iraq

This is my first write up, and I would like to share with you my bug that I found in picturepush through their bug bounty program

During my recent bug bounty hunt, I came across a critical and yet simple vulnerability.this bug made me able to read any victim album password

[Insecure Direct Object References]

Proof of concept (PoC)

1-Create Account & Login

2-Create Album and protect it with Password

click on create album

3-go to our private album that we created
https://iraq12.picturepush.com/album/1058848/p-1337.html
4- click on album options then Access Rights

5-it will redirect to https://13371.picturepush.com/accessedit.php?mode=arights&alid=1058848

Get Murtada Kamil’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

alid:[id of album]

6-Change alid to victime album id

Press enter or click to view image in full size

we have the password now !

Timeline:

30/9/2017 -Report Sent

1/10/2017-Bug Fixed& Hall of fame

23/5/2018-Report disclosure

Thanks for reading!
https://www.facebook.com/murtada.kamil.754
