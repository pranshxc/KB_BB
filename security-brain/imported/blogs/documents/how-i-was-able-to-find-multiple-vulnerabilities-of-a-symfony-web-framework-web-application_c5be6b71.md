---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-01-23_how-i-was-able-to-find-multiple-vulnerabilities-of-a-symfony-web-framework-web-a.md
original_filename: 2022-01-23_how-i-was-able-to-find-multiple-vulnerabilities-of-a-symfony-web-framework-web-a.md
title: How I was able to find multiple vulnerabilities of a Symfony Web Framework
  web application
category: documents
detected_topics:
- command-injection
- otp
- information-disclosure
- api-security
tags:
- imported
- documents
- command-injection
- otp
- information-disclosure
- api-security
language: en
raw_sha256: c5be6b71a6950041a94fa0d8e0f93df813c36b97fafd7d36c9c7229ccacc36f8
text_sha256: 72c90cc006cf300f2c5cedd1edd4455b2f5b318917a901adffb9191f09e2f63f
ingested_at: '2026-06-28T07:32:09Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to find multiple vulnerabilities of a Symfony Web Framework web application

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-01-23_how-i-was-able-to-find-multiple-vulnerabilities-of-a-symfony-web-framework-web-a.md
- Source Type: markdown
- Detected Topics: command-injection, otp, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:09Z
- Redactions Applied: False
- Raw SHA256: `c5be6b71a6950041a94fa0d8e0f93df813c36b97fafd7d36c9c7229ccacc36f8`
- Text SHA256: `72c90cc006cf300f2c5cedd1edd4455b2f5b318917a901adffb9191f09e2f63f`


## Content

---
title: "How I was able to find multiple vulnerabilities of a Symfony Web Framework web application"
url: "https://infosecwriteups.com/how-i-was-able-to-find-multiple-vulnerabilities-of-a-symfony-web-framework-web-application-2b82cd5de144"
authors: ["Abid Ahmad (@RootIntrud3r)"]
bugs: ["Debug mode enabled", "Information disclosure"]
publication_date: "2022-01-23"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2989
scraped_via: "browseros"
---

# How I was able to find multiple vulnerabilities of a Symfony Web Framework web application

How I was able to find multiple vulnerabilities of a Symfony Web Framework web application
Found high severity vulnerability in 5 minutes just from reconnaissance. Found multiple vulnerabilities on a web application that used the Symfony web framework, enabled Symfony profiler/debug mode.
Abid Ahmad
Follow
4 min read
·
Jan 23, 2022

296

2

bi-smi llāhi r-raḥmāni r-raḥīmi (In the name of Allah, most gracious and most merciful)

Hello! beautiful people,

I’m Abid Ahmad, Cyber Security Student & Ethical Hacker. Today I’ll explain how I found multiple vulnerabilities on a web application that used the Symfony Web Framework where Symfony profiler/debug mode was enabled.

Understanding Symfony Profiler & Debug component

Symfony web framework has a feature called Symfony Profiler. This profiler component can only be used when the debug mode is enabled. Here is the twist. The Symfony web framework is much more secure, but enabling debug mode will make this framework extremely vulnerable. The symfony web profiler component exposes sensitive information of the web application that attackers can abuse.

Then why do developers enable Debug Component?

The Debug component provides tools to ease debugging PHP code. It offers several tools to help debugging PHP code. This component helps developer a lot in the development stage. Symfony provides three environments by default called dev, test, and prod (production). Symfony highly recommends disabling profiler tools in the production environment. But sometimes, developers forget about it and make the web application vulnerable.

How I found vulnerabilities (Step by step)

Let’s assume the target site is https://redacted.com. I have found this vulnerability on a subdomain of the target (https://sub.redacted.com).

At
first, I browsed the subdomain and checked what web technologies were used. Using the Wappalyzer addon, I discovered https://sub.redacted.com used the “Symfony” web framework.

‎

Then I proceed to the asset discovery phase. Initially, I tried to fuzz directories using FFUF. I have found an interesting file which is “app_dev.php”. It indicates there might be Debug mode for Symfony is enabled.

Press enter or click to view image in full size

‎

Get Abid Ahmad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Let’s check it on the browser. Whenever I browsed “https://sub.redacted.com/app_dev.php”, found debug mode is enabled and got a profiler token to access Symfony Profiler. Also, I got the phpinfo file location.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

‎

Until now, the severity of my finding is Medium. I knew Symfony Debug toolbars allow reading files that could expose sensitive information. So, I tried to dig more to increase the severity. Then I researched some articles and read Symfony web framework documentation. I found Symfony version 3.4 database default configuration file location, which is app/config/parameters.yml

Press enter or click to view image in full size
Symfony version 3.4 configuration documentation (https://symfony.com/doc/3.4/best_practices/configuration.html)

‎

So I tried to open configuration file and Boom. I have found database and mail server credentials.

Impact

The impact of exposed credentials has a wide range of consequences because those credentials can be used in data breaches, system compromises, loss of brand reputation, as well as financial losses.

Mitigation

Disable the debug mode by setting APP_DEBUG to false. Debug mode should be disabled in the production environment.

Tips:

If you found a web application that uses the Symfony web framework, do not forget to check debug mode and profiler. It might be developer forget to disable it.

https://example.com/_profiler
https://example.com/app_dev.php/_profiler
https://example.com/app_dev.php
Read more to Learn:
Understanding how the Front Controller, Kernel and Environments Work together (Symfony 4.4 Docs)
The configuration environments section explained the basics on how Symfony uses environments to run your application…

symfony.com
