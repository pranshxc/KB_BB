---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-18_250-for-email-account-enumeration-using-nametomail-tool.md
original_filename: 2022-11-18_250-for-email-account-enumeration-using-nametomail-tool.md
title: $250 for Email account enumeration using “NameToMail” tool
category: documents
detected_topics:
- idor
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- idor
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: 32e8a25d13e1f383f63a3a2a8c528412553f56017b4dab56b242e978afd5395d
text_sha256: ff53abe8daed8e5d6537ceafb914c5d65d82a6e50b5955ed35fccdff446263a6
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# $250 for Email account enumeration using “NameToMail” tool

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-18_250-for-email-account-enumeration-using-nametomail-tool.md
- Source Type: markdown
- Detected Topics: idor, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `32e8a25d13e1f383f63a3a2a8c528412553f56017b4dab56b242e978afd5395d`
- Text SHA256: `ff53abe8daed8e5d6537ceafb914c5d65d82a6e50b5955ed35fccdff446263a6`


## Content

---
title: "$250 for Email account enumeration using “NameToMail” tool"
url: "https://medium.com/@snoopy101/250-for-email-account-enumeration-using-nametomail-tool-cce02a17ade8"
authors: ["snoopy (@snoopy101101)"]
bugs: ["Username enumeration"]
bounty: "250"
publication_date: "2022-11-18"
added_date: "2022-11-21"
source: "pentester.land/writeups.json"
original_index: 1895
scraped_via: "browseros"
---

# $250 for Email account enumeration using “NameToMail” tool

snoopy
 highlighted

$250 for Email account enumeration using “NameToMail” tool
snoopy
Follow
3 min read
·
Nov 18, 2022

445

6

This is the story of the easiest bug I’ve ever found.

Introduction

I was invited to a private program on HackerOne, so I’ll be referring to the site as ‘target.com’, in accordance with certain privacy-related requests.

While I was testing one of their subdomains, the reset-password functionality caught my attention.

Press enter or click to view image in full size

I captured the request with Burp Suite and the response was weird:

Press enter or click to view image in full size

Interesting. Does this mean if I manually input an email, it will produce a different response? Could I potentially just enumerate through all sorts of emails?

To test this, I needed to generate a bunch of emails with a specific company domain name.

name@target.com
firstname-lastname@target.com
FIRSTNAME_Lastname@target.com
test@target.com
dev@target.com

This is far too time-consuming for a Bug Hunter, so what can we do to automate this?

NameToMail
GitHub - ali01imani01/NameToMail: Generate Emails for a company/website from a given list of names.
Generate Emails for a company/website from a given list of names. - GitHub - ali01imani01/NameToMail: Generate Emails…

github.com

Press enter or click to view image in full size

NameToMail generates emails from a list of names in more than 70 different ways. For example, consider a single name — “Charlie Brown”.

charlie-brown@target.com
charlie@target.com
brown@target.com
CHARLIE-BROWN@target.com
CHARLIE@target.com
BROWN@target.com
Charlie-Brown@target.com
Charlie@target.com
Brown@target.com
Charlie-brown@target.com
brown-charlie@target.com
BROWN-CHARLIE@target.com
Brown-Charlie@target.com
Brown-charlie@target.com
c-brown@target.com
charlie-b@target.com
C-BROWN@target.com
CHARLIE-B@target.com
C-brown@target.com
c-BROWN@target.com
c-Brown@target.com
C-Brown@target.com
charlie-B@target.com
CHARLIE-b@target.com
Charlie-B@target.com
Charlie-b@target.com
charlie_brown@target.com
charlie@target.com
brown@target.com
CHARLIE_BROWN@target.com
CHARLIE@target.com
BROWN@target.com
Charlie_Brown@target.com
Charlie@target.com
Brown@target.com
Charlie_brown@target.com
brown_charlie@target.com
BROWN_CHARLIE@target.com
Brown_Charlie@target.com
Brown_charlie@target.com
c_brown@target.com
charlie_b@target.com
C_BROWN@target.com
CHARLIE_B@target.com
C_brown@target.com
c_BROWN@target.com
c_Brown@target.com
C_Brown@target.com
charlie_B@target.com
CHARLIE_b@target.com
Charlie_B@target.com
Charlie_b@target.com
charlie.brown@target.com
charlie@target.com
brown@target.com
CHARLIE.BROWN@target.com
CHARLIE@target.com
BROWN@target.com
Charlie.Brown@target.com
Charlie@target.com
Brown@target.com
Charlie.brown@target.com
brown.charlie@target.com
BROWN.CHARLIE@target.com
Brown.Charlie@target.com
Brown.charlie@target.com
c.brown@target.com
charlie.b@target.com
C.BROWN@target.com
CHARLIE.B@target.com
C.brown@target.com
c.BROWN@target.com
c.Brown@target.com
C.Brown@target.com
charlie.B@target.com
CHARLIE.b@target.com
Charlie.B@target.com
Charlie.b@target.com
Press enter or click to view image in full size
The number of emails which was generated

I wrote this simple script ages ago, and it’s incredibly helpful.

Get snoopy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now all I had to do was finding contacts related to ‘target.com’ which was fairly trivial using various tools such as crunchbase.com or theHarvester.

Press enter or click to view image in full size
Crunchbase

Finally, I ran my script and I found multiple valid emails:

Press enter or click to view image in full size
Valid mail

Notice that the response has been changed.

Bounty:
Press enter or click to view image in full size

According to great James Kettle:

“So far, so simple.”

(HTTP Desync Attacks Request Smuggling Reborn 00:18:07)

The Gray Area is a collection of great cybersecurity and computer science posts. The best articles are highlighted in a weekly newsletter, sent out every Wednesday. To get updates whenever The Gray Area publishes an article, check out our Twitter page, @TGAonMedium.
