---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-03_bypassing-lfi-local-file-inclusion.md
original_filename: 2021-06-03_bypassing-lfi-local-file-inclusion.md
title: Bypassing LFI (Local File Inclusion)
category: documents
detected_topics:
- path-traversal
- command-injection
- otp
tags:
- imported
- documents
- path-traversal
- command-injection
- otp
language: en
raw_sha256: 303ebf4132cc9a656d6ad8dbfd832f9b2ecb66a4d46e1b673ef1df22284dc1bf
text_sha256: aae002f92a477a6b860f22fbc5b7a4103f9ffec94d9d9e85ad10e549f01f29a1
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: true
---

# Bypassing LFI (Local File Inclusion)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-03_bypassing-lfi-local-file-inclusion.md
- Source Type: markdown
- Detected Topics: path-traversal, command-injection, otp
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: True
- Raw SHA256: `303ebf4132cc9a656d6ad8dbfd832f9b2ecb66a4d46e1b673ef1df22284dc1bf`
- Text SHA256: `aae002f92a477a6b860f22fbc5b7a4103f9ffec94d9d9e85ad10e549f01f29a1`


## Content

---
title: "Bypassing LFI (Local File Inclusion)"
url: "https://medium.com/@abhishake21/bypassing-lfi-local-file-inclusion-ebf4274e7027"
authors: ["Abhishek (@abhishake21)"]
bugs: ["LFI"]
publication_date: "2021-06-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3603
scraped_via: "browseros"
---

# Bypassing LFI (Local File Inclusion)

Top highlight

Bypassing LFI (Local File Inclusion)
Abhishek
Follow
3 min read
·
Jun 3, 2021

212

3

Press enter or click to view image in full size

Curated list of Bug bounty programs — https://bugbountydirectory.com

LFI (Local File Inclusion) allows an attacker to expose a file on the target server. With the help of directory traversal(../) we can access files that should not be accessible to a user.

For example,

https://example.com/redirect.php?page=/home/index.html This will return the index.html

https://example.com/redirect.php?page=../../../etc/passwd This will return the passwd file.

Its a serious issue, P1 and could lead to RCE with various methods.

Press enter or click to view image in full size
Bugcrowd VRT

In my case the URL was www.target.com/rd?page=/change/lmtstats.html

So i tried directory traversal in the page parameter. The list of payloads can be found here. Its a huge list but ../../../etc/passwd works most of the time but the amount of time you need to add ../ can be huge, and even even if you add maybe 20 ../ the command i.e etc/passwd maybe blocked. So its a bit of try and error.

Get Abhishek’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In my case i had to add ../ 7 times but the final command had .html at the end like so ../../../../../../../etc/passwd.html

Press enter or click to view image in full size

Tried changing filetype to txt, png etc no luck.

Press enter or click to view image in full size

NullByte - %00

Press enter or click to view image in full size

After trying various techniques and encoding, the final payload was

www.target.com/rd?page=Li4lMkYuLiUyRi4uJTJGLi4lMkYuLiUyRi4uJTJGLi4lMkZl***REDACTED-SUSPECT-TOKEN***That is the below payload encoded in base64.

..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc..%2Fpasswd..%2F00.txt//.%00

Press enter or click to view image in full size

After a lot of trial and error and getting blocked i could finally access the passwd file. Now time to escalate this to RCE. Unfortunately, i could not escalate this to RCE cause i could only read a few files and for RCE we need to access specific files. But you can escalate it to RCE via the below methods if you find LFI.

swisskyrepo/PayloadsAllTheThings
The File Inclusion vulnerability allows an attacker to include a file, usually exploiting a "dynamic file inclusion"…

github.com

File Inclusion/Path traversal
Do you use Hacktricks every day ? Did you find the book very ? Would you like to so we can dedicate more time to it and…

book.hacktricks.xyz

There are a ton of blogs that explain various methods for RCE which are just a google search away.

For those who ask me on twitter from where do i learn all the bug bounty stuff, the below resources should help.

List of bug bounty writeups
Home AMA Challenges Cheatsheets Conference notes The 5 Hacking NewsLetter The Bug Hunter Podcast Tips & Tricks…

pentester.land

Web Security Academy: Free Online Training from PortSwigger
Boost your career Flexible learning Learn from experts The Web Security Academy is a free online training center for…

portswigger.net

HackTricks
Welcome to the page where you will find each hacking trick/technique/whatever I have learnt in CTFs, real life apps…

book.hacktricks.xyz

bugbytes Archives - Intigriti
Bug Bytes is a weekly newsletter curated by members of the bug bounty community. The first series is curated by Mariem…

blog.intigriti.com

HackerOne
Hacktivity

Basically i just read a lot of blogs and try that on my target website 😆

Follow me on twitter — https://twitter.com/abhishekY495

Thanks 😄
