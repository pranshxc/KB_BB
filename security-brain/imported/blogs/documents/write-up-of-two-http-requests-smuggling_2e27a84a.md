---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-09-07_write-up-of-two-http-requests-smuggling.md
original_filename: 2019-09-07_write-up-of-two-http-requests-smuggling.md
title: Write up of two HTTP Requests Smuggling
category: documents
detected_topics:
- xss
- command-injection
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- supply-chain
language: en
raw_sha256: 2e27a84ac1be8d3ffdbaf99bc7a5b5cdbb4450f26880e33f72fba47ada630407
text_sha256: 1a3ceab7b1905886800721c161846256c2ca440d3e52a1047a36ab77b10250ae
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Write up of two HTTP Requests Smuggling

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-09-07_write-up-of-two-http-requests-smuggling.md
- Source Type: markdown
- Detected Topics: xss, command-injection, supply-chain
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `2e27a84ac1be8d3ffdbaf99bc7a5b5cdbb4450f26880e33f72fba47ada630407`
- Text SHA256: `1a3ceab7b1905886800721c161846256c2ca440d3e52a1047a36ab77b10250ae`


## Content

---
title: "Write up of two HTTP Requests Smuggling"
url: "https://medium.com/@cc1h2e1/write-up-of-two-http-requests-smuggling-ff211656fe7d"
authors: ["C1h2e1 (@C1h2e11)"]
bugs: ["HTTP request smuggling"]
publication_date: "2019-09-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5045
scraped_via: "browseros"
---

# Write up of two HTTP Requests Smuggling

Top highlight

Write up of two HTTP Requests Smuggling
C1h2e1
Follow
4 min read
·
Sep 7, 2019

421

1

This article about how I found two sites for HTTP Request Smuugling

let’s go

About HTTP Requests Smuggling

My information here is not enough for you to understand this vulnerability, be sure to read the below article and complete their challenge

protswigger airticle

https://portswigger.net/blog/http-desync-attacks-request-smuggling-reborn

Since HTTP/1.1 there’s been widespread support for sending multiple HTTP requests over a single underlying TCP or SSL/TLS socket. The protocol is extremely simple — HTTP requests are simply placed back to back, and the server parses headers to work out where each one ends and the next one starts. This is often confused with HTTP pipelining, which is a rarer subtype that’s not required for the attacks described in this paper.

The end of our message must be consistent with the request sent by the front end. If the attacker sends an ambiguous request, it may be parsed into two different HTTP requests.

The obvious approach to detecting request smuggling vulnerabilities is to issue an ambiguous request followed by a normal ‘victim’ request, then observe whether the latter gets an unexpected response. However, this is extremely prone to interference; if another user’s request hits the poisoned socket before our victim request, they’ll get the corrupted response and we won’t spot the vulnerability. This means that on a live site with a high volume of traffic it can be hard to prove request smuggling exists without exploiting numerous genuine users in the process. Even on a site with no other traffic, you’ll risk false negatives caused by application-level quirks terminating connections.

First Bug

My idea is to find all the function points and perform HTTP Request Smggling detection. Here I use the https://github.com/PortSwigger/http-request-smuggler tool to scan and discover the vulnerability and use Trubo Intruder. to attack.Because at that time, I didn’t learn how to further exploit the vulnerability, so I simply controlled the user request. In the following vulnerability, there is a way to get the user response.

Since I didn’t use this tool at first, I just searched for POST requests and added a simple Payload for detection.I discovered this vulnerability at first but I did not successfully exploit the vulnerability to control user requests.

POC

In my search, I found this function to save the shipping address.This function point exists HTTP Request Smuggling.This is a CL.TE.I use it to control user requestsHere /configs/web/switches/list can return the user’s sensitive information. I am just doing a GET request to send the test.

Press enter or click to view image in full size

Here I used Trubo intruder to verify this Bug, successfully returned the user’s information to prove that the user’s request is controlled

Secone Bug

When I discovered the first vulnerability, I understood how to detect the discovery of the vulnerability, so I discovered the next vulnerability in recent days.

Get C1h2e1’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The target website is a shopping website,I used the same idea to discover the vulnerability.Found this vulnerability at the shipping address

Press enter or click to view image in full size

I let the user redirect to the 404 page

I am no longer satisfied with controlling user requests, I decided to choose to find reflection points.At first I wanted to find XSS, even if it was Self XSS.But I didn’t find it, so I chose to save the data to the location I can view. Here I chose to save the address of the address but I found that there is a limit of 50 bytes.I tried to bypass the limit but didn’t succeedSo I started looking again, because this is a shopping site, I was looking for at the profile but failed again.So I tried various functions, and finally I found an invoice title at the point of printing the invoice.

I decided to start using it. First I need to create an order and create an invoice, write the invoice title to the location of the last parameter like this

Press enter or click to view image in full size

Then I need to run the attack,is is my Trubo Intruder configuration.I use my own cookie to send a request packet to save the invoice title as the victim’s response

Press enter or click to view image in full size

Pay attention to the Content-length setting. I didn’t add Content-length in the first test, so I didn’t get the victim’s response successfully.

Boom!!!User response was successfully obtained by me, I can get information such as cookies! !

Press enter or click to view image in full size

Check Out My twitter @C1h2e11

./Logout
