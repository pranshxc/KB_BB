---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-18_from-security-misconfiguration-to-gaining-access-of-smtp-server.md
original_filename: 2018-11-18_from-security-misconfiguration-to-gaining-access-of-smtp-server.md
title: From Security Misconfiguration to Gaining Access of SMTP server
category: documents
detected_topics:
- command-injection
- information-disclosure
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- information-disclosure
- api-security
- cloud-security
language: en
raw_sha256: 4ad98eb3bcbed587c1bfdda50bca73b39f251da74eac7a0ef805cfdaf575b96c
text_sha256: 1c4cbfd7ae9ceb5d956c8d9b91fc67abefb1a4b0953ff10db34a5a1a1faf3e69
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# From Security Misconfiguration to Gaining Access of SMTP server

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-18_from-security-misconfiguration-to-gaining-access-of-smtp-server.md
- Source Type: markdown
- Detected Topics: command-injection, information-disclosure, api-security, cloud-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `4ad98eb3bcbed587c1bfdda50bca73b39f251da74eac7a0ef805cfdaf575b96c`
- Text SHA256: `1c4cbfd7ae9ceb5d956c8d9b91fc67abefb1a4b0953ff10db34a5a1a1faf3e69`


## Content

---
title: "From Security Misconfiguration to Gaining Access of SMTP server"
url: "https://medium.com/bugbountywriteup/from-security-misconfiguration-to-gaining-access-of-smtp-server-ed833e757e6e"
authors: ["Daniel V. (@d4niel_v)"]
bugs: ["File disclosure"]
publication_date: "2018-11-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5576
scraped_via: "browseros"
---

# From Security Misconfiguration to Gaining Access of SMTP server

Daniel "V" Morais
Follow
3 min read
·
Nov 18, 2018

215

From Security Misconfiguration to Gaining Access of SMTP server

Hello Guys!

In this article i want to show you how simple a security misconfiguration can compromise a company, even if that flaw is in their testing environment.

Summary:

I can send emails through any mail software (such as glock easymail) using SMTP settings provided by Amazon Simple email Service. With this, i can use any name such as ‘support@company.com.br’ or ‘admin@company.com.br’.

What is ‘Security Misconfiguration’ ?

Let’s get right to the point. Based on OWASP:

Security misconfiguration is the most commonly seen issue. This is commonly a result of insecure default configurations, incomplete or ad hoc configurations, open cloud storage, misconfigured HTTP headers, and verbose error messages containing sensitive information. Not only must all operating systems, frameworks, libraries, and applications be securely configured, but they must be patched/upgraded in a timely fashion.

How did i Discover:

I started with the recognition and mapping all domains of the company, as it was a large company, there were 84 domains to be analyzed, so i started to map each domain separately, accessing them and navigating manually to try to understand how the application works.

Get Daniel "V" Morais’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After visiting all of them, i noticed one subdomain was with the same application as the main website. Then i noticed that the subdomain were a test base, probably the company used to send new updates before they actually go to the main website.

Here is the problem:

Sometimes the developers leave enabled in the test base several features that, in production, would never be exposed for obvious reasons. Based on this principle, i decided to run a ‘Dirb https://company.com.br/’ to check if there were any open directory.

Bingo!

The phpinfo function was active on that subdomain. Basically, phpinfo is a useful PHP function for returning compiled information about the PHP environment on your server. This sould never be active, at least not publicly.

Press enter or click to view image in full size
phpinfo() function

Then i started to check the content that was exposed. As you can see in the image above, i had all the information needed to exploit several applications like postgres, mysql, smtp and many others. I decided to test their SMTP server settings.

So i downloaded the first software that i found on google and configured it according to the information from php function itself.

Press enter or click to view image in full size
Setting up the smtp server
Press enter or click to view image in full size
Setting up SMTP Server

I sent a test to myself saying “your password needs to be changed”, note, the most interesting thing is: It’s highlighted ‘sent by Amazon SeS’:

Press enter or click to view image in full size
Email received

never think that a low level fault can not produce good results. Always check all domains, including with the same tools as you used in the main domain, each domain represents a wide range of flaws.

That’s it, friends. Hope you liked it!

find me at linkedin .
