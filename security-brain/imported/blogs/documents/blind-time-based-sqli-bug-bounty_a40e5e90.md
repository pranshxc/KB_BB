---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-05_blind-time-based-sqli-bug-bounty.md
original_filename: 2019-07-05_blind-time-based-sqli-bug-bounty.md
title: Blind (time-based) SQLi - Bug Bounty
category: documents
detected_topics:
- sqli
- command-injection
- file-upload
- supply-chain
tags:
- imported
- documents
- sqli
- command-injection
- file-upload
- supply-chain
language: en
raw_sha256: a40e5e909c71625c2783ad957b33e46c7b85c24af002ad83f0df32a719c0afcf
text_sha256: fd1a0b0056f3b20f762fc0f42f3402718a1da739bc28380a88965e6b20870f47
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Blind (time-based) SQLi - Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-05_blind-time-based-sqli-bug-bounty.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, file-upload, supply-chain
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `a40e5e909c71625c2783ad957b33e46c7b85c24af002ad83f0df32a719c0afcf`
- Text SHA256: `fd1a0b0056f3b20f762fc0f42f3402718a1da739bc28380a88965e6b20870f47`


## Content

---
title: "Blind (time-based) SQLi - Bug Bounty"
url: "https://jspin.re/fileupload-blind-sqli/"
final_url: "https://jspin.re/fileupload-blind-sqli/"
authors: ["jspin (@jespinhara)"]
bugs: ["SQL injection"]
publication_date: "2019-07-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5164
---

# Blind (time-based) SQLi - Bug Bounty

  * [ ![jspin](/content/images/size/w100/2019/06/pipirate-1.png) ](/author/jspin/)

#### [jspin](/author/jspin/)

Jul 5, 2019 • 3 min read

This will be a short blog post and the first writing about Bug Bounties, I'm trying to get more involved into this matter and I'm hunting on my spare time and 90% of the time on [Synack](https://www.synack.com/red-team/). 

Early this month I got invited to a private bug bounty program running on [HackerOne](https://hackerone.com) and for obvious reasons I'll not name the company here. As soon I got invited to the program I asked some friends that were into this very same program before myself if they knew some "fishy" areas in the application that they were willing to share with me, well this is what friends are for. :)

Talking to <https://twitter.com/reefbr> he sent me a self-register page in a critical domain (in-scope). The registration went through without any problem and a few seconds after hit the send button I got an email with the access details. 

With my self-registered user working good it was very quick to found a file upload feature within the application. File Uploads functions are straightforward so I tried to upload a random file to see if any security control was in place by the application. The limitations that I found were:

  * PDF files accept only
  * AV running on the backend server

After poking around the upload function, I realise that the application was only validating the file type extension, such as "_filename_**.pdf** ". I did several tries to bypass this validation and I got success in some, but in the end I did not reach any execution in the server-side, time to change the strategy.

Back in the past, when doing my official daily duties as a Penetration Tester I came across a web application that was including the filename into the database, as far I remember that time I got a Blind (time-based) SQL Injection in the **filename parameter**. So, why not test in this application? 

Burp Proxy set to intercept the HTTP requests, then I hit the _Upload button_ in the application and replace the original filename parameter to:

![](https://jspin.re/content/images/2019/06/sqli-blog-01.png)

Note: I tried to send the request without the **.pdf** extension but the application was rejecting. BTW, this is the same payload used by the Burp Scanner for active tests.

The application was running "behind" the [Cloudflare](https://www.cloudflare.com/) WAF, so after some tries to confirm if the application was vulnerable all my requests were getting the "Access Denied" message. Now it's time to bring back <https://twitter.com/reefbr>, Manoel had reported a Cloudflare bypass to the same program and again... he told me about this. Using the bypass (configuration issue) found by @reefbr I did manage to confirm the SQL Injection (finally).

Talk is cheap show me the PoC. Initial request bellow:

![](https://jspin.re/content/images/2019/06/sqli-blog-02.png)

Let's increase the sleeping time...

![](https://jspin.re/content/images/2019/06/sqli-blog-03.png)

Going up a bit on the sleeping time:

![](https://jspin.re/content/images/2019/06/sqli-blog-04.png)

Let's make sure that the triage team will understand and be able to reproduce, so +1 request...

![](https://jspin.re/content/images/2019/06/sqli-blog-05.png)

That's all folks, hope you did enjoy.

As a final note, this private program is handling very sensitive information (PII) so extracting any data would create new issues to the program's owner. Having this in mind, I choose to proceed with the exploitation process by using the sleep payload and comparing the responses time to proof the vulnerability.

* * *

Timeline:

  1. Report Sent
  2. Report Triaged
  3. Report Solved (bug fixed)
  4. Bounty Paid
