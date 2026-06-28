---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-12_blind-ssrf-in-url-validator.md
original_filename: 2021-08-12_blind-ssrf-in-url-validator.md
title: Blind SSRF in URL Validator
category: documents
detected_topics:
- ssrf
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- ssrf
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 6a87dd35493296af77c657963f03882383cf8122b4d5588c70c08c92d07fde29
text_sha256: 0513926bdc9bfa130cf3f1c090339c964dbb0c7b85e26400b7cdcbc59b8880f1
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Blind SSRF in URL Validator

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-12_blind-ssrf-in-url-validator.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `6a87dd35493296af77c657963f03882383cf8122b4d5588c70c08c92d07fde29`
- Text SHA256: `0513926bdc9bfa130cf3f1c090339c964dbb0c7b85e26400b7cdcbc59b8880f1`


## Content

---
title: "Blind SSRF in URL Validator"
url: "https://yasshk.medium.com/blind-ssrf-in-url-validator-93cbe7521c68"
authors: ["Yash Kandekar (@Neutron__)"]
bugs: ["Blind SSRF"]
publication_date: "2021-08-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3425
scraped_via: "browseros"
---

# Blind SSRF in URL Validator

Blind SSRF in URL Validator
Yash Kandekar
Follow
3 min read
·
Aug 12, 2021

548

3

Introduction :

Hello Amazing Hackers! I’m Yash Kandekar, and In this blog I’ll be sharing an Interesting bug which led me to my first paid Blind SSRF :)

I will try my best to make this Blog as Fun and Interesting as possible! So let’s get started !

The Story starts from me Testing on a program to find any “Valid” bugs, but unfortunately couldn’t find any as the Program was already tested Heavily by many good hackers (The Usual story). But this program was relying on APIs and as you know, APIs aren’t always 100% properly configured!

Let’s call our Target as cheems.com as I cannot disclose the Real Target’s name.

Press enter or click to view image in full size
http://cheems.com is our Target
URL Validator:

The Application had a Feature to Post anything on your Feed. Here you can Introduce any browse-able Links as well. Think of Twitter , where you can paste a link in your post, and twitter makes an Interaction with that link to Validate it ? Same situation was here but with HTTP interaction!

The API will make a request to that link (to validate it) :

POST /api/validate
Host : cheems.com
<Other Headers>
url=http://ourlink.example.com

This is an Intended Feature and not a Bug.

The Problem:

We couldn’t just use localhost or 127.0.0.1 or 169.254.169.254 right in the url section and hope for a positive reply from cheems.com :(

I used a Lot of Payloads, different encodings of 169.254.169.254 for nearly 1–2 hours, but no Positive response from server. Also, using payloads like 0.0.0.0:25 (for port scanning) was not working .

The Solution :D

After Roaming around the Infosec internet for a relevant resource, I found this recent Gem Report from SirLeeroyJenkins

Get Yash Kandekar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This Included an Attacker server which will be hosting a script (PHP for example), which will redirect the Incoming requests to another destination. We can setup our own server using Ngrok and PHP.

Actual Blind SSRF :

This is how we will reproduce the Issue :

Prepare a PHP script “redir.php” which will redirect the incoming requests

<?php header("Location: <http://127.0.0.1:443>");?>
Setup Ngrok and PHP on your side :

Note that both commands are executed at same path.

a) $ ngrok http 80 #This will start our ngrok server

b) $ PHP -S 127.0.0.1:80 #This will let the php script execute, once requests are received.

2.Navigate to cheems.com and add our ngrok URL with script path:

POST /api/validate
 Host : cheems.com
 <Other Headers>

 url=http://uniqid.ngrok.io/script.php

3. Forward the request, notice the port we included in our script, it is ‘443’. This will return Noticeably faster response. As cheems.com will first visit http://uniq.ngrok.io.script.php and then redirect to itself, since 443 was open port it results in faster response.

Press enter or click to view image in full size
requesting a Valid port

4. Now just change the port from 443 to something potentially inactive like ‘54321’. Once we send the request, it will return a Delayed response, because cheems.com will be searching for this port and will try to make a connection (but fails, miserably).

Press enter or click to view image in full size

I tried to increase the impact, like switching the protocol to gopher, but cheems.com was protected with various filters.

And that’s how Folks, I managed to mark my first paid Blind SSRF from a heavily tested application.

There is no Secret sauce, as the wise zseano says, stick to one program, you will eventually find something interesting !

Till then, Stay safe and do Hunting Baazi !

Thank you for Reading till here .
