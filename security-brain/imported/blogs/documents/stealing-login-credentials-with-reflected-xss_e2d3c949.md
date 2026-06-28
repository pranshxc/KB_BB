---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-01_stealing-login-credentials-with-reflected-xss.md
original_filename: 2019-10-01_stealing-login-credentials-with-reflected-xss.md
title: Stealing login credentials with Reflected XSS
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
language: en
raw_sha256: e2d3c949f9b70d9170b36ef41e9ab5d7ba915ef1850a2a2dd8171fe7acba101e
text_sha256: 9b6520983afd65c190575d89cc7569bed712c357d1114c8ee9df72b9e98783ea
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Stealing login credentials with Reflected XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-01_stealing-login-credentials-with-reflected-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `e2d3c949f9b70d9170b36ef41e9ab5d7ba915ef1850a2a2dd8171fe7acba101e`
- Text SHA256: `9b6520983afd65c190575d89cc7569bed712c357d1114c8ee9df72b9e98783ea`


## Content

---
title: "Stealing login credentials with Reflected XSS"
url: "https://medium.com/@mehulcodes/stealing-login-credentials-with-reflected-xss-7cb450bf5710"
authors: ["mehulpanchal007 (@007_sharky)"]
bugs: ["Reflected XSS"]
bounty: "100"
publication_date: "2019-10-01"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5002
scraped_via: "browseros"
---

# Stealing login credentials with Reflected XSS

Stealing login credentials with Reflected XSS
mehulpanchal007
Follow
1 min read
·
Oct 1, 2019

215

Hello Hackers,

This was my first bounty worth $100. I got really exited at the moment the email notification popped-up. Read this write-up to know how I got that bug.

Let’s name the website as www.example.com. I understood that how the application works. After understanding, I logged out of the application and tried to visit the paths that are only available to logged-in users. As soon as I hit the first path in my list, I was redirected to “/login?redirect_to=%2fsettings”.

And Open-redirect vulnerability clicked into my mind and I was successful to get a redirect to https://google.com/ by visiting https://www.example.com/login?redirect_to=https%3A%2f%2fgoogle.com%2f

and logging in to www.example.com

Get mehulpanchal007’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then, I tried to get XSS by visiting https://www.example.com/login?redirect_to=javascript%3Aalert(1) and got that alert popup.

Then I thought why not try to steal login credentials.

So I went for that after a good night sleep. I visited the link:

https://www.example.com%2Flogin%3Fredirect_to%3Djavascript%3Aalert%28document.getElementById%28%2522email%2522%29.value%29%253B%2520alert%28document.getElementById%28%2522password%2522%29.value%29

An Alert popped up for both email and password of victim

So the attack is like, attacker sends email to vicitm including the above URL with javascript such as to send credentials to attack server and the victim clicks the link and bOOOOm…
