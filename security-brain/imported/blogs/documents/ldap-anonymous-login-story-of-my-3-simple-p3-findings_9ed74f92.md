---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-12-28_ldap-anonymous-login-story-of-my-3-simple-p3-findings.md
original_filename: 2022-12-28_ldap-anonymous-login-story-of-my-3-simple-p3-findings.md
title: LDAP anonymous login story of my 3 simple P3 findings
category: documents
detected_topics:
- xss
- command-injection
- csrf
tags:
- imported
- documents
- xss
- command-injection
- csrf
language: en
raw_sha256: 9ed74f92f7818120fbe95c2c54a2ee100af1267d612b55887070776d90b8fd28
text_sha256: ed2819dd41ba7d95ccdb1dd1a843bcca061fc3d4480ca06f9098b7b303301475
ingested_at: '2026-06-28T07:32:16Z'
sensitivity: unknown
redactions_applied: false
---

# LDAP anonymous login story of my 3 simple P3 findings

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-12-28_ldap-anonymous-login-story-of-my-3-simple-p3-findings.md
- Source Type: markdown
- Detected Topics: xss, command-injection, csrf
- Ingested At: 2026-06-28T07:32:16Z
- Redactions Applied: False
- Raw SHA256: `9ed74f92f7818120fbe95c2c54a2ee100af1267d612b55887070776d90b8fd28`
- Text SHA256: `ed2819dd41ba7d95ccdb1dd1a843bcca061fc3d4480ca06f9098b7b303301475`


## Content

---
title: "LDAP anonymous login story of my 3 simple P3 findings"
url: "https://tamimhasan404.medium.com/ldap-anonymous-login-story-of-my-3-simple-p3-findings-d5b4a991b345"
authors: ["Tamim Hasan (@tamimhasan404)"]
programs: ["Department of Homeland Security"]
bugs: ["LDAP anonymous login"]
publication_date: "2022-12-28"
added_date: "2022-12-30"
source: "pentester.land/writeups.json"
original_index: 1725
scraped_via: "browseros"
---

# LDAP anonymous login story of my 3 simple P3 findings

LDAP anonymous login story of my 3 simple P3 findings in DHS
Tamim Hasan
Follow
4 min read
·
Dec 28, 2022

204

Press enter or click to view image in full size
Assalamu Alaikum
peace be upon you

Hello hackers. I hope you are well. I am Tamim Hasan a Security Researcher and Bug Bounty hunter From Bangladesh 🇧🇩. Today I am telling you one of my recent findings which is about LDAP.

I haven’t found many writeups about LDAP. Then I decided to write about that. This is a very short write-up.

So let’s started….

What Is LDAP

It is a lightweight Directory Access Protocol(LDAP) an open, vendor-neutral, industry standard application protocol for accessing and maintaining distributed directory information services over an Internet Protocol network.

Background Scenario

As I don’t disclose the real domain name so I called target DHS target as xyz.dhs.gov

While hunting I found that the target has 3 ports open

Press enter or click to view image in full size

Other ports are nothing special but port 389 caught my attention

I search about the port and found that “ LDAP TCP and UDP port 389 is used for Directory, Replication, User and Computer Authentication, Group Policy, Trusts.”

The standard port for LDAP communication is 389, although other ports can be used. For example, if you must be able to start the server as a regular user, use an unprivileged port, by default 1389. Port numbers less than 1024 require privileged access.

So I search on google and try to find vulnerabilities related to LDAP when his default is open on a website and I found that if this happens there is a chance of a Malformed Bind Request (LDAP Anonymous Login).

Now time to test

First, You need to install ldapsearch then you can check it. like

ldapsearch -h <targetip> 389 -x -s base -b '' "(objectClass=*)" "*" +

OR

Get Tamim Hasan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

You can directly use the Nmap script for verifying it the command is

nmap -n -sV - script "ldap* and not brute" xyx.dhs.gov

And I successfully see their internal dir and other information(for security purposes I can’t show everything ) without authentication

Press enter or click to view image in full size
Impact:

If Anonymous LDAP Binding is enabled it allows an attacker to connect and search the directory (bind and search) without logging in. Attackers do not need to include binddn and bindpasswd.

As LDAP anonymous login is confirmed now so I didn’t dig deep and report it to the Department of Homeland Security: Vulnerability Disclosure Program.

And the response was

Press enter or click to view image in full size
Press enter or click to view image in full size
Listed On their HALL-OF-FAME

## Then I mass hunt on DHS program and found same type of vulnerability in their 3 different domains.

You can learn more about LDAP and its vulnerability here.
A tool that helps you find vulnerabilities in LDAP
If you want to do “Anonymously bruteforce Active Directory usernames from Domain Controllers by abusing LDAP Ping requests (cLDAP)” then check this tool.
Another tool that may help you.
## Tips

Don’t always look for XSS, CSRF, and other common stuff. Give some importance to Network, Server related vulnerabilities. If you don’t know what is in front of you while recon then just google it and dig deep.

💦 That’s all for today guys. If you find it useful then do clapt and If I made any mistakes please pardon me and if you have any suggestions/questions let me know. Have a nice day :)

You can follow me on Youtube | Github | Twitter | Linkedin | Facebook

👉 Explain In Bengali language
