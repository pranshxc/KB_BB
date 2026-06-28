---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-23_how-i-get-10-sqli-and-30-xss-via-automation-tool.md
original_filename: 2022-11-23_how-i-get-10-sqli-and-30-xss-via-automation-tool.md
title: How I get +10 SQLi and +30 XSS via Automation Tool
category: documents
detected_topics:
- sqli
- ssrf
- xss
- command-injection
- otp
- automation-abuse
tags:
- imported
- documents
- sqli
- ssrf
- xss
- command-injection
- otp
- automation-abuse
language: en
raw_sha256: 5c5abfc3aece1c1d964e68bdf97a66a05c7478eea541ecb8c2083a46cda6f07e
text_sha256: 6af4bab6e91fdc31c9573ce548a0561d2927cb38706c1951eebe4e6e0c7f4f42
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# How I get +10 SQLi and +30 XSS via Automation Tool

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-23_how-i-get-10-sqli-and-30-xss-via-automation-tool.md
- Source Type: markdown
- Detected Topics: sqli, ssrf, xss, command-injection, otp, automation-abuse
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `5c5abfc3aece1c1d964e68bdf97a66a05c7478eea541ecb8c2083a46cda6f07e`
- Text SHA256: `6af4bab6e91fdc31c9573ce548a0561d2927cb38706c1951eebe4e6e0c7f4f42`


## Content

---
title: "How I get +10 SQLi and +30 XSS via Automation Tool"
url: "https://medium.com/@0xelkot/how-i-get-10-sqli-and-30-xss-via-automation-tool-cebbd9104479"
authors: ["Mahmoud Attia (@0xElkot)"]
bugs: ["SQL injection", "XSS"]
publication_date: "2022-11-23"
added_date: "2022-11-25"
source: "pentester.land/writeups.json"
original_index: 1872
scraped_via: "browseros"
---

# How I get +10 SQLi and +30 XSS via Automation Tool

0xElkot
 highlighted

1

0xElkot
Follow
3 min read
·
Nov 24, 2022

1.2K

11

1

How I get +10 SQLi and +30 XSS via Automation Tool

Hello all, My name is Mahmoud Attia aka 0xelkot

This is a short story about how to automate your recon stuff and get more vulnerabilities.

Everyone doing the same circle story with any changing,

Find Subdomains.
Get alive subs.
Nuclei all alive subs.
Get Dublicates!!

So what we will do then ??!!

Think Out of The Box

There are a lot of tools testing Generic vulnerabilities and get a wonderful results.

One of this tools is xray, This is a fantastic tool to test Generic vulnerabilities with a crawler built-in with it.

This is some results from it.

Press enter or click to view image in full size

So this is an Interesting adventure, Let’s make a script to automate all of it to test some bug bounty programs.

Firstly making a nice recon results to find subdomainds

Tools:

Subfinder

Assetfinder

Amass

github-subdomains

Get 0xElkot’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Sublist3r

subfinder -d $1 -silent | anew /root/$1/subs.txt

assetfinder -subs-only $1 | anew /root/$1/subs.txt

amass enum -passive -d $1 | anew /root/$1/subs.txt

python sublist3r.py -d $1| anew /root/$1/subs.txt

github-subdomains -t <github token> -d $1 | anew /root/$1/subs.txt

Then checking open ports and get live hosts

naabu

httpx

cat /root/$1/subs.txt | naabu -p — -silent | anew open-ports.txt

cat open-ports.txt | httpx -silent | anew alive.txt

Finally checking vulnerabilities

here we have two types of vulnerabilities:

1- CVEs and Misconfigurations .

2- Generic Vulnerabilities.

Everyone can find CVEs via Nuclei , but you can make your Own templates or use the others templates NOT only project discovery templates.

Cent is a tool collect all templates of nuclei from others Repos on GitHub and make it in one repo to test all nuclei templates on GitHub and validate all results later, So you will get an amazing results.

cat alive.txt | nuclei -t /path/to/cent/ -es info | anew nuclei-results.txt

Xray crawl every host and test generic vulnerabilities for all params on URL and Body request.

for i in $(cat /root/$1/alive.txt); do xray_linux_amd64 ws — basic-crawler $i — plugins xss,sqldet,xxe,ssrf,cmd-injection,path-traversal — ho $(date +”%T”).html ; done

Now, You can automate bug hunting process and be focus in something else.

This is the script from Github

For any question you can DM me at twitter 0xElkot

See y’all next time till then.

Happy Hacking ❤
