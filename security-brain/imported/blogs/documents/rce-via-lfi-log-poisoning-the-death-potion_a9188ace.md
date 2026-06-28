---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-12-06_rce-via-lfi-log-poisoning-the-death-potion.md
original_filename: 2020-12-06_rce-via-lfi-log-poisoning-the-death-potion.md
title: RCE via LFI Log Poisoning - The Death Potion
category: documents
detected_topics:
- command-injection
- path-traversal
- access-control
- xss
- information-disclosure
tags:
- imported
- documents
- command-injection
- path-traversal
- access-control
- xss
- information-disclosure
language: en
raw_sha256: a9188acee077eee36d3e7e0c00ad46069e65fd0a70fafc9589cc2776d2df785f
text_sha256: f91d6fef54279c4ae980cd598361f758d37704e4650bbea1a1e2cf00c487ec7c
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# RCE via LFI Log Poisoning - The Death Potion

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-12-06_rce-via-lfi-log-poisoning-the-death-potion.md
- Source Type: markdown
- Detected Topics: command-injection, path-traversal, access-control, xss, information-disclosure
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `a9188acee077eee36d3e7e0c00ad46069e65fd0a70fafc9589cc2776d2df785f`
- Text SHA256: `f91d6fef54279c4ae980cd598361f758d37704e4650bbea1a1e2cf00c487ec7c`


## Content

---
title: "RCE via LFI Log Poisoning - The Death Potion"
url: "https://shahjerry33.medium.com/rce-via-lfi-log-poisoning-the-death-potion-c0831cebc16d"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["RCE", "LFI", "Log poisoning"]
publication_date: "2020-12-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4087
scraped_via: "browseros"
---

# RCE via LFI Log Poisoning - The Death Potion

Top highlight

RCE via LFI Log Poisoning - The Death Potion
Jerry Shah (Jerry)
Follow
4 min read
·
Dec 6, 2020

688

5

Hello everyone, I would like to share one of my recent findings on a Vulnerability Disclosure Program. It is related to how I escalated to Remote Code Execution using Local File Inclusion with Log Poisoning.

What is RCE ?

In basic words Remote Code Execution is a vulnerability that allows attackers to access a system and read or delete their contents, make changes etc.

What is LFI ?

In basic words Local File Inclusion is used by attackers to trick the web application into exposing or running files on the web server. It can lead to information disclosure, remote code execution, or XSS. LFI occurs when an application uses the path to a file as input. If the application treats this input as trusted, a local file may be used in the include statement.

What are Logs ?

A log file is a computer generated data file that contains information about usage patterns, activities, and operations within an operating system, application, server or another device.

What is vsftpd.log file ?

It is use to trace malicious activity facilitated by the FTP service, it must be configured to ensure that all commands sent to the ftp server are logged using the verbose vsftpd log format. The default vsftpd log file is /var/log/vsftpd. log. Basically it keeps the track of the login activity or failed login attempts on the FTP server.

What is auth.log file ?

It contains system authorization information, including user logins and authentication mechanism that were used.

NOTE : If you want to learn more about different log files then visit - https://www.thegeekstuff.com/2011/08/linux-var-log-files/

What is log poisoning ?

Log Poisoning is a common technique used to gain a reverse shell from a LFI vulnerability. To make it work an attacker attempts to inject malicious input to the server log.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How I found this vulnerability ?

I discovered an endpoint where I found Local File Inclusion
Press enter or click to view image in full size
Local File Inclusion

2. Then I tried to access /etc/shadow file but I didn’t get any result

3. Then I tried to access /var/log/auth.log file but no result

Press enter or click to view image in full size
auth.log

4. Moving further I did a nmap scan to check what are the open ports

Press enter or click to view image in full size
Nmap Scan

As you can see port 21, 22 and 80 were open so I thought of doing a log poisoning on ssh login but unfortunately the /var/log/auth.log file wasn’t accessible on the web so I thought that it is not possible to achieve Remote Code Execution.

I wasn’t aware that ftp logs are saved in a different file called vsftpd.log, I thought it is also saved in auth.log so I tried to access /var/log/vsftpd.log file and was successfully able to see the contents of it on the web so now the next step was to go for a log poisoning on ftp server.

For log poisoning it was necessary to find which technologies are used by the web application in order to find a perfect payload for it, I used wappalyzer to find the technologies used and I found it was using PHP 7 and some other technologies too.

5. I tried to make fake attempts with a PHP payload as a user on the ftp server of my target which will be saved in the vsftpd.log file

Payload : ‘<?php system($_GET[‘commandInjection’]); ?>’

Press enter or click to view image in full size
FTP attempt

6. Now I accessed the endpoint with /var/log/vsftpd.log&commandInjection=ifconfig and successfully got a Remote Code Execution

Press enter or click to view image in full size
Remote Code Execution
Press enter or click to view image in full size
