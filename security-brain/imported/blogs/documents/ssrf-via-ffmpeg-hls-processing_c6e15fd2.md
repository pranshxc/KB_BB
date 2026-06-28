---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-11_ssrf-via-ffmpeg-hls-processing.md
original_filename: 2019-12-11_ssrf-via-ffmpeg-hls-processing.md
title: SSRF via FFmpeg HLS processing
category: documents
detected_topics:
- ssrf
- xss
- command-injection
- cloud-security
tags:
- imported
- documents
- ssrf
- xss
- command-injection
- cloud-security
language: en
raw_sha256: c6e15fd21a58a4d5426e93fff3d72cd818dc81d6496b4243b8088971fb2cfa78
text_sha256: 826154ca3c321e0e70e10dad89f8e7fbd2006ef164c936412a682922f4c61d06
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# SSRF via FFmpeg HLS processing

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-11_ssrf-via-ffmpeg-hls-processing.md
- Source Type: markdown
- Detected Topics: ssrf, xss, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `c6e15fd21a58a4d5426e93fff3d72cd818dc81d6496b4243b8088971fb2cfa78`
- Text SHA256: `826154ca3c321e0e70e10dad89f8e7fbd2006ef164c936412a682922f4c61d06`


## Content

---
title: "SSRF via FFmpeg HLS processing"
url: "https://medium.com/@pflash0x0punk/ssrf-via-ffmpeg-hls-processing-a04e0288a8c5"
authors: ["Pflash Punk (@PflashPunk)"]
bugs: ["SSRF"]
publication_date: "2019-12-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4895
scraped_via: "browseros"
---

# SSRF via FFmpeg HLS processing

SSRF via FFmpeg HLS processing
Pflash Punk
Follow
2 min read
·
Dec 12, 2019

149

2

Press enter or click to view image in full size
FFmpeg Logo

FFmpeg is a free and open-source project consisting of a vast software suite of libraries and programs for handling video, audio, and other multimedia files and streams. At its core is the FFmpeg program itself, designed for command-line-based processing of video and audio files, and widely used for format transcoding, basic editing (trimming and concatenation), video scaling, video post-production effects, and standards compliance. FFmpeg is known to process HLS playlists that may contain references to external files.

Story !

I received a private invitation on bugcrowd , lets call it REDACTED.COM .

Basically Redacted.com is a video transcoding platform , so its 99% sure that they’ll be using FFmpeg :P
So its obvious the first test i’ll perform on the target will be SSRF only using FFmpeg HLS Processing.

Setup !

1.A small server , just to check logs , you can use AWS or DigitalOcean.

2. B-XSSRF to check the requests. Download it from Here . ( Don’t forget to read the instructions given in repo )

3. Malicious AVI file. Download it from Here.

Get Pflash Punk’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4. Open the downloaded AVI file in notepad++ , search for http://127.0.0.1/request.php and replace it with yours.

Testing !

Now we are ready to test SSRF with FFmpeg.

Logged in to Redacted.com
Uploaded the video.
Checked for requests received .
Press enter or click to view image in full size

4. Bingo ! its vulnerable :P

What’s next ?

Reported to the vendor on bugcrowd -> Duplicate -> LOL

Press enter or click to view image in full size

Anyway’s it may help you :)
