---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-06-03_simple-pathtraversal-bypass.md
original_filename: 2019-06-03_simple-pathtraversal-bypass.md
title: Simple PathTraversal bypass
category: documents
detected_topics:
- xss
- sqli
- command-injection
- path-traversal
- api-security
- mobile-security
tags:
- imported
- documents
- xss
- sqli
- command-injection
- path-traversal
- api-security
- mobile-security
language: en
raw_sha256: f57ddae09825cc197140a86736d97edc968ec816729cf543687121ca9546dee9
text_sha256: 9e0f56147c5e75b54e3bbfe275caedd633da7ab954bddfc6e42cac305e19dac1
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Simple PathTraversal bypass

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-06-03_simple-pathtraversal-bypass.md
- Source Type: markdown
- Detected Topics: xss, sqli, command-injection, path-traversal, api-security, mobile-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `f57ddae09825cc197140a86736d97edc968ec816729cf543687121ca9546dee9`
- Text SHA256: `9e0f56147c5e75b54e3bbfe275caedd633da7ab954bddfc6e42cac305e19dac1`


## Content

---
title: "Simple PathTraversal bypass"
url: "https://medium.com/@frostnull/hi-guys-again-here-bringing-an-experience-to-share-with-you-as-usual-i-will-overshadow-some-f85a1d5a8d8c"
authors: ["fr0stNuLL"]
bugs: ["Path traversal"]
publication_date: "2019-06-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5233
scraped_via: "browseros"
---

# Simple PathTraversal bypass

Simple PathTraversal bypass
fr0stNuLL
Follow
3 min read
·
Jun 3, 2019

95

1

.

Hi guys again here bringing an experience to share with you, as usual I will overshadow some information let’s go ..

Get fr0stNuLL’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Passing through the application, I came across a feature which, it was possible to download a document, the functionality trigger the following request:

Press enter or click to view image in full size

As you can see, in the body of the request, precisely in the info parameter, there was a lot of numbers, I tried some SQLi payloads, XSS but without success, after I tried the payload foo/../304368[rest of numbers], and the application still returned me the file, I found it interesting.. so I tried to search for /etc/passwd, using the techniques of path traversal, after trying a bit and reading this article , and test some payloads using fuzzing techniques, i finally got one that worked ../../../etc/passwd%00, the %00 is a known bypass for several scenarios not only path traversal more info here. The following images illustrates the payload and response:

Press enter or click to view image in full size
Press enter or click to view image in full size

After getting all the users with payload quoted, I made a list with the absolute path of each user retrieved, and made another wordlist containing common linux files like .bashrc, .vimrc and others. By doing this it was possible to recover one user’s .bash_history file, as demonstrated below:

Press enter or click to view image in full size
Press enter or click to view image in full size

After reading the contents of the .bash_history(if you don’t know what is .bash_history here) file of the user in question, I could see that there was a file with a .zip extension, so I went to recover this file, using the same 00% payload technique as shown Next:

Press enter or click to view image in full size

After getting this file, i unzip and got a lot of java files like bellow:

Press enter or click to view image in full size

Finally, I used a tool to decompile JD-GUI the .jar files, retrieved them, and got some information. As shown below

Press enter or click to view image in full size

So that’s it folks. This was simple I hope to have contributed a bit with you xD.

Sharing is Caring

best regards, fr0stNuLL
