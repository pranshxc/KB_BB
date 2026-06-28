---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-03_how-i-got-a-lousyt-shirt-from-the-dutch-government.md
original_filename: 2022-05-03_how-i-got-a-lousyt-shirt-from-the-dutch-government.md
title: How I got a lousyT-Shirt from the Dutch Government.
category: documents
detected_topics:
- command-injection
- otp
tags:
- imported
- documents
- command-injection
- otp
language: en
raw_sha256: d91dd4d0f2f5c344d1a8dbdc1e22ca25bc15d01e5476c63a8a0ee32256bd77e4
text_sha256: 7354270dbfe03af9472fb86414875a5122f39454a1ad26c174cf28c003055962
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: true
---

# How I got a lousyT-Shirt from the Dutch Government.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-03_how-i-got-a-lousyt-shirt-from-the-dutch-government.md
- Source Type: markdown
- Detected Topics: command-injection, otp
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: True
- Raw SHA256: `d91dd4d0f2f5c344d1a8dbdc1e22ca25bc15d01e5476c63a8a0ee32256bd77e4`
- Text SHA256: `7354270dbfe03af9472fb86414875a5122f39454a1ad26c174cf28c003055962`


## Content

---
title: "How I got a lousyT-Shirt from the Dutch Government."
url: "https://maxva.medium.com/how-i-got-a-lousyt-shirt-from-the-dutch-goverment-2a0d13fe7675"
authors: ["Mava (@mava656)"]
programs: ["Dutch Government"]
bugs: ["Old components with known vulnerabilities"]
publication_date: "2022-05-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2671
scraped_via: "browseros"
---

# How I got a lousyT-Shirt from the Dutch Government.

How I got a lousyT-Shirt from the Dutch Government.
Mava
Follow
3 min read
·
May 4, 2022

155

1

Hello everyone,
my name is Max. I’m a Computer Science student and ethical hacker from Germany. Today I want to tell you how I hacked the Dutch Government and got a lousy T-shirt, so hopefully, you can get one yourself.

Dutch Goverment VDP

First, let’s have a look at the VDP of the Dutch Government:
https://www.government.nl/topics/cybercrime/fighting-cybercrime-in-the-netherlands/responsible-disclosure
As this program is not listed on Hackerone or Bugcrowd, this VDP is especially a nice target for beginners, as there is less competition. Furthermore the Scope of this program is really huge. You can have a look at this gist for a curated list of domains that are in scope:
https://gist.github.com/random-robbi/***REDACTED-SUSPECT-TOKEN***You can use this list as a starting point for recon and go from there.

Finding a vulnerability

As I’m a beginner and just starting my way in bug bounty, I was just looking for simple low-hanging fruit vulnerabilities. This is why I was focusing on WordPress! It is an awesome CMS, but in my experience, a lot of WordPress sites are vulnerable, especially if a lot of plugins are used. So to find a valid WordPress installation with some vulnerability, I had two things to do:
1. Find as many domains inside the scope hosting WordPress as possible.
2. Check every found domain, if it has some sort of known vulnerability.

Recon

To find as many WordPress installations as possible, I used two approaches,
Google-Dorking and Nuclei. As the name suggests, Google-Dorking is a technique that utilizes the power of Google’s search engine to gather some information. You can find a lot of helpful Google-Dorks at the Google Hacking Database at:
https://www.exploit-db.com/google-hacking-database
A nice Google-Dork to identify WordPress installations is:

"Proudly powered by WordPress”

This is very useful, if you have a wildcard scope like *.mil from the DoD-VDP, so you can combine them:

site:*.mil "Proudly powered by WordPress”

You can check every domain from the gist like this, for further subdomains hosting WordPress.

Get Mava’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The other approach I used was Nulcei from Project Discovery:
https://github.com/projectdiscovery/nuclei
It’s a nice template-based vulnerability scanner, but you can also use it, to identify WordPress installations from a list of given domains. We can do this by running a command like:

nuclei -l wordpress.subs.txt -t /root/nuclei-templates/technologies/wordpress-detect.yaml
Press enter or click to view image in full size

This method is a lot quicker if you have a given list of domains.
Combining these two methods provides a list of domains hosting WordPress.

Exploitation via WPScan

The tool to check if a given WordPress installation has some vulnerabilities is WPScan:
https://wpscan.com/wordpress-security-scanner
This is a WordPress vulnerability scanner and is free for non-commercial use. You can register a free account to obtain an API-Token. The API Token unlocks the full potential of WPScan, as the tool will check and display possible vulnerabilities. WPScan can be run like:

wpscan --url <domain> --api-token <your API-Token>
Press enter or click to view image in full size

If WPScan displays some vulnerabilities, be sure to manually check if they can be exploited, as a lot of vulnerabilities require for example an Admin account.

I used this approach to identify and report multiple vulnerabilities to the Dutch Government. As a reward, I got a letter and a nice “lousy” T-shirt.

Timeline
Report multiple vulnerabilities at 19.11.2021
Initial response and triaged at 19.11.2021
Fixed and T-shirt awarded at 04.01.2022

I hope you enjoyed my first write-up!
Have a great day and happy Hacking!

Social Media

Twitter: https://twitter.com/mava656
