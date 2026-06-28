---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-20_rce-on-a-laravel-private-program.md
original_filename: 2021-02-20_rce-on-a-laravel-private-program.md
title: RCE On A Laravel Private Program
category: documents
detected_topics:
- supply-chain
- command-injection
- rate-limit
- api-security
tags:
- imported
- documents
- supply-chain
- command-injection
- rate-limit
- api-security
language: en
raw_sha256: bb53ed02f9ed040c1114841a4ade8d472fc3c8934287dd62d35e36e8a7eb2b35
text_sha256: 591cfef7652150cf1be2b493549d33d4d8a55340021aacaa6ae15c8a0856f1d6
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# RCE On A Laravel Private Program

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-20_rce-on-a-laravel-private-program.md
- Source Type: markdown
- Detected Topics: supply-chain, command-injection, rate-limit, api-security
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `bb53ed02f9ed040c1114841a4ade8d472fc3c8934287dd62d35e36e8a7eb2b35`
- Text SHA256: `591cfef7652150cf1be2b493549d33d4d8a55340021aacaa6ae15c8a0856f1d6`


## Content

---
title: "RCE On A Laravel Private Program"
page_title: "RCE on a Laravel Private Program - ZDResearch"
url: "https://zdresearch.com/rce-on-a-laravel-private-program/"
final_url: "https://zdresearch.com/rce-on-a-laravel-private-program/"
authors: ["Yashar Shahinzadeh (@YShahinzadeh)"]
bugs: ["RCE"]
publication_date: "2021-02-20"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3877
---

[P Shahinzadeh](https://zdresearch.com/author/pipsh/) __20 Feb 2021 [ __0 Comments](https://zdresearch.com/rce-on-a-laravel-private-program/#respond)

The recent [Laravel CVE](https://nvd.nist.gov/vuln/detail/CVE-2021-3129) enables remote attackers to exploit a RCE flaw in websites using Laravel. I’ve read the [article](https://www.ambionics.io/blog/laravel-debug-rce) about the exploitation procedure using the Ignition library on Laravel.

To get started, I went through our recon database which contains the domains and subdomains of many web applications. We have built this system for bug bounty hunting:

![](https://zdresearch.com/wp-content/uploads/Screen-Shot-2021-02-16-at-8.02.51-PM-1024x255.png)bug bounty database containing domains and assets

There were roughly 526k live assets to filter for Laravel. The methodology is simple, sending out HTTP request to all assets, looking for the Laravel signature to match. [MEG](https://github.com/tomnomnom/meg) is a good tool for fetching lots of URLs. However, we run our tool which is similar to MEG:

![](https://zdresearch.com/wp-content/uploads/image-1-1024x179.png)sending HTTP request to all assets

I run the script using 20 threads, looking for status code 200 and “text/html” content type. The results are saved with the respective responses in separated directories:

![](https://zdresearch.com/wp-content/uploads/Screen-Shot-2021-02-16-at-9.30.36-PM-1024x399.png)

There are many ways to detect Laravel, I went through the following command which found several matches:

![](https://zdresearch.com/wp-content/uploads/image-2-1024x172.png)grep command on the results

I then checked them one by one to see if they have Ignition running.

One interesting case was a private program we had discovered recently. Due to ethical concerns I can’t name the website/company, and as such will redact the names and URLs.

![](https://zdresearch.com/wp-content/uploads/1-redacted-1024x478.png)

First thing I always do is check whether the web app is running on debug mode or not. There are many methods to do so. The one which is convenient for me on Laravel is sending permitted HTTP methods to endpoints ([need more information?](https://laravel.com/docs/8.x/routing)).

So I just changed the POST method to the PUT when sending credentials to the login endpoint and it returned Laravel’s debug error, confirming that the app has debug mode enabled:

![](https://zdresearch.com/wp-content/uploads/2-redacted-1024x635.png)

You can also get Laravel’s version via the debug message, along with PHP and server OS and other extra information from displaying error messages.

![](https://zdresearch.com/wp-content/uploads/3-1.png)

Since the private program’s Laravel version was greater than 6 and it was also running Ignition, I decided to test the exploit and luckily the log file was on the default path and I could exploit it via [this exploit](https://github.com/ambionics/laravel-exploits):

![](https://zdresearch.com/wp-content/uploads/4-redacted.png)

However, if the log file path wasn’t on default location, I would have to brute force to guess the path or try the second method, i.e., talking to PHP-FPM using FTP.
