---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-10-13_blind-ssrf-the-hide-seek-game.md
original_filename: 2020-10-13_blind-ssrf-the-hide-seek-game.md
title: Blind SSRF - The Hide & Seek Game
category: documents
detected_topics:
- command-injection
- ssrf
- automation-abuse
tags:
- imported
- documents
- command-injection
- ssrf
- automation-abuse
language: en
raw_sha256: 18828a961c6e0b019fc679afaa58d59c9eca8d73645c7059dc7ef75801f28e35
text_sha256: 99d5f1a148c61abeba358691c84b23ebbf9c22269091d20fac49180d79d0fc79
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# Blind SSRF - The Hide & Seek Game

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-10-13_blind-ssrf-the-hide-seek-game.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, automation-abuse
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `18828a961c6e0b019fc679afaa58d59c9eca8d73645c7059dc7ef75801f28e35`
- Text SHA256: `99d5f1a148c61abeba358691c84b23ebbf9c22269091d20fac49180d79d0fc79`


## Content

---
title: "Blind SSRF - The Hide & Seek Game"
url: "https://medium.com/@shahjerry33/blind-ssrf-the-hide-seek-game-da9d0ecef2fb"
authors: ["Shrey Shah (@ShreySh43332033)"]
bugs: ["Blind SSRF"]
bounty: "400"
publication_date: "2020-10-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4199
scraped_via: "browseros"
---

# Blind SSRF - The Hide & Seek Game

Top highlight

Blind SSRF - The Hide & Seek Game
Jerry Shah (Jerry)
Follow
4 min read
·
Oct 13, 2020

593

5

Hello everyone I wanted to share one of my finding related to Blind SSRF on a private program on HackerOne for which they paid me $400.

Press enter or click to view image in full size

Summary :

Blind SSRF vulnerabilities occur when an application is making a request to a back-end server due to some reasons but the response is not shown on the front-end.

If we talk about the impact, it is low than that of normal SSRF because of their one way nature. They can be exploited to retrieve sensitive information from back-end systems and in a rare case it can be exploited to achieve remote code execution.

For this finding I used an extension of BurpSuite known as Collaborator Everywhere and I also used Collaborator Client. So I’ll be discussing both of them here.

How to add Collaborator Extension in your BurpSuite ?

Start your BurpSuite
Go to extender and click on BApp Store
Find the extension
Press enter or click to view image in full size
BApp Store

4. Install it to your BurpSuite

One of the easiest way to find Blind SSRF vulnerability is the out-of-band technique which means to use an external server to find blind vulnerabilities. That external server should be under your control which can be used to monitor network interactions with the system.

If you don’t want to setup your own server then you can use Burp Collaborator.

How I found this vulnerability ?

I went to my target website and it was using an API for interaction with the server, so I thought of using the extension Collaborator Everywhere
I started BurpSuite, went to Extender and clicked on Extensions. Then I selected the installed extension (Collaborator Everywhere).
Press enter or click to view image in full size
Collaborator Everywhere

3. Then I changed the browser proxy to manual

Press enter or click to view image in full size
Manual Proxy

4. I refreshed the page and I went to BurpSuite > Target > Site Map

5. I right clicked on my target and chose the option Add to scope

Press enter or click to view image in full size
Add to scope

You’ll get this pop-up, select Yes

Select Yes

6. Now just visit the site properly, means open your profile or you can go to your settings etc.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In my case I was having following options on dashboard to visit.

Options To Visit

So every request will be captured by BurpSuite (because of Add to Scope) and evaluated by Collaborator Everywhere extension.

7. After sometime I checked the Site map and found this issues

Press enter or click to view image in full size
Collaborator Pingback HTTP
Press enter or click to view image in full size
Collaborator Pingback HTTP
Press enter or click to view image in full size
Collaborator Pingback DNS

8. So I knew that it is vulnerable to Blind SSRF

9. Now I wanted to confirm it again so I used Burp Collaborator, you’ll find it in the BurpSuite it comes pre-installed

Press enter or click to view image in full size
Burp Collaborator Client

10. Click on Copy to clipboard for copying the payload

Press enter or click to view image in full size
Copying Payload

11. I sent the request to repeater and replaced the referrer header URL with the copied payload of Burp Collaborator client

Press enter or click to view image in full size
Burp Collaborator client payload

12. Now I clicked on go and waited for 5 to 10 seconds, then I clicked on Poll now and got the response from the server

Press enter or click to view image in full size
HTTP Response
Press enter or click to view image in full size
DNS Lookup

NOTE : You’ll find different payload in last 3rd image and in last 2nd image, it is because I reproduced the issue 2 times nothing else, so different payload for each time.

Important Points :

When testing for Blind SSRF it is common that you’ll find a DNS lookup for the given Burp Collaborator domain, but no HTTP request. This happens because the application attempted to make HTTP request to domain, which caused initial DNS lookup but the actual HTTP request was blocked by the network-level filtering.
If you find only the DNS lookup or DNS query then it is not a vulnerability, it is mandatory to have the HTTP response which will make it a valid vulnerability
Press enter or click to view image in full size
DNS Query - P5

You can see that it is considered as P5 according to bugcrowd’s VRT.

Press enter or click to view image in full size
