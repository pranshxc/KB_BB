---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-08-18_user-credential-are-sent-in-clear-text-in-whatsapp-web-fixed-facebook-bug-bounty.md
original_filename: 2018-08-18_user-credential-are-sent-in-clear-text-in-whatsapp-web-fixed-facebook-bug-bounty.md
title: User credential are sent in clear text in Whatsapp web— FIXED | Facebook Bug
  Bounty
category: documents
detected_topics:
- command-injection
tags:
- imported
- documents
- command-injection
language: en
raw_sha256: ccd501c8713ce1447c982d757e27cc435792f4282560250df5954d645ac4c64a
text_sha256: 8ec0b514939f2dadb3fac59943618953bf749eccd82b651921162d1b43eb41cd
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# User credential are sent in clear text in Whatsapp web— FIXED | Facebook Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-08-18_user-credential-are-sent-in-clear-text-in-whatsapp-web-fixed-facebook-bug-bounty.md
- Source Type: markdown
- Detected Topics: command-injection
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `ccd501c8713ce1447c982d757e27cc435792f4282560250df5954d645ac4c64a`
- Text SHA256: `8ec0b514939f2dadb3fac59943618953bf749eccd82b651921162d1b43eb41cd`


## Content

---
title: "User credential are sent in clear text in Whatsapp web— FIXED | Facebook Bug Bounty"
url: "https://medium.com/@Thuva11/user-credentials-are-sent-in-clear-text-fixed-facebook-bug-bounty-7f1e05ecedd9"
authors: ["Thuvarakan Nakarajah"]
programs: ["Meta / Facebook"]
bugs: ["Credentials sent over unencrypted channel"]
publication_date: "2018-08-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5745
scraped_via: "browseros"
---

# User credential are sent in clear text in Whatsapp web— FIXED | Facebook Bug Bounty

User credential are sent in clear text in Whatsapp web— FIXED | Facebook Bug Bounty
Thuvarakan Nakarajah
Follow
2 min read
·
Aug 18, 2018

6

INTRODUCTION

HTTPS (Hyper Text Transfer Protocol Secure) is the secure version of HTTP, the protocol over which data is sent between your browser and the website we are connected to. It means it encrypts all the communication between the browser and the website. All communication sent over HTTP connections are in ‘plain text’ and can be read by any hacker that manages to break into the connection between the browser and the website.

Confidential information such as user credentials and credit card information should not sent over the HTTP connection since it can be read by the hacker.

SCOPE

https://translate.whatsapp.com

DESCRIPTION

The website https://translate.whatsapp.com sends the user credentials. Hence this information should always be transferred via an encrypted channel (HTTPS) to avoid being intercepted by malicious users. If the user accesses the above website through HTTP, it should be redirected to HTTPS to make it secure which is referred to as Force HTTPS. I tested it on some browsers.

1. Chrome Browser

Get Thuvarakan Nakarajah’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If we access http://translate.whatsapp.com (HTTP — Not secure)

It automatically redirects to https://translate.whatsapp.com (HTTPS — Secured)

2. Epic Browser

But if we access http://translate.whatsapp.com (HTTP — Not secure) in the Epic Browser it does not redirecting to the HTTPS secured site. Hence if any user accesses the above website on Epic Browser, user credentials are transmitted over an unencrypted channel which can be read by any hacker that manages to break into the connection between the browser and the website.

Example URL

http://translate.whatsapp.com/sign-in?next

http://translate.whatsapp.com/sign-in?next=%2Flogin%2Ftwitter

So third party applications may be able to capture the user credentials by intercepting an unencrypted HTTP connection. Which is serious since the hacker gets full access to the user’s account by having the user credentials.

Facebook accept as vulnerability and awarded bounty amount also.

POC Link https://drive.google.com/file/d/1O_jpbTDSf2sVCa8-Fuse7c1vmLMIXIY1/view
