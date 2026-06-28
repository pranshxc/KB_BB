---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-17_one-param-10k.md
original_filename: 2020-05-17_one-param-10k.md
title: One Param => $10k
category: documents
detected_topics:
- access-control
- csrf
- idor
- xss
- command-injection
- otp
tags:
- imported
- documents
- access-control
- csrf
- idor
- xss
- command-injection
- otp
language: en
raw_sha256: bc4b88ddc6ca7400ec099be40aa03904863e157f6795591a5150df25323445d3
text_sha256: b8a0a471fe0b6b6ddbd93620cba31e2b6fdfb2ad37bcb169784ced1244eb8072
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# One Param => $10k

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-17_one-param-10k.md
- Source Type: markdown
- Detected Topics: access-control, csrf, idor, xss, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `bc4b88ddc6ca7400ec099be40aa03904863e157f6795591a5150df25323445d3`
- Text SHA256: `b8a0a471fe0b6b6ddbd93620cba31e2b6fdfb2ad37bcb169784ced1244eb8072`


## Content

---
title: "One Param => $10k"
url: "https://medium.com/@bilalmerokhel/one-param-10k-9d80a33f5eb5"
authors: ["Bilal Khan (@bilalmerokhel)"]
bugs: ["IDOR", "XSS", "Account takeover"]
bounty: "10,000"
publication_date: "2020-05-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4583
scraped_via: "browseros"
---

# One Param => $10k

1

·

Top highlight

One Param => $10k
Bilal Khan
Follow
3 min read
·
May 18, 2020

1.1K

4

Hi everyone, 8 months before I was invited to a private program on BugCrowd, where I reported 8 bugs and all of them were marked as duplicate. I was so depressed. I left that program and started hunting other programs on BugCrowd. After 8 months I got an email saying the following bugs have been resolved, I just ignored that email, at that time I was hunting a private program, suddenly I just thought let's give it a try and see if the bugs are really fixed. I fired up my burp suite and started digging.

About the web-application

The web application was built on react, there was role-based authentication, they were using Bearer Authentication, which means no chance for CSRF, CORS etc.

Param

I found nothing, I was going through my burp HTTP history, saw an endpoint where a lot of parameters were there, I thought let's try each parameter in every request and see what happens, I didn’t even know what I will end up with. I tried the parameters in every request in GET and POST. found nothing then I realize, let's save them in a file and make a wordlist of it and then try them on their API. there was an HTTP request like this.

GET /v2/ HTTP/1.1
Host: api.redacted.com
Connection: close
Content-Length: 159
Accept: application/json, text/plain, */*
authorization: Bearer {token}
x-redacted-client: web/7.80.0
x-connection-id: 94881378-e4dsb-4cf4-8569-fb5e434223b61
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: https://api.redacted.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

Now here I had to use my brain more because every request has their own method and parameters, what to be done in every request?. I send the request to the intruder and select the positions like this.

§CHECK§ /v2/§one§?§two§=§three§ HTTP/1.1
Host: api.reacted.com
Connection: close
Accept: application/json, text/plain, */*
authorization: Bearer {token}
x-reacted-client: web/7.76.2
x-connection-id: 94881378-eassb-4cf4-5569-fb5as334223b61
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
Origin: https://app.reacted.com
Sec-Fetch-Site: same-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

I ran the intruder and came up with some interesting results like this.

Press enter or click to view image in full size
Password Disclosure

Sorry I can not disclose the param and the company name but try to understand the scenario here.

Get Bilal Khan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After reporting it I got their reply with $1k bounty.

Press enter or click to view image in full size
1k$ bounty. but
Bounty Time

After the bounty, I thought let's try one parameter everywhere but, how about changing requests like changing GET to POST and POST to GET and just like that PUT to POST and GET, not just that let's play around with Content-Type and change the content type as application/JSON to application/x-www-form-urlencoded vice versa. The results were so surprising I got a lot of endpoints, all of them were disclosing sensitive information including passwords (plain text 😁). The parameters I used doesn't actually belong to the original request.

Press enter or click to view image in full size
$10k ❤

Always go through your burp HTTP history and note every parameter make a list of it and fuzz as much as you can. Try everything in every format like if there is a GET request try that request in POST, PUT, PATCH and DELETE, play around with the content-type and you will get there ❤
