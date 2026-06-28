---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-08_how-i-was-able-to-take-over-one-of-dells-subdomains.md
original_filename: 2020-12-08_how-i-was-able-to-take-over-one-of-dells-subdomains.md
title: How I Was Able To Take Over One Of Dell’s Subdomains
category: documents
detected_topics:
- command-injection
- automation-abuse
tags:
- imported
- documents
- command-injection
- automation-abuse
language: en
raw_sha256: 4e8b86ef9bed3cb332055d04778957b2254831465fd26d3ba7fe688d921f0b70
text_sha256: 2f19d0ecc4cc9910afa069b36cf44b46204cc71c4af527c5a6aa9c293afb6419
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How I Was Able To Take Over One Of Dell’s Subdomains

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-08_how-i-was-able-to-take-over-one-of-dells-subdomains.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `4e8b86ef9bed3cb332055d04778957b2254831465fd26d3ba7fe688d921f0b70`
- Text SHA256: `2f19d0ecc4cc9910afa069b36cf44b46204cc71c4af527c5a6aa9c293afb6419`


## Content

---
title: "How I Was Able To Take Over One Of Dell’s Subdomains"
page_title: "Taking over a dell.com subdomain | Medium"
url: "https://pyrrhon.medium.com/how-i-was-able-to-take-over-one-of-dells-subdomains-7e06b8516e41"
authors: ["Taha Bıyıklı (@tahabykl)"]
programs: ["Dell"]
bugs: ["Subdomain takeover"]
publication_date: "2020-12-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4082
scraped_via: "browseros"
---

# How I Was Able To Take Over One Of Dell’s Subdomains

HOW I WAS ABLE TO TAKE OVER ONE OF DELL’S SUBDOMAINS
Taha Bıyıklı
Follow
4 min read
·
Dec 7, 2020

136

1

Hi everyone, I found a subdomain takeover recently on Dell, and I wanted to write a write-up of it. I hope you enjoy it!

First of all, I chose a bounty program. Then, as usual, I started with a subdomain scan. I scanned all the subdomains using subfinder. The scan finished, and I probed the output using httpx. I separated live and dead subdomains then started my research by checking for subdomain takeovers.

WHAT IS A SUBDOMAIN TAKEOVER?

Subdomain takeover is the process of registering a non-existing domain name to gain control over another domain. It generally occurs when there is a domain name (e.g. subdomain.example.com) using a CNAME record to another domain (e.g. subdomain.example.com CNAME anotherdomain.com). At some point, anotherdomain.com expires and is available for registration by anyone. If the CNAME record is not deleted from the example.com DNS zone, anyone who registers to anotherdomain.com has full control over subdomain.example.com until the DNS record is present.

Since you get a basic understanding of subdomain takeover vulnerability and impact of it, we can now skip to how to find a subdomain takeover, and how I found one.

Subdomain takeover is only possible on dead subdomains because the flaw occurs when an expired subdomain’s CNAME records are not deleted. So we can ignore the live subdomains. We need to check every dead subdomain. We can do it manually, or we can use a script that automates the process for us. I’m going to show you both two methods.

SEARCHING FOR TAKEOVERS MANUALLY

First things first we need to see every dead subdomain and their CNAME records. We can use a simple command to do that: dig. You can use it like the following:

Press enter or click to view image in full size
Dig Results

The output of this command is important and we are going to use that later. And we need to see the responses they return. We can use a browser to do it, but there are tools that take screenshots of the subdomains we specify, like aquatone. Since we can see the contents of dead subdomains, we need to see if the subdomain returns a custom error message or something else. If it returns an error message, we are going to use the error message and the anotherdomain.com (herokuapp.com in this situation) that we have seen in the output of the dig command and learn that if it is possible to takeover a subdomain. You can use can-i-take-over-xyz.

SEARCHING FOR TAKEOVERS AUTOMATICALLY

The method and process are the same, but tools can do all the process instead of us. I used a tool called subjack which is written in golang and is really fast. You can download it from here: subjack.

Get Taha Bıyıklı’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Once I found the bug, I skipped to the Proof of Concept to write and submit my report.

PoC (PROOF OF CONCEPT)

After finding a subdomain with a Heroku app in its dig results, I visited the page which led me to the following error page:

Press enter or click to view image in full size
Heroku Error Message

(This is not the same error page that I encountered but I forgot to take a screenshot since I was in a hurry to report it :) )

Then I visited can-i-take-over-xyz and looked to the engine column and found Heroku with the error message it returns, “app not found”. It was the same error as I saw in the dead subdomain.

Later, I visited the official website of Heroku engine and tried to take the subdomain over. And I was successful doing it :) To proof it, I left a little message on the subdomain:

Press enter or click to view image in full size
Proof of Concept

I tried to tell you about how I found a

My Twitter: twitter.com/tahabykl
