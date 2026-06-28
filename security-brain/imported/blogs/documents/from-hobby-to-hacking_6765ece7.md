---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-31_from-hobby-to-hacking_2.md
original_filename: 2021-07-31_from-hobby-to-hacking_2.md
title: From Hobby to Hacking
category: documents
detected_topics:
- command-injection
- file-upload
- csrf
- api-security
tags:
- imported
- documents
- command-injection
- file-upload
- csrf
- api-security
language: en
raw_sha256: 6765ece7329a8dd0908ff35dced197b435ec183376381e8f20f3183f9d75624d
text_sha256: 419deebc921848c174d04bc72c5b2c0f6b84d92bdf7efea79ef8770e5a1e500d
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# From Hobby to Hacking

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-31_from-hobby-to-hacking_2.md
- Source Type: markdown
- Detected Topics: command-injection, file-upload, csrf, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6765ece7329a8dd0908ff35dced197b435ec183376381e8f20f3183f9d75624d`
- Text SHA256: `419deebc921848c174d04bc72c5b2c0f6b84d92bdf7efea79ef8770e5a1e500d`


## Content

---
title: "From Hobby to Hacking"
url: "https://medium.com/@mumeido/from-hobby-to-hacking-5d8befb3adde"
authors: ["Muhammad Syahrul Haniawan (@b0x_in)"]
bugs: ["Unrestricted file upload", "RCE", "Missing authentication"]
publication_date: "2021-07-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3458
scraped_via: "browseros"
---

# From Hobby to Hacking

From Hobby to Hacking
Muhammad Syahrul Haniawan
Follow
3 min read
·
Jul 30, 2021

68

Hello,my name is Muhammad Syahrul Haniawan. I am from Indonesia and this is my first write up on Medium.com. I’ll tell you a little about the experience I had and my first bug bounty.

Have you ever thought that having a paid hobby is very fun? xD. I have interest about Japanese Culture especially Anime and Manga. At that time I was just reading news about some Japanese culture on one of the biggest Japanese news websites in Indonesia,because this is a private bug bounty program, we call the website as redacted.com.

Ok lets go….

That day I was very surprised to hear the news that my idol actress Yui Aragaki announced her marriage to a Japanese actor. I immediately looked for articles about it and found a website that I used to frequent to read news about Japan.

At first I had no intention of trying to test the security of the website,but i found something that caught my attention, yes … the plugins that is used uses an older version of jquery 3.4.1, which was released in 2019.

Jquery version

I did fuzzing the directory on the main domain and didn’t get a good entry point. after that I found subdomain.redacted.com. I just doing recon directory with view-page source on the main page xD. Found something suspicious directory called jquery-fileupload there hehe…

Press enter or click to view image in full size

I remember reading an article related to jquery-fileupload on this site https://blog.detectify.com/2018/12/13/jquery-file-upload-a-tale-of-three-vulnerabilities/ .

Lets try that !

Get Muhammad Syahrul Haniawan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I go to https://subdomain.redacted.com/jquery-fileupload/server/php and found the entry point and it’s shown “files[]”. HMMMMMM…… I have made simple CSRF to try this entry point for uploading webshell.

Press enter or click to view image in full size
Entry point
Press enter or click to view image in full size
result CSRF

WOW we can see the response here, there it does show an error message but I think my webshell uploaded successfully. “How we know the directory of files ?” That’s simple,just add one more directory “/files/”. And boom….. it really happened xD.

I immediately reported this to the website developer, They respond it quickly. I was awarded for internship at the company for 1 month and got a certificate appreciation.

That’s all my write up about my hobby and hacking xixixi…See you next time guys and hope you enjoy it.

CONTACT :

Linkedin : https://www.linkedin.com/in/msyahrulh/

TIMELINE :

Found the bug : 10 July 2021
Report : 11 July 2021
Rewarded : 12 July 2021.
