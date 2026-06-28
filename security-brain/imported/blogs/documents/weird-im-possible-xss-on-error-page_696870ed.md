---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-11-21_weird-impossible-xss-on-error-page.md
original_filename: 2020-11-21_weird-impossible-xss-on-error-page.md
title: Weird (im)possible XSS on error page
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
raw_sha256: 696870ed577a099be8110e5379b64578caf6c808659b5873a670d02fb3d38aa2
text_sha256: 9b462262d31cb84572f888c84a57ced1c04fa383186bfa6f8d467d31a08b5eac
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Weird (im)possible XSS on error page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-11-21_weird-impossible-xss-on-error-page.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `696870ed577a099be8110e5379b64578caf6c808659b5873a670d02fb3d38aa2`
- Text SHA256: `9b462262d31cb84572f888c84a57ced1c04fa383186bfa6f8d467d31a08b5eac`


## Content

---
title: "Weird (im)possible XSS on error page"
url: "https://komradz86.medium.com/weird-im-possible-xss-on-error-page-a0b943ead41"
authors: ["Rody Shahnazarian (@Komradz86)"]
bugs: ["Reflected XSS"]
publication_date: "2020-11-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4113
scraped_via: "browseros"
---

# Weird (im)possible XSS on error page

Weird (im)possible XSS on error page
Rody Shahnazarian (Komradz86)
Follow
3 min read
·
Nov 21, 2020

32

Hello all,

This is my first write up.

I am not usually a person who does write ups, but wanted to start sharing some with everyone.

I was working on a private program, which I am not allowed to mention the name lets say test.com.

The error page was disabled on this website and it was kind of integrated in the website itself with a background and all even when trying to add something malicious it redirects you to another page. In test.com/test I was able to get an error ( Reflection Exception) which surprised me. I started searching for more information regarding this error found that some Researchers were able to inject html into it. How I found this error ? by adding extensions to the directories. Ex: test.com/test is the original page, I tested test.com/test.php or test.aspx and I got an error page. So I saw that I can manipulate the error pages error message to my own error message.

Doing that old trick , I have reported the bug but I got a reply from the program Security engineer that they are aware of this issue and it is not eligible for a bounty so they are going to close it as RTFS.

So I left the error page to check for something else, since I thought that this was an easy bounty and I was wrong. After a while , while testing I stumbled into the same error page. I tested for html injection which I forgot, I was able to inject html with the error message making the message BOLD or Underlined ,etc..

I did not want to report it, since I knew they are going to tell me “ We don't see any impact”.

Get Rody Shahnazarian (Komradz86)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I started testing for XSS, I did everything in the book that can be done, tested a lot of payloads. It was very weird that the page was only responding to only specific tags and others are being ignored. I retested html and same thing happened.. when the tags are not accepted I am being redirected to the home page.

Press enter or click to view image in full size

I started with XSS payloads with <img src= tags instead of every other tag and it reflected on the page with a small icon that shows that the photo is being imported but no photo was there, I figured that I was able to get an XSS here. Every payload I tried redirected me to home page. so I felt that I was back to the beginning and that made me crazy.

Press enter or click to view image in full size

After doing a lot of tests, I found out that when I am adding the whole payload Ex: <script>alert(1)</script> it is redirecting me to the home page or an error page which was used by the web admin to detect malicious codes in the website, but what the admin did not know, is that he had some kind of a misconfiguration that I was able to inject any malicious payload without closing the tag Ex: <script>alert(1) the tag is being closed. and Yes, I even tried to start the payload with “><script>.. tried alert , onerror, and all..

Press enter or click to view image in full size

Finally , I removed test.aspx as mentioned and added the payload as a directory and ended the payload with .aspx

so the final payload as seen in the photo: %3Cimg%20src=%22'%22id=’%3Cimg%20src=%22%22%3E’onerror=alert(1).aspx

Got some bounty and learned something new!

Thanks

twitter: komradz86
