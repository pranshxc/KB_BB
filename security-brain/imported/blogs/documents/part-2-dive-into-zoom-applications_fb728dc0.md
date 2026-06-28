---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-07-13_part-2-dive-into-zoom-applications.md
original_filename: 2021-07-13_part-2-dive-into-zoom-applications.md
title: 'Part 2: Dive into Zoom Applications'
category: documents
detected_topics:
- api-security
- jwt
- access-control
- xss
- command-injection
- otp
tags:
- imported
- documents
- api-security
- jwt
- access-control
- xss
- command-injection
- otp
language: en
raw_sha256: fb728dc01a258ae013fc32f6e35e5bb87e8f1fe538f9888ac91cbf6895a481c7
text_sha256: c1bd9527dba07ceb51e420066516482f4d30b2034f6b1eb4a5e80056bc9a60b1
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Part 2: Dive into Zoom Applications

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-07-13_part-2-dive-into-zoom-applications.md
- Source Type: markdown
- Detected Topics: api-security, jwt, access-control, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `fb728dc01a258ae013fc32f6e35e5bb87e8f1fe538f9888ac91cbf6895a481c7`
- Text SHA256: `c1bd9527dba07ceb51e420066516482f4d30b2034f6b1eb4a5e80056bc9a60b1`


## Content

---
title: "Part 2: Dive into Zoom Applications"
url: "https://rakesh-thodupunoori.medium.com/part-2-dive-into-zoom-applications-1b01091345c1"
authors: ["Rakesh Thodupunoori (@rakesh_3895)"]
programs: ["Zoom"]
bugs: ["CSRF", "Account takeover", "Information disclosure", "Session expiration issue", "Broken authorization", "Logic flaw"]
publication_date: "2021-07-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3511
scraped_via: "browseros"
---

# Part 2: Dive into Zoom Applications

Part 2: Dive into Zoom Applications
Rakesh Thodupunoori
Follow
5 min read
·
Jul 13, 2021

230

TL;DR

This time I took permission from the zoom team to test out-of-scope applications. However, they did not accept at first but later they said they will accept only if the vulnerability comes under the P1 or P2 category.

Cool…

Let's dig into OOS

#7 Remember Part-1 #2 where they fixed CSRF by adding wp-nonce, Later I bypassed that by using another logged-in zoom user “wp-nonce” token to perform a successful CSRF attack everything looks fine as of now but this won't come under the P1 or P2 category. Now comes the XSS, there are few fields where I can inject XSS payload, and that’s not the end, I can’t steal cookies because of the HTTPOnly flag which is set to “TRUE”. Is it over?

No, Instead of cookies I focused on stealing API keys, I used blind XSS payload from XSS hunter to read the source page of an api/* endpoints. With the API keys, I can perform any actions with the help of the Zoom API playground.

The final POC looks like

<html>
<body>
<script>history.pushState(‘’, ‘’, ‘/’)</script>
<form action=”https://developer.zoom.us/me/" method=”POST”>
<input type=”hidden” name=”company&#45;name” value=”test” />
<input type=”hidden” name=”developer&#45;contact” value=”test@test.com” />
<input type=”hidden” name=”app&#45;name” value=”test” />
<input type=”hidden” name=”app&#45;description” value=”</textarea><BLIND XSS PAYLOAD>” />
<input type=”hidden” name=”platforms&#91;&#93;” value=”web” />
<input type=”hidden” name=”wp&#95;nonce” value=”914fbb3bb0" />
<input type=”submit” value=”Submit request” />
</form>
</body>
</html>

Sending the above exploit to any user, among successful attack I can steal their API key and secret.

further found in two more endpoints and got rewarded.

#8 Stealing Zak tokens leads to compromise zoom accounts.

I thought of working on api’s more, one API endpoint /user/get gives all the user information if we provide user-id

Request

Press enter or click to view image in full size
Press enter or click to view image in full size

Getting a user id is not a big deal, refer to Part-1 #3 to know how I was able to find user-id, once I requested, below is the response which I got

Response

Press enter or click to view image in full size

few things I noticed here token, zpk, and zak, what exactly are these? How to use them, where to use them? Lots of questions :|

But one thing I understood zak and zpk are JWT tokens! wait, zoom is not using JWT for authentication. I tried to decode zak using JWT.io

Press enter or click to view image in full size

No other information, still not sure how to exploit. The next day I tried the same technique which is used to compromise analyst account refer to Part-1 #5

Crafted URL: https://zoom.us/<reducted>?zak=<zak token>

Get Rakesh Thodupunoori’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Guess what! I was able to login to the owner account directly

Press enter or click to view image in full size

Found multiple API endpoints which disclose zak tokens and reported, Got a good reward!

#9 Later I tried to remove all the privileges to one of the users within the account and tried to log in but failed to access the zoom.us account.

However, I was able to access the developer.zoom.us account. Here I can get API keys and perform any action using API endpoints. Reported and rewarded.

#10 Zoom states that v1 API will be deprecated and they already started v2 API soon I checked v2 and the documentation shows that API keys are valid only for 10 minutes. however, it is not expiring after 10 minutes. Reported and got rewarded.

**After few days I got a notification as Zoom added all subdomains in the scope and increased the reward. Time to dig deeper..

#11 bypassing Signature & Stealing pager-duty API keys of any zoom user

Zoom introduced marketplace.zoom.us, where anyone can create integration which is later verified by the zoom team and approves.

I installed pager duty integration from the marketplace and configured the application with a pager duty API key.

Press enter or click to view image in full size

After a few backs and forth trials I checked my burp history, where I found a <Reducted>.zoom.us is managing the pager duty API keys which are configured earlier.

Request

GET /pagerduty/config?signature=7HuiNVkFlvvqNxooZzLAevNuvyA&user_id=M4u<REDUCTED> HTTP/1.1
Host: <REDUCTED>.zoom.us
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Origin: https://<REDUCTED>.zoom.us
Connection: close

There are no cookies, so I directly try accessing the Request in repeater and the Response is

HTTP/1.1 200 OK
Date: Mon, 29 Jul 2019 20:08:26 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 80
Connection: close
x-amzn-RequestId: a048105e-b23c-11e9-8381-6d6d62790a0e
access-control-allow-origin: *
access-control-allow-headers: Content-Type, Authorization
x-amzn-Remapped-content-length: 80
x-amz-apigw-id: dmnJMFymoAMF6Nw=
access-control-allow-methods: OPTIONS, GET, POST, PUT, PATCH, DELETE
etag: W/"50-pySbe+m76pCbniLaJ/LRkpJvylU"
x-powered-by: Express
X-Amzn-Trace-Id: Root=1-5d3f523a-696bd7c04ada12240312a370;Sampled=0
{"is_admin":true,"platform_token":"<REDUCTED>","service_id":"P9ZRCKP"}

Okay, what is the vulnerability here, lack of cookies? No

If you observe the Request, the URL contains two things Signature and User_id

URL: https://<REDUCTED>.zoom.us/pagerduty/config?signature=7HuiNVkFlvvqNxooZzLAevNuvyA&user_id=M4u<REDUCTED>

of course, finding a user-id is very easy, if you think how? refer to part 1 #3. However the problem is with the signature, this acts as an auth. If I can bypass this I can steal any zoom user pager duty API key if configured, tried multiple ways, after some time I simply removed the value of a signature and then? you know what happened, I was able to access the pager duty API key. Now changing the user_id to others I was able to view the pager duty API key.

Press enter or click to view image in full size

Reported and Rewarded later.

any feedback, comments, and suggestions would be highly appreciated

To be continued …

Thanks for the review Ankit, Ganesh, Neelam, Prashanth
