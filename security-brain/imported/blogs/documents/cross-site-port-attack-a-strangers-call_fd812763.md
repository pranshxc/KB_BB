---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-03-21_cross-site-port-attack-a-strangers-call.md
original_filename: 2021-03-21_cross-site-port-attack-a-strangers-call.md
title: Cross Site Port Attack - A Stranger’s Call
category: documents
detected_topics:
- command-injection
- ssrf
- sqli
- path-traversal
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- ssrf
- sqli
- path-traversal
- automation-abuse
- api-security
language: en
raw_sha256: fd812763d6b20edb3f3412738ae456a91e9d6d356a81a770d0f54ecf17b4a34c
text_sha256: f4fc85ee66056a29df935c3b895211e3bd384d07509578975417f6d350e1722b
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Cross Site Port Attack - A Stranger’s Call

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-03-21_cross-site-port-attack-a-strangers-call.md
- Source Type: markdown
- Detected Topics: command-injection, ssrf, sqli, path-traversal, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `fd812763d6b20edb3f3412738ae456a91e9d6d356a81a770d0f54ecf17b4a34c`
- Text SHA256: `f4fc85ee66056a29df935c3b895211e3bd384d07509578975417f6d350e1722b`


## Content

---
title: "Cross Site Port Attack - A Stranger’s Call"
url: "https://shahjerry33.medium.com/cross-site-port-attack-a-strangers-call-c2467f93792f"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["XSPA"]
publication_date: "2021-03-21"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3800
scraped_via: "browseros"
---

# Cross Site Port Attack - A Stranger’s Call

Top highlight

Cross Site Port Attack - A Stranger’s Call
Jerry Shah (Jerry)
Follow
5 min read
·
Mar 21, 2021

478

2

Press enter or click to view image in full size

Summary :

Cross Site Port Attack is an abbreviation of XSPA. In this attack an application processes user supplied URLs and does not verify or sanitize the back end response received from remote servers before sending it back to the client. An attacker can send crafted queries to a vulnerable web application to proxy attacks to external Internet facing servers, intranet devices and the web server itself. The responses, in certain cases, can be studied to identify service availability like open ports , banner versions etc. and even fetch data from remote services in an unconventional ways.

It allows attackers to abuse available functionality in most web applications to scan port of intranet and external Internet facing servers, fingerprint internal (non-Internet exposed) network aware services, perform banner grabbing, identify web application frameworks, exploit vulnerable programs, run code on reachable machines, exploit web application vulnerabilities listening on internal networks, read local files using the file protocol and much more.

My target website was built in WordPress (I found it using wappalyzer) and the most common xmlrpc.php file was enabled. Most XSPA attack occurs when xmlrpc.php file is enabled. I exploited the file and got an IP address and when I visited that IP address there wasn’t any content on it but when I used directory traversal payload I was able to call /etc/passwd file.

Attacks You Can Perform Using XSPA :

Port scanning remote Internet facing servers
Port scanning Intranet
Port scanning local web server
Exploit vulnerable programs running on intranet or on local web server
Attacking internal and external web applications that are vulnerable to GET parameter based vulnerabilities such as SQLi
Reading local web server files using the file:/// protocol handler

How I found this vulnerability ?

I went to my target website and added an endpoint /xmlrpc.php and as usual it gave me an error
Press enter or click to view image in full size
xmlrpc.php

2. Then I changed GET verb to POST verb and got a weird response

Press enter or click to view image in full size
POST Response

3. I searched for the exploit and found a blog on xmlrpc.php file exploitation, I used the exploit and got some methods in response

Press enter or click to view image in full size
Exploit xmlrpc.php
Press enter or click to view image in full size
Exploit xmlrpc.php

4. As mentioned in the blog I found the pingback.ping method, I opened my burp collaborator client for XSPA attack and copied the collaborator URL

Press enter or click to view image in full size
Burp Collaborator Client
Press enter or click to view image in full size
Collaborator URL Copied

5. Then I used the exploit of pingback.ping method and got a weird response again

Press enter or click to view image in full size
Exploit pingback.ping
Press enter or click to view image in full size
Response

6. Then I checked my collaborator client and got a successful DNS and HTTP request, so it was confirmed that the website is vulnerable to XSPA attack

Press enter or click to view image in full size
HTTP and DNS Request

7. Then for a cross check, instead of burp collaborator client I used https://hookbin.com/ for a callback and even there I got a successful callback

Press enter or click to view image in full size
Callback on hookbin
Press enter or click to view image in full size
Callback on hookbin

8. Then I used my ngrok server for checking XSPA attack again

Press enter or click to view image in full size
Ngrok
Press enter or click to view image in full size
Ngrok Web Interface

Here you can is in the response the faultCode value is 17, which means that the port is open. If you hit the value (faultCode) greater than 0 means that the port is open.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Now usually you get the internal IP address but the IP that I got wasn’t internal but it was owned by my target company when I checked the whois record. I visited that IP which was 184.xxx.xx.xx and found an empty page and I randomly added a directory traversal payload and got a listing.

Press enter or click to view image in full size
/etc/passwd

Impact :

This kind of attacks are used to perform Denial-Of-Service, Port Scanning, Remote Code Execution, Reading Internal Files etc.

Mitigation :

There are many mitigations against XSPA attack and some of those are :

Unauthorized URL access should be restricted
Restrict connectivity to internal ports
Blacklist internal IP addresses and internal host names
Disable unwanted protocols

Exploit Codes :

For directory traversal :

https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Directory%20Traversal

2. For listing all available methods :

<methodCall>
<methodName>system.listMethods</methodName>
<params></params>
</methodCall>

3. For exploiting pingback.ping method :

<?xml version=”1.0" encoding=”UTF-8"?>
<methodCall>
<methodName>pingback.ping</methodName>
<params>
<param>
<value><string>URL of your server</string></value>
</param>
<param>
<value><string>Target URL with an endpoint</string></value>
</param>
</params>
</methodCall>

In pingback.ping exploit, the <methodName> is pingback.ping and the first <string> value is the URL of your server and the second <string> value is the URL of your target with any of its endpoint. It is mandatory to use the endpoint of the target website otherwise it will give you below mentioned error.

Press enter or click to view image in full size
Error

Here the error says “The specified target URL cannot be used as a target. It either doesn’t exist, or it is not a pingback-enabled resource.” This error came because I used the target URL without any endpoint. (for eg. https://www.mytarget.com instead of https://www.mytarget.com/visit-my-new-interesting-blogs)

It happens because the pingback methods are usually enabled where the blog links are mentioned.

For eg : If we have two websites and both of them have pingback enabled on blog endpoint, so if website 1’s owner mentioned any of your blog in there comment section you will get a pingback on your server and vice versa.

To know more about pingback you can visit : https://www.youtube.com/watch?v=Q3YE5pueS90

Great thanks to : https://the-bilal-rizwan.medium.com/ for xmlrpc.php exploit.

Press enter or click to view image in full size
