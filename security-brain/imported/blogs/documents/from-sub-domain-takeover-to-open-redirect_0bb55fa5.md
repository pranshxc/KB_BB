---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-02_from-sub-domain-takeover-to-open-redirect.md
original_filename: 2019-08-02_from-sub-domain-takeover-to-open-redirect.md
title: From Sub domain Takeover to Open-Redirect
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
raw_sha256: 0bb55fa54ee71669d61711d62e06a85ba8f9a042521ae289188f59ab91101e5a
text_sha256: 4db6034d61b4259fa3994f7a93b1140b364991dbfdd8eb77d66ebd0a0b4aaca7
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# From Sub domain Takeover to Open-Redirect

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-02_from-sub-domain-takeover-to-open-redirect.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `0bb55fa54ee71669d61711d62e06a85ba8f9a042521ae289188f59ab91101e5a`
- Text SHA256: `4db6034d61b4259fa3994f7a93b1140b364991dbfdd8eb77d66ebd0a0b4aaca7`


## Content

---
title: "From Sub domain Takeover to Open-Redirect"
url: "https://medium.com/@aniltom/https-medium-com-aniltom-from-sub-domain-takeover-to-open-redirect-b5be4906e1a4"
authors: ["Anil Tom (mr_4nk)"]
bugs: ["Subdomain takeover", "Open redirect"]
bounty: "150"
publication_date: "2019-08-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5103
scraped_via: "browseros"
---

# From Sub domain Takeover to Open-Redirect

From Sub domain Takeover to Open-Redirect
Anil Tom
Follow
3 min read
·
Aug 2, 2019

262

Hey guys,

I am Anil Tom. Since I haven’t written a blog for a while, I just thought of writing one. Today, I am going to share one of my findings in Bugcrowd Private Bug Bounty Program.

After a long break, I logged in to my Bugcrowd Account and while checking the programs I noticed that there were some pending private program invitations. On further checking, one program grabbed my attention. So I selected that program and checked its scope. There were around SIX Domains in scope for that program, so I started opening each website.

While checking, I found that one website was greeted by this Godaddy web page

Press enter or click to view image in full size

When I saw this page I was like “heyyyyy!!! Sub Domain Takeover.”

But when I checked it further and saw this

Press enter or click to view image in full size

It was not expired :( the sub domain takeover was not possible

And as I was closing the tab, suddenly my mind said, why not try recon on this website. So I checked Domain Name Registration Data Lookup using https://lookup.icann.org/lookup and discovered that it was owned by the company itself. So I ran dirsearch against the domain but I could not find anything.

Get Anil Tom’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then I checked whether this web site was Vulnerable for Open-Redirect ?

What is Open-Redirect Vulnerability?

Open-Redirect is basically is not a high impact vulnerability , A web application accepts a user-controlled input that specifies a link to an external site, and uses that link in a Redirect. This simplifies phishing attacks.
Open redirection is listed in the OWASP Top 10 for 2013 and 2010 (10th position in both lists) since it is still an active threat in modern web applications. Open redirection occurs when a vulnerable web page is redirected to an untrusted and malicious page that may compromise the user. Open redirection attacks usually come with a phishing attack because the modified vulnerable link is identical to the original site, which increases the likelihood of success for the phishing attack.

The target let’s just say it was named redact.com. I changed the URL to https://redact.com//google.co.in/ and executed it and as expected I got a redirect to https://google.com

Then I made a PoC video and reported it to the Team

Press enter or click to view image in full size

Timeline

Initial Report: 16 Jul 2019 , 12:45 am

Triaged : 17 Jul 2019 , 2:56 AM

Fixed: 17 Jul 2019, 3:06 AM

Bounty Awarded: 17 Jul 2019, 3:08 AM (150$)

Thanks for reading my writeup. I hope you enjoyed it.

wanna connect

Facebook : Anil Tom

Linkedin : Anil Tom
