---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-17_strange-admin-panel-bypass-story-bug-bounty.md
original_filename: 2021-01-17_strange-admin-panel-bypass-story-bug-bounty.md
title: Strange Admin Panel Bypass Story | | Bug Bounty
category: documents
detected_topics:
- sqli
- command-injection
- api-security
tags:
- imported
- documents
- sqli
- command-injection
- api-security
language: en
raw_sha256: 9c589d9e3ae4c2c8815665753bab95e55b022889d96f9254bbf4ef2f9290141d
text_sha256: f930a1a51a7b80ec5a7e4bec383c6172fb3263a096fd51bdb5f94be2ccda8058
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# Strange Admin Panel Bypass Story | | Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-17_strange-admin-panel-bypass-story-bug-bounty.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `9c589d9e3ae4c2c8815665753bab95e55b022889d96f9254bbf4ef2f9290141d`
- Text SHA256: `f930a1a51a7b80ec5a7e4bec383c6172fb3263a096fd51bdb5f94be2ccda8058`


## Content

---
title: "Strange Admin Panel Bypass Story | | Bug Bounty"
url: "https://geekboyranjeet.medium.com/strange-admin-panel-bypass-story-bug-bounty-5e618099baaf"
authors: ["Ranjeet Kumar Singh (@geekboyranjeet)"]
bugs: ["Authentication bypass", "Account takeover"]
publication_date: "2021-01-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3988
scraped_via: "browseros"
---

# Strange Admin Panel Bypass Story | | Bug Bounty

Top highlight

Strange Admin Panel Bypass Story | | Bug Bounty
Ranjeet Kumar Singh
Follow
3 min read
·
Jan 17, 2021

600

4

Hello Friends, My name is Ranjeet Singh and currently I am pursuing B-Tech from LPU and a part time bug hunter. I am doing bug hunting from past 3 years & I am still noob so if I will do some mistake then please notify me so I can correct it. So without wasting time lets get into the point.

WELCOME

One of my friend has given this private site so lets call that domain as :<redacted>.com

So the target has vast scope i.e *.redacted.com . So I started recon. because without recon we don’t get to know how things are working , developers mindset and lots of interesting subdomains etc.

This is the steps how I recon. Basically I use my own private tool for recon but I am going to explain how I have created this tool using some public tools.If you know bash scripting then you can easily create your own tool using this methodology.

My recon starts with like first I gather subdomain using Amass, Asstefinder then send subdomains to httprobe for checking which is alive and then I check for open ports using nmap then at last I take screenshot using eyewitness.

So after recon I start with checking screenshot that we have taken during recon process. So I have discovered lots of admin panel but I don’t know weather I was able to bypass or not so on 1 day I have checked main app. and checked each functionalities + endpoints of that app but I haven’t found anything interesting. Then on 2 day I was like lets try some sqli payloads on admin panel but here too I haven’t found any sqli.

So Sad :(

Then I started visiting each admin panel & checking js files in hope that I will found something interesting .But again I haven’t found anything interesting.

Get Ranjeet Kumar Singh’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So one by one I have picked each subdomain and see how it looks like when I have first visited to this subdomain.redacted.com . It was asking for username and password for login.

Press enter or click to view image in full size

So I started fuzzing for directories,any js files and I have found one endpoint and that endpoint has redirected me to another endpoint and the interface was like this :)

Press enter or click to view image in full size

I was like w00woo !! because this is the first time I have found something like this from past 3 years.

After that I have used google, github search and from every where I have collected ton’s of emails of that ‘@redacted.com’ . And again started brute forcing email parameter and approx 3–5 has shown 2xx response and other has shown 4xx response. So I have tried to login using that 2xx response email addresses and ya I was into the admin panel :) Then I have reported this and after 4–5 days they have patched and rewarded me with $$$$ 😎

At last I want to say few things :

Everything depends on observation and it was not like if you are not finding p1-p2 then you are not good.Everyone is good at his own level.So instead of demotivating keep trying until you find something interesting.May be sometime you report will get dup. but still try to find something more interesting that older one.

Work Hard

Hope you have enjoyed this :)

Stay Safe & Happy !!
Thank You
