---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-23_from-broken-link-to-subfolder-takeover-on-bukalapak.md
original_filename: 2019-12-23_from-broken-link-to-subfolder-takeover-on-bukalapak.md
title: From broken link to subfolder takeover on Bukalapak
category: documents
detected_topics:
- xss
- cloud-security
- command-injection
- clickjacking
- api-security
tags:
- imported
- documents
- xss
- cloud-security
- command-injection
- clickjacking
- api-security
language: en
raw_sha256: 9abb5e4dfdc2ee86caa89bcdc2ec27009c6a2533c161b442f14ff99f4b770a37
text_sha256: eb469badff2dda2568c255305b3d81b25d5462d0d882c46d73ef1390c94af410
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# From broken link to subfolder takeover on Bukalapak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-23_from-broken-link-to-subfolder-takeover-on-bukalapak.md
- Source Type: markdown
- Detected Topics: xss, cloud-security, command-injection, clickjacking, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `9abb5e4dfdc2ee86caa89bcdc2ec27009c6a2533c161b442f14ff99f4b770a37`
- Text SHA256: `eb469badff2dda2568c255305b3d81b25d5462d0d882c46d73ef1390c94af410`


## Content

---
title: "From broken link to subfolder takeover on Bukalapak"
page_title: "How Inspect Element lead to Subfolder takeover and Stored XSS on Bukalapak’s website | by accalon | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/from-broken-link-to-sub-folder-takeover-on-bukalapak-3aa985e622c4"
authors: ["wis4nggeni"]
programs: ["Bukalapak"]
bugs: ["AWS misconfiguration"]
publication_date: "2019-12-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4873
scraped_via: "browseros"
---

# From broken link to subfolder takeover on Bukalapak

How Inspect Element lead to Subfolder takeover and Stored XSS on Bukalapak’s website
accalon
Follow
4 min read
·
Dec 23, 2019

255

Tl;dr : a unique high severity misconfiguration I found on Bukalapak website that lead to Subfolder takeover and stored XSS, by only inspecting an HTML element on their webpage. Blocked by login/pay wall? Read for free here : (https://c2a.github.io/Subfolder-takeover-and-Stored-XSS-on-Bukalapak).

…

Greetings.

Bukalapak is one of the biggest online marketplace and “unicorn” startup located in Indonesia. One day when I was taking a break and checking their website to buy something, I noticed that they held a Bug Bounty Program and I think it would be cool if I could carve my name on their lovely “Wall of fame”.

I’m especially interested to look for vulnerability on one of their new feature that is hosted on a specific subdomain, REDACTED.bukalapak.com. Simply because it’s a new feature, so I think it’s more likely that they missed something which could lead to a vulnerability.

Long story short, after some time, I couldn’t find anything interesting beside some minor or very low severity bug like clickjacking with no sensitive action, rate-limiting issue, etc.

But, when I did inspect element on one of the pages to check if my XSS payload fired or not (it’s not, sadly), I found something that catches my eye on the browser console. The page is trying to fetch an image on another subdomain, but failed and return a 404 response printed on the browser console. The URL looks like this:

https://REDACTED.bukalapak.com/img/some-random-text.jpg

Broken link

I got curious and opened the link on a new tab, and surprisingly, i got that beautiful “NoSuchBucket” error page from Amazon S3 along with the bucket name.

Press enter or click to view image in full size
Beautiful…

At this point, I know that takeover is mostly possible, but I’m curious because previously, all the tools related to subdomain takeover scanner that I used can’t detect this. So I strip the URL to find the main address that pointed to the unclaimed Amazon S3 Bucket. I found out that the URL is something like this :

https://REDACTED.bukalapak.com/img/

Turns out that the REDACTED.bukalapak.com is up and well, it host another feature from bukalapak website and work beautifully. That’s why I decided to write this as “subfolder takeover” and not “subdomain takeover” because I took over a subfolder and not a subdomain, although it has the same methodology.

Get accalon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After taking a sip of my coffee, I started the takeover process, i made an Amazon S3 Bucket with the name printed on the error page. When choosing a region, Patrik Hudak on his blog actually have wrote about how to guess the region (he wrote a lot of amazing articles about subdomain takeover, you should read them if you have the time), but considering bukalapak is a product from Indonesia, I decided to just choose the nearest possible region (Asia Pacific), and turns out I was right. Take over is complete, the subfolder is now pointed to my controlled Amazon S3 bucket.

So, what could I achieve by taking over this subfolder?

The first one comes to my mind is stored XSS, i found out that their cookies is set to a wildcard subdomain, so basically they used the same cookies everywhere, XSS to steal session cookies is possible. The second one, because this subfolder is hosted in one of their subdomain, clickjacking is possible on any page with X-Frame Options set to same origin subdomain, which most of the times contain very sensitive actions. I could also host a phishing content too, which if combined with the XSS and clickjacking, could be a very powerful attack vector.

The Popup everyone loves.

But I didn’t exploit further because I’m afraid it’s against their rule, so I decided to report it right away and let them decide the severity.

Surprisingly, their Cyber Incident Responder reply my report within less than half an hour! very cool response time, kudos to their security team. They asked me to upload a specific file to confirm my findings so I do it right away.

Thanks.

Timeline:

August 13 2019: report sent.
August 13 2019 (Less than half an hour later): Cyber incident responder reply my email, asking me to upload a specific file to confirm my findings.
August 14 2019: report validated, categorized as misconfiguration with High severity level.
August 26 2019: they carved my name on their Wall of Fame.
September 24 2019: $$$ paid with a thank you note.
December 23 2019: disclose request approved by security team, write-up published.

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
