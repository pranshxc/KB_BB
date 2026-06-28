---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-11-02_blog-post-bypassing-an-admin-panel-with-sql-injection.md
original_filename: 2023-11-02_blog-post-bypassing-an-admin-panel-with-sql-injection.md
title: 'Blog Post: Bypassing an Admin Panel with SQL Injection'
category: blogs
detected_topics:
- sqli
- command-injection
- automation-abuse
tags:
- imported
- blogs
- sqli
- command-injection
- automation-abuse
language: en
raw_sha256: 76615666f9cb74fbc1192464f93133482bdfd8331f3dccffc610311d772f9f83
text_sha256: 4ae6f32928154e1e26f455d72905f265da73ef3c931ad6d9ebc043e2739dc529
ingested_at: '2026-06-28T07:32:27Z'
sensitivity: unknown
redactions_applied: false
---

# Blog Post: Bypassing an Admin Panel with SQL Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-11-02_blog-post-bypassing-an-admin-panel-with-sql-injection.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:27Z
- Redactions Applied: False
- Raw SHA256: `76615666f9cb74fbc1192464f93133482bdfd8331f3dccffc610311d772f9f83`
- Text SHA256: `4ae6f32928154e1e26f455d72905f265da73ef3c931ad6d9ebc043e2739dc529`


## Content

---
title: "Blog Post: Bypassing an Admin Panel with SQL Injection"
url: "https://medium.com/@medz20876/blog-post-bypassing-an-admin-panel-with-sql-injection-20b844442711"
authors: ["r3aper__"]
bugs: ["SQL injection", "Authentication bypass"]
publication_date: "2023-11-02"
added_date: "2023-12-27"
source: "pentester.land/writeups.json"
original_index: 690
scraped_via: "browseros"
---

# Blog Post: Bypassing an Admin Panel with SQL Injection

Top highlight

Blog Post: Bypassing an Admin Panel with SQL Injection
r3aper__
Follow
3 min read
·
Nov 2, 2023

812

10

r3aper__ | https://hackerone.com/r3aper__?type=user

Introduction

Welcome to my very first blog post! I’m excited to share my bug bounty hunting journey with you. A year ago, I delved into the world of cybersecurity without any formal technology or IT training. Instead, I started my bug bounty adventure by self-teaching using resources like PortSwigger’s labs and educational content on YouTube. Today, I want to share a recent discovery where I found a vulnerability in a web application that allowed me to bypass its admin panel. I’ll explain how this vulnerability, known as SQL injection, works and how I used it to gain unauthorized access.

Understanding SQL Injection

SQL injection is a type of attack where an attacker can manipulate an application’s SQL query by injecting malicious SQL code into user inputs. If the application doesn’t properly validate and sanitize these inputs, it can execute unintended SQL commands, leading to security breaches. Most often, you will see attackers/researchers injecting into vulnerable URL parameters (both in GET and POST requests), but sometimes, you can use SQL syntax/injections to bypass login screens. In this attack, I was able to demonstrate both of these attacks- bypassing the login panel, and also returning the database contents.

Exploiting the Vulnerability
Identifying the Vulnerable Login Page

When I visited https://redacted.com/redacted/redacted_admin.xml, I noticed a login prompt. When you enter your credentials and click login, the application sends a GET request with the credentials in the following way:

GET /redacted/redacted_admin.xml?id=admin&pswd=admin&uniqueId=0.5331820440279285 HTTP/1.1 2

After trying the basic admin:admin with no luck, and reading through the JS on the page, I decided to try an SQL injection. Testing some various payloads led me to the one that actually worked- I was able to inject into the id parameter using the payload:

-6513%27%20OR%20%28SELECT%20INSTR2%28NULL%2CNULL%29%20FROM%20DUAL%29%20IS%20NULL--%20SpSw

The full request was:

https://redacted.com/redacted/redacted_admin.xml?id=-6513%27%20OR%20%28SELECT%20INSTR2%28NULL%2CNULL%29%20FROM%20DUAL%29%20IS%20NULL--%20SpSw&pswd=admin&uniqueId=0.5331820440279285

After visiting this link, I was able to access the admin panel:

Press enter or click to view image in full size
Additional Exploitation with sqlmap

I also ran sqlmap on the raw request from Step 1, which helped me retrieve all the databases. This powerful tool can provide valuable insights into the structure of the database and its contents. The command I used:

Get r3aper__’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

sqlmap -r request.txt --random-agent --dbs --proxy=http://127.0.0.1:8080 --force-ssl --batch --risk 3 --level 3

Which returned the databases, as expected:

Press enter or click to view image in full size
Impact and Conclusion

This vulnerability, known as SQL injection, has the potential to be highly damaging. It allows attackers to bypass security measures and access sensitive information. It’s essential for developers to validate and sanitize user inputs to prevent such issues.

After discovering this vulnerability, I reported it to the website’s administrators, who, I hope, have taken the necessary steps to fix it. SQL injection is a common vulnerability on the web, and understanding how it works can help both security experts and website developers improve their practices.

Stay tuned to this channel, as I plan to share more write ups with you all in the near future.

Cheers!

@r3aper__
