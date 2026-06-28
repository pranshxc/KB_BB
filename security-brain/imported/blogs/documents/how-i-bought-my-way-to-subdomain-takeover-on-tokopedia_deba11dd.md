---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-01-20_how-i-bought-my-way-to-subdomain-takeover-on-tokopedia.md
original_filename: 2020-01-20_how-i-bought-my-way-to-subdomain-takeover-on-tokopedia.md
title: How i bought my way to subdomain takeover on Tokopedia
category: documents
detected_topics:
- xss
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- xss
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: deba11dd0ffd000c1c662500c51a886257a78ef1cfe868dc134307bcfab9356e
text_sha256: a48cf2a746612191737904e5822392efb23fc15a831a09d31fe184ddd063d6ed
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How i bought my way to subdomain takeover on Tokopedia

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-01-20_how-i-bought-my-way-to-subdomain-takeover-on-tokopedia.md
- Source Type: markdown
- Detected Topics: xss, command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `deba11dd0ffd000c1c662500c51a886257a78ef1cfe868dc134307bcfab9356e`
- Text SHA256: `a48cf2a746612191737904e5822392efb23fc15a831a09d31fe184ddd063d6ed`


## Content

---
title: "How i bought my way to subdomain takeover on Tokopedia"
page_title: "How i bought a subdomain of Tokopedia’s website (yeah you read it right) | by accalon | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/how-i-bought-my-way-to-subdomain-takeover-on-tokopedia-8c6697c85b4d"
authors: ["wis4nggeni"]
programs: ["Tokopedia"]
bugs: ["Subdomain takeover"]
publication_date: "2020-01-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4823
scraped_via: "browseros"
---

# How i bought my way to subdomain takeover on Tokopedia

How i bought a subdomain of Tokopedia’s website (yeah you read it right)
accalon
Follow
4 min read
·
Jan 20, 2020

282

3

Tl;dr : a subdomain of tokopedia’s website is pointed to an expired Top-Level-Domain available to buy, so obviously I go ahead and buy it. Blocked by login/pay wall? Read for free here : (https://c2a.github.io/How-I-bought-a-subdomain-of-Tokopedia-website).

…

Greetings.

When digging some old emails, i found one of my findings on tokopedia.com, and I decided to make a write-up about it. Tokopedia is one of the few company from Indonesia, that host their own public Bug Bounty Program. You can read the rules and details here: https://github.com/tokopedia/Bug-Bounty.

After reading their rules, I noticed that the targets is mainly set to wildcard domains (*.tokopedia.com and *.tokopedia.net). So i began to enumerate the subdomain using a couple of open source tools like sublist3r, knockpy, massdns, etc.

I found some interesting subdomain where i found some interesting findings too (The forgotten content : information disclosure and reflected XSS on Tokopedia). But the one that catches my eyes is REDACTED.tokopedia.com, because when i access the subdomain, i was getting an ERR_NAME_NOT_RESOLVED error page from my browser.

Using dig command in my terminal, turns out that the CNAME configuration is pointing to another Top Level Domain (REDACTED.com). So REDACTED.tokopedia.com is actually an alias for another different domain which is REDACTED.com.

Surprisingly, when i checked the whois record, the domain is actually expired. So i head straight up to namecheap.com to check if it’s available to buy, and well, it is.

Press enter or click to view image in full size

Here comes the dilemma, I was really broke at that time (seriously), i can’t even afford a domain for $8, PLUS, I’m still not sure whether this subdomain is actually takeover-able or not. I even consider to report this vulnerability without buying the domain, but i don’t think that’s a good proof of concept.

So, decided to take the risk, borrowing $8 from my friend (kudos to Mr. N), then bought the domain.

Get accalon’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After pointing it to a free hosting service, i try to open the subdomain again, and well, i successfully taken over the subdomain because it’s now pointing to my own server.

I decided to make some PoC for stored XSS, but stumble upon a problem because the cookies is set with secure flag, so the site needs to be hosted in https. After i set a free SSL certificate for REDACTED.com, another problem arise, the browser throws a privacy warning, because the site is accessed from REDACTED.tokopedia.com, while the certificate is signed for REDACTED.com.

I got this from stackoverflow, the warning is different but you got the idea.

They won’t allow me to make a *.tokopedia.com SSL certificate since it’s reserved by the company, so i decided to report it right away. We could still steal cookies if the user decided to click ‘proceed to…’ button anyway, so yeah.

Press enter or click to view image in full size

NOTE: If you found a subdomain takeover, i think it’s not wise to show something unnecessary on the front page, the company won’t like it because users could saw it, and it’s bad for their reputations. This report is from my earlier days as a Bug Bounty Hunter, so showing “Subdomain taken over” on front page might not be the best idea. Instead, we could write our PoC on hidden html tag, and maybe showing “Under Maintenance” on the front page. And don’t forget to randomize the file name we hosted on that subdomain so it won’t be accidentally found by users.

Well, the Security Team verified my report, and it’s a valid security bug with High Severity, and they decided to reward me.

Spending 8 bucks for three digits bounty rewards? I see this as an absolute win.

Press enter or click to view image in full size

Thanks.

Timeline:

July 27 2019: Report sent.
July 29 2019: Security team verified the report, valid with High Severity.
July 31 2019: Bug fixed, they asked me to re-test the bug.
November 20 2019: $$$ awarded.

Follow Infosec Write-ups for more such awesome write-ups.

InfoSec Write-ups
A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub…

medium.com
