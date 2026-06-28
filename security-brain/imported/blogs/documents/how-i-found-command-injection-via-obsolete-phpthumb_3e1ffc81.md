---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-30_how-i-found-command-injection-via-obsolete-phpthumb.md
original_filename: 2021-10-30_how-i-found-command-injection-via-obsolete-phpthumb.md
title: How I found Command Injection via Obsolete PHPThumb
category: documents
detected_topics:
- command-injection
- api-security
- cloud-security
- supply-chain
tags:
- imported
- documents
- command-injection
- api-security
- cloud-security
- supply-chain
language: en
raw_sha256: 3e1ffc81ce7d39ef0c6ae4b8655eeb6e6f168c9a37a692d3b2cb1c258f706252
text_sha256: 3518affbad9551e11caefa436f97ba0633465a3481893f5cb853ce80bf25c54d
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# How I found Command Injection via Obsolete PHPThumb

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-30_how-i-found-command-injection-via-obsolete-phpthumb.md
- Source Type: markdown
- Detected Topics: command-injection, api-security, cloud-security, supply-chain
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `3e1ffc81ce7d39ef0c6ae4b8655eeb6e6f168c9a37a692d3b2cb1c258f706252`
- Text SHA256: `3518affbad9551e11caefa436f97ba0633465a3481893f5cb853ce80bf25c54d`


## Content

---
title: "How I found Command Injection via Obsolete PHPThumb"
url: "https://sushant-kamble.medium.com/how-i-found-command-injection-via-obsolete-phpthumb-p1-vulnerability-e4811248ce12"
authors: ["Sushant Kamble"]
bugs: ["OS command injection", "RCE"]
publication_date: "2021-10-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3202
scraped_via: "browseros"
---

# How I found Command Injection via Obsolete PHPThumb

How I found Command Injection via Obsolete PHPThumb
Sushant Kamble
Follow
4 min read
·
Oct 30, 2021

301

3

Press enter or click to view image in full size

Hello Readers, after a great response to my previous write-up on Account Takeover Chained to Host Header Injection. I would like to thank each and everyone for appreciating for showing their gratitude and also for those who found this helpful in their hunting journey. I would like to share another P1 vulnerability that is “Command Injection via Obsolete PHPThumb”.

As usual, I was hunting on some private programs I was just doing all the recon process and in one of the endpoints I ran Dirbuster and after several checks, I noticed some error in the application which was known to me so I quickly checked on google what exactly was the error and is that vulnerable or not so that I can exploit further.

B
efore starting with the exploitation let us understand what exactly is PHPThumb and its vulnerability?

Press enter or click to view image in full size

phpThumb() uses the GD library to create thumbnails from images (JPEG, PNG, GIF, BMP, etc) on the fly. The output size is configurable (can be larger or smaller than the source), and the source may be the entire image or only a portion of the original image. True color and resampling are used if GD v2.0+ is available, otherwise, paletted-color and nearest-neighbor resizing are used. ImageMagick is used wherever possible for speed. Basic functionality is available even if GD functions are not installed (as long as ImageMagick is installed).

Multiple vendor applications utilize phpThumb(). phpThumb() uses the GD library to create thumbnails from images (JPEG, PNG, GIF, BMP, etc) on the fly. phpThumb() versions 1.7.9 and below are vulnerable to a command injection vulnerability that allows an attacker to execute arbitrary shell commands.

A command injection vulnerability exists in a PHPThumb phpThumb fltr parameter. A remote, authenticated attacker can exploit this vulnerability by sending crafted requests to the phpThumb web page. Successful exploitation will result in arbitrary command execution.

Note:-

Attackers can exploit this issue to execute arbitrary commands in the context of the webserver.

Successful exploitation requires ’ImageMagick’ to be installed.

This vulnerability does not affect the phpThumb that is included in the MODx Revolution distribution.

Steps To Reproduce:

Step 1: After recon process I landed to a endpoint where application was throwing some errors.

Press enter or click to view image in full size
Error Page

Step 2: Then after checking the error on google it was found that the application was vulnerable to Command Injection.

Step 3: After checking several github and exploitdb I finally found the useful payload for this vulnerability.

Get Sushant Kamble’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Payload: “$target/phpThumb.php?src=file.jpg&fltr[]=blur|9 -quality 75 -interlace line fail.jpg jpeg:fail.jpg ; uname -a ; &phpThumbDebug=9”

Step 4: I used those payload and I got the exact response which I was expecting. Command Injection was triggered to the application.

Press enter or click to view image in full size
uname -a

Step 5: Trying to change the Payload and checking the response.

Press enter or click to view image in full size
ls -la
Press enter or click to view image in full size
cat etc/passwd

Remediation:

Upgrade to the latest version of phpThumb.

You can Connect with me :-

Twitter :- https://twitter.com/imsushantkamble
Linkedin :- https://in.linkedin.com/in/iamsushantkamble
Facebook :- https://www.facebook.com/iamsushantkamble/

Kindly Give a Clap if you found this helpful and came across this kinda scenario.
