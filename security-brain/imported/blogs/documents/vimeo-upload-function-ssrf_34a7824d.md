---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-15_vimeo-upload-function-ssrf.md
original_filename: 2019-12-15_vimeo-upload-function-ssrf.md
title: Vimeo upload function SSRF
category: documents
detected_topics:
- access-control
- ssrf
- command-injection
- otp
- api-security
tags:
- imported
- documents
- access-control
- ssrf
- command-injection
- otp
- api-security
language: en
raw_sha256: 34a7824d5ce44118d4abcd1998db613f13739fcd705faf005dc8acac2789f685
text_sha256: 422b75f796209ea3ef03adfc539e5c470601343bb11a8c361d0371958e8d723e
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Vimeo upload function SSRF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-15_vimeo-upload-function-ssrf.md
- Source Type: markdown
- Detected Topics: access-control, ssrf, command-injection, otp, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `34a7824d5ce44118d4abcd1998db613f13739fcd705faf005dc8acac2789f685`
- Text SHA256: `422b75f796209ea3ef03adfc539e5c470601343bb11a8c361d0371958e8d723e`


## Content

---
title: "Vimeo upload function SSRF"
url: "https://medium.com/@dPhoeniixx/vimeo-upload-function-ssrf-7466d8630437"
authors: ["Sayed Abdelhafiz (@dPhoeniixx)"]
bugs: ["SSRF"]
bounty: "5,000"
publication_date: "2019-12-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4889
scraped_via: "browseros"
---

# Vimeo upload function SSRF

Vimeo upload function SSRF
Sayed Abdelhafiz
Follow
4 min read
·
Dec 14, 2019

1.8K

8

1

TL;DR

I have found an SSRF vulnerability by exploiting content partial flow which the Vimeo upload function implements in the uploading process.

The Journey

I was studying the most subject I hate and decided to take a rest, I told myself that I wouldn’t lose anything If I hunted on my lovely target in HackerOne “Vimeo”, I bring my MacBook and I went direct to upload function specifically Google Drive upload feature, I chose to upload from google drive, chose video file, back to BurpSuite to catch the request:

Press enter or click to view image in full size
Upload Request

As you can see, It sends the file URL with google authorization to let the backend server fetch the file from the URL and pass the authorization on the header to access the file from google drive.
let’s setup WireShark in our VPS and make the backend request a video file from our server to see what would happen in the backend, that was the result:

Press enter or click to view image in full size
HTTP Stream Of Download request

I noticed unusual headers, like Range, Content-Range. But its name was enough to tell me what it's work. we can assume that most of the time, the size of video files is big, so Vimeo doesn’t request the full file in one request if the size was big. if the video file is small, It will request the full file, if not It will request the file partially until collecting the full file, the following diagram can describe what happens:

Press enter or click to view image in full size
Normal person uploading

The server sends a request to check the file size, then if the file was small as it can be transferred to the server by a single connection, it will request the full file.
Suddenly, an idea came to me, what if I didn’t send the full file to the server? For example, if my server responded to the backend server telling it that the file length was 500B, the server will request the 500B, now what if I responded to the server with 200Bof data? let’s try it ;)
I have coded a Web Server in Python to test it, The full file length is 554231B, when Vimeo requests the full file, my server will respond by 8228B Only! my server will log Vimeo Range the header for me :)

Press enter or click to view image in full size
My baby script

Cool! the server stored the 8228B, requested the rest of the file, Cool! I have a scenario that can lead to SSRF in this case.
What If my server responded with a redirect response? vimeo will follow the redirect? store the response? request me the rest? If there rest
The following diagram knocked my brain:

Press enter or click to view image in full size
I love drawing diagrams

some web servers restricted me to reproduce the attack, So I decided to code a pure HTTP server to perform this attack, I coded, ran it, and passed my attacker host to the upload function, SURPRISE! my attack works fine! my thoughts were right D:
Notice: in Vimeo you can download your original video file, so you can find the request forgery response easily

Press enter or click to view image in full size
Time to exploit

I have gathered information about the server, it was a google cloud Instance, so lets try to retrieve instance metadata, I changed the redirect target to http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token, reproduced the attack and I was able to get their compute engine API access token! it was a great moment for me because it was the first SSRF with the most critical impact I have ever found.

Press enter or click to view image in full size
Oh
What now?

Sent to Vimeo, resolved, and paid in 2d!

Get Sayed Abdelhafiz’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Thanks for reading ;)

Timeline

Apr 29th: Triaged by HackerOne team.
Apr 29th: Vimeo rewarded me initially.
May 1st: The vulnerability has been fixed.
May 1st: Vimeo rewarded me with the rest of the bounty.
