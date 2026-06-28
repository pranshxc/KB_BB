---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-11-16_ldap-admin-account-bypassed-.md
original_filename: 2019-11-16_ldap-admin-account-bypassed-.md
title: LDAP Admin Account Bypassed :)
category: documents
detected_topics:
- command-injection
- rate-limit
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- rate-limit
- automation-abuse
- api-security
language: en
raw_sha256: 4cac6edb4403005d6f67326861c23a26fa4e247cb642ae4c9b90b8be07f8441f
text_sha256: 1a211840a7a336b558bca78bc458fad7af525b2a630d4bc948799d8611e831dc
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: true
---

# LDAP Admin Account Bypassed :)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-11-16_ldap-admin-account-bypassed-.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: True
- Raw SHA256: `4cac6edb4403005d6f67326861c23a26fa4e247cb642ae4c9b90b8be07f8441f`
- Text SHA256: `1a211840a7a336b558bca78bc458fad7af525b2a630d4bc948799d8611e831dc`


## Content

---
title: "LDAP Admin Account Bypassed :)"
url: "https://medium.com/@himanshu_pdy/ldap-admin-account-bypassed-2cc8b264d66e"
authors: ["Himanshu Pdy (@himanshu_pdy)"]
bugs: ["LDAP injection", "Authentication bypass"]
publication_date: "2019-11-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4939
scraped_via: "browseros"
---

# LDAP Admin Account Bypassed :)

Top highlight

LDAP Admin Account Bypassed :)
himanshu pdy
Follow
3 min read
·
Nov 16, 2019

140

7

Introduction :

Hi guys! My name is Himanshu Pdy, and I am a security researcher. This is my first blog so ignore any grammatical mistake :)

About the issue:-

LDAP injection is an injection attack in which an attacker can insert malicious LDAP statements in to the original LDAP query used by an application. As a result, an attacker may be able to send malicious LDAP requests to the LDAP server which may lead to security implications such as reading or updating sensitive information. LDAP injections usually occur because an application fails to properly sanitize untrusted data which may come from an adversary.

Main Story:

Let’s take the target as “xyz.com”

So as usual i was doing recon on the target and it’s scope was limited (which is actually not good option for any noob like me).

So i was following 
Behrouz Sadeghipour
 method for recon and i found a sub-domain like “ldap.xyz.com”.

And it was simply showing an Ubuntu Apache page which is normal thing. But i don’t know why, i started testing on it for some purpose.

So i started using dirsearch and dirb, and i got some 200 status like robot.txt and some admin link. But using dirb and doing an intense directory search i manage to find the admin panel after some attempts.

link was :- ldap.xyz.com/phpldapadmin/htdocs/index.php

Next day i actually ask my friend Pratik Yadav in college “https://blog.usejournal.com/@pratiky054” about exploiting it and he said that he hasn’t exploited it ever but he gave me some really good idea about it.

On login Portal it was already showing username but i have to give password. I use a simple brute force method (one of the easiest way for a noob like me ). But there’s also no luck :(

Get himanshu pdy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I started searching for hackerone report for related issue but found none :(

So i read about ldap and other thing and used some command injection.

ldap.xyz.com/phpldapadmin/htdocs/index.php?login=

The username was having “cn” field which was vulnerable to ldap injection. Example:- Username= cn=admin dc=ldap dc=xyz dc=com & userPassword=***REDACTED***

Press enter or click to view image in full size

so i visited https://www.owasp.org/index.php/Testing_for_LDAP_Injection_%28OTG-INPVAL-006%29

And i used this command login=*)& Userpassword=***REDACTED***

And i got an unusual error saying “ you cannot perform updates while server is in read-only mode”. WELL THAT’S INTERESTING :)

Press enter or click to view image in full size

After Some more read and apply method i actually bypassed the ldap admin panel.

i focused on “cn” field and finally bypassed the login portal.

I added another command in cn field which was :- “(&(uid=*)(uid=*))(|(uid=*) and BOOM i was successfully logged in.

Press enter or click to view image in full size

I was like WOW, gonna get some bounty hehe….

Thank You for your time :)

Hope you liked it.
