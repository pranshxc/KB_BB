---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-12_svg-based-stored-xss.md
original_filename: 2021-12-12_svg-based-stored-xss.md
title: SVG based Stored XSS
category: documents
detected_topics:
- xss
- ssrf
- command-injection
- otp
tags:
- imported
- documents
- xss
- ssrf
- command-injection
- otp
language: en
raw_sha256: f920f0a9fcb1b6ad523a860b5403c2fad833beed914befcd4450871469d423c8
text_sha256: d1d5be84272544897901670780b67f6732ee5a6aea401a2df64212440bd2b4fc
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# SVG based Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-12_svg-based-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, ssrf, command-injection, otp
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `f920f0a9fcb1b6ad523a860b5403c2fad833beed914befcd4450871469d423c8`
- Text SHA256: `d1d5be84272544897901670780b67f6732ee5a6aea401a2df64212440bd2b4fc`


## Content

---
title: "SVG based Stored XSS"
url: "https://prashantbhatkal2000.medium.com/svg-based-stored-xss-ee6e9b240dee"
authors: ["xaonan44"]
bugs: ["Stored XSS"]
publication_date: "2021-12-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3091
scraped_via: "browseros"
---

# SVG based Stored XSS

SVG based Stored XSS
Prashant Bhatkal
Follow
3 min read
·
Dec 12, 2021

240

1

Hi, hope you guys doing great! Here is a story about me finding a stored XSS using svg files

Goal before approaching the program

To find a one-click exploit (XSS or SSRF)

Approach

Found a target that has many features which included Discussion, Discovery, Mixtapes, Shorts, Activity and what not. I went ahead with looking at user dashboard.

Why would I look for xss at a user dashboard where only I am the visitor?

Nice Question! If I found XSS there then it would be considered self XSS. which has no impact. It would be a challenge to convert self XSS into a valid one.

One parameter that could have been shared outside the dashboard was the profile picture url. So I need to find a way to upload malicious file instead of a jpeg.

After doing some research, I found out that svg is considered as an image and it also allows javascript to execute. click here for svg_xss demo

Get Prashant Bhatkal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If you check the source code of this page you will find that there is a script tag within this svg dom

Press enter or click to view image in full size

Ok so we know now that we have to upload svg file instead of valid jpeg.

Bypassing Filter

Only valid file that could have been uploaded was either jpeg or png file.

How was the file being verified?

They were creating an api POST request with only the image header being sent. If the header is valid then there was another POST request that was uploading the actual file. No validation on this second POST request.
Here we can just send a valid png and in the second request we can replace the png contents with the svg payload.
Press enter or click to view image in full size

After successfully bypassing checks and uploading the image, there was no alert box waiting for me to close it 🙁. Later I found out that they were using ImageMagick to compress the image size.

https://media.redacted.com/img/<image_name>?size=medium Just had to remove the size parameter. which loaded the original svg image.

Press enter or click to view image in full size

How is this impactful?

Instead of calling alert we can write XHR request that sends the cookie data to our server. Because it has very critical ACCESS_TOKEN we could possibly take over someones account. Just send the user the link and wait for them to click.

Making it a successful one click exploit.

Thanks for the read and I hope you learned something new!
