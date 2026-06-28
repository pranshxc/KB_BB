---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-14_blind-command-injection-it-hurts.md
original_filename: 2021-06-14_blind-command-injection-it-hurts.md
title: Blind Command Injection - It hurts
category: documents
detected_topics:
- command-injection
- mobile-security
- supply-chain
tags:
- imported
- documents
- command-injection
- mobile-security
- supply-chain
language: en
raw_sha256: 05886ee937cc2b3710e82acaee73fd37dfd0e40c89a006ae2ea640d9453ea84c
text_sha256: ed88aeb44d0e6d97bc743024057b42cbb5b894b6396f98539cd45eb3670644be
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Blind Command Injection - It hurts

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-14_blind-command-injection-it-hurts.md
- Source Type: markdown
- Detected Topics: command-injection, mobile-security, supply-chain
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `05886ee937cc2b3710e82acaee73fd37dfd0e40c89a006ae2ea640d9453ea84c`
- Text SHA256: `ed88aeb44d0e6d97bc743024057b42cbb5b894b6396f98539cd45eb3670644be`


## Content

---
title: "Blind Command Injection - It hurts"
url: "https://shahjerry33.medium.com/blind-command-injection-it-hurts-9f396c1f63f2"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Command injection", "RCE"]
publication_date: "2021-06-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3579
scraped_via: "browseros"
---

# Blind Command Injection - It hurts

Top highlight

Blind Command Injection - It hurts
Jerry Shah (Jerry)
Follow
3 min read
·
Jun 14, 2020

492

5

Press enter or click to view image in full size

Summary :

Command Injection is a type of attack that executes arbitrary commands on the host operating system. Command injection happens when an application passes an unsafe user supplied data to a system shell. Command injection is possible due to insufficient input validation.

Generally it is tough to find command injection but luckily I found one few months ago. I noticed something weird with the GET parameter /?search= when I was testing for command injection. I tested so many payloads but nothing worked.

When I checked the response in burp suite it said “this object will store some %symbols% in the javascript space, so that libs can read them” so I thought it might be a blind command injection so I used tcpdump to find it out. Tcpdump comes pre-installed in kali linux.

How to find this vulnerability ?

Go to your target website and check for some common parameters (in my case it was /?search=)

2. I tried injecting a payload by simply using a pipe operator but I didn’t get any response, it was a normal 200 OK

Press enter or click to view image in full size
Pipe Operator

3. I used so many payloads for testing but only one worked which was a bypass using null byte character

Press enter or click to view image in full size
Payload

4. I started tcpdump on kali because I knew that it was a blind command injection

Press enter or click to view image in full size
TcpDump

You can use payloads from here : https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Command%20Injection

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

My custom payload that worked : http://www.mytarget.com/?search=%00{.exec|ping <MyIP>

You can also use wireshark instead of tcpdump for checking blind command injection

Though I found this command injection after a lot of efforts it was a duplicate of another report on a private program :( .

Some Common Parameters For Testing Command Injection :

/?query=
/?email=
/?id=
/?username=
/?user=
/?to=
/?from=
/?search=
/?query=
/?q=
/?s=
/?shopId=
/?blogId=
/?phone=
/?mode=
/?next=
/?firstname=
/?lastname=
/?locale=
/?cmd=
/?sys=
/?system=

There is a good tool on github for detecting command injection vulnerabilities automatically.

Link : https://github.com/commixproject/commix

Commix is an automated tool written by Anastasios Stasinopoulos that can be used from web developers, penetration testers or even security researchers in order to test web-based applications with the view to find bugs, errors or vulnerabilities related to command injection attacks. By using this tool, it is very easy to find and exploit a command injection vulnerability in a certain vulnerable parameter or HTTP header.

Mitigation : To prevent Command Injections, never call out to OS commands from application-layer code.

Press enter or click to view image in full size
