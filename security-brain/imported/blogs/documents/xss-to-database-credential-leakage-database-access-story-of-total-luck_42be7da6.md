---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-06-06_xss-to-database-credential-leakage-database-access-story-of-total-luck.md
original_filename: 2020-06-06_xss-to-database-credential-leakage-database-access-story-of-total-luck.md
title: XSS to Database Credential Leakage & Database Access — Story of total luck!
category: documents
detected_topics:
- xss
- command-injection
- automation-abuse
- information-disclosure
- api-security
- supply-chain
tags:
- imported
- documents
- xss
- command-injection
- automation-abuse
- information-disclosure
- api-security
- supply-chain
language: en
raw_sha256: 42be7da64b6d66ea916573c20c75680ac6590914c19597b68457295434d9ca41
text_sha256: 60ee970201072f1b55347cea944b308175891d85a5970c31359d83efe1fad2e0
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# XSS to Database Credential Leakage & Database Access — Story of total luck!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-06-06_xss-to-database-credential-leakage-database-access-story-of-total-luck.md
- Source Type: markdown
- Detected Topics: xss, command-injection, automation-abuse, information-disclosure, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `42be7da64b6d66ea916573c20c75680ac6590914c19597b68457295434d9ca41`
- Text SHA256: `60ee970201072f1b55347cea944b308175891d85a5970c31359d83efe1fad2e0`


## Content

---
title: "XSS to Database Credential Leakage & Database Access — Story of total luck!"
url: "https://medium.com/bugbountywriteup/xss-to-database-credential-leakage-database-access-story-of-total-luck-77c990be8ab2"
authors: ["Harsh Bothra (@harshbothra_)"]
bugs: ["Reflected XSS", "Information disclosure"]
publication_date: "2020-06-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4521
scraped_via: "browseros"
---

# XSS to Database Credential Leakage & Database Access — Story of total luck!

Top highlight

XSS to Database Credential Leakage & Database Access — Story of total luck!
Harsh Bothra
Follow
3 min read
·
Jun 6, 2020

728

Press enter or click to view image in full size

Reflected Cross-Site Scripting happens when you provide a malicious javascript code to some input parsing functionality and due to lack of sanitization and filtration the application process your malicious code considering it as a valid input and thus, usually giving a popup of happiness.

However, when it is your lucky day and just for fun and learning you try to increase impact, and all of a sudden the server crashes, reveals the Database Credentials, your mind says only one thing “It’s a holy adventure time”.

Hi fellow hackers and enthusiasts, Today, I will be sharing my recent weird yet lucky experience which occurred accidentally while playing around with reflected XSS. Let’s call the target “redacted.com”.

The application “redacted.com” was having a blog website hosted on Wordpress at domain blog.redacted.com. When it comes to Wordpress, there are relatively fewer attack vectors that you can perform because it’s limiting, and being a third-party service you can not test for each and every functionality. Being lucky enough, I found a reflected XSS in Search Bar in a couple of minutes with this simple payload <img src=”x” onerror=alert(1)>.

That’s it? I just reported it and though to explore other areas of the application but no luck as such. I was getting bored so I planned to check for some of the new “XSS Payloads” discovered from online resources and Portswigger academy and see how they are working. I just ran intruder with all the payloads with maximum threads possible i.e. 999 and went away for a walk.

Get Harsh Bothra’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

When I came back and navigated to “blog.redacted.com” to check for XML-RPC and other stuff, I observed that the application is crashed and the error message revealed a “Database connection string containing Login Credentials”.

After fiddling around, trying to login via “wp-admin” endpoint, there was no luck but I reported it anyway. All of sudden, I again started performing recursive directory search and to my luck, I found “/server/phpmyadmin” directory accessible publically. I accessed the endpoint and found the PhpMyAdmin login page and I used the credentials revealed from Error Message and a Successful Login & Access to all databases.

Quickly added comments and updated my Initial Proof-of-Concept Reported. Triaged as P1 the same day and fixed in 3 days. :)

Probable Reason it Might have happened is while searching for and retrieving data from the database, the malicious javascript payload might have broken the MySQL query string logic resulting in a temporary error message until the cache expires.

Takeaways

If some functionality interacts with Database and you have found any bug on that functionality, just perform little stress testing IF ALLOWED. Some time due to improper handling, the backend logic may break temporary and error messages may reveal you interesting information.
You never know when is your lucky day, never stop looking for things. You’ll surely succeed.

If you liked the writeup, do clap and follow on Twitter to stay updated about new posts, tips, and tweets :D

Twitter: https://twitter.com/harshbothra_
