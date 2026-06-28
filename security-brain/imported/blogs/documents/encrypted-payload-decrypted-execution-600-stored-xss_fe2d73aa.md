---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-25_encrypted-payload-decrypted-execution-600-stored-xss.md
original_filename: 2021-03-25_encrypted-payload-decrypted-execution-600-stored-xss.md
title: 'Encrypted Payload -> Decrypted Execution ($600) : Stored XSS'
category: documents
detected_topics:
- xss
- command-injection
tags:
- imported
- documents
- xss
- command-injection
language: en
raw_sha256: fe2d73aa5f9eb709cb443e0d5003150841ebcc2ba4eb5205e7ec9576a1ce9323
text_sha256: 1ddb60e2b5c672be19a4e4618e77d7c6414b5a606bcf94ca086cad1d9638bb79
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Encrypted Payload -> Decrypted Execution ($600) : Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-25_encrypted-payload-decrypted-execution-600-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, command-injection
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `fe2d73aa5f9eb709cb443e0d5003150841ebcc2ba4eb5205e7ec9576a1ce9323`
- Text SHA256: `1ddb60e2b5c672be19a4e4618e77d7c6414b5a606bcf94ca086cad1d9638bb79`


## Content

---
title: "Encrypted Payload -> Decrypted Execution ($600) : Stored XSS"
url: "https://shrirangdiwakar.medium.com/encrypted-payload-decrypted-execution-600-stored-xss-3e517cea8f13"
authors: ["Shrirang Diwakar"]
bugs: ["Stored XSS"]
bounty: "600"
publication_date: "2021-03-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3790
scraped_via: "browseros"
---

# Encrypted Payload -> Decrypted Execution ($600) : Stored XSS

Encrypted Payload -> Decrypted Execution ($600) : Stored XSS
Shrirang Diwakar
Follow
3 min read
·
Mar 25, 2021

151

Hello Hunters, This is a Tale of how I used an Application’s feature against itself to give rise to a Stored Cross Site Scripting Vulnerability. So relax and Enjoy the article ❤

Damn Excited to share this story…..😍

Let’s Begin

Cross site scripting (XSS) is a common attack vector that injects malicious code into a vulnerable web application. Stored XSS are the most dangerous of all. To successfully execute a stored XSS attack, a perpetrator has to locate a vulnerability in a web application and then inject malicious script into its server.
Unlike Reflected, The attacker does not need to find an external way of inducing other users to make a particular request containing their exploit. Rather, the attacker places their exploit into the application itself and simply waits for users to encounter it.

Summary :

The Web Application was a Server Hosting Management System with 24x7 support, Datacentre facilities, etc. The Application had a feature to create Support tickets for technical Support, server hosting support, Billing support, etc. Admins, technical support team members along with the application’s support team were now involved in a conversation. Here, we can raise our questions which were resolved by the support, similar like a Chat feature.

Get Shrirang Diwakar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If any sensitive information such as passwords needed to be sent, an Encryption feature was added where any member can encrypt the message and send as a reply to the support ticket, which when clicked was getting decrypted. So after analysing deeper, I figured out a way to use their own feature which encrypted my specially crafted payload & when clicked got executed giving rise to a Stored Cross Site Scripting Vulnerability.

Steps Followed :
Created a Support Ticket
Analysed the “Encrypt Message” feature and figured out that the Encrypted message was decrypted on click in a <textarea> tag
Also, the application didn’t allow alert, prompt or confirm functions but allowed Uppercased version of them
So, Crafted a special payload to first escape the tag, then input as uppercased “ALERT(1)” but processed as “alert(1)” due to specially crafted payload
Using the “Encrypt Message” feature, encrypted the payload & sent as a reply to the support ticket.
So if anyone from the support team, technical team or admin, clicks on the message (obviously would) to check the original content, it would be decrypted & the payload then got executed.
Now, all victims involved in the application were vulnerable to XSS on decrypting the message💯

Payload : </textarea><img src=x onerror=”var pop=’ALERT(document.cookie);’; eval(pop.toLowerCase());”

Hence, the title : Encrypted Payload -> Decrypted Execution 💯😎

The Submission was triaged and I got rewarded with a $600 bounty under P3 category because the affected actors were the Admins, Technical Support Team & the backend support, but the act that the technical team must be added by the admin is what lowered the possible impact 😁

That’s all for this Article, I Hope you guys enjoyed this form of learning ❤

Stay Safe 🤗

Follow my Instagram Creator account for more Bug Bounty & Ethical Hacking related content : https://www.instagram.com/shrirangdiwakar/ 😇

My LinkedIn: www.linkedin.com/in/shrirangdiwakar 🥰

Shower your love with the claps & share this with your friends ❣
