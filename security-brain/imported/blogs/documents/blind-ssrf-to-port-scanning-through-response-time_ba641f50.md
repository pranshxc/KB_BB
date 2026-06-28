---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-04-19_blind-ssrf-to-port-scanning-through-response-time.md
original_filename: 2021-04-19_blind-ssrf-to-port-scanning-through-response-time.md
title: Blind SSRF to Port Scanning through response time
category: documents
detected_topics:
- idor
- access-control
- ssrf
- xss
- command-injection
- file-upload
tags:
- imported
- documents
- idor
- access-control
- ssrf
- xss
- command-injection
- file-upload
language: en
raw_sha256: ba641f50d1e6a9b2f66159d5074a0b0e97c6461ce655182529fed9423dd53cc2
text_sha256: ec696f3c73b3bccb6702ae5655f6710acfd5717cdaba70711e6df2497cabb393
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Blind SSRF to Port Scanning through response time

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-04-19_blind-ssrf-to-port-scanning-through-response-time.md
- Source Type: markdown
- Detected Topics: idor, access-control, ssrf, xss, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `ba641f50d1e6a9b2f66159d5074a0b0e97c6461ce655182529fed9423dd53cc2`
- Text SHA256: `ec696f3c73b3bccb6702ae5655f6710acfd5717cdaba70711e6df2497cabb393`


## Content

---
title: "Blind SSRF to Port Scanning through response time"
url: "https://pharish4948.medium.com/blind-ssrf-to-port-scanning-through-response-time-d7336667299d"
authors: ["Harish"]
bugs: ["SSRF"]
publication_date: "2021-04-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3726
scraped_via: "browseros"
---

# Blind SSRF to Port Scanning through response time

Blind SSRF to Port Scanning through response time
Harish
Follow
3 min read
·
Apr 18, 2021

202

Introduction:

This article is about how I found an Server Side Request forgery in image upload link feature and escalated to port scanning.

For the unaware

Blind SSRF vulnerabilities arise when an application can be induced to issue a back-end HTTP request to a supplied URL, but the response from the back-end request is not returned in the application’s front-end response.

Mindset:

The other day, I started hunting on a fresh target which had a lot of features and functionality. A few different user roles.

As usual, configured Autorize for IDOR/Access controls and started browsing the application. Tested for xss but couldn’t pop it anywhere. It was in qr. Others who tested it, messaged in that they tested thoroughly and couldn’t find any.

Wanna stress one more thing here,

The way one thinks is different from what others do, you might find something which others might not have thought of though known to them.

So this target was tested by some of the guys who I know are really good at this. But I decided to test it anyway.

There was a image upload feature where user could upload image for their organization or submit a link to the image.
The request was GET request and the param was like

iurl=https://xyz.burpcollab.net/img.jpg

Get Harish’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I tried giving in the Burp collab link with /img.jpg to evade the validations if in case there was any.(First try how it’s supposed to work then try to manipulate it).

Got a response back. This by in itself doesn’t have any impact as it’s a feature and not a bug.

So I tried poking around and reading some articles to escalate it. And while reading one I remembered something. Rushed to test it and it worked.

So tried “url=http://localhost:80” and it gave a response, usually the server blocks anything related to localhost, there wasn’t any here. The response however wasn’t any different. It was just returning me “” in the body of response.

Tried url=http://www.google.com/favicon.ico and it returned base64 of favicon. At this point I didn’t do much coz whatever I did the response was throwing an error on giving anything any other file types.

So I went back to the localhost testing, I tried changing the port to 801 and it delayed a bit. I was like

To confirm it again, I tried some of the ports I was sure was open like 80,443 and it responded almost within 300 millis on average and where as the invalid one 801,65000 responded after 1000 millis on average. In case you still don’t get it, lemme spill the beans. It was delaying and getting timed out on closed port and replying instantly on open port.

Quickly wrote up a report. I was a bit excited this time and made a mistake of not giving my 100% while reporting. Just concentrated more on the steps to reproduce. Usually I give my best in the Desc and impact part too but this time just gave a brief of what it was in a single sentence and submitted it.

After a while when the adrenaline rush calmed down, I didn’t feel confident on my report though was confident on the POC. I was like still in qr so wasn’t able to see if anyone else reported the same. I was still in a bit of dilemma if it’ll be accepted. I didn’t wait for the qr to end and see the other reports for dups.

It was late and went to bed. As usual couldn’t sleep the night after bug report. I was checking back and forth and in initial phase it was in soft reject, I thought someone else did a good job in report. I still couldn’t sleep since I wanted to know why it was about to get rejected.

At the final review, they accepted it saying the POC made it accepted(probably others didn’t notice the difference in response time). I got the minimum payout $$$ for SSRF since it was a port scan.

Thanks alot for reading. Hope it helped you in some way.

I’m c
