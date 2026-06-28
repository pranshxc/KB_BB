---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-10-19_23000-for-authentication-bypass-file-upload-arbitrary-file-overwrite.md
original_filename: 2022-10-19_23000-for-authentication-bypass-file-upload-arbitrary-file-overwrite.md
title: 23000$ for Authentication Bypass & File Upload & Arbitrary File Overwrite
category: documents
detected_topics:
- jwt
- xss
- idor
- access-control
- command-injection
- file-upload
tags:
- imported
- documents
- jwt
- xss
- idor
- access-control
- command-injection
- file-upload
language: en
raw_sha256: 9d375408a526c0509cb0fc4ad604e68eefbe97967cdf5e73f20ad93e197e0688
text_sha256: 8469a9668c72c84d27757328c2f7992a7c6b524702fd75dabf746989e0be39b7
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# 23000$ for Authentication Bypass & File Upload & Arbitrary File Overwrite

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-10-19_23000-for-authentication-bypass-file-upload-arbitrary-file-overwrite.md
- Source Type: markdown
- Detected Topics: jwt, xss, idor, access-control, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `9d375408a526c0509cb0fc4ad604e68eefbe97967cdf5e73f20ad93e197e0688`
- Text SHA256: `8469a9668c72c84d27757328c2f7992a7c6b524702fd75dabf746989e0be39b7`


## Content

---
title: "23000$ for Authentication Bypass & File Upload & Arbitrary File Overwrite"
url: "https://medium.com/@h4x0r_dz/23000-for-authentication-bypass-file-upload-arbitrary-file-overwrite-2578b730a5f8"
authors: ["Souhaib Naceri (@h4x0r_dz)"]
bugs: ["JWT", "Authentication bypass", "Arbitrary file write", "Unrestricted file upload"]
bounty: "23,000"
publication_date: "2022-10-19"
added_date: "2022-10-23"
source: "pentester.land/writeups.json"
original_index: 2015
scraped_via: "browseros"
---

# 23000$ for Authentication Bypass & File Upload & Arbitrary File Overwrite

h4x0r_dz
 highlighted

23000$ for Authentication Bypass & File Upload & Arbitrary File Overwrite
How I found Authentication Bypass >> File upload vulnerability >> Arbitrary File Overwrite and how I managed I found the path of the file after the upload !!!!
h4x0r_dz
Follow
7 min read
·
Oct 19, 2022

3.7K

38

4

Hello Awesome Hackers, I hope you all doing well!

My name is Souhaib Naceri Or h4x0r_dz Algerian Ethical Hacker.

today I’m sharing a vulnerability that I found a while ago, which I believe is quite interesting.

but I’m not going to share the bug bounty program name & domain name ..etc, because I didn’t get permission to disclose it.

so let’s assume the target is test.com

when I started hunting on the program, I found the admin panel UI bypass

the target uses JSON Web Token (JWT) for the authentication mechanism, and I have put A bit of time into order to understand, trying to find bugs on the bug bounty targets that use JSON Web Token (JWT) .

when you log in to the main website test.comA JSON Web Token (JWT) will be generated for the regular user,

now After I know how the target work, I started doing recon. reading javascript files, running Burp Suite, and clicking on any bottom in the website & also I used Wayback Machine to get all the possible endpoints, and finally subdomain enumeration.

I found The interesting subdomain admin.test.com and now we have come to the interesting part, the admin panel exposes the js file app.js and after I read the whole file 200000 lines of code, I found it uses the JSON Web Token (JWT) for authentication, and I found a list of realm.

but the interesting realm was test-dashboard

what is realm?

The “realm” authentication parameter is reserved for use by
authentication schemes that wish to indicate a scope of protection.
A protection space is defined by the canonical root URI (the scheme
and authority components of the effective request URI;

more info here: https://www.rfc-editor.org/rfc/rfc7235#section-2.2

I used https://jwt.io/ to decode the user Token, and there is a realm=test-user

now I know if I am able to manipulate the realm to test-dashboard I will be able to login to the admin panel, just a feeling.

the test-dashboard is the website name instead of the test, it was like : target-dashboard

### steps :

go to https://test.com/
make internet on
login to your account and change the realm to test-dashboard in the post request : https://test.com.com/api/v1/login
HTTP request
POST /api/v1/login HTTP/1.1
Host: accounts.test.com
Connection: close
Content-Length: 79
Accept: */*
Content-Type: application/json
{“email”:”youremail@gmail.com”,”password”:”<password>”,”realm”:”test-dashboard”}
Press enter or click to view image in full size

if you decode the jwt you can see the realm has been changed.

Press enter or click to view image in full size

now using the manipulated JWT token I’m able to login to the admin panel.

I reported this bug immediately, but this was the expected response from the bug bounty program :

We discussed this with the devs and they said that the admin dashboard you’ve got access to is just a react application that gets rendered client-side (the kind of pages that only need public info to be rendered) and not much else since the actual API is a separate application with endpoints that require a valid auth token with specific scopes. So, unless you can craft a token that will let you interact with the API, we will be lowering the severity of the issue.

test-staff updated the severity from Critical to Medium

Press enter or click to view image in full size

I almost gave up, but I decided to continue digging deeper.

I agree with the Team, to consider the bug critical I need to miniplate the scope in the JSON Web Token (JWT) .

but this is impossible, I need to find 0day and JWT mechanism and any website uses JSON Web Token (JWT) will be vulnerable.

But I’m crazy enough because I start looking for something similar .

since I can control the realm and generate valid JWT, I tried every payload to manipulate the scope, but nothing worked for me and didn’t able to do the escape that I want .

I started doing content discovery using ffuf against admin.test.com but Unfortunately, I didn’t find any valid endpoint,

by default ffuf uses the GET HTTP Method, so I Gave a try to the POST Method. and I found this endpoint https://admin.test.com/upload return 403, it is quite interesting because I found this endpoint in the app.js file.

now, what if I am able to upload a web shell? I got excited

after I spend hours reading the javascript file, I was able to build the file upload request:

POST /upload HTTP/1.1
Host: admin.test.com
Connection: close
Content-Length: 300
Accept: application/json, text/plain, */*
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarypxxxxxx
Authorization: Bearer <JWT>
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4629.0 Safari/537.36
------WebKitFormBoundarypxxxxxx
Content-Disposition: form-data; name="destination"
gallery/
------WebKitFormBoundarypxxxxxx
Content-Disposition: form-data; name="file"; filename="poc.txt"
Content-Type: Text/plain
h4x0r-dz POC 
------WebKitFormBoundarypxxxxxx--

but I got a 401 HTTP error :( . Even after I manipulate the realm In JWT

Authentication Bypass

do you know what is Fuzzing ?

if your answer is NO then you miss so many bugs behind you !

Fuzz testing or Fuzzing is a Black Box software testing technique, which basically consists in finding implementation bugs using malformed/semi-malformed data injection in an automated fashion.

Get h4x0r_dz’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

more information: Fuzzing — OWASP Foundation

I start Fuzzing the Authorization: Bearer <JWT>

and finally, I saw 200 responses :) .

steps
go to test.com
login to your account .
grep the Authorization header

the issue here is when you delete Bearer from the Authorization header You will be able to authenticate in https://admin.test.com. and you will be able to have the admin permission

send this request to upload the file

POST /upload HTTP/1.1
Host: admin.test.com
Connection: close
Content-Length: 300
Accept: application/json, text/plain, */*
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarypxxxxxx
Authorization: <JWT>
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4629.0 Safari/537.36
------WebKitFormBoundarypxxxxxx
Content-Disposition: form-data; name="destination"
gallery/
------WebKitFormBoundarypxxxxxx
Content-Disposition: form-data; name="file"; filename="poc.txt"
Content-Type: Text/plain
h4x0r-dz POC 
------WebKitFormBoundarypxxxxxx--

I go 200 responses with massage uploaded

Press enter or click to view image in full size

now where I can find the path of my file ??

At first, I thought it is the end, there is no way to know where my file was stored.

I tried the content discovery using ffuf against all the subdomains trying to find something like admin.test.com/uploads/poc.txt

but I didn’t find anything, I start looking into my burp history and reading the response, and I found this href=https://xxxxxxxx.cloudfront.net/gallery/xxxxxxxxx

hmmm, the gallery is the same value at my file upload request at destination input.

I browsed https://XXXXXXXXX.cloudfront.net/gallery/poc.txt

and I found my file is there

Press enter or click to view image in full size
but what is CloudFront ?

Amazon CloudFront is a content delivery network operated by Amazon Web Services. Content delivery networks provide a globally-distributed network of proxy servers that cache content, such as web videos or other bulky media, more locally to consumers, thus improving access speed for downloading the content.

so I can’t upload web shell :( .

even if I report this file upload now, The severity will be very low. again I need to dig deep.

Arbitrary File Overwrite

by default Amazon S3 is vulnerable to Misconfiguration Arbitrary File Overwrite if you upload file.txt Amazon S3.

now I have Arbitrary File Overwrite, Now I can do so many things I found that xxxxxxxx.cloudfront.net was used in the main website to host javascript and HTML and other files

Press enter or click to view image in full size

so many files are hosted in xxxxxxxx.cloudfront.net , and as an attacker, I can change the content of the files and managed to get stored XSS and other security issues in the main domain, because they used xxxxxxxx.cloudfront.net to host windows software and pdfs, where the user can download, it is a part of the main website,

so I can change the content of these files and gain RCE on the user’s computers by putting malicious codes in the existing EXE or pdf files CSS …etc

steps

the attacker can change other files’ content. the destination parameter in the request body Specify the file path, so I can change any file

first POC file :

Press enter or click to view image in full size

We could not verify the vulnerability from the browser due to the cache, so you can CURL

now after I changed the content of the file poc.txt via this requset :

POST /upload HTTP/1.1
Host: admin.test.com
Connection: close
Content-Length: 300
Accept: application/json, text/plain, */*
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarypxxxxxx
Authorization: <JWT>
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4629.0 Safari/537.36
------WebKitFormBoundarypxxxxxx
Content-Disposition: form-data; name="destination"
gallery/
------WebKitFormBoundarypxxxxxx
Content-Disposition: form-data; name="file"; filename="poc.txt"
Content-Type: Text/plain
Arbitrary File Overwrite 
------WebKitFormBoundarypxxxxxx--
Press enter or click to view image in full size

as you can see in my terminal, I was able to over write the existing file.

team response
Press enter or click to view image in full size

I got 20k for this vulnerability

also, I got $3,000 for UI admin panel access, 23000$ in total

Press enter or click to view image in full size

I hope you learned something new Today, and I’m Really sorry If my write-up was not clear, or if I’m talking too much.

Best regards,

h4x0r_dz
