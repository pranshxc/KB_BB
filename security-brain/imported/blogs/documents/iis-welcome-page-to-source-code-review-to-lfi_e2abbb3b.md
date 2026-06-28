---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-01_iis-welcome-page-to-source-code-review-to-lfi.md
original_filename: 2024-09-01_iis-welcome-page-to-source-code-review-to-lfi.md
title: IIS welcome page to source code review to LFI!
category: documents
detected_topics:
- path-traversal
- ssrf
- command-injection
tags:
- imported
- documents
- path-traversal
- ssrf
- command-injection
language: en
raw_sha256: e2abbb3b4f86fa683f40e6c6e6fa6b65dc0198e1523f3b289ac2833c8f3f878b
text_sha256: 491980f4524a350f16bea89c57d45bbad2038f5aba259e1e467a9ce48b6d044a
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# IIS welcome page to source code review to LFI!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-01_iis-welcome-page-to-source-code-review-to-lfi.md
- Source Type: markdown
- Detected Topics: path-traversal, ssrf, command-injection
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `e2abbb3b4f86fa683f40e6c6e6fa6b65dc0198e1523f3b289ac2833c8f3f878b`
- Text SHA256: `491980f4524a350f16bea89c57d45bbad2038f5aba259e1e467a9ce48b6d044a`


## Content

---
title: "IIS welcome page to source code review to LFI!"
url: "https://medium.com/@omarahmed_13016/iis-welcome-page-to-source-code-review-to-lfi-23ec581049f5"
authors: ["Omar Ahmed (@spaceboy2O)"]
bugs: ["LFI", "Blind SSRF", "Security code review"]
publication_date: "2024-09-01"
added_date: "2024-09-04"
source: "pentester.land/writeups.json"
original_index: 25
scraped_via: "browseros"
---

# IIS welcome page to source code review to LFI!

IIS welcome page to source code review to LFI!
Omar Ahmed
Follow
3 min read
·
Aug 31, 2024

567

3

Hi, in this writeup I’ll walk you through how I managed to get a limited Local file disclousre (LFI) / Blind SSRF.

TL;DR:

found an IIS welcome page, enumerated directories& files using IIS Short name scanner and FFUF, found an open source webchat software, source code review led to LFI and blind SSRF.

So, I had this subdomain that returned the IIS welcome page ->

Press enter or click to view image in full size

then I used https://github.com/irsdl/IIS-ShortName-Scanner before fuzzing and It showed that this target was vulnerable to IIS Short File Name Disclosure.

Press enter or click to view image in full size

after finding those, use ffuf to try to find those files, I found that one of the folders is EVOLUTION! then I ran the tool again & so on and so forth till I reached finally to this path

Press enter or click to view image in full size

but before going forward I thought about maybe this web chat is open source, is it? turns out it is!

Press enter or click to view image in full size
Press enter or click to view image in full size

My first impression was if it’s created 10 years ago, they didn’t know what security means back then, right? ¯\_(ツ)_/¯

Get Omar Ahmed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

digging through the source code I found the following snippet:

https://github.com/eStream/eStreamChat/blob/2417a12c0999609e3feedbf5281d07393b126c23/eStreamChat/Thumbnail.ashx.cs

Press enter or click to view image in full size

Looking at the source which is in this case the img parameter which took a parameter “img” and based on its value it interpreted it in 2 different ways, if it found UserFiles in the value of that parameter, it would try to query it from the server directly (LFI) which can be trivially bypassed using path traversal, UserFiles/../wheredoyouwannago

and in the second case it would do a request on the server’s behalf to the url you specify :). However, through analysis we can find that the response isn’t directly returned but in fact it goes into ResizeImage function which sadly wouldn’t accept the type of data we are trying to return unlessi it’s an image.

Press enter or click to view image in full size

so we could exfilterate images on the server or perform Blind SSRF by simply hitting that endpoint

Press enter or click to view image in full size

when trying the LFI on our server, it turns out it didn’t need to specify the UserData path:

Press enter or click to view image in full size
Press enter or click to view image in full size

I hope this writeup added some fresh ways of thinking & valuable information to you!

till we meet again :)
