---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-18_rce-via-webdav-power-of-put.md
original_filename: 2021-07-18_rce-via-webdav-power-of-put.md
title: RCE via WebDav - Power Of PUT
category: documents
detected_topics:
- command-injection
- access-control
- xss
- api-security
tags:
- imported
- documents
- command-injection
- access-control
- xss
- api-security
language: en
raw_sha256: b0003fe37baefacaa679e1e80e24e10362bd6bf0e56d3f9aeb0c0f7ea30ef755
text_sha256: 75070ef1e86cb68e80436bd69727ad96c8ca0c014726c647a072fa83323f6d79
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# RCE via WebDav - Power Of PUT

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-18_rce-via-webdav-power-of-put.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, xss, api-security
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `b0003fe37baefacaa679e1e80e24e10362bd6bf0e56d3f9aeb0c0f7ea30ef755`
- Text SHA256: `75070ef1e86cb68e80436bd69727ad96c8ca0c014726c647a072fa83323f6d79`


## Content

---
title: "RCE via WebDav - Power Of PUT"
url: "https://shahjerry33.medium.com/rce-via-webdav-power-of-put-7e1c06c71e60"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Default credentials", "RCE"]
publication_date: "2021-07-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3499
scraped_via: "browseros"
---

# RCE via WebDav - Power Of PUT

RCE via WebDav - Power Of PUT
Jerry Shah (Jerry)
Follow
6 min read
·
Jul 18, 2021

642

5

Press enter or click to view image in full size

Hello everyone, at first I want to thank you all for 1K family and I hope you guys are getting some knowledge from my blogs. I decided to write something interesting on 1K followers and luckily I found this material for the blog on vulnerability which I discovered in 2018.

Summary :

Remote code execution has many different types and the easiest way to achieve it is when a “WebDav” is enabled allowing PUT method.

What is WebDav ?

WebDav stands for Web Distributed Authoring and Versioning which is an extension of the Hypertext Transfer Protocol that allows clients to perform remote Web content authoring operations. It provides the ability to create a file or folder, edit a file in place, copy or move or delete a file on a remote web server. It uses port 80 for unencrypted access and port 443 for secure access. It enables users access to cloud files or files on a separate server in real time, without any problem of downloading, caching, editing and uploading.

If WebDav is enable and all rights are given publicly then any user on the internet can upload, delete and modify the files on the remote server which can lead to remote code execution.

What is Authorization request header ?

The HTTP Authorization request header contains the credentials to authenticate a user agent with a server. When you send a request to server to access a resource for which you don’t have a permission, the server respond back the 401 Unauthorized error. It happens because no credentials were provided while trying to access the restricted resource.

In WebDav, for security purpose developers uses authentication mechanism for accessing resource or to make changes on the server.

Syntax :

Authorization: Basic YWRtMW46cEBzJHdvcmQ=

Here Basic is the type of authorization and YWRtMW46cEBzJHdvcmQ= (adm1n:p@s$word) are the base64 encoded credentials

What is WWW-Authenticate response header ?

The HTTP WWW-Authenticate is response header that defines the authentication method that should be used to gain access to a resource.

Syntax :

WWW-Authenticate: Basic realm=”webdav”

Here Basic is the type of authorization and realm is a description of the protected area. If no realm is specified, developers often display a formatted hostname instead.

Description :

I found this remote code execution vulnerability via WebDav in 2018 on a private project. At first I did a directory brute forcing and found that /webdav directory with 401 Unauthorized status code. When I checked the response I found a response header WWW-Authenticate and found that it needs credentials to access. I searched on the google for default credentials of webdav and found that default credentials are jigsaw and jigsaw as user and password.

I used the Authorization header in the request with the base64 encoded (amlnc2F3OmppZ3Nhdw==) credentials jigsaw:jigsaw, but it failed. Then I found a blog where the credentials were wampp as user and xampp as a password. I again used the Authorization header in the request with base64 encoded (d2FtcHA6eGFtcHA=) credentials wampp:xampp and got 200 OK response.

Then I manipulated the HTTP verb from GET to OPTIONS to check how many methods or HTTP verbs are allowed. I found that HTTP PUT verb is allowed with other HTTP verbs. At first I tried to upload a normal text file which got uploaded successfully. Then I uploaded a file with XSS payload and it fired the pop-up. So the last thing was to upload a PHP file for remote code execution and it worked perfectly.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How I found this vulnerability ?

I found a webdav directory with 401 Unauthorized response status, WWW-Authenticate response header and an error message
Press enter or click to view image in full size
WebDav Directory - 401 Unauthorized

2. Then I searched for default credentials of WebDav and found it was jigsaw as username and password

Press enter or click to view image in full size
WebDav Default Credentials

3. Then I encoded them in base64 but it didn’t work

Press enter or click to view image in full size
Base64 - jigsaw:jigsaw

4. Then I found another default webdav credentials in a blog

Press enter or click to view image in full size
WebDav Default Credentials

5. I again encoded it in base64 and this time they worked and I got 301 Moved Permanently response and following the redirection I got 200 OK response

Press enter or click to view image in full size
Base64 Encoded Credentials - wampp:xampp
Press enter or click to view image in full size
301 Moved Permanently
Press enter or click to view image in full size
200 OK

6. I changed the HTTP verb from GET to OPTIONS for checking the allowed verbs and found many were allowed including PUT verb

Press enter or click to view image in full size
HTTP Verb - OPTIONS

7. I simply tried to upload a .txt file using PUT verb on the server and it was successful created

Press enter or click to view image in full size
Text File

8. Then I uploaded .html file using PUT verb with XSS payload in request body and it got fired

Press enter or click to view image in full size
XSS Payload - .html File
Press enter or click to view image in full size
XSS Fired

9. Then I uploaded .php file using PUT verb with normal php payload in request body and it was successful

Press enter or click to view image in full size
PHP Payload - .php File
Press enter or click to view image in full size
PHPInfo()

10. I again uploaded .php file using PUT verb with rce payload in request body and it gave me 204 No Content response

Press enter or click to view image in full size
RCE Payload - PHP

11. I visited the web page https://www.mytarget.com/webdav/Jerry.php and added ?JerryCommand=id as the parameter and it worked, I got remote code execution

Press enter or click to view image in full size
Remote Code Execution

12. Exploiting further I searched for reverse shell cheat sheet on pentestmonkey

Press enter or click to view image in full size
PentestMonkey - Reverse Shell Cheat Sheet

13. Then I started a netcat listener on my machine

Press enter or click to view image in full size
Netcat Listener

14. In next step I searched for python, is it using python or not

Press enter or click to view image in full size
Command - which python

NOTE : Using a command “which python” will tell whether the system is using python3 or python2.

15. I used a normal python reverse shell payload of pentestmonkey and got a reverse shell on my netcat listener

Press enter or click to view image in full size
Python Reverse Shell Payload
Press enter or click to view image in full size
Reverse Shell

Why it happened ?

In my opinion,

Fault 1 : The password set for authorization was one of the default credentials used by webdav.

Fault 2 : The webdav was enabled and was publicly accessible.

Fault 3 : WebDav was allowing some dangerous methods like PUT, DELETE, COPY etc.

Impact :

Any user can easily upload file on the server which can lead to remote code execution because PUT method was allowed.

Mitigation :

There are few mitigations that could be taken into consideration are stop using default credentials, do not enable webdav and stop allowing dangerous methods like PUT.

NOTE : This vulnerability is not only limited to WebDav, you can also try this where APIs are used. Just capture the request and change the HTTP verb from GET to OPTIONS for checking how many methods are allowed.

Reference report : https://hackerone.com/reports/487656

Press enter or click to view image in full size
