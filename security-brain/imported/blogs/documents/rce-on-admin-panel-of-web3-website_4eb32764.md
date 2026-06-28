---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-21_rce-on-admin-panel-of-web3-website.md
original_filename: 2022-12-21_rce-on-admin-panel-of-web3-website.md
title: RCE on admin panel of web3 website
category: documents
detected_topics:
- command-injection
- sso
- ssrf
- sqli
- api-security
tags:
- imported
- documents
- command-injection
- sso
- ssrf
- sqli
- api-security
language: en
raw_sha256: 4eb327643951d7caf24ee7394f777397caa241ac9e3e66463b640de31e52d3f5
text_sha256: c34dec9f54c85ef190ba930ec59e09be39f7e460d4fca58f5ce2985f076ed32a
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# RCE on admin panel of web3 website

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-21_rce-on-admin-panel-of-web3-website.md
- Source Type: markdown
- Detected Topics: command-injection, sso, ssrf, sqli, api-security
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `4eb327643951d7caf24ee7394f777397caa241ac9e3e66463b640de31e52d3f5`
- Text SHA256: `c34dec9f54c85ef190ba930ec59e09be39f7e460d4fca58f5ce2985f076ed32a`


## Content

---
title: "RCE on admin panel of web3 website"
url: "https://medium.com/@vamshivaran110/rce-on-admin-panel-of-web3-website-2d0acf34d6ea"
authors: ["T VAMSHI"]
bugs: ["RCE", "Components with known vulnerabilities"]
publication_date: "2022-12-21"
added_date: "2022-12-23"
source: "pentester.land/writeups.json"
original_index: 1752
scraped_via: "browseros"
---

# RCE on admin panel of web3 website

RCE on admin panel of web3 website
T VAMSHI
Follow
4 min read
·
Dec 21, 2022

234

4

Hello Hackers…

I hope everyone is doing great. Today, I’m going to tell you about how I hacked into a web3 company and gained remote command execution on their admin panel.

let’s start…

I was hacking on web3 companies and came across a company that has their website in scope, but not the subdomains of the main domain. The main domain doesn’t have any features; it’s just used as a static webpage. When we click on any feature, it will redirect to a subdomain where all of the signup and signin features are available.

I found a bug in the subdomain that consists of the majority of activities. However, due to program rules, subdomains are not in scope, so the bug was considered out of scope. Despite this, the company paid me a significant amount of money for the bug. It is not recommended for any program to set subdomains out of scope when they are associated with and redirecting the majority of user activities to that subdomain.

They also deployed admin panel to the same subdomain.

Process Of Testing

Let the website be target.com. Since subdomains are not in scope, I focused on the main website, which didn’t have any features that a common user could use. When I clicked on any tab, it redirected me to a subdomain where all the features were available. So I started testing on the subdomain.

I started with port scanning and didn’t find anything interesting in the open ports. Then I tried to exploit different bugs like SQL injection, authentication bypass, and SSRF. After that, I moved on to directory fuzzing. I used different methods to collect a wordlist for fuzzing, which I explained in the following blog: https://medium.com/@vamshivaran110/fuzzing-with-custom-wordlists-bb7a808d943f

Get T VAMSHI’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After the fuzzing, I came across some interesting directories. One of them, the “/admin” directory, caught my attention, so I opened it. They were using GravCMS for the admin panel login. I started searching for known vulnerabilities in GravCMS and found a known vulnerability that could lead to RCE (CVE-2021–21425).

Press enter or click to view image in full size

Grav Admin Plugin is an HTML user interface that provides a way for users to configure Grav and create and modify pages. However, an unauthenticated user can execute certain methods of the administrator controller without needing any credentials. If these methods are successfully exploited, it can result in the creation of arbitrary YAML files or the modification of existing YAML files on the system. This vulnerability can lead to changes in configuration, such as changes to general site information or the definition of custom scheduler jobs. Due to the nature of this vulnerability, an adversary may be able to alter parts of a webpage, hijack an administrator account, or execute operating system commands under the context of the web-server user.

Exploitation:
Open the target directory at https://target.xyz/admin.
Enter random credentials and intercept the request in burp, Get cookie and extract admin-nonce value from login form.
Send the request to the repeater and modify the parameters as follows task=SaveDefault&data[title]=PWNED&admin-nonce=(value)
Press enter or click to view image in full size
forward the request and we can see in the response “200 OK”.

We will sucessfully exploit and change the webpage Title to the PWNED. Which is only possible for admin level privilleges. A remote code execution (RCE) vulnerability in Grav CMS could allow an attacker to execute arbitrary code on the server hosting the CMS. This could allow the attacker to take full control of the server and potentially compromise sensitive data.

Press enter or click to view image in full size
PWNED
Press enter or click to view image in full size

We can also exploit the vulnerability by automating the process with the Metasploit Framework. Simply search for the “GravCMS Remote Command Execution” module in Metasploit and set the required parameters to exploit.

After that, I crafted the report and submitted it to the concerned company with a proper proof-of-concept (POC). They were so smart that they simply marked it as “out of scope” because it was not the main domain. What is the point of keeping “in-scope” for a static webpage and keeping everything in a subdomain, including the admin dashboard?

After explaining the criticality and impact of the bug, they resolved it and paid the bounty$$$.

Thanks for reading…

Twitter: https://twitter.com/Th3Sc0rp10n

LinkedIn: https://www.linkedin.com/in/t-vamshi-2b5716165/
