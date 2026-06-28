---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-11-07_stormshield-sns-cleartext-password-leak.md
original_filename: 2022-11-07_stormshield-sns-cleartext-password-leak.md
title: Stormshield SNS cleartext password leak
category: documents
detected_topics:
- sso
- command-injection
- automation-abuse
tags:
- imported
- documents
- sso
- command-injection
- automation-abuse
language: en
raw_sha256: e951952bc27bcfaf84007f1da3d4a7c04acbe8f1afe759232531cd616ca06db2
text_sha256: ef91857e656b9c8ce910c6e171a77f924100cc551dd5e2e13f2a42dc3f39d7c9
ingested_at: '2026-06-28T07:32:15Z'
sensitivity: unknown
redactions_applied: true
---

# Stormshield SNS cleartext password leak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-11-07_stormshield-sns-cleartext-password-leak.md
- Source Type: markdown
- Detected Topics: sso, command-injection, automation-abuse
- Ingested At: 2026-06-28T07:32:15Z
- Redactions Applied: True
- Raw SHA256: `e951952bc27bcfaf84007f1da3d4a7c04acbe8f1afe759232531cd616ca06db2`
- Text SHA256: `ef91857e656b9c8ce910c6e171a77f924100cc551dd5e2e13f2a42dc3f39d7c9`


## Content

---
title: "Stormshield SNS cleartext password leak"
url: "https://medium.com/@mehdi.alouache/stormshield-sns-cleartext-password-leak-b436ef312fe9"
authors: ["Mehdi Alouache"]
programs: ["Stormshield"]
bugs: ["Use of GET request Method With sensitive query strings"]
publication_date: "2022-11-07"
added_date: "2022-11-08"
source: "pentester.land/writeups.json"
original_index: 1942
scraped_via: "browseros"
---

# Stormshield SNS cleartext password leak

Stormshield SNS cleartext password leak
Mehdi Alouache
Follow
3 min read
·
Nov 7, 2022

12

Press enter or click to view image in full size

Foreword : the issue was privately disclosed to Stormshield. It is in their eyes a minor inconvenience but are not willing to address this as a vulnerability. Tested on SNS 4.3.7.

I stumbled on a very surprising behaviour on a Stormshield SNS login page.

When using Stormshield SSO modules, a user might want to login in order to get access to the company internal resources.

Press enter or click to view image in full size
Stormshield SNS login page

Several authentication methods are supported, such as LDAP(S) or SSL authentication for example. There is even a fallback mode : if the authentication is failing or timing out on method 1, SNS would try to authenticate on method 2, then method 3, etc…

Get Mehdi Alouache’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And this is where things start to become annoying. Let’s take the following scenario :

Authentication method 1 is LDAP(S)
Authentication method 2 is SSL certificate

User tries to authenticate, so SNS starts to authenticate with method 1 using a POST request.

A standard POST authentication request from SNS

If this method fails, the SNS will try to authenticate with the second method. And because SNS isn’t able to chain POST requests, it then switches to a GET request, containing both username and user password in cleartext.

Press enter or click to view image in full size
Failover GET authentication request with credentials in cleartext.
How can this be a security issue ?

If properly setup, the HTTP requests are encrypted with SSL/TLS and thus are not vulnerable to a sniffing attack. However, the GET request with the plaintext credentials can be found in two places :

In the user’s browser history
In your SIEM/EDR if you have TLS interception enabled
Additional details

The failover authentication only triggers if the first method fails. Reasons for the failure :

Service timeout (can happen, but low probability)
User types the wrong password

But if it triggers when he types the wrong password, how can this be a security concern ?

Well, usually there is 2 reasons to type the wrong password=***REDACTED*** did a typo (so the input is just 1 character inaccurate, easy to guess the real one)
User typed an old password or password from another application — and even if this is not his current domain password, this is still an entry point for a lateral movement.
