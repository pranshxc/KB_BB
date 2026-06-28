---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-12_how-i-was-able-to-bypass-the-admin-panel-without-the-credentials.md
original_filename: 2021-06-12_how-i-was-able-to-bypass-the-admin-panel-without-the-credentials.md
title: How I was able to bypass the admin panel without the credentials.
category: documents
detected_topics:
- command-injection
- rate-limit
- information-disclosure
tags:
- imported
- documents
- command-injection
- rate-limit
- information-disclosure
language: en
raw_sha256: 8c4329c059393366f7d3dbe1284fb59cd08debdea20fd17bca298af557502bfc
text_sha256: 89fa50da957a2b8d4a19dd8b6fd492dc19da6b604c09be41fb9ad53bc65f96d1
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to bypass the admin panel without the credentials.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-12_how-i-was-able-to-bypass-the-admin-panel-without-the-credentials.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, information-disclosure
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `8c4329c059393366f7d3dbe1284fb59cd08debdea20fd17bca298af557502bfc`
- Text SHA256: `89fa50da957a2b8d4a19dd8b6fd492dc19da6b604c09be41fb9ad53bc65f96d1`


## Content

---
title: "How I was able to bypass the admin panel without the credentials."
url: "https://pratikkhalane91.medium.com/how-i-was-able-to-bypass-the-admin-panel-without-the-credentials-d65f90e0e1e4"
authors: ["Pratikkhalane (@KhalanePratik)"]
bugs: ["Information disclosure"]
bounty: "500"
publication_date: "2021-06-12"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3585
scraped_via: "browseros"
---

# How I was able to bypass the admin panel without the credentials.

How I was able to bypass the admin panel without the credentials.
Pratikkhalane
Follow
5 min read
·
Jun 12, 2021

1K

9

This is my first article and I hope you guys will surely learn something new. Since I am not allowed to disclose the information about the company, let’s assume it as example.com. The main domain was the only scope to test for finding vulnerabilities. Now Lets Jump into the bug………….

Whenever we visit a website we try to first understand the technologies which are used and for that, I used an extension that is called as wappalyzer.

You must be thinking that yes there is a CMS(Content management system)which is WordPress and let's go for /wp-admin for the bypass. But no that is not the case, this result can be stated as false-positive. So to verify we can use a tool called Wpscan which comes pre-installed in Kali Linux.

Press enter or click to view image in full size

So this is a good example of how wappalyzer can show you a false-positive result. This made me think then what would be the CMS of this website if WordPress is a false-positive result. Now, let's start with the recon process.

NOW THE FUN BEGINS…

1 ) Directory Bruteforcing

There are multiple tools to brute force the directory. A few of them are given below.

i) FFUF

ii) GoBuster

iii) DirDar

There are soo many lists which is available for brute-forcing the directory. A few of them are given below.

i) Seclist:

ii ) DirSearch:

iii) Assetnote

I used the ffuf tool along with the assetnote file so the command looks like

Command : ffuf -c -w /wordlist -u /URL/FUZZ -mc 200,301,302 -t 500

After using the wordlist, I was able to get into one of the directories which is “sitemanager”. I opened the directory and I got the CMS Login Page of the company.

Admin Portal

Now I tried using the default credentials but still, I was not able to get into the admin portal.

The website looked something like this https://www.example.com/sitemanager/login.php?location=%2Fsitemanager%2F

Get Pratikkhalane’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Without wasting anytime, I tried to Re-Bruteforce the directory of /sitemanager/FUZZ, and boom I got soo many endpoints (all of them were false-positive showing 200 OK with the size “0" ) but only one from the wordlist worked which was /startup.sh/

Press enter or click to view image in full size
Startup. sh

This made me feel happy that yes I got some endpoints by which I can be able to escalate into the admin portal, but still, there might be some chances of the credentials getting exposed in “settings.txt” or “errors_php.txt” by which I can get into the admin portal.

Now after opening the errors_php.txt and settings.txt

errors_php.txt

— — — — — — — — — — — — — — — — — — — — — — — — — —

Error occurred: 02.11.2020 10:02:32
user: admin, script: /sitemanager/admin.php
IP:77.**.**.**| ISP info: host-77–236–201–15| Session: emdcjngeinl81f9kl5c9hjlp31| Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:16.0) Gecko/20100101 Firefox/16.0
8, Undefined variable: edit_profile_page_pid, /home/text/www/site/modrw.php, 42

Error occured: 02.11.2020 10:56:16
user: admin, script: /sitemanager/admin.php
IP:77.**.**.**| ISP info: host-77–236–201–15| Session: emdcjngeinl81f9kl5c9hjlp31| Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:16.0) Gecko/20100101 Firefox/16.0
8, Undefined variable: edit_profile_page_pid, /home/text/www/site/modrw.php, 42

Error occured: 05.11.2020 11:41:46
user: admin, script: /sitemanager/admin.php
IP:77.**.**.**| ISP info: host-77–236–201–15| Session: i6f928p13qcd1bpoin5lkljj31| Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:16.0) Gecko/20100101 Firefox/16.0
8, Undefined variable: edit_profile_page_pid, /home/text/www/site/modrw.php, 45

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

This was the point I felt that I can use this error file to escalate into the admin portal. But unfortunately, I was not able to. So ethically I reported this file separately and got €€€.

2. settings.txt

After opening this file again, I got some of the HTTP burp request files, but this time they were having cookies. These request responses were of the admin along with the cookies and of multiple users along with the cookies. Now the HTTP request of admin looks like this:

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

date: 2020–11–20 15:19:41
settings
headers: GET
Host: www.example.com
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://www.example.com/sitemanager/admin.php
Accept-Encoding: gzip, deflate, br
Accept-Language: cs,en-GB;q=0.9,en;q=0.8,sk;q=0.7
Cookie: __stripe_mid=b1a624a3-b1da-45aa-9aca-6236dd8###; _ga=GA1.2.805574655.149725####; __atuvc=0%7C41%2C0%7C42%2C0%7C43%2C0%7C44%2C1%7C45; language=cs; PHPSESSID=lqcp890ff17r02erb#####; _gid=GA1.2.1643979482.1542716##; login_config=u%3admin; _gat=1
IP info:
script: /sitemanager/settings.php
IP:213.**.**.**
ISP info: 213.**.**.**
Session: lqcp890ff17r02erbkot5u###
Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36

— — — — — — — — — — — — — — — — — — — — — — — — — — — — — —

After pasting this into the repeater of the burpsuite and doing some basic changes as per the repeater & adding the target section, I got the 200 OK. I was like ……….

Now we are back in business

I added the directory which is “/dashboard.php” and boom I got admin access and I was able to use the portal.

Reward/Bounty

This was reported to the security team and they removed the sitemanager portal.

I was awarded 500 € for this bug.

Take Away

Always look for the endpoints which can be used to escalate the bug from low level to critical/high level.

Thanks for reading this. Comments and feedback are welcome.
