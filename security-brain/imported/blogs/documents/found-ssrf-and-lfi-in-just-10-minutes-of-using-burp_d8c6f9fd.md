---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-30_found-ssrf-and-lfi-in-just-10-minutes-of-using-burp.md
original_filename: 2023-03-30_found-ssrf-and-lfi-in-just-10-minutes-of-using-burp.md
title: Found SSRF and LFI in Just 10 minutes of using burp!
category: documents
detected_topics:
- ssrf
- command-injection
- path-traversal
- api-security
- cloud-security
tags:
- imported
- documents
- ssrf
- command-injection
- path-traversal
- api-security
- cloud-security
language: en
raw_sha256: d8c6f9fd733d31de0688b6c004e803789bab200e3dfe75923c85a326a574cada
text_sha256: 2518cecf413be535a1e5ea5aa9f17d23544d8a5d684e35c797a14db763086f2b
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Found SSRF and LFI in Just 10 minutes of using burp!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-30_found-ssrf-and-lfi-in-just-10-minutes-of-using-burp.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, path-traversal, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `d8c6f9fd733d31de0688b6c004e803789bab200e3dfe75923c85a326a574cada`
- Text SHA256: `2518cecf413be535a1e5ea5aa9f17d23544d8a5d684e35c797a14db763086f2b`


## Content

---
title: "Found SSRF and LFI in Just 10 minutes of using burp!"
url: "https://xelkomy.medium.com/found-ssrf-and-lfi-in-just-10-minutes-of-using-burp-492fddef3f3e"
authors: ["Khaled Mohamed (@0xElkomy)"]
bugs: ["SSRF", "LFI"]
publication_date: "2023-03-30"
added_date: "2023-03-31"
source: "pentester.land/writeups.json"
original_index: 1322
scraped_via: "browseros"
---

# Found SSRF and LFI in Just 10 minutes of using burp!

Top highlight

Found SSRF and LFI in Just 10 minutes of using burp!
Khaled Mohamed
Follow
4 min read
·
Mar 30, 2023

493

3

Press enter or click to view image in full size
Photo by Maria Teneva on Unsplash — Searching for bugs :)

Hello, and welcome again after about two years from the last published write-up. Here is a new write-up about a simple vulnerability I have got by just the browser and the burp suite.

Summary

At the beginning of the article, I have to say the vulnerability is so sample, but it needs some browsing into your targets, I have got two vulnerabilities in just one parameter named src and this parameter is taken URL as an input.

Requirements

We just need to have the burp suite professional or the community edition. I think it will be enough for testing this vulnerability because we just need to crawl the target with the burp and use the Auto Repeater to test it.

The Story

On the normal days, when I have to do bug bounty, already I have recon script using bash the script run subfinder, amass, assetfinder,httpx , nuclei, ffuf, uncover, notify…etc and after this script finished I do my manual work like creating new burp suite project and preparing my burp with my extensions like AutoRepeater and ActiveScan++,.etc

From three years I have seen an AutoRepeater regex was interesting to me on a medium blog from @Renato Dante and his write-up about the Bug Bounty tip Automating SSRF it was a good write-up but in the last three years I got nothing with this regex in the Renato write up but at least in this year I got a bounty with it.

AutoRepeater Replacement Settings
https?://(www.)?[-a-zA-Z0–9@:%.+~#=]{1,256}.[a-zA-Z0–9()]{1,6}\b([-a-zA-Z0–9()@:%+.~#?&//=]*)

The Above regex is what I have used to get the SSRF, with those steps like below.

1 — Get the alive subdomain from subfinder and send them to httpx

Get Khaled Mohamed’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

2 — Open the burp suite, create a new project and set up your autorepeater with the above regex and settings like the above image.

3 — Use Katana tool by projectdiscvery and use the proxy option and add the burp proxy URL by the default, it will be http://127.0.0.1:8080

4 — Open the subdomain manually by the browser and visit every login page and any page you have seen on the target website you have.

5 — Open the burp again and you will see the catch by the burp suite auto repeater extension, if there are any parameters to take an input like http://google.com it will change to your collab URL you have been replaced with in the autorepeater and if that no response send to your collab you will see that the autorepeater have saved the tested URL in it until you close the burp suite.

One-liner for using subfinder, httpx, katana to send the result to burp proxy:

subfinder -d hackerone.com | httpx -timeout 10 | katana -proxy http://127.0.0.1:8080 -jc -aff 

In my case, I already got a SSRF by it just a low impact because I can’t get anything locally in the vulnerable website because there is an internal WAF block me from accessing the 127.0.0.1 or the AWS internal metadata IP.

Press enter or click to view image in full size
Burp Collaborator

But After some testing and testing multiple vulnerabilities on the same parameter I got LFI by the normal input was this

?src=c%3a%5cwindows%5cwin.ini

And after that, I have got a good deal of information about the targets, but I stop here because I don’t want to get banned from the H1 platform to getting any sensitive information about the internal system without permissions.

And I report it and get $$$$ bounty after an about a week or week and half from reporting it.

Conclusion

I have found a SSRF with help by AutoRepeater burp extension and didn’t get enough impact from SSRF and tried to find another vulnerability on the same parameter and I have found an LFI Vulnerability and accessing the internal file for the server.

Please don’t forget to follow me on Twitter @0xELkomy, please don't hesitate to connect with me if you have anything.
