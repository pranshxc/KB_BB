---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-05-03_server-side-request-forgeryssrfport-issue-hidden-approch-.md
original_filename: 2019-05-03_server-side-request-forgeryssrfport-issue-hidden-approch-.md
title: Server Side Request Forgery(SSRF){port issue hidden approch }
category: documents
detected_topics:
- ssrf
- command-injection
tags:
- imported
- documents
- ssrf
- command-injection
language: en
raw_sha256: 6c96e9671a531f52df9ae75b42dc853f675678c2bed263815cdf116c36e923e0
text_sha256: 52b7be8a85e71d71fb09de44b09fcb31ae60f2d03dc392ee5744b3f31aa8db5a
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Server Side Request Forgery(SSRF){port issue hidden approch }

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-05-03_server-side-request-forgeryssrfport-issue-hidden-approch-.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `6c96e9671a531f52df9ae75b42dc853f675678c2bed263815cdf116c36e923e0`
- Text SHA256: `52b7be8a85e71d71fb09de44b09fcb31ae60f2d03dc392ee5744b3f31aa8db5a`


## Content

---
title: "Server Side Request Forgery(SSRF){port issue hidden approch }"
url: "https://medium.com/@w_hat_boy/server-side-request-forgery-ssrf-port-issue-hidden-approch-f4e67bd8cc86"
authors: ["Deepak Holani (@w_hat_boy)"]
bugs: ["SSRF"]
publication_date: "2019-05-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5270
scraped_via: "browseros"
---

# Server Side Request Forgery(SSRF){port issue hidden approch }

Server Side Request Forgery(SSRF){port issue hidden approch }
Deepak Holani
Follow
3 min read
·
May 3, 2019

482

1

Hello,

This is my first write-up. I hope you will like this.

Deepak Holani (@w_hat_boy) | Twitter
The latest Tweets from Deepak Holani (@w_hat_boy). #appsec 🤗...#security

twitter.com

I was testing a private program, domain was in limited scope. This is related to social networking domain www.abc.com

I was looking for the server-side issue I see their box for adding URL for job advertise first thing that come to my mind try for SSRF. SSRF Actions apply on different approaches depending on where you are looking for SSRF.

what are some SSRF Actions >>
Abuse the trust relationship between the vulnerable server and others.
Bypass IP whitelisting.
Bypass host-based authentication services.
Read resources which are not accessible to the public.
Scan the internal network to which the server is connected.
Read files from the web server.
View Status Pages and interact with APIs as the web server.
Retrieve sensitive information such as the IP address of a web server behind a reverse proxy.

As I said, it was a kind of social networking site.

job posting URL box below:

Press enter or click to view image in full size
To add external job link

I was testing for a port scan by simple localhost (127.0.0.1) and different ports.
but on the web page, it was not showing any error as we have a cool friend burp. It was not showing me a open port or close.
Now, what????

In addition to http:// I tried the other URL schema to read and make the server perform actions (file:///, dict://, ftp://, ldap:// and gopher://).

Get Deepak Holani’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

However, only http:// working, so I open my burp.

I had two choices to check, so first I will check it with burp-collaborator you can read more about below link given and other by manual check by port ..
Burp Collaborator
This section contains information about What Burp Collaborator is, How Burp Collaborator works, Security of data…

portswigger.net

I check the target, below is the request and response.

Note: If you do not have a VPS, a collaborator everywhere in the burp, can help you with testing.

Press enter or click to view image in full size
Press enter or click to view image in full size
Received DNS lookup

I decided to check whether the port was open or close. HTTPS:// was only allowed. port 443, 127.0.0.1:443 gave me 400 bad requests.

Press enter or click to view image in full size
400 bad request on port 443

Port 22, 127.0.0.1:22

Press enter or click to view image in full size
on port 22

In this way, I found many open ports or closed ones,and scanned all ports which threw 201 and 400 responses.

Report details -

29-june-2018— Bug Reported to the company.

29-june-2018 — Bug triaged by team

29- june -2018—bug fixed

2-july-2018 — Reward me with a cool bounty and a program launched on hackerOne soon.

Feel free to ask any question on this.

Twitter @w_hat_boy

Deepak Holani
Deepak Holani is on Facebook. Join Facebook to connect with Deepak Holani and others you may know. Facebook gives…

www.facebook.com

Thanks :)
