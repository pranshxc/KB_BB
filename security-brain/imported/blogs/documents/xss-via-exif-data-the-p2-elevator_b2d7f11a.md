---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-18_xss-via-exif-data-the-p2-elevator.md
original_filename: 2021-04-18_xss-via-exif-data-the-p2-elevator.md
title: XSS via Exif Data - The P2 Elevator
category: documents
detected_topics:
- xss
- command-injection
- file-upload
tags:
- imported
- documents
- xss
- command-injection
- file-upload
language: en
raw_sha256: b2d7f11ab619dacba76b59f9f5868a0c8d47a124acdc0baf3e362d2370952c85
text_sha256: e7a780ff2d35b1b1440738f46c808c441e5a48b66fb35136f3b594b45a255b5a
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# XSS via Exif Data - The P2 Elevator

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-18_xss-via-exif-data-the-p2-elevator.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `b2d7f11ab619dacba76b59f9f5868a0c8d47a124acdc0baf3e362d2370952c85`
- Text SHA256: `e7a780ff2d35b1b1440738f46c808c441e5a48b66fb35136f3b594b45a255b5a`


## Content

---
title: "XSS via Exif Data - The P2 Elevator"
url: "https://shahjerry33.medium.com/xss-via-exif-data-the-p2-elevator-d09e7b7fe9b9"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Stored XSS"]
publication_date: "2021-04-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3732
scraped_via: "browseros"
---

# XSS via Exif Data - The P2 Elevator

XSS via Exif Data - The P2 Elevator
Jerry Shah (Jerry)
Follow
4 min read
·
Apr 18, 2021

861

2

Summary :

Everyone knows what is an “Exif Data”, so I found this exif data vulnerability on my target website where the server was not stripping the exif data from the uploaded images. Reporting exif data vulnerability is considered as P4 and in some cases P3 as per Bugcrowd’s VRT. So I thought of updating the severity of the bug by converting it into Cross Site Scripting (XSS) attack. So using Exiftool I injected XSS payload into an image and uploaded it on the website and got XSS.

Now in normal case exif data has two categories P3 and P4 where in P3 means when data is publicly available (for eg. comment section) and P4 means where few users are invited to work on a specific project. Same way we have different categories for cross site scripting too from which I will be mentioning two, Reflected and Stored. Here the severity of stored is anyhow more than reflected, so in my case the exif data was on P3 and I made it XSS which was a stored one so the severity got updated to P2.

If I would have reported exif data exposure it would gone for P3 but I converted it into XSS to it got accepted in P2. So I would suggest that one should always try to chain the vulnerabilities to find something more severe.

Understanding Exif Tags :

EXIF stands for “Exchangeable Image File Format”. This type of information is formatted according to the TIFF specification and may be found in JPG, TIFF, PNG, JP2, PGF, MIFF, HDP, PSP and XCF images, as well as many TIFF-based RAW images and even some AVI and MOV videos.

The EXIF meta information is organized into different Image File Directories (IFD’s) within an image. Exif IFD is a set of tags for recording Exif-specific attribute information. There are lots of exif tags in an image but I am discussing only one which I have used for an attack, “Comment” tag which is also known as UserComment tag or ImageDescription tag.

Comment tag for Exif users is used to write keywords or comments on the image besides those in ImageDescription and without the character code limitations of the ImageDescription tag which is then processed by Exif/DCF reader that reads the UserComment tag.

Why it happened ?

In my opinion,

There are many image processing libraries which processes the image’s metadata. Now this metadata also includes the meta tags of an image also known as exif data. This image processing libraries which is Exif/DCF reader in this case was not sanitizing the exif tags of an image on uploading which led to XSS. It should have removed exif data or it should have scanned the exif tags and converted the XSS payload into HTML entities in this case.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How I found this vulnerability ?

My target website was having an option to upload photos
Press enter or click to view image in full size
Upload Functionality

2. So at first I uploaded a normal exif image to check for exif data exposure vulnerability

Press enter or click to view image in full size
Uploading Exif Image
Press enter or click to view image in full size
Image Uploaded - Public

3. Then I had an option to download the image, so I downloaded it and checked the exif data

Press enter or click to view image in full size
Downloading The Image
Press enter or click to view image in full size
Exif Data
Press enter or click to view image in full size
Exif Data

4. Then I downloaded another image from google and checked the exifdata

Press enter or click to view image in full size
Normal Image

5. Then I inserted the XSS payload as an exif data into the image using exiftool

Press enter or click to view image in full size
XSS Payload in Exif Data

6. Then I uploaded the image on the website and got the XSS popup

Press enter or click to view image in full size
XSS via Exif Data

Impact :

It can allow an attacker to hijack the user’s session and take over the account. As it is a stored one and the image is public it can be more severe.

Mitigation :

Always strip the exif data (meta-data) from the uploaded images. If you don’t want to strip the exif data then there should be a validation check for metadata where it should check whether the metadata (exifdata) is containing any malicious payload and if yes then it should be removed.

Press enter or click to view image in full size
