---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-12_a-tale-of-open-redirection-to-stored-xss.md
original_filename: 2022-03-12_a-tale-of-open-redirection-to-stored-xss.md
title: A Tale of Open Redirection to Stored XSS
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 2b0118dfc07efa5ae8390cedb39147a7ca5e8d7c63ab572104f3c5702e9e7a49
text_sha256: a73aacab086b53179355c65d47a1b634f83676394208f192b38d1711c43a0cab
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# A Tale of Open Redirection to Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-12_a-tale-of-open-redirection-to-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `2b0118dfc07efa5ae8390cedb39147a7ca5e8d7c63ab572104f3c5702e9e7a49`
- Text SHA256: `a73aacab086b53179355c65d47a1b634f83676394208f192b38d1711c43a0cab`


## Content

---
title: "A Tale of Open Redirection to Stored XSS"
url: "https://medium.com/@tushar.tilak.sharma/a-tale-of-open-redirection-to-stored-xss-6ad426ae9d43"
authors: ["Tushar Sharma (@tusharSharma_0)"]
bugs: ["Stored XSS", "Open redirect"]
publication_date: "2022-03-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2829
scraped_via: "browseros"
---

# A Tale of Open Redirection to Stored XSS

Top highlight

A Tale of Open Redirection to Stored XSS
Tushar Sharma
Follow
2 min read
·
Mar 12, 2022

136

1

Hello guys,

I am back with another write-up of an interesting vulnerability I came across.

I will make this write-up short and easy to understand.

During hunting on a Private BB program(which I found through these dorks: https://github.com/tushar-arch/Bug-Bounty-Dorks). I came up with the main login page where I found out Open Redirection using the

payload: target. com/<>//google.com and it successfully redirected me to google.com, to escalate the impact I tried RXSS on it.

Payload: https://target.com/<>javascript:alert(1);

and I got a beautiful Popup :).

If you are thinking about how I ended up using this payload, I took reference from this report: https://hackerone.com/reports/196846 ( I always keep this payload in my Arsenal).

Now I immediately made a report and sent it to the security team.

I want to tell you guys that my target website is a marketplace for pictures/wallpapers and more. and I can make a Public profile where I can list pictures and other arts.

After reporting this issue I started looking for other vulnerabilities and came across a functionality where on Public profile we can add our social media handle links.

So I added different payloads in the inputs that will be saved to my public profile but nothing happened.

Get Tushar Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So if I add <script>alert(1)</script> in the input of twitter handle.

Then on clicking on the Twitter handle(which is present on my Public profile) the user will be redirected to https://<script>alert(1)</script>.

So You know what I am thinking !! Right??

I saved this payload on my Twitter handle input: https://target.com/<>javascript:alert(1); .

So whenever someone clicks on my Twitter handle ( Present on my profile page) he will be redirected to this URL which is vulnerable to Reflected XSS.

Both Authenticated and Unauthenticated are vulnerable to this vulnerability and as an attacker, I can steal the cookies.

So, In the same thread of Email, I updated the report. Which got accepted within 2 days and the Team is working on the Fix. I am expecting $$$$ for it .

Hope you liked it !!!

Thank you

Follow me on:

Twitter: https://twitter.com/tusharSharma_0

Linkedin: https://www.linkedin.com/in/tushar-sharma-8557a716b/
