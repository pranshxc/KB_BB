---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2017-12-19_p4-to-p2-the-story-of-one-blind-ssrf.md
original_filename: 2017-12-19_p4-to-p2-the-story-of-one-blind-ssrf.md
title: P4 to P2 - The story of one blind SSRF
category: documents
detected_topics:
- ssrf
- xss
- command-injection
tags:
- imported
- documents
- ssrf
- xss
- command-injection
language: en
raw_sha256: 8a75a8736aef9ffeb1f4211cbd8f1336e2cb2a34deb6035556566bc6a1984d7a
text_sha256: fe164dfa6ea75285e0cc1679a82ec2c50b0afd3fcb13f7cdd9e149174e41cdc3
ingested_at: '2026-06-28T07:31:56Z'
sensitivity: unknown
redactions_applied: false
---

# P4 to P2 - The story of one blind SSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2017-12-19_p4-to-p2-the-story-of-one-blind-ssrf.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection
- Ingested At: 2026-06-28T07:31:56Z
- Redactions Applied: False
- Raw SHA256: `8a75a8736aef9ffeb1f4211cbd8f1336e2cb2a34deb6035556566bc6a1984d7a`
- Text SHA256: `fe164dfa6ea75285e0cc1679a82ec2c50b0afd3fcb13f7cdd9e149174e41cdc3`


## Content

---
title: "P4 to P2 - The story of one blind SSRF"
page_title: "P4 to P2 - The story of one blind SSRF · Script Kiddie`s notes"
url: "https://mike-n1.github.io/SSRF_P4toP2"
final_url: "https://mike-n1.github.io/SSRF_P4toP2"
authors: ["Mikhail Klyuchnikov (@__Mn1__)"]
bugs: ["Blind SSRF"]
publication_date: "2017-12-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 6026
---

# P4 to P2 - The story of one blind SSRF

19 Dec 2017

![](/public/CardTrick.jpg)

Hello everyone. This is my second blog post where I want to tell how I managed to get Blind Local SSRF (P2) instead of External SSRF (P4). Unfortunately, I can’t disclose the vulnerable application, so instead of some screenshots I will be using cute kittens or funny gifs.

Initially, I found functional of uploading receipts that were later converted in PDF format. I noticed that the file could be uploaded in the “html” format.

The first thing I tried was uploading “html” file, which included  tag with link to my ordinary sniffer. This was done in order to understand whether a vulnerable script parsed our file.

[ ![](/public/SnifferScreen_s.png) ](/public/SnifferScreen.png)

After that “html” files were uploaded with different javascript payloads (with “script” tag, with different events, etc.). I tried to read local files using js, or execute an alert box, or dynamically changed the source code of web page. Sadly, none of these options didn’t worked.

If you find yourself in similar situation, but you’ll be more lucky and you’ll have an opportunity to execute a javascript code, here are some examples that can help you:

  * <http://www.noob.ninja/2017/11/local-file-read-via-xss-in-dynamically.html>
  * <https://buer.haus/2017/06/29/escalating-xss-in-phantomjs-image-rendering-to-ssrflocal-file-read/>

It is very important to note that at the stage of trying to read a local file it was noted that if the substring `file://` appears in the uploaded html file, it won`t be processed. However, if we send `file :///asd` string (here is a tab character, not a whitespace), our file will be processed in ordinary way.

Next idea that came to my mind was reading local files using iframe, object and so on, but tag <iframe> was completely blocked and html didn’t processed in any ways, and tag  simply didn’t read the local file.

![](/public/Sadly.png)

In contemporary browsers, you can read local files using object, iframe or embed tags. For example:

  * `<object width="400" height="400" data="file://c:/windows/win.ini"></object>`
  * `<iframe src="file:///C:/Windows/win.ini" width="400" height="400">`
  * `<embed src="file://c:/windows/win.ini" width="400" height="400">`

[ ![alt text](/public/ObjectRead_s.png) ](/public/ObjectRead.png)

None of the methods I tried didn’t worked, but it seemed to me that I could achieve more than just a simple External SSRF. Then I remembered about [@BugBountyHQ](https://twitter.com/BugBountyHQ) [tweet](https://twitter.com/BugBountyHQ/status/868242771617792000) and decided to try to include existed local image via img tag. But, what kind of picture on a 100 percent exists on the web server? Remembering about type of the user-agent `Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)` which probably means that it was header of the Internet Explorer. I found the image that exist on the web server by default with this browser - `C:\Program Files\Internet Explorer\images\bing.ico` and tried to include it (don’t forget about using ‘file://’).

Finally, I’ve got a payload: `<img src="file :///C:\Program Files\Internet Explorer\images\bing.ico">`

[ ![alt text](/public/BingImage_s.png) ](/public/BingImage.png)

In the result, we successfully bypassed the filter and changed the priority from P4 to P2.

![](/public/Woow.gif)
