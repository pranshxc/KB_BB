---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-08_comodo-from-git-to-takeover.md
original_filename: 2022-11-08_comodo-from-git-to-takeover.md
title: 'Comodo: From .Git to Takeover'
category: documents
detected_topics:
- access-control
- command-injection
tags:
- imported
- documents
- access-control
- command-injection
language: en
raw_sha256: 670e763fbdbd8aa1b5eb6db8b933b4789e5e1f3f6e869caded15dfb4888567ef
text_sha256: 726e08715990b230cd19606686583125d7a0497434dacf2bc0be4096d9c97548
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: false
---

# Comodo: From .Git to Takeover

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-08_comodo-from-git-to-takeover.md
- Source Type: markdown
- Detected Topics: access-control, command-injection
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: False
- Raw SHA256: `670e763fbdbd8aa1b5eb6db8b933b4789e5e1f3f6e869caded15dfb4888567ef`
- Text SHA256: `726e08715990b230cd19606686583125d7a0497434dacf2bc0be4096d9c97548`


## Content

---
title: "Comodo: From .Git to Takeover"
url: "https://maordayanofficial.medium.com/comodo-from-git-to-takeover-803ffb8b57e3"
authors: ["Maor Dayan (@mord1234)"]
programs: ["Comodo"]
bugs: [".git folder disclosure"]
publication_date: "2022-11-08"
added_date: "2022-11-11"
source: "pentester.land/writeups.json"
original_index: 1939
scraped_via: "browseros"
---

# Comodo: From .Git to Takeover

Comodo: From .Git to Takeover
Maor Dayan - מאור דיין
Follow
4 min read
·
Nov 9, 2022

66

Understanding Comodo Security Solutions, Inc.

Comodo Security Solutions, Inc., headquartered in Clifton, New Jersey, USA, is a leading cybersecurity company. known for its certificate authority operations, Comodo issues SSL certificates and delivers comprehensive information security products tailored for enterprises and consumers alike. The company has also made significant contributions to standard-setting efforts, including the Internet Engineering Task Force (IETF) DNS Certification Authority Authorization (CAA) Resource Record.

Vulnerability Analysis: Git Source Code Exposure

What is Git Source Code Exposure Vulnerability?

Git Source Code Exposure Vulnerability arises when an application fails to safeguard sensitive data embedded within its source code, such as intellectual property, database passwords, and secret keys. This vulnerability typically results from web server misconfigurations or typographical errors in scripts, such as granting executable permissions to certain directories or scripts. One common method of exploitation involves an exposed .git folder on the web server.

Risks of an Exposed Git Folder

When a .git folder is deployed along with a web application, attackers can exploit this misconfiguration to download the entire source code, including sensitive data. This vulnerability poses significant risks, as it can lead to intellectual property theft and unauthorized access to critical information.

Case Study: Comodo Forum Vulnerability

The vulnerability, now remediated, was identified on the Comodo Forum domain:

https://forums.comodo.com/.git/config

Get Maor Dayan - מאור דיין’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

The Comodo Forum serves as a platform for support, updates, and interactions between regular users, clients and Comodo support staff and volunteers. Given the forum’s role, the exposure of sensitive data even on a subdomain could have critical implications. An attacker exploiting this .git folder could have potentially downloaded the complete source code of Comodo’s Forum, and do a lot more! posing a substantial security threat.

Comodo Forum Source Code (was not saved and was removed after the report for Comodo security team!)
Exploitation Details

During the analysis, it was discovered that an unauthorized shell had been inadvertently left within the exposed files. This oversight allowed for a rapid escalation of the attack. Leveraging the shell, I was able to create new files and gain comprehensive access to the forum’s system. This access extended beyond the initial data obtained via the .git folder vulnerability, providing up-to-date information, including current database details.

Press enter or click to view image in full size
Connected to the database (POC):

for security reasons, I have to hide most of the data from the screenshots.

Again for clarification, nothing has been saved! and all information has been sent to Comodo security team

With all these options in the hands of a black hat hacker, this is a full takeover of their forum system!

Conclusion:
An attacker could of :

Download — Download everything including the database.
Remove files — Remove everything including the database.
Add & Edit files — an attacker could edit and insert to an existing page for example the index page a malicious file or code to infect Comodo’s clients, users, and employees.
and a lot more.

How to fix it?

Very simple in this case, before and after deploying your code always check for hidden files and folders, usually on servers because there is a dot before the .Git the folder becomes hidden. Yes, that's simple but many don’t check it until it’s too late.

Notes & information:

I hope you enjoyed reading and learning, Usually, I write articles/blogs once in a while, and not that often.

Nothing from the next examples has been downloaded and if so nothing has been saved, all have been screenshotted for the Security team of Comodo, which has not replied to any of my reports but all have been fixed a couple of hours/days after my reports, all of the shells were reported to Comodo.

But ! because I do not know for sure how the ‘not-that-good’ shell was uploaded to the server in the first place there is a significant risk until Comodo’s security team will take care of it!

The vulnerabilities has been fixed a couple of hours after my reports and some after a couple of days and a lot of urgent emails from me, but again Comodo Security team does not answer any emails, or tickets right away, and sometimes can take a couple of months or not at all.

Press enter or click to view image in full size
