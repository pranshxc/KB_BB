---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-08-19_us-department-of-defense-info-disclosure-and-sqli-writeup.md
original_filename: 2019-08-19_us-department-of-defense-info-disclosure-and-sqli-writeup.md
title: U.S. Department of Defense - Info Disclosure and SQLi Writeup
category: blogs
detected_topics:
- sqli
- command-injection
- ssrf
- xss
- otp
- csrf
tags:
- imported
- blogs
- sqli
- command-injection
- ssrf
- xss
- otp
- csrf
language: en
raw_sha256: 6d0df1020624cb2c7495c1089cce2f1773343ef92799a718c792ce3d488a9643
text_sha256: efee460866631d20b2d93faab576ea09407dad0021ac1612576c2a323eb773e4
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# U.S. Department of Defense - Info Disclosure and SQLi Writeup

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-08-19_us-department-of-defense-info-disclosure-and-sqli-writeup.md
- Source Type: markdown
- Detected Topics: sqli, command-injection, ssrf, xss, otp, csrf
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `6d0df1020624cb2c7495c1089cce2f1773343ef92799a718c792ce3d488a9643`
- Text SHA256: `efee460866631d20b2d93faab576ea09407dad0021ac1612576c2a323eb773e4`


## Content

---
title: "U.S. Department of Defense - Info Disclosure and SQLi Writeup"
page_title: "Aaron Esau (arinerron)"
url: "https://aaronesau.com/blog/posts/5"
final_url: "https://aaronesau.com/blog/posts/5"
authors: ["Aaron Esau (@arinerron)"]
programs: ["U.S. Dept Of Defense"]
bugs: ["Information disclosure", "SQL injection"]
publication_date: "2019-08-19"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5075
---

[← Home](/)

[Aaron's Blog](/blog/)

[U.S. Department of Defense - Info Disclosure and SQLi Writeup](/blog/post/5)

This is a short writeup about a critical severity vulnerability that led me to discover another high severity vulnerability in a Navy website covered by the Department of Defense's HackerOne program.

# Discovering the Vulnerabilities

I intend to apply for the Naval ROTC scholarship as I will be going to college in late 2020, so recently, I have been testing the Navy's education and training website that candidates use to apply for scholarships. The [Department of Defense's HackerOne program](https://hackerone.com/deptofdefense) authorizes bug hunters to test the application. I found a few high and critical severity vulnerabilities while testing, but there are two in particular I want to write about.

I was doing reconnaissance on the application by doing an unauthenticated web path scan on the subdirectory `/nrotc` when I discovered a strange page called `Trace.axd` that returned the HTTP status code 302 and redirected to a login page.

I opened up Firefox, went to `/nrotc/Trace.axd`, and logged in using some test credentials, curious to see what was at this page. Once I was signed in, `/nrotc/Trace.axd` returned the status code 200. To my suprise, I was presented with a page titled “Application Trace”.

Well that isn't right! The page did not look like the rest of the application's webpages, so I figured that it was a built-in debugging feature in the web server or some framework that the application uses.

I googled `Trace.axd` and found out that this is an ASP.NET debugging feature that displays the details of previous HTTP requests. It is only accessible from localhost by default. That means that the feature was manually enabled by someone who didn't think it through.

Note for the future: If you get an SSRF vulnerability in an application that uses ASP.NET, an easy way to escalate it is simply to see if you can access `Trace.axd`.

I wanted to see what an attacker could obtain through this page, so I looked through a few of the requests to the application. Among other things, there were social security numbers, usernames, email addresses, plaintext passwords, session tokens, CSRF tokens, and of course, application-specific details (e.g. information about the software and filesystem), and headers for the HTTP traffic.

![social security number screenshot](https://arinerron.com/blogres/5_dod_app_ssns.png)

This vulnerability is of critical severity because it is low complexity, high impact, and technically no privileges required since anyone can create an account. I reported it on HackerOne on April 1, 2019 and the report was resolved on April 10, 2019.

In the meantime, I decided to use the debugger to my advantage to do more active reconnaissance. I used the page to map out the application and find more pages on the application that I could not find with dirsearch.

Most of the application's pages required a higher level of privilege than my test account had, so I was unable to test them. While I could have hijacked the session of a user with a higher privilege using the information I could've obtained through the debugger, I decided that that would be going too far.

There was a subdirectory in which all of the pages required a higher privilege to access except one page. I looked in the application debugger for a request to that one page and saw the `POST` body of a request. I replayed the request but replaced the session token with mine, but modified the parameters in the `POST` body to test for SQL injection and XSS using a payload like `'">`.

Surprisingly, one of the parameters was vulnerable to SQL injection. I felt like I had gone too far at this point, so I did not try to obtain remote code execution through the SQL injection vulnerability. I reported this vulnerability on April 1, 2019, and the report was marked as resolved on April 11, 2019.

For these two vulnerabilities, I was recognized as [researcher of the month](https://twitter.com/DC3VDP/status/1125483870902788100) in April by the Department of Defense Cyber Crime Center (DC3).

Also, outside of these reports, through my research on Navy websites, I have learned the importance of reverse engineering JavaScript while doing reconnaissance. Often, web developers leave undocumented and unused API features implemented in the JavaScript that have likely not been discovered and tested by other researchers. Those features are great to test as they're often riddled with vulnerabilities.

# Disclosed Reports

  * [#519418](https://hackerone.com/reports/519418) — Sensitive Information Disclosure
  * [#519631](https://hackerone.com/reports/519631) — SQL Injection

Although this report is unrelated to this writeup, I found it earlier while doing testing on the same web application:

  * [#419017](https://hackerone.com/reports/419017) — SQL Injection

# Timeline
  
  
  March 31, 2019: Reported sensitive information exposure vulnerability.
  April 1, 2019: Sensitive information exposure vulnerability triaged.
  April 1, 2019: Reported SQL injection vulnerability.
  April 2, 2019: SQL injection vulnerability triaged.
  April 10, 2019: Sensitive information exposure report marked as resolved.
  April 10, 2019: Requested disclosure of sensitive information exposure report.
  April 11, 2019: SQL injection report marked as resolved.
  April 11, 2019: Requested disclosure of SQL injection report.
  May 6, 2019: Recognized as researcher of the month: https://twitter.com/DC3VDP/status/1125483870902788100
  August 19, 2019: Sensitive information exposure report disclosed.
  August 19, 2019: SQL injection report disclosed.
  

Loading...
