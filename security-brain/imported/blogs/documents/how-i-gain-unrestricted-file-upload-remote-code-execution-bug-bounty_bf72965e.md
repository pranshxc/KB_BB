---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-02-17_how-i-gain-unrestricted-file-upload-remote-code-execution-bug-bounty.md
original_filename: 2020-02-17_how-i-gain-unrestricted-file-upload-remote-code-execution-bug-bounty.md
title: How I Gain Unrestricted File Upload Remote Code Execution Bug Bounty
category: documents
detected_topics:
- command-injection
- access-control
- file-upload
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- access-control
- file-upload
- automation-abuse
- api-security
language: en
raw_sha256: bf72965ec18cd20f208ab935ce6091954ef1ddb12ea81f19470e38dedca328c0
text_sha256: 3e050057a9ef02cd4fee329658709fa4c6c3a22de6c798253533149023794b11
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How I Gain Unrestricted File Upload Remote Code Execution Bug Bounty

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-02-17_how-i-gain-unrestricted-file-upload-remote-code-execution-bug-bounty.md
- Source Type: markdown
- Detected Topics: command-injection, access-control, file-upload, automation-abuse, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `bf72965ec18cd20f208ab935ce6091954ef1ddb12ea81f19470e38dedca328c0`
- Text SHA256: `3e050057a9ef02cd4fee329658709fa4c6c3a22de6c798253533149023794b11`


## Content

---
title: "How I Gain Unrestricted File Upload Remote Code Execution Bug Bounty"
url: "https://medium.com/@shayboy123/how-i-gain-unrestricted-file-upload-remote-code-execution-bug-bounty-381d0aab0dad"
authors: ["Shay Grant (@kidshay)"]
bugs: ["Unrestricted file upload"]
publication_date: "2020-02-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4769
scraped_via: "browseros"
---

# How I Gain Unrestricted File Upload Remote Code Execution Bug Bounty

Top highlight

shay grant
Follow
5 min read
·
Feb 17, 2020

93

2

How I Gain Unrestricted File Upload Remote Code Execution Bug Bounty.

This vulnerability is patched and fixed by the team. Because this application is a private scope, I can’t show the company name or branding.

I would use the company name as target.

How I Found The Vulnerability

After scoping the target application, I began to test for several vulnerabilities. Typically I first test for file upload functionality and the target had a profile upload feature in scope.

The Vulnerability

Logo Upload Functionality that allows users to upload a logo to their profile. https://target.com/profile/upload.php/

Press enter or click to view image in full size
Logo Upload Form

Client-side filtering

In this case, the check is performed in the browser using JavaScript, VBScript or HTML5 before sending files to the server. Programmers use this method to optimize user interaction with the application and quickly issue a response at the browser level.

Bypassing client-side filtering

We were able to bypass this check by loading the image through the browser, then changing the extension in the request before it sent to the server using burp suite, as well as changing the content type of the file from image/png to application/php.

We changed the extensions from .jpeg to .php and replaced the contents of the file with <?php echo shell_exec($_GET[’e’].’ 2>&1’); ?>. A basic command shell.

Press enter or click to view image in full size
Changing the file content before upload
Press enter or click to view image in full size
file upload to the webserver results

At the bottom right of the image above you would see Apache, when running the command whoami. This vulnerability is known as Unrestricted File Upload https://www.owasp.org/index.php/Unrestricted_File_Upload. At this point, I stopped testing the application since I was able to gain code execution.

Impact of this vulnerability

The consequences of unrestricted file upload can vary, including complete system takeover, an overloaded file system or database, forwarding attacks to back-end systems, client-side attacks, or simple defacement.

The impact of this vulnerability is high, supposed code can be executed in the server context or on the client-side. The likelihood of detection for the attacker is high. The prevalence is common. As a result, the severity of this type of vulnerability is high.

It is important to check a file upload module’s access controls to examine the risks properly.

Get shay grant’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Server-side attacks: The web server can be compromised by uploading and executing a web-shell that can run commands, browse system files, browse local resources, attack other servers, or exploit the local vulnerabilities, and so forth.

Tips for security blue team to identify this type of attack being exploited.

Tip 1: We can use two sigma rules (Free)

title: Webshell Detection With Command Line Keywords
id: bed2a484-9348-4143-8a8a-b801c979301c
description: Detects certain command line parameters often used during reconnaissance activity via web shells
author: Florian Roth
reference:
  - https://www.fireeye.com/blog/threat-research/2013/08/breaking-down-the-china-chopper-web-shell-part-ii.html
date: 2017/01/01
modified: 2019/10/26
tags:
  - attack.privilege_escalation
  - attack.persistence
  - attack.t1100
logsource:
  category: process_creation
  product: windows
detection:
  selection:
  ParentImage:
  - '*\apache*'
  - '*\tomcat*'
  - '*\w3wp.exe'
  - '*\php-cgi.exe'
  - '*\nginx.exe'
  - '*\httpd.exe'
  CommandLine:
  - '*whoami*'
  - '*net user *'
  - '*ping -n *'
  - '*systeminfo'
  - '*&cd&echo*'
  - '*cd /d*'  # https://www.computerhope.com/cdhlp.htm
  condition: selection
fields:
  - CommandLine
  - ParentCommandLine
falsepositives:
  - unknown
level: high
title: Suspicious Activity in Shell Commands
id: 2aa1440c-9ae9-4d92-84a7-a9e5f5e31695
description: Detects suspicious shell commands used in various exploit codes (see references)
references:
  - http://www.threatgeek.com/2017/03/widespread-exploitation-attempts-using-cve-2017-5638.html
  - https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/multi/http/struts_code_exec_exception_delegator.rb#L121
  - http://pastebin.com/FtygZ1cg
  - https://artkond.com/2017/03/23/pivoting-guide/
author: Florian Roth
date: 2017/08/21
modified: 2019/02/05
logsource:
  product: linux
detection:
  keywords:
  # Generic suspicious commands
  - 'wget * - http* | perl'
  - 'wget * - http* | sh'
  - 'wget * - http* | bash'
  - 'python -m SimpleHTTPServer'
  - '-m http.server'  # Python 3
  - 'import pty; pty.spawn*'
  - 'socat exec:*'
  - 'socat -O /tmp/*'
  - 'socat tcp-connect*'
  - '*echo binary >>*'
  # Malware 
  - '*wget *; chmod +x*'
  - '*wget *; chmod 777 *'
  - '*cd /tmp || cd /var/run || cd /mnt*'
  # Apache Struts in-the-wild exploit codes  
  - '*stop;service iptables stop;*'
  - '*stop;SuSEfirewall2 stop;*'
  - 'chmod 777 2020*'
  - '*>>/etc/rc.local'
  # Metasploit framework exploit codes
  - '*base64 -d /tmp/*'
  - '* | base64 -d *'
  - '*/chmod u+s *'
  - '*chmod +s /tmp/*'
  - '*chmod u+s /tmp/*'
  - '* /tmp/haxhax*'
  - '* /tmp/ns_sploit*'
  - 'nc -l -p *'
  - 'cp /bin/ksh *'
  - 'cp /bin/sh *'
  - '* /tmp/*.b64 *'
  - '*/tmp/ysocereal.jar*'
  - '*/tmp/x *'
  - '*; chmod +x /tmp/*'
  - '*;chmod +x /tmp/*'
  condition: keywords
falsepositives:
  - Unknown
level: high

Forward apache logs and windows iis logs into your SIEM, can be elastic search kibana or splunk. Use the sigma rule converter for your SIEM with the right index and you should be able to detect if someone uploads and execute a web shell on your server.

Tip 2: Using Microsoft Defender ATP (Paid)

Microsoft Defender ATP exposes these behaviors that indicate web shell installation and post-compromise activity by analyzing script file writes and process executions. When alerted of these activities, security operations teams can then use the rich capabilities in Microsoft Defender ATP to investigate and resolve web shell attacks.

https://www.microsoft.com/security/blog/2020/02/04/ghost-in-the-shell-investigating-web-shell-attacks/

Tips for Web Developers

To avoid these types of file upload attacks, I recommend the following best practices:

1. Only allow specific file extensions, by using a white list of allowed files, you can avoid executables, scripts, and other potentially malicious content from being uploaded to your site.

2. Randomize uploaded file names, randomly alter the uploaded file names so that attackers cannot try to access the file with the file name they uploaded.

3. Store uploaded files outside webroot, The directory to which files are uploaded should be outside of the website’s public directory so that the attackers cannot execute the file via a website URL.

4. Use simple error messages, when displaying file upload errors, do not include directory paths, server configuration settings or other information that attackers could potentially use.

5. Finally, anything that arrives in the network via an upload should be scanned for malware and viruses. Excellent API to use would be virustotal or just an edr on the server.
https://developers.virustotal.com/reference

6. Never ever, ever trust client-side validation. Always try to use server-side validation.

Reported Time-line

Reported @ Mar 31, 2019, 5:43 PM
Response Apr 8, 2019, 10:47 Am
Rewarded May 9, 2019

Resources

Burp Suite — Cybersecurity Software from PortSwigger
Burp Suite is a leading range of cybersecurity tools, brought to you by PortSwigger. We believe in giving our users a…

portswigger.net

Neo23x0/sigma
Generic Signature Format for SIEM Systems Sigma is a generic and open signature format that allows you to describe…

github.com

Unrestricted File Upload
Last revision (mm/dd/yy): // Uploaded files represent a significant risk to applications. The first step in many…

owasp.org
