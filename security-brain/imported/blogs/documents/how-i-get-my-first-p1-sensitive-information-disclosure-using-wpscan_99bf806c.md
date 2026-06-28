---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-26_how-i-get-my-first-p1-sensitive-information-disclosure-using-wpscan.md
original_filename: 2020-02-26_how-i-get-my-first-p1-sensitive-information-disclosure-using-wpscan.md
title: How I Get my first P1 (Sensitive Information Disclosure) using WPScan
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
language: en
raw_sha256: 99bf806ce48124235e320244551d6add68027a4c18b3de89c11a90e3c49dc932
text_sha256: d074c852031b0f08976bad1655d646e13c3f87daf45f4f5c2a63a1905d7c0d59
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I Get my first P1 (Sensitive Information Disclosure) using WPScan

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-26_how-i-get-my-first-p1-sensitive-information-disclosure-using-wpscan.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `99bf806ce48124235e320244551d6add68027a4c18b3de89c11a90e3c49dc932`
- Text SHA256: `d074c852031b0f08976bad1655d646e13c3f87daf45f4f5c2a63a1905d7c0d59`


## Content

---
title: "How I Get my first P1 (Sensitive Information Disclosure) using WPScan"
url: "https://medium.com/@harrmahar/how-i-get-my-first-p1-sensitive-information-disclosure-using-wpscan-c2fba00ac361"
authors: ["Harrmahar (@harrmahar)"]
bugs: ["Information disclosure"]
publication_date: "2020-02-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4752
scraped_via: "browseros"
---

# How I Get my first P1 (Sensitive Information Disclosure) using WPScan

Top highlight

How I Get my first P1 (Sensitive Information Disclosure) using WPScan
Harrmahar
Follow
3 min read
·
Feb 26, 2020

603

2

بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ

Background

Hello,

I was started to do bug hunting on October 2019. I spent almost 4 months to learning on common vulneralibility and focusing on how to do Recon. Until I found my first P1 with using basic recon technique. In this article, I would like to share with you about my very first P1, hope you like it, enjoy!

Press enter or click to view image in full size
P1 Resolved Submission on Bugcrowd
Reconnaissance Phase

I was invited to a Private Program on Bugcrowd with a huge in-scope target (wildcard). So the first step to do is finding all the subdomains. I used crtsh combined with httpprobe (By Tomnomnom), run this command on my VPS:

curl -s https://crt.sh/\?q\=\%.$1\&output\=json | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | httprobe | tee -a ./alive.txt

This command is about :

curl -> searching the target domain on crt.sh and save the output to json
jq & sed -> slicing and filtering the output, so we got only the domains;
sort -> eliminating duplicate domains;
httprobe -> check that the subdomains is active or not;
tee -> breaks the output from httprobe to two part , so it would be displayed on terminal and also write on to the output file.

Btw, did I type that very long command every time I do recon ? Absolutely No. I use .bash_profile to do this by shortcut, I learn to using this by Youtube video of 
Behrouz Sadeghipour
 on https://www.youtube.com/watch?v=YhUiAH5SIqk . Thanks Nahamsec!

Get Harrmahar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I also got that command from Nahamsec’s recon_profile . Thanks again Nahamsec! :D

Check all the subdomains

I’m a GUI-guy, so after I get all the subdomains, what I do is check one by one the subdomains. Open it in the browser, and see what features in there. But, there is no way I can do it one by one, copy the url one by one, paste it into the browser, wait until the page is fully loaded. It’s very wasting time bro. So I use these very helpful extensions on Firefox (also available on Chrome):

Open Multiple URLs (We can open multiple url in just one click)
Open Multiple URLs
Opens a list of URLs and optionally extracts URLs from text. Source Code…

chrome.google.com

2. Wappalyer (Tells us about what technologies are use on the website : CMS, Web Server, Database, Programming Language, etc.)

Wappalyzer - Identify technologies on websites
Find out what technology a website is built with. Identify technologies in bulk with the Lookup API. No applications…

www.wappalyzer.com

For all the subdomain I got, usually I open 20–30 subdomains in one click, so my computer did not process too much. And then I check it one by one.

Press enter or click to view image in full size
Open Multiple URLs Extension

By using this technique, I found that more than 50% of the subdomains is using wordpress (including the main domain). Without thinking too much, I try to wpscan the main domain first.

Output from Wappalyzer
WPscan Finding

After waiting for the wpscan be done, I found a very interesting alert. It say that wp-config backup file (wp-config.php.bak) was found! So I try to access it from URL, like https://redacted.com/wp-config.php.bak . Boom! Found db_name, db_password, and other sensitive information!

Press enter or click to view image in full size
wp-config file

Resolved after 2 days.

Awarded with 40 points!

Thats all, thanks for read this write up!

Regards, Harrmahar.

Credits
Behrouz Sadeghipour
 (Thanks for bash_profile, and live recon + all amazing videos on Youtube! )
YoKo Kho
 (Thanks for the Bug Hunting 101 book and all the tips you gave to me!)
Crt.sh
TomNomNom
 ‘s httprobe
Open Multiple URLs extension on Chrome and Firefox
Wappalyzer
