---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-05-05_mass-assignment-leads-to-the-victims-account-being-inaccessible-forever.md
original_filename: 2023-05-05_mass-assignment-leads-to-the-victims-account-being-inaccessible-forever.md
title: Mass Assignment leads to the victim’s account being inaccessible forever
category: documents
detected_topics:
- api-security
- idor
- command-injection
- rate-limit
- business-logic
tags:
- imported
- documents
- api-security
- idor
- command-injection
- rate-limit
- business-logic
language: en
raw_sha256: ba651124497868ce442b504ba43af53ee661e448011a93ad59f4dbd045746c9c
text_sha256: f1878b1b4e9729f85acf80be6e9218e68074ae7bbb104d5fa08c7c0c78a6998b
ingested_at: '2026-06-28T07:32:20Z'
sensitivity: unknown
redactions_applied: false
---

# Mass Assignment leads to the victim’s account being inaccessible forever

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-05-05_mass-assignment-leads-to-the-victims-account-being-inaccessible-forever.md
- Source Type: markdown
- Detected Topics: api-security, idor, command-injection, rate-limit, business-logic
- Ingested At: 2026-06-28T07:32:20Z
- Redactions Applied: False
- Raw SHA256: `ba651124497868ce442b504ba43af53ee661e448011a93ad59f4dbd045746c9c`
- Text SHA256: `f1878b1b4e9729f85acf80be6e9218e68074ae7bbb104d5fa08c7c0c78a6998b`


## Content

---
title: "Mass Assignment leads to the victim’s account being inaccessible forever"
url: "https://infosecwriteups.com/mass-assignment-leads-to-the-victims-account-being-inaccessible-forever-52e48c6a8a4d"
authors: ["Arman (@M7arm4n)"]
bugs: ["Mass assignment", "Logic flaw"]
publication_date: "2023-05-05"
added_date: "2023-05-08"
source: "pentester.land/writeups.json"
original_index: 1184
scraped_via: "browseros"
---

# Mass Assignment leads to the victim’s account being inaccessible forever

Mass Assignment leads to the victim’s account being inaccessible forever
M7arm4n
Follow
4 min read
·
May 4, 2023

324

2

Hi Guys, My name is m7arm4n and today I wanna talk about one of my findings on a private program that was vulnerable to Mass Assignment leads to make victim’s accounts inaccessible. I discovered many Mass Assignment in different programs and functions but this one is my favorite and the first one.

Press enter or click to view image in full size
What Is Mass Assignment Vulnerability?

Mass Assignment Vulnerability is a type of security weakness that can occur in web applications. Whereas the web application allows the user to change the object multiple times with a single request, without properly filtering or validating the input.

This vulnerability occurs because developers often use a feature in some web frameworks to automatically map incoming data to object properties. Attackers can exploit this feature by submitting specially crafted input that includes additional properties or modifying existing ones that were not intended to be modified. This may allow access to or modification of sensitive data including user account information, payment information, or other sensitive information.

For example, suppose a web application allows a user to update profile information, including name, email address, and password. If the developer does not prepare or validate the input properly, the attacker can send a request that includes additional parameters such as “isAdmin=true”, giving them administrative access to the application.

steps to reproduce

I skipped subdomain enumeration. when I reach the website registered as a normal user and after a few minutes, I understood the website had two endpoints to update the user’s data. One of them was for an email address which required a password to update it, Other one was only for first name and last name which does not require a password to update it.

Press enter or click to view image in full size
Press enter or click to view image in full size
Press enter or click to view image in full size

I tried to update the email to an existing email but unfortunately, I got an error.

Press enter or click to view image in full size

I thought a little differently and opened the Edit part to update the first name and last name and captured the update request in my Burp.

Press enter or click to view image in full size

I was looking for an interesting parameter to exploit, but the response was a redirection page that did not expose any hidden parameters in the response. I tried to add some interest parameters such as isAdmin, etc.

Get M7arm4n’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I added an Email parameter to the body and set a new email, Surprisingly my email updated to the new email.

Press enter or click to view image in full size

But the impact of this vulnerability till now is information/P5 and we should escalate this to something impactful. And I set up an existing victim’s email then forward it. Bingo I got success 😍🤯

My email address was updated to a victim’s email address, now let’s take check the victim’s account. On the victim side, I tried to log in with valid credentials but I got the error, tried to forget password? Nope, I got the same error.

Press enter or click to view image in full size
What Happened

We set the same email for 2 accounts. and when functions ask the database for email, the database does not return anything or returns two accounts which mean functions do not work correctly. Now, The victim's account is inaccessible forever :D

Thank you for following me here, Don’t forget to follow me for more write-ups.

Twitter 🐦
