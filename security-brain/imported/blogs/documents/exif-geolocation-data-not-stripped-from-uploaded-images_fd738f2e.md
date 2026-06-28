---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-09_exif-geolocation-data-not-stripped-from-uploaded-images.md
original_filename: 2019-10-09_exif-geolocation-data-not-stripped-from-uploaded-images.md
title: EXIF Geolocation Data Not Stripped From Uploaded Images
category: documents
detected_topics:
- command-injection
- mfa
- information-disclosure
tags:
- imported
- documents
- command-injection
- mfa
- information-disclosure
language: en
raw_sha256: fd738f2e67dc71421ed689e5e14b7007792400927f6b477b498fc7d2d2cee63f
text_sha256: 2bc502df49e3761064778e5e14212e15a32747b5f3dc57f72129dd7dd24cda84
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# EXIF Geolocation Data Not Stripped From Uploaded Images

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-09_exif-geolocation-data-not-stripped-from-uploaded-images.md
- Source Type: markdown
- Detected Topics: command-injection, mfa, information-disclosure
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `fd738f2e67dc71421ed689e5e14b7007792400927f6b477b498fc7d2d2cee63f`
- Text SHA256: `2bc502df49e3761064778e5e14212e15a32747b5f3dc57f72129dd7dd24cda84`


## Content

---
title: "EXIF Geolocation Data Not Stripped From Uploaded Images"
url: "https://medium.com/@souravnewatia/exif-geolocation-data-not-stripped-from-uploaded-images-794d20d2fa7d"
authors: ["Sourav Newatia (@souravnewatia)"]
bugs: ["Information disclosure"]
bounty: "500"
publication_date: "2019-10-09"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4993
scraped_via: "browseros"
---

# EXIF Geolocation Data Not Stripped From Uploaded Images

Sourav Newatia
 highlighted

EXIF Geolocation Data Not Stripped From Uploaded Images
Sourav Newatia
Follow
2 min read
·
Oct 9, 2019

230

3

Description:

What is EXIF

EXIF is short for Exchangeable Image File, a format that is a standard for storing interchange information in digital photography image files using JPEG compression. Almost all new digital cameras use the EXIF annotation, storing information on the image such as shutter speed, exposure compensation, F number, what metering system was used, if a flash was used, ISO number, date and time the image was taken, white balance, auxiliary lenses that were used and resolution. Some images may even store GPS information so you can easily see where the images were taken!

Because of that there is a possibility of Security Imapct.

In Bugcrowd, This Issue is considered as P3 and P4.

P3 : When the profile picture or file shared is publically available.

P4 : When the profile picture is only saw by You.

Let’s See how we can Exploit this ??????

Get Sourav Newatia’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I am adding a report that i have submitted on one of the Private Program in Bugcrowd.

________________________

VRT : EXIF Geolocation Data Not Stripped From Uploaded Images

URL: www.example.com

Summary:
When a user uploads an image in example.com, the uploaded image’s EXIF Geolocation Data does not gets stripped. As a result, anyone can get sensitive information of example.com users like their Geolocation, their Device information like Device Name, Version, Software & Software version used etc.

Steps:

1) Got to Github ( https://github.com/ianare/exif-samples/tree/master/jpg)
2) There are lot of images having resolutions (i.e 1280 * 720 ) , and also whith different MB’s .
3) Go to Upload option on the website
2) Upload the image
3) see the path of uploaded image ( Either by right click on image then copy image address OR right click, inspect the image, the URL will come in the inspect , edit it as html )
4) open it (http://exif.regex.info/exif.cgi)
5) See wheather is that still showing exif data , if it is then Report it.

Impact
This vulnerability is CRITICAL and impacts all the example.com customer base. This vulnerability violates the privacy of a User and shares sensitive information of the user who uploads an image on example.com or any of the example.com instances.

Awarded : 500$ , Bugcrowd.

Thanks friends, This is my first , Please share your views.
