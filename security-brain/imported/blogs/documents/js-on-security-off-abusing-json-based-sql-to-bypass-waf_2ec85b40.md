---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-08_js-on-security-off-abusing-json-based-sql-to-bypass-waf.md
original_filename: 2022-12-08_js-on-security-off-abusing-json-based-sql-to-bypass-waf.md
title: '{JS-ON: Security-OFF}: Abusing JSON-Based SQL to Bypass WAF'
category: documents
detected_topics:
- sqli
- otp
- api-security
- access-control
- xss
- command-injection
tags:
- imported
- documents
- sqli
- otp
- api-security
- access-control
- xss
- command-injection
language: en
raw_sha256: 2ec85b40dd3d8dcce0539271f5cc7057746cdee88faacb89cd4ddfff2fa18c5f
text_sha256: 15be1a945ac8b646bb4684d6f2d4c2d0e8d5f7650d4b0e5941a21e03f7a071e6
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# {JS-ON: Security-OFF}: Abusing JSON-Based SQL to Bypass WAF

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-08_js-on-security-off-abusing-json-based-sql-to-bypass-waf.md
- Source Type: markdown
- Detected Topics: sqli, otp, api-security, access-control, xss, command-injection
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `2ec85b40dd3d8dcce0539271f5cc7057746cdee88faacb89cd4ddfff2fa18c5f`
- Text SHA256: `15be1a945ac8b646bb4684d6f2d4c2d0e8d5f7650d4b0e5941a21e03f7a071e6`


## Content

---
title: "{JS-ON: Security-OFF}: Abusing JSON-Based SQL to Bypass WAF"
page_title: "{JS-ON: Security-OFF}: Abusing JSON-Based SQL to Bypass WAF | Claroty"
url: "https://claroty.com/team82/research/js-on-security-off-abusing-json-based-sql-to-bypass-waf"
final_url: "https://claroty.com/team82/research/js-on-security-off-abusing-json-based-sql-to-bypass-waf"
authors: ["Noam Moshe"]
programs: ["Palo Alto Networks", "AWS", "Cloudflare", "F5", "Imperva"]
bugs: ["WAF bypass", "SQL injection"]
publication_date: "2022-12-08"
added_date: "2022-12-09"
source: "pentester.land/writeups.json"
original_index: 1802
---

[ ![Team82 Logo](https://claroty.com/build/assets/team82-logo-white-BGiCQ9zb.svg) ](/team82)

  * [Research](/team82/research)
  * [Vulnerability Dashboard](/team82/disclosure-dashboard)
  * [Talks](/team82/talks)
  * [Tools](/team82/#tools)
  * [About](/team82/#about)

[ ![Claroty](https://claroty.com/build/assets/logo-solid-white-DcRiqKcD.svg) ](/)

[ Return to Team82 Research ](/team82/research)

# {JS-ON: Security-OFF}: Abusing JSON-Based SQL to Bypass WAF

Noam Moshe 

/ December 8th, 2022

![{JS-ON: Security-OFF}: Abusing JSON-Based SQL to Bypass WAF](/img/asset/YXNzZXRzL2NsYXJvdHktYmxvZy1ncmFwaGljc18xMi0yMi0wMS5wbmc/claroty-blog-graphics_12-22-01.png?fm=webp&fit=crop&w=800&h=450&s=b494f94408196f53e118cf59f86e0742)

## Executive Summary

  * Team82 has developed a generic bypass of industry-leading web application firewalls (WAF). 

  * The attack technique involves appending JSON syntax to SQL injection payloads that a WAF is unable to parse. 

  * Major WAF vendors lacked JSON support in their products, despite it being supported by most database engines for a decade. 

  * Most WAFs will easily detect SQLi attacks, but prepending JSON to SQL syntax left the WAF blind to these attacks.

  * Our bypass worked against WAFs sold by five leading vendors: Palo Alto Networks, Amazon Web Services, Cloudflare, F5, and Imperva. All five have been notified and have updated their products to support JSON syntax in their SQL injection inspection process. 

  * Attackers using this technique would be able to bypass the WAF’s protection and use additional vulnerabilities to exfiltrate data.

## Table of Contents

  1. Previous Work Leads to New Technique

  2. Cloud Deployment

  3. Getting Stuck With a Zero Day You Can’t Exploit

  4. Limitation 1: We Can Only Retrieve Integers

  5. Limitation 2: The Returned Rows Are Returned In Random Order

  6. Limitation 3: We Can Only Return a Limited Number Of Rows In Each Request

  7. Constructing Our Payload

  8. Going To The Clouds (and Falling Down)

  9. Researching AWS WAF

  10. JSON in SQL

  11. The New ‘ or ‘a’=’a

  12. Armed With JSON Syntax

  13. Dream Big: A Generic WAF Bypass

  14. Automating The Process

  15. Conclusion

## What is Web Application Firewall (WAF)?

Web application firewalls (WAF) are designed to safeguard web-based applications and APIs from malicious external HTTPs traffic, most notably cross-site scripting and SQL injection attacks that just don’t seem to drop off the security radar. 

While recognized and relatively simple to remedy, SQL injection in particular is a constant among the output of automated code scans, and a regular feature on industry lists of top vulnerabilities, including the OWASP Top 10. 

The introduction of WAFs in the early 2000s was largely a counter to these coding errors. WAFs are now a key line of defense in securing organizational information stored in a database that can be reached through a web application. WAFs are also increasingly used to protect cloud-based management platforms that oversee connected embedded devices such as routers and access points. 

An attacker able to bypass the traffic scanning and blocking capabilities of WAFs often has a direct line to sensitive business and customer information. Such bypasses, thankfully, have been infrequent, and one-offs targeting a particular vendor’s implementation.

Today, Team82 introduces an attack technique that acts as the first generic bypass of multiple web application firewalls sold by industry-leading vendors. Our bypass works on WAFs sold by five leading vendors: Palo Alto, F5, Amazon Web Services, Cloudflare, and Imperva. All of the affected vendors acknowledged Team82’s disclosure and implemented fixes that add support for JSON syntax to their products’ SQL inspection processes. 

Our technique relies first on understanding how WAFs identify and flag SQL syntax as malicious, and then finding SQL syntax the WAF is blind to. This turned out to be JSON. JSON is a standard file and data exchange format, and is commonly used when data is sent from a server to a web application. 

JSON support was introduced in SQL databases going back almost 10 years. Modern database engines today support JSON syntax by default, basic searches and modifications, as well as a range of JSON functions and operators. While JSON support is the norm among database engines, the same cannot be said for WAFs. Vendors have been slow to add JSON support, which allowed us to craft new SQL injection payloads that include JSON that bypassed the security WAFs provide. 

Attackers using this novel technique could access a backend database and use additional vulnerabilities and exploits to exfiltrate information via either direct access to the server or over the cloud. 

This is especially important for OT and IoT platforms that have moved to cloud-based management and monitoring systems. WAFs offer a promise of additional security from the cloud; an attacker able to bypass these protections has expansive access to systems. 

## Previous Work Leads to New Technique

Our journey to developing this technique began last year during unrelated research on Cambium Networks’ wireless device management platform, including its cnMaestro wireless network manager that is sold either on-premises or in the cloud.

![cnmaestro](/img/asset/YXNzZXRzL2NubWFlc3Ryby0xNjcwNTE2OTgxLnBuZw/cnmaestro-1670516981.png?fm=webp&fit=crop&s=594771dda26b7d2b7b99b4c011f09471) __ A Cambium Networks wireless access point.  ![cnMaestro workflow](/img/asset/YXNzZXRzL2NsYXJvdHktYmxvZy1ncmFwaGljc18xMi0yMi0wMi5wbmc/claroty-blog-graphics_12-22-02.png?fm=webp&fit=crop&s=4e791607e6842675a91d0d1baa7795ab) __ Cambium's cnMaestro cloud architecture allows users to configure and control their AP Wi-Fi devices remotely from the cloud.

In order to understand how the platform is built and many of its internal APIs and routes, we downloaded an Open Virtualization Format virtual machine of cnMaestro’s on premises deployment from Cambium’s website.

We learned that cnMaestro is built from many different NodeJS backend services that handle users’ requests to specific routes. Each of those services is lightly obfuscated to make researching the platform difficult. In order to proxy each request to the correct service, Nginx is used to pass the requests by the requested URL.

cnMaestro offers two different deployment types:

  1. On-Premise Deployment: A dedicated cnMaestro server is created that is hosted and managed by the user.

  2. Cloud Deployment: A cnMaestro server hosted on Cambium Networks’ cloud infrastructure; all such instances of cnMaestro are hosted on Amazon AWS’ cloud under Cambium’s organization in a multi-tenant architecture.

When we started fiddling with the cnMaestro application, we noticed a few interesting things with regard to the cloud deployment.

## Cloud Deployment

cnMaestro cloud deployments hosted on Amazon’s AWS include a main instance of cnMaestro (hosted on [https://cloud.cambiumnetworks.com](https://cloud.cambiumnetworks.com/)) that handles logins, device deployment, and saves most of the platform’s data inside a main database. 

Any user who registers to the cnMaestro Cloud application is given a personal Amazon AWS instance, with a personal URL (a sub-domain of Cambium’s main cloud), and an organizational identifier. This helps to separate the different users in a multi-tenant design. In order to access your cnMaestro instance, a unique URL is generated following this scheme:
  
  
  https://us-e1-sXX-XXXXXXXXXX.cloud.cambiumnetworks.com

At the end of our research into Cambium cnMaestro, we discovered seven different vulnerabilities, which can be seen [here](https://www.cisa.gov/uscert/ics/advisories/icsa-22-132-04) and on [Team82’s Disclosure Dashboard](https://claroty.com/team82/disclosure-dashboard). However, one vulnerability in particular made us go down a huge rabbit hole that led us into discovering and developing this new technique.

## Getting Stuck With a Zero Day You Can’t Exploit 

One particular Cambium vulnerability we discovered proved more difficult to exploit: [CVE-2022-1361](https://claroty.com/team82/disclosure-dashboard/cve-2022-1361). At the core of the vulnerability is a simple SQL injection vulnerability, however the actual exploitation process required us to think outside the box and create a whole new SQL technique. Using this vulnerability, we were able to exfiltrate users’ sessions, SSH keys, password hashes, tokens, and verification codes.

The core issue of this vulnerability was that in this particular case, the developers did not use a prepared statement to append user-supplied data to a query. Instead of using a safe method of appending user parameters into an SQL query and sanitizing the input, they simply appended it to the query directly.

![waf sink point](/img/asset/YXNzZXRzL3dhZl9zaW5rLXBvaW50LTE2NzA1MjA3NzMucG5n/waf_sink-point-1670520773.png?fm=webp&fit=crop&s=dab2413eee0ddfb4d2bfffac15e53936) __ The SQL Injection sink point we abused in CVE-2022-1361.

As we can see in the sink point above, the application takes user-supplied data (in this case: a.serialNo or a.mac) and appends it to a SQL query. Our goal using this vulnerability was to exfiltrate sensitive data stored in the database. However, while this seemed simple enough, after a quick analysis of this vulnerability we realized it had three key weaknesses/limitations:

  1. We can only retrieve integers as the returned rows

  2. The returned rows are returned in random order

  3. We can only return a limited number of rows in each request.

Let’s analyze the limitations in-depth.

## Top SQL Injection Limitations

### Limitation 1: We Can Only Retrieve Integers

The first limitation returns only integers, and not strings. Since the original request returns integers, any union statement we will use must also return integers. In SQL, if you perform a union operation, you must make sure both columns are of the same type, and since one side fetched integers, we had to return integers as well. Since the data that we will want to exfiltrate will most likely be strings (session tokens, SSH keys etc.), we must somehow gain the ability to exfiltrate strings.

This limitation was easily overcome by casting any string we want to exfiltrate into an integer array, returning each character as a separate row. To do so, we used the `stringtoarray` and `ASCII` SQL functions.

![waf select ascii](/img/asset/YXNzZXRzL3dhZl9zZWxlY3Rhc2NpaS0xNjcwNTIwODQxLnBuZw/waf_selectascii-1670520841.png?fm=webp&fit=crop&s=2b389ed66c46956af081692eef4455b7) __ ![waf test](/img/asset/YXNzZXRzL3dhZl90ZXN0YXNjaWkucG5n/waf_testascii.png?fm=webp&fit=crop&s=1f34046a0fe156e0cebf1a8ce13a5993) __ A SQL query returning a string as an integer list of its characters.

### Limitation 2: The Returned Rows Are Returned In Random Order

The second limitation was that when we return multiple rows, the web server will return it to us in random order. When we looked at the code that is executed after the vulnerability, we saw that for each row that the SQL query returned, the server will perform a few other asynchronous actions (which can be seen by the `async.parallel` function being called). This means that the original order of the returned rows will not be kept, instead the order will be the order of the asynchronous action being finished.

This meant that if we were to exfiltrate a string as an integer array, we would lose the character order thus rendering the exfiltration irrelevant.

We managed to overcome this limitation by appending the row index, which translates the index of the character in the string to the returned integer, using the `row_number` SQL function. Because we only return ASCII characters, each character value is limited to 128. By adding the index number multiplied by a thousand (`i * 1000`) and appending it to the result, we can always be sure of the character index using a simple division and module actions.

![waf select ascii](/img/asset/YXNzZXRzL3dhZl9zZWxlY3RjLTE2NzA1MjA5NTEucG5n/waf_selectc-1670520951.png?fm=webp&fit=crop&s=916d14492b3c74ab8d0220bef21b1b6f) __ ![waf test index](/img/asset/YXNzZXRzL3dhZl90ZXN0aW5kZXgyLTE2Njk5MjAyOTAucG5n/waf_testindex2-1669920290.png?fm=webp&fit=crop&s=bae325c920dbc3853e191a95ca9c23b7) __ A SQL payload that returns the ascii value of each letter in a string, with the character’s index multiplied by 1,000.

After we retrieve the exfiltrated data, we can simply divide each returned row by a thousand in order to know the character index. We can also recover the original character ASCII value by using the module action on the returned value.

### Limitation 3: We Can Only Return a Limited Number Of Rows In Each Request

The final limitation was the most difficult to overcome: a timeout issue. For each row we returned, the server performed a few other actions, including another SQL query and data manipulation. When we tried to retrieve a large number of rows, the request was timed out. To make matters worse, the API endpoint was fairly slow, so retrieving one row at a time was too time consuming.

Our solution was actually very elegant: instead of returning one row for each character, we would instead construct an integer out of many rows. This is possible because of the difference in byte size between integers and characters. In PostgreSQL, an integer is 4 bytes long, while the character we try to exfiltrate is up to 1 byte long (as long as we are talking about ascii characters). This means that by performing simple byte operations, we can house four different characters in each integer. Furthermore, if we cast our integer into a `BIGINT` in our union command, which is possible to do in PostgreSQL, we can expand each row into 8 bytes.

![waf numeric types](/img/asset/YXNzZXRzL3dhZl9udW1lcmljLXR5cGVzLnBuZw/waf_numeric-types.png?fm=webp&fit=crop&s=1c2738fdc5069ca2c258ff7c520fd2f3) __ PostgreSQL types sizes. Source: PostgreSQL.

This means that if we were to append 8 bytes for each character we exfiltrate, and append it into a `BIGINT`, we could exfiltrate 7 times more characters in each request (1 byte is reserved to the character index).

![waf select id](/img/asset/YXNzZXRzL3dhZl9zZWxlY3RpZC0xNjcwNTIxMTI2LnBuZw/waf_selectid-1670521126.png?fm=webp&fit=crop&s=a9fa457b6016b3f3d13079e2491c2de2) __ ![waf testsss](/img/asset/YXNzZXRzL3dhZl90ZXN0c3NzLnBuZw/waf_testsss.png?fm=webp&fit=crop&s=53bdea3a0e8515e2cb100dfca7eda410) __ A SQL query that takes a string, and creates a BIGINT out of every few characters

Using this methodology, we were able to exfiltrate up to 8 times more data in each request. This reduced the time it would take us to exfiltrate a meaningful amount of data and make the attack scenario plausible.

## Constructing Our Payload

After we bypassed all three limitations, we were left with a big payload allowing us to extract any data we chose:

![waf evasion](/img/asset/YXNzZXRzL2NsYXJvdHktYmxvZy1ncmFwaGljc18xMi0yMi0wNC5wbmc/claroty-blog-graphics_12-22-04.png?fm=webp&fit=crop&s=7a764b24879c14029500c618cc82b796) __

  
And indeed, when we used this payload we managed to exfiltrate sensitive information stored in the database ranging from session cookies to tokens, SSH keys and hashed passwords.

![waf cookie](/img/asset/YXNzZXRzL3dhZl9jb29raWUucG5n/waf_cookie.png?fm=webp&fit=crop&s=6cabe0c57f546f09531207dc38d1e4b5) __ An example of data we exfiltrated using our SQLi payload.

## Going To The Clouds (and Falling Down)

After managing to fully exploit this vulnerability on the on-prem version, our next step was to try the same vulnerability on Cambium’s cloud. Soon enough we found the corresponding cloud route, and we managed to confirm it is vulnerable to the same vulnerability. We then tried a safe version of our payload, and we received this response:

![waf 403](/img/asset/YXNzZXRzL3dhZl80MDMtZm9yYmlkZGVuLnBuZw/waf_403-forbidden.png?fm=webp&fit=crop&s=0aa8830751f943350946926ef9a775cf) __ The response to our SQL Injection vulnerability. We can see that our request was dropped, returning a 403 Forbidden.

After a short panic, we noticed the `HTTP Server` header, containing `awselb/2.0`. This clued us in that our request was not stopped by the application, instead the AWS WAF dropped our request because it probably flagged it as malicious. This stumped us for a minute, however soon enough we set our goal on bypassing this WAF. This ignited our current research.

## Researching AWS WAF

In order to research the AWS WAF, we first created our own setup where we control all moving parts: the application, the client and the WAF settings and logs. We created a simple machine on the AWS cloud, and set up the AWS WAF to protect the application from malicious requests (we set up the WAF).

![waf addsql](/img/asset/YXNzZXRzL3dhZl9hZGRzcWwucG5n/waf_addsql.png?fm=webp&fit=crop&s=88ae6e4ab3f3a63535c94e43dfbc77b1) __ The interface for configuring the WAF ruleset.

Then, we created a web application with a SQLi vulnerability, and hosted it on AWS.

![waf vulnapp](/img/asset/YXNzZXRzL3dhZl92dWxuYXBwLTE2NzA1MjExNjkucG5n/waf_vulnapp-1670521169.png?fm=webp&fit=crop&s=fa964fe61228b7bd9ce5e7fb74e4810d) __ The vulnerable Flask web application we created.

Lastly, we started sending hundreds of specially crafted requests to try and analyze how the WAF flags requests as malicious.

![waf malicious SQL](/img/asset/YXNzZXRzL3dhZl9tYWxzcWxpcGF5bG9hZC0xNjcwNTIxMjAxLnBuZw/waf_malsqlipayload-1670521201.png?fm=webp&fit=crop&s=f10b314f77547b861e5de1dde0efb7fa) __ Requests the WAF flagged as malicious were blocked. In this request we pass a common SQLi payload, which is flagged by the WAF

From our testing, we concluded that in general, there are two methodologies for WAFs to flag a request as malicious:

  1. Search for blacklisted words: The WAF can search for words it recognizes as SQL syntax, and if too many matches exist in a request, it will flag the request as a malicious SQLi attempt.

  2. Parse SQL syntax from the request: The WAF can try and parse valid SQL syntax using different parts of the request. If the WAF successfully identifies SQL syntax, it will flag the request as a malicious SQLi attempt.

While most WAFs will use a combination of both methodologies in addition to anything unique the WAF does, they both have one common weakness: they require the WAF to recognize the SQL syntax. This triggered our interest and raised one major research question: what if we could find SQL syntax that no WAF would recognize?

### JSON in SQL

Our answer came quickly in the form of a (major) SQL feature: JSON. In modern times, JSON has become one of the predominant forms of data storage and transfer. In order to support JSON syntax and allow developers to interact with data in similar ways to how they interact with it in other applications, JSON support was needed in SQL.

Currently all major relational database engines support native JSON syntax; this includes MSSQL, PostgreSQL, SQLite, and MySQL. Furthemore, in the latest versions, all database engines enable JSON syntax by default, meaning it is prevalent in most database setups today.

Developers have chosen to use JSON features within SQL databases since its availability for a number of reasons, starting with better performance and efficiency. Since many backends already work with JSON data, performing all data manipulation and transition on the SQL engine itself reduces the number of database calls needed. Furthermore, if the database can work with the JSON data format, which the backend API most likely uses as well, less data preprocessing and postprocessing is required, allowing the application to use it immediately without the need to convert it first.

By using JSON in SQL, an application can fetch data, combine multiple sources from within the database, perform data modification and transform it to JSON format—all within the SQL API. Then, the application can receive the JSON-formatted data and work with it immediately, without processing the data as well.

![waf input table](/img/asset/YXNzZXRzL3dhZl9pbnB1dHRhYmxlLnBuZw/waf_inputtable.png?fm=webp&fit=crop&s=2814011d2b63c9394fea5bd4188759dd) __ The data flow of using JSON in SQL, allowing developers to use JSON API within SQL to better interact with the data.

While each database chose a different implementation and JSON parser, each supports a different range of JSON functions and operators. Also, they all support the JSON data type and basic JSON searches and modifications.

![{JS-ON: Security-OFF}: Abusing JSON-Based SQL to Bypass WAF](/img/asset/YXNzZXRzL2NsYXJvdHktYmxvZy1ncmFwaGljc18xMi0yMi0wMS5wbmc/claroty-blog-graphics_12-22-01.png?fm=webp&fit=crop&s=4296eb124eaef7aa05b4c36a9c5618f7) __ Levels of JSON support for each major database.

However, even though all database engines added support for JSON, not all security tools added support for this “new” feature (which was added as early as 2012). This lack of support in security tools could introduce a mismatch in parsing primitives between the security tool (in our case, the WAF) and the actual database engines, and cause SQL syntax misidentification.

### The New ‘ or ‘a’=’a

Using JSON syntax, it is possible to craft new SQLi payloads. These payloads, since they are not commonly known, could be used to fly under the radar and bypass many security tools. Using syntax from different database engines, we were able to compile the following list of true statements in SQL:

  * PostgreSQL: `'{"b":2}'::jsonb <@ '{"a":1, "b":2}'::jsonb` Is the left JSON contained in the right one? `True`.

  * SQLite: `'{"a":2,"c":[4,5,{"f":7}]}' -> '$.c[2].f' = 7` Does the extracted value of this JSON equals 7? `True`. 

  * MySQL: `JSON_EXTRACT('{"id": 14, "name": "Aztalan"}', '$.name') = 'Aztalan'` Does the extracted value of this JSON equals to ‘Aztalan’? `True`.

### Armed With JSON Syntax

From our understanding of how a WAF could flag requests as malicious, we reached the conclusion that we need to find SQL syntax the WAF will not understand. If we could supply a SQLi payload that the WAF will not recognize as valid SQL, but the database engine will parse it, we could actually achieve the bypass.

As it turns out, JSON was exactly this mismatch between the WAF’s parser and the database engine. When we passed valid SQL statements that used less prevalent JSON syntax, the WAF actually did not flag the request as malicious.

![waf sqlbypass](/img/asset/YXNzZXRzL3dhZl9zcWxpYnlwYXNzLTE2NzA1MjEyMzkucG5n/waf_sqlibypass-1670521239.png?fm=webp&fit=crop&s=992901a4aa197461ef2bd201f2d5652c) __ Here is a malicious SQLi payload, containing JSON syntax. As we can see, the WAF did not flag the request as malicious and did not drop it.

This simple JSON operator, `@>` in this case, which checks whether the right JSON is contained in the left one, above, threw the WAF into a loop and allowed us to supply malicious SQLi payloads, allowing us to bypass the WAF. By simply prepending simple JSON syntax to the start of the request, we were able to exfiltrate sensitive information using our SQLi vulnerability over the cloud!

![waf expolit](/img/asset/YXNzZXRzL3dhZl9leHBsb2l0LnBuZw/waf_exploit.png?fm=webp&fit=crop&s=d96c855e8eafba43144f6805ba009925) __ Exploitation of an SQL Injection vulnerability over the cloud.

## Dream Big: A Generic WAF Bypass

After demonstrating our bypass over Amazon AWS WAF, we wondered: “Maybe we have a bigger issue at hand?” The core issue of this bypass was a lack of conformance between the database engines and SQLi detection solutions; this is because JSON in SQL is not such a popular and well-known feature, and its syntax was not added to the WAF parser.

However we thought that maybe this issue is not relevant for this WAF vendor alone, maybe other vendors have not added support for JSON syntax as well. So we took our vulnerable web application, and created a setup on most major WAF vendors. After a long few days, we discovered that JSON syntax could be used to bypass most vendors we checked:

  * Palo-Alto Next Generation Firewall

  * F5 Big-IP

  * Amazon AWS ELB

  * Cloudflare

  * Imperva

![waf vendors](/img/asset/YXNzZXRzL3dhZl92ZW5kb3JzLnBuZw/waf_vendors.png?fm=webp&fit=crop&s=38a1f12db18b030cd5282698ecd26d89) __ List of WAF vendors and products we managed to bypass using JSON syntax.

One vendor's WAF that was immune to our attack was Check Point's [CloudGuard AppSec](https://www.checkpoint.com/cloudguard/appsec/) and [open-appsec](https://www.openappsec.io/), which we verified already had mitigations in place to stop our attack technique. 

Meanwhile, the fact we managed to bypass so many big WAF products, with limited if any changes to our payload meant we had a generic WAF bypass on our hands. This means that even without knowing exactly what WAF lies between us and our target, we can still exploit a SQL injection vulnerability, bypassing the WAF’s protection. 

## Automating The Process

In order to showcase how big this WAF bypass is, we decided to add support for JSON syntax evasion techniques to the biggest open-source exploitation tool, [SQLMap](https://github.com/sqlmapproject/sqlmap). 

![waf sql map](/img/asset/YXNzZXRzL3dhZl9zcWxtYXAucG5n/waf_sqlmap.png?fm=webp&fit=crop&s=a36e6b67ee4c6d4c4c9530e031a25e19) __ The SQLMap tool allows users to automate and attack targets.

SQLMap offers an automatic process of SQL injection exploitation, allowing users to scan entire sites for a vulnerability. After SQLMap identifies a SQL vulnerability, it offers the ability to both fingerprint the vulnerability type and to identify an exploitation technique best suited to this specific vulnerability. 

After correctly choosing the technique to exploit the vulnerability, SQLMap even offers users the ability to automatically dump information stored in the database, enumerate tables and databases, exfiltrate password hashes, and perform a few post-exploitation techniques.

While SQLMap offers some WAF evasion techniques, we found that it is still easily identified by most modern WAFs, meaning that users cannot use it in cases where a WAF is present.

![waf sql map bypass](/img/asset/YXNzZXRzL3dhZl9zcWxtYXBieXBhc3MtMTY3MDUxODE3MS5wbmc/waf_sqlmapbypass-1670518171.png?fm=webp&fit=crop&s=10d94389c2ddf3e8d658ce85b0292651) __ Trying to execute SQLMap on an application protected by a WAF. We can clearly see that even though the application is vulnerable, SQLMap does not deem it exploitable since most requests are dropped by the WAF.

Our goal was to bring this new technique into SQLMap, and to use JSON syntax in order to bypass WAFs. In order to do so, we injected payloads generated by SQLMap, adding randomly generated JSON syntax. Since every database engine implemented a different set of JSON functions and operators, we implemented a separate script for each database engine. Using our addition to SQLMap, we were able to bypass a well-known WAF and successfully exploit a vulnerable web application.

![waf evasion](/img/asset/YXNzZXRzL3dhZl9ldmFzaW9uLnBuZw/waf_evasion.png?fm=webp&fit=crop&s=b042c559f6e57e213418533bf5f1dfa6) __ Running SQLMap using our script allowed SQLMap to successfully exploit the vulnerable web application and to bypass the WAF.

If you would like to use this script in order to test this bypass, simply clone the latest version of [SQLMap](https://github.com/sqlmapproject/sqlmap) from Github.

> A demo of Team82's WAF bypass. 

## Conclusion

Team82’s novel attack technique effectively bypasses the ability of a web application firewall to adequately detect SQL injection attacks. We did so through a complex journey that began with unrelated research that was being thwarted by a web application firewall, setting off a chain of events leading to our generic WAF bypass. 

We discovered that the leading vendors’ WAFs did not support JSON syntax in their SQL injection inspection process, allowing us to prepend JSON syntax to a SQL statement that blinded a WAF to the malicious code. 

Team82 disclosed its findings to five of the leading WAF vendors, all of which have added JSON syntax support to their products. We believe that other vendors’ products may be affected, and that reviews for JSON support should be carried out. Below are Amazon’s and F5’s acknowledgements and fixes, for example. 

![waf aws](/img/asset/YXNzZXRzL3dhZl9hd3MtMTY3MDUyMTI4NS5wbmc/waf_aws-1670521285.png?fm=webp&fit=crop&s=8c6a3c5dff33573eea7f8c206fc2ea69) __ AWS release notes for the Amazon AWS ELB ruleset, adding support for JSON syntax in SQLi inspection and blocking this bypass. ![waf f5](/img/asset/YXNzZXRzL3dhZl9mNS5wbmc/waf_f5.png?fm=webp&fit=crop&s=2ac72b40acac8ca4a5b2832b36953f89) __ F5 SIRT Security Acknowledgment of F5 BIG-IP, adding support for JSON syntax in SQLi inspection.

This is a dangerous bypass, especially as more organizations continue to migrate more business and functionality to the cloud. IoT and OT processes that are monitored and managed from the cloud may also be impacted by this issue, and organizations should ensure they’re running updated versions of security tools in order to block these bypass attempts.

Share

[ __ LinkedIn ](https://www.linkedin.com/shareArticle/?url=https://claroty.com/team82/research/js-on-security-off-abusing-json-based-sql-to-bypass-waf) [ __ Twitter ](https://twitter.com/intent/post?text={JS-ON: Security-OFF}: Abusing JSON-Based SQL to Bypass WAF&url=https://claroty.com/team82/research/js-on-security-off-abusing-json-based-sql-to-bypass-waf) [ __ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://claroty.com/team82/research/js-on-security-off-abusing-json-based-sql-to-bypass-waf) [ __ ](mailto:?subject={JS-ON: Security-OFF}: Abusing JSON-Based SQL to Bypass WAF&body=https://claroty.com/team82/research/js-on-security-off-abusing-json-based-sql-to-bypass-waf)

![](https://claroty.com/build/assets/team82-newsletter-bg-BlXIsUMi.jpg)

Stay in the know Get the Team82 Newsletter

Share

[ __ LinkedIn ](https://www.linkedin.com/shareArticle/?url=https://claroty.com/team82/research/js-on-security-off-abusing-json-based-sql-to-bypass-waf) [ __ Twitter ](https://twitter.com/intent/post?text={JS-ON: Security-OFF}: Abusing JSON-Based SQL to Bypass WAF&url=https://claroty.com/team82/research/js-on-security-off-abusing-json-based-sql-to-bypass-waf) [ __ Facebook ](https://www.facebook.com/sharer/sharer.php?u=https://claroty.com/team82/research/js-on-security-off-abusing-json-based-sql-to-bypass-waf) [ __ ](mailto:?subject={JS-ON: Security-OFF}: Abusing JSON-Based SQL to Bypass WAF&body=https://claroty.com/team82/research/js-on-security-off-abusing-json-based-sql-to-bypass-waf)

Recent Vulnerability Disclosures

  * ##### [CVE-2026-28256 A Use of Hard-coded, Security-relevant Constants vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an attacker to disclose sensitive information and take over accounts. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 5.8 ](/team82/disclosure-dashboard/cve-2026-28256)
  * ##### [CVE-2026-28255 A Use of Hard-coded Credentials vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an attacker to disclose sensitive information and take over accounts. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 6.8 ](/team82/disclosure-dashboard/cve-2026-28255)
  * ##### [CVE-2026-28254 A Missing Authorization vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an unauthenticated attacker to access sensitive information through unprotected APIs. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 5.8 ](/team82/disclosure-dashboard/cve-2026-28254)
  * ##### [CVE-2026-28253 A Memory Allocation with Excessive Size Value vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an unauthenticated attacker to cause a denial-of-service condition. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 7.5 ](/team82/disclosure-dashboard/cve-2026-28253)
  * ##### [CVE-2026-28252 A Use of a Broken or Risky Cryptographic Algorithm vulnerability in Trane Tracer SC, Tracer SC+, and Tracer Concierge could allow an attacker to bypass authentication and gain root-level access to the device. Successful exploitation of these vulnerabilities could allow an attacker to disclose sensitive information, execute arbitrary commands, or perform a denial-of-service on the product. The following versions of Trane Tracer SC, Tracer SC+, and Tracer Concierge are affected:
  * Tracer SC
  * Tracer SC+
  * Tracer Concierge
Trane asks Tracer SC+ users to upgrade to version v6.30.2313 CVSS v3: 8.1 ](/team82/disclosure-dashboard/cve-2026-28252)

Solutions

  * [Claroty xDome Platform](/platform)
  * [Industrial Cybersecurity](/industrial-cybersecurity)
  * [Healthcare Cybersecurity](/healthcare-cybersecurity)
  * [Commercial Cybersecurity](/commercial-cybersecurity)
  * [Public Sector Cybersecurity](/public-sector-cybersecurity)

Threat Research

  * [Team82 Home](/team82)
  * [Vulnerability Disclosure Dashboard](/team82/disclosure-dashboard)
  * [Research](/team82/research)
  * [PGP Key](/team82/pgp-key)

Partners

  * [Partners](/partners)
  * [Technology Alliance Partners](/partners/technology-alliances)
  * [Channel Partners](/partners/channel-partners)
  * [Become a Partner](https://portal.claroty.com/#/page/partner-reg)
  * [Partner Login](https://portal.claroty.com/#/page/login)

Resources

  * [Resource Library](/resources)
  * [Blog](/blog)
  * [White Papers](/resources/white-papers)
  * [Reports](/resources/reports)
  * [Case Studies](/resources/case-studies)
  * [Datasheets](/resources/datasheets)
  * [Integration Briefs](/resources/integration-briefs)
  * [Videos](https://www.youtube.com/@claroty20)
  * [Claroty Nexus](https://nexusconnect.io)

Company

  * [About Us](/company)
  * [Careers](/careers)
  * [Leadership](/leadership)
  * [Newsroom](/newsroom)
  * [xCel Enablement & Training](/xcel-enablement-and-training)
  * [Trust Center](/trust)
  * [Customer Experience](/customer-experience)
  * [Events](/event-listing)
  * [Environmental, Social, and Governance Policies](/environmental-social-and-governance-policies)
  * [Contact Us](/contact-us)

[ ![Claroty](https://claroty.com/build/assets/logo-white-VeF9EwMy.svg) ](/)

© 2026 Claroty. All rights reserved.

[ __ LinkedIn ](https://www.linkedin.com/company/claroty/) [ __ Twitter ](https://twitter.com/claroty) [ __ YouTube ](https://www.youtube.com/@claroty20) [ __ Facebook ](https://www.facebook.com/ClarotyOT/)

[Terms & Conditions](/terms-conditions) / [Privacy Policy](/privacy-policy)

__ Close Modal ![cnmaestro](/img/asset/YXNzZXRzL2NubWFlc3Ryby0xNjcwNTE2OTgxLnBuZw/cnmaestro-1670516981.png?fm=webp&fit=crop&s=594771dda26b7d2b7b99b4c011f09471)

__ Close Modal ![cnMaestro workflow](/img/asset/YXNzZXRzL2NsYXJvdHktYmxvZy1ncmFwaGljc18xMi0yMi0wMi5wbmc/claroty-blog-graphics_12-22-02.png?fm=webp&fit=crop&s=4e791607e6842675a91d0d1baa7795ab)

__ Close Modal ![waf sink point](/img/asset/YXNzZXRzL3dhZl9zaW5rLXBvaW50LTE2NzA1MjA3NzMucG5n/waf_sink-point-1670520773.png?fm=webp&fit=crop&s=dab2413eee0ddfb4d2bfffac15e53936)

__ Close Modal ![waf select ascii](/img/asset/YXNzZXRzL3dhZl9zZWxlY3Rhc2NpaS0xNjcwNTIwODQxLnBuZw/waf_selectascii-1670520841.png?fm=webp&fit=crop&s=2b389ed66c46956af081692eef4455b7)

__ Close Modal ![waf test](/img/asset/YXNzZXRzL3dhZl90ZXN0YXNjaWkucG5n/waf_testascii.png?fm=webp&fit=crop&s=1f34046a0fe156e0cebf1a8ce13a5993)

__ Close Modal ![waf select ascii](/img/asset/YXNzZXRzL3dhZl9zZWxlY3RjLTE2NzA1MjA5NTEucG5n/waf_selectc-1670520951.png?fm=webp&fit=crop&s=916d14492b3c74ab8d0220bef21b1b6f)

__ Close Modal ![waf test index](/img/asset/YXNzZXRzL3dhZl90ZXN0aW5kZXgyLTE2Njk5MjAyOTAucG5n/waf_testindex2-1669920290.png?fm=webp&fit=crop&s=bae325c920dbc3853e191a95ca9c23b7)

__ Close Modal ![waf numeric types](/img/asset/YXNzZXRzL3dhZl9udW1lcmljLXR5cGVzLnBuZw/waf_numeric-types.png?fm=webp&fit=crop&s=1c2738fdc5069ca2c258ff7c520fd2f3)

__ Close Modal ![waf select id](/img/asset/YXNzZXRzL3dhZl9zZWxlY3RpZC0xNjcwNTIxMTI2LnBuZw/waf_selectid-1670521126.png?fm=webp&fit=crop&s=a9fa457b6016b3f3d13079e2491c2de2)

__ Close Modal ![waf testsss](/img/asset/YXNzZXRzL3dhZl90ZXN0c3NzLnBuZw/waf_testsss.png?fm=webp&fit=crop&s=53bdea3a0e8515e2cb100dfca7eda410)

__ Close Modal ![waf evasion](/img/asset/YXNzZXRzL2NsYXJvdHktYmxvZy1ncmFwaGljc18xMi0yMi0wNC5wbmc/claroty-blog-graphics_12-22-04.png?fm=webp&fit=crop&s=7a764b24879c14029500c618cc82b796)

__ Close Modal ![waf cookie](/img/asset/YXNzZXRzL3dhZl9jb29raWUucG5n/waf_cookie.png?fm=webp&fit=crop&s=6cabe0c57f546f09531207dc38d1e4b5)

__ Close Modal ![waf 403](/img/asset/YXNzZXRzL3dhZl80MDMtZm9yYmlkZGVuLnBuZw/waf_403-forbidden.png?fm=webp&fit=crop&s=0aa8830751f943350946926ef9a775cf)

__ Close Modal ![waf addsql](/img/asset/YXNzZXRzL3dhZl9hZGRzcWwucG5n/waf_addsql.png?fm=webp&fit=crop&s=88ae6e4ab3f3a63535c94e43dfbc77b1)

__ Close Modal ![waf vulnapp](/img/asset/YXNzZXRzL3dhZl92dWxuYXBwLTE2NzA1MjExNjkucG5n/waf_vulnapp-1670521169.png?fm=webp&fit=crop&s=fa964fe61228b7bd9ce5e7fb74e4810d)

__ Close Modal ![waf malicious SQL](/img/asset/YXNzZXRzL3dhZl9tYWxzcWxpcGF5bG9hZC0xNjcwNTIxMjAxLnBuZw/waf_malsqlipayload-1670521201.png?fm=webp&fit=crop&s=f10b314f77547b861e5de1dde0efb7fa)

__ Close Modal ![waf input table](/img/asset/YXNzZXRzL3dhZl9pbnB1dHRhYmxlLnBuZw/waf_inputtable.png?fm=webp&fit=crop&s=2814011d2b63c9394fea5bd4188759dd)

__ Close Modal ![{JS-ON: Security-OFF}: Abusing JSON-Based SQL to Bypass WAF](/img/asset/YXNzZXRzL2NsYXJvdHktYmxvZy1ncmFwaGljc18xMi0yMi0wMS5wbmc/claroty-blog-graphics_12-22-01.png?fm=webp&fit=crop&s=4296eb124eaef7aa05b4c36a9c5618f7)

__ Close Modal ![waf sqlbypass](/img/asset/YXNzZXRzL3dhZl9zcWxpYnlwYXNzLTE2NzA1MjEyMzkucG5n/waf_sqlibypass-1670521239.png?fm=webp&fit=crop&s=992901a4aa197461ef2bd201f2d5652c)

__ Close Modal ![waf expolit](/img/asset/YXNzZXRzL3dhZl9leHBsb2l0LnBuZw/waf_exploit.png?fm=webp&fit=crop&s=d96c855e8eafba43144f6805ba009925)

__ Close Modal ![waf vendors](/img/asset/YXNzZXRzL3dhZl92ZW5kb3JzLnBuZw/waf_vendors.png?fm=webp&fit=crop&s=38a1f12db18b030cd5282698ecd26d89)

__ Close Modal ![waf sql map](/img/asset/YXNzZXRzL3dhZl9zcWxtYXAucG5n/waf_sqlmap.png?fm=webp&fit=crop&s=a36e6b67ee4c6d4c4c9530e031a25e19)

__ Close Modal ![waf sql map bypass](/img/asset/YXNzZXRzL3dhZl9zcWxtYXBieXBhc3MtMTY3MDUxODE3MS5wbmc/waf_sqlmapbypass-1670518171.png?fm=webp&fit=crop&s=10d94389c2ddf3e8d658ce85b0292651)

__ Close Modal ![waf evasion](/img/asset/YXNzZXRzL3dhZl9ldmFzaW9uLnBuZw/waf_evasion.png?fm=webp&fit=crop&s=b042c559f6e57e213418533bf5f1dfa6)

__ Close Modal ![waf aws](/img/asset/YXNzZXRzL3dhZl9hd3MtMTY3MDUyMTI4NS5wbmc/waf_aws-1670521285.png?fm=webp&fit=crop&s=8c6a3c5dff33573eea7f8c206fc2ea69)

__ Close Modal ![waf f5](/img/asset/YXNzZXRzL3dhZl9mNS5wbmc/waf_f5.png?fm=webp&fit=crop&s=2ac72b40acac8ca4a5b2832b36953f89)

![Claroty](https://claroty.com/build/assets/logo-white-VeF9EwMy.svg) __ Close Menu

  * [Platform](/platform) __

[The Claroty Platform](/platform) [Claroty CPS Protection Program](/cps-protection-program) [Claire, the AI Security Agent](/claire) [Asset Inventory](/platform/asset-inventory) [Exposure Management](/platform/exposure-management) [Network Protection](/platform/network-protection) [Secure Access](/platform/secure-access) [Threat Detection](/platform/threat-detection) [Operational Efficiency](/platform/operational-efficiency) [Integrations](/platform/integrations)

  * [Industries]() __

[Industrial Home](/industrial-cybersecurity) [Industrial Verticals](/industrial-cybersecurity/verticals) [Healthcare Home](/healthcare-cybersecurity) [Commercial Home](/commercial-cybersecurity) [Commercial Verticals](/commercial-cybersecurity/verticals)

  * [Public Sector](/public-sector-cybersecurity) __

[Public Sector Home](/public-sector-cybersecurity) [Federal Government Home](/public-sector-cybersecurity/us-government-cybersecurity) [SLED Home](/public-sector-cybersecurity/sled-government-cybersecurity)

  * [Customers](/customer-experience) __

[Customer Experience](/customer-experience) [Case Studies](/resources/case-studies) [xCel Enablement & Training for Customers](/xcel-enablement-and-training-for-customers)

  * [Partners](/partners) __

[Partners](/partners) [Technology Alliance Partners](/partners/technology-alliances) [Channel Partners](/partners/channel-partners) [Partner Login](https://portal.claroty.com/#/page/login)

  * [Threat Research](/team82) __

[Team82 Home](/team82) [Threat Intelligence](/threat-intelligence) [Vulnerability Disclosure Dashboard](/team82/disclosure-dashboard) [Research](/team82/research) [Talks](/team82/talks) [PGP Key](/team82/pgp-key)

  * [Resources](/resources) __

[Blog](/blog) [Reports](/resources/reports) [White Papers](/resources/white-papers) [Datasheets & Solution Overviews](/resources/datasheets) [Integration Briefs](/resources/integration-briefs) [Case Studies](/resources/case-studies) [On-Demand Webinars](/resources/webinars) [Visit our Nexus Website](https://nexusconnect.io)

  * [Company](/company) __

[About Us](/company) [Careers](/careers) [Leadership](/leadership) [Newsroom](/newsroom) [xCel Enablement & Training](/xcel-enablement-and-training) [Trust Center](/trust) [Events](/event-listing) [Environmental, Social, and Governance Policies](/environmental-social-and-governance-policies) [Contact Us](/contact-us)

  * [__Search](/search)

[ __ LinkedIn ](https://www.linkedin.com/company/claroty/) [ __ Twitter ](https://twitter.com/claroty) [ __ YouTube ](https://www.youtube.com/@claroty20) [ __ Facebook ](https://www.facebook.com/ClarotyOT/)
