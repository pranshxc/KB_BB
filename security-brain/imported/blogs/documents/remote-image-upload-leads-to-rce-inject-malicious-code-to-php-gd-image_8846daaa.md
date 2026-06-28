---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-21_remote-image-upload-leads-to-rce-inject-malicious-code-to-php-gd-image.md
original_filename: 2020-03-21_remote-image-upload-leads-to-rce-inject-malicious-code-to-php-gd-image.md
title: Remote Image Upload Leads to RCE (Inject Malicious Code to PHP-GD Image)
category: documents
detected_topics:
- file-upload
- ssrf
- xss
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- file-upload
- ssrf
- xss
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 8846daaa772cc9cf56e17508c63afbf3147690e231af2cf88eb94810e9989a21
text_sha256: 62b4aff226e52ad27df55f31688558d41344b22bdcb733f185d05623f96d01b5
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: true
---

# Remote Image Upload Leads to RCE (Inject Malicious Code to PHP-GD Image)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-21_remote-image-upload-leads-to-rce-inject-malicious-code-to-php-gd-image.md
- Source Type: markdown
- Detected Topics: file-upload, ssrf, xss, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: True
- Raw SHA256: `8846daaa772cc9cf56e17508c63afbf3147690e231af2cf88eb94810e9989a21`
- Text SHA256: `62b4aff226e52ad27df55f31688558d41344b22bdcb733f185d05623f96d01b5`


## Content

---
title: "Remote Image Upload Leads to RCE (Inject Malicious Code to PHP-GD Image)"
url: "https://asdqw3.medium.com/remote-image-upload-leads-to-rce-inject-malicious-code-to-php-gd-image-90e1e8b2aada"
authors: ["asdqw3"]
bugs: ["Unrestricted file upload", "RCE"]
publication_date: "2020-03-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4697
scraped_via: "browseros"
---

# Remote Image Upload Leads to RCE (Inject Malicious Code to PHP-GD Image)

Remote Image Upload Leads to RCE (Inject Malicious Code to PHP-GD Image)
asdqw3
Follow
5 min read
·
Mar 21, 2020

316

2

Inject Malicious Code to PHP-GD Image

بسم الله الرحمن الرحيم

I recently came across a web application with two methods for adding images to its media library: local file upload and remote file upload from a stock photo website. My first thought was to check for an SSRF vulnerability through the remote file upload feature, but I decided to start by testing the local file upload.

After several tests, I found that the app only allowed image files (.jpg, .png, .gif, and .svg). The .svg format could potentially lead to XSS, but that wasn’t my focus this time.

Moving on to the remote file upload feature, I intercepted a request while adding an image. The request included three POST form-data fields: name, url, and photoId.

I tried changing the url to my server, but got an Internal Server Error response with no incoming connection. Removing the photoId data resulted in the same error, but this time I got an incoming connection on my server. This was likely due to the lack of a valid image file at the provided url.

Next, I provided a url with a valid jpg image file, which successfully uploaded to the media library. Interestingly, when I modified the “name” form-data to image.html and image.php, both uploads were successful.

I quickly realized that injecting PHP scripts into image exif metadata wouldn’t work because the app recreated the fetched image file using the PHP-GD library, which removes exif metadata.

However, I found several articles suggesting that it’s still possible to inject PHP scripts into images that won’t be removed after processing.

https://github.com/fakhrizulkifli/Defeating-PHP-GD-imagecreatefromjpeg

fakhrizulkifli/Defeating-PHP-GD-imagecreatefromgif
Developer uses GD (or Imagemagick) library in order to prevent image header script execution by recreating the image…

github.com

BookFresh Tricky File Upload Bypass to RCE
Hello all today i'm going to write about an interesting vulnerability i've found in Square's Acquisition website…

secgeek.net

These methods are limited to a few characters, though.

Also there is payload injector created by dlegs.

dlegs/php-jpeg-injector
Injects php payloads into jpeg images. Related to this post. You have a web application that runs a jpeg image through…

github.com

First attempt, I use dlegs tool to inject payload to .jpg image. You need to recreate a .jpg image with php-gd first then inject the payload with gd-jpeg.py

$ php gd.php image.jpg image-gd.jpg

Then inject the payload to image-gd.jpg

$ python gd-jpeg.py image-gd.jpg ‘<?php phpinfo()?>’ image-gd-poc.jpg

To make sure the injected payload working, try re-create the image-gd-poc.jpg with php-gd.

$ php gd.php image-gd-poc.jpg image-gd-poc-1.jpg

Then compare binary image-gd-poc.jpg and image-gd-poc-1.jpg

Get asdqw3’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I use vbindiff to compare both image.

$ vbindiff image-gd-poc.jpg image-gd-poc-1.jpg

Press enter or click to view image in full size

The injector writed by dlegs will inject your provided payload into a .jpg image file. This is only working if your target app recreate the image with default quality (default -1). Unfortunately, this method failed because the target app converted images with a quality setting of 90, removing the injected payload.

My next attempt used a .gif image payload by @ABOUL3LA. This time, I successfully uploaded the POC.gif file and renamed the form-data “name” to test.php, resulting in code execution. On his article he provided POC.gif image that already injected with <?phpinfo()?>.

Finally, this is what I got after upload POC.gif and renaming the form-data “name” to test.php

Press enter or click to view image in full size

If you want to use POC.gif payload by @ABOUL3LA the target app must haveshort_open_tag=Onset in php.ini, otherwise the php script won’t executed and you have to modify the payload with <?php ?> tag to make it work.

I reported this vulnerability to the bug bounty program, and they triaged it within minutes, patching it in just a few hours.

I explore bit more into the php-gd lib, just want to know how many bytes we can inject to image. After several testing on different .jpg and .gif image, I can conclude that .jpg image can be injected with payload up to 13 bytes, but .gif image could be injected with more bytes.

GIF image that could be injected is GIF image that has null byte blocks. I found out that GIF images with Netscape Looping Application Extension have this null byte blocks.

Netscape Looping Application Extension is the most popular Application Extension Block that tells browser or other GIF viewer to loop the entire animated GIF file. http://www.vurdalakov.net/misc/gif/netscape-looping-application-extension

This is example GIF image that has Netscape Looping Application Extension https://media2.giphy.com/media/6NjZoOdEbXs1W/source.gif

If we recreate the GIF image with php-gd, the null byte blocks not removed. Look at binary comparison between original gif and gd gif below.

Press enter or click to view image in full size

So let’s try inject php shellcode to this null byte blocks and recreate the GIF image with PHP-GD, this is the binary comparison:

Press enter or click to view image in full size

The injected payload remain there. Then you can upload the gif image to your vulnerable target app.

Press enter or click to view image in full size

You can get the GIF Injector and other scripts here: https://gist.github.com/asdqwe3124/***REDACTED-SUSPECT-TOKEN***MRM
The latest Tweets from MRM (@agamimaulana). asdqwe. Indonesia

twitter.com
