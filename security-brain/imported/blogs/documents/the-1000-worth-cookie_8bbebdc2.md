---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-19_the-1000-worth-cookie.md
original_filename: 2020-07-19_the-1000-worth-cookie.md
title: The $1,000 worth cookie
category: documents
detected_topics:
- xss
- command-injection
- rate-limit
- csrf
- api-security
tags:
- imported
- documents
- xss
- command-injection
- rate-limit
- csrf
- api-security
language: en
raw_sha256: 8bbebdc28f32565737e44a21f6b6c5a4476d348bc0c86cc88a7b26288bf51d8f
text_sha256: 2b46d8a0bd8a8a1c157183d476bb6eb79fe63636f7d3d1c4eba2a395cfafae01
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# The $1,000 worth cookie

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-19_the-1000-worth-cookie.md
- Source Type: markdown
- Detected Topics: xss, command-injection, rate-limit, csrf, api-security
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `8bbebdc28f32565737e44a21f6b6c5a4476d348bc0c86cc88a7b26288bf51d8f`
- Text SHA256: `2b46d8a0bd8a8a1c157183d476bb6eb79fe63636f7d3d1c4eba2a395cfafae01`


## Content

---
title: "The $1,000 worth cookie"
url: "https://medium.com/bugbountywriteup/the-1-000-worth-cookie-6cf48af08e08"
authors: ["Jadek Mark (@mase289)"]
programs: ["Mail.ru"]
bugs: ["XSS"]
bounty: "1,000"
publication_date: "2020-07-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4395
scraped_via: "browseros"
---

# The $1,000 worth cookie

The $1,000 worth cookie
Mase289
Follow
4 min read
·
Jul 20, 2020

362

1

A story of DOM XSS in Mail.ru

It wasn’t till a year of joining the HackerOne platform that I actively started hunting for bugs. At the time, I was completely new to the various server and client-side bug classes that were being reported daily to programs on the platform. Amongst the vulnerabilities being disclosed at the time, Cross-Site Scripting, commonly known as XSS seemed like a very popular one that a lot of hunters were going for. So when I set out to find a cross site scripting vulnerability in the top-level domain of Russia’s biggest Internet company, little could I have known that my beginner’s luck would enable me to discover a vulnerable header parameter within minutes of searching and score me my first bounty in the process.

Finding the vulnerable parameter.

I was playing with requests and observing their responses in burpsuite while browsing https://mail.ru. In order to find hidden parameters, I use this helpful extension known as param miner (https://portswigger.net/bappstore/17d2949a985c4b7ca092728dba871943) authored by James ‘albinowax’ Kettle of PortSwigger Web Security. Looking through the issue’s tab in burpsuite revealed some parameters that the extension had brute-forced and found to be valid. One of these was a cookie HTTP request header called “gp”. This one was of particular interest because its value got reflected in the response to any request containing it thereby making it a potential candidate for XSS.

Verifying the XSS vulnerability.

One useful tip while testing for reflected XSS is to throw dangerous characters at the vulnerable parameter one at a time in order to determine which characters are being filtered out by the Web Application Firewall if present. Once you know which characters are filtered out and which are accepted, you are in a better position to craft a payload which will bypass the WAF. Luckily, that wasn’t the case with the application I was testing. Being the noob I was at the time, I did not understand the concept of context in relation to cross site scripting vulnerabilities. I tried to test the Cookie parameter by inserting the following payload into its value.

<script>alert(document.cookie)</script>

I clicked the response in burpsuite, selected “Show response in browser”, and then loaded the generated link in Firefox. I gave it a few seconds to load but once it did, there was no popup with an alert box revealing my cookies . I tried a couple of variations on my payload for about an hour longer before I decided to retire for the day having posted my issue on a Facebook bug bounty forum to try and seek help.

This is what the request and response looked like

GET / HTTP/1.1 
Host: mail.ru 
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0 
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8 Accept-Language: en-US,en;q=0.5 Accept-Encoding: gzip, deflate Cookie: gp= some alpha numeric string; 
Connection: close 
Upgrade-Insecure-Requests: 1 
Cache-Control: max-age=0
200 OK
</script><script id="script:globals">var mr={:{BUILD:"307ad21",VERSION:1566410797,TIMESTAMP:1567848214281,TIMESTAMP_LOCAL: Date.now(),TIMEZONE:10800,AUTH:!1,CITY:"Кампала",REGION_ID:233, PAGE_ID: "15678651219031568689886875",ACC_CNT: false,MEDIA_ORDER:"regional,regional,auto,auto,lady,lady,deti,deti,health,health,sport,sport,cinema,cinema,hitech,hitech,games,games",INCUT_ORDER:"incut,stub",WIDGET_ORDER:"horo,tv,torg",FEATURE_ORDER:"auto,lady,sport,cinema,hitech,games",TARGET:"default",SITEZONE:15,SITEID:169,DEVICE:"desktop",BROWSER:"Firefox",PLATFORM:"Linux",REGION_LEVEL_ID:188,GP:"Payload gets reflected here ;",CSRF:"3b021e69c3bf49fe900037b18fc581be",MANUAL_REGION_NOT_RUSSIA:true,HONEYPOT: '.gridmain-col .tgb, .grid .grid_main-col

I got back to testing the next day when suddenly it occurred to me that I had to close the initial script tag then introduce a new tag. I quickly modified my payload to </script><script>alert(document.domain)</script>

Get Mase289’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

fired the request and observed it get properly reflected in the response.

Press enter or click to view image in full size

Loading the response in the browser finally popped the alert box and the domain upon which the XSS had been triggered on for the above payload.

Press enter or click to view image in full size
Output for payload revealing user’s cookies
Press enter or click to view image in full size

I reported this to Mail.ru and was somewhat skeptical about it being rewarded since it appeared to be a self-XSS issue at best. However, my hopes were raised after reading up on a couple of reports where bug bounty hunters had demonstrated to Mail.ru that the Man-in-the-middle attack vector could be used to deliver attacks to legitimate user’s- taking advantage of vulnerable cookie parameters in their website infrastructure. I have included a link for further reading at the end of this writeup.

Timeline:

September 7, 2019 — Reported.

September 8, 2019 — Triaged.

September 26th,2019 — Bounty awarded

September 27th,2019 — Issue Fixed

Link to my HackerOne report https://hackerone.com/reports/690072

For further reading please check the following informative medium story from 
Max
:

Сookie-based XSS exploitation | $2300 Bug Bounty story
For quite a long time I have been hunting for vulnerabilities on the HackerOne platform, allocating a certain amount of…

medium.com
