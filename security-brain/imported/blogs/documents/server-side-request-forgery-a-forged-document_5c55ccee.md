---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-06-03_server-side-request-forgery-a-forged-document.md
original_filename: 2021-06-03_server-side-request-forgery-a-forged-document.md
title: Server Side Request Forgery - A Forged Document
category: documents
detected_topics:
- ssrf
- command-injection
- file-upload
tags:
- imported
- documents
- ssrf
- command-injection
- file-upload
language: en
raw_sha256: 5c55ccee85bb24aa83a8fd1b8dad7999f1b1de30b951f1eb98b9c95318501b38
text_sha256: 71f7b17ab9271121706abf72b5bce1c8033b1828231d98259da1f12d89687acd
ingested_at: '2026-06-28T07:32:06Z'
sensitivity: unknown
redactions_applied: false
---

# Server Side Request Forgery - A Forged Document

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-06-03_server-side-request-forgery-a-forged-document.md
- Source Type: markdown
- Detected Topics: ssrf, command-injection, file-upload
- Ingested At: 2026-06-28T07:32:06Z
- Redactions Applied: False
- Raw SHA256: `5c55ccee85bb24aa83a8fd1b8dad7999f1b1de30b951f1eb98b9c95318501b38`
- Text SHA256: `71f7b17ab9271121706abf72b5bce1c8033b1828231d98259da1f12d89687acd`


## Content

---
title: "Server Side Request Forgery - A Forged Document"
url: "https://shahjerry33.medium.com/server-side-request-forgery-a-forged-document-6359ef25058d"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["SSRF", "File upload"]
bounty: "500"
publication_date: "2021-06-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3602
scraped_via: "browseros"
---

# Server Side Request Forgery - A Forged Document

Top highlight

Server Side Request Forgery - A Forged Document
Jerry Shah (Jerry)
Follow
3 min read
·
Jun 2, 2021

408

3

Summary :

Server Side Request Forgery (SSRF) attacks are used to target internal systems that are behind firewalls and are not accessible from the external network. SSRF attacks can be exploited to access internally running services like SSH, Local-Host, FTP, Gopher etc. In a normal SSRF attack, the attacker might cause the server to make a connection to internal-only services within the organization’s infrastructure.

Description :

I have found this server side request forgery vulnerability on a private bugcrowd program. The program was having an option to upload the documents where there was no validation on the uploaded file type. It was allowing all the files to get uploaded. So I simply wrote the payload and saved the file as .html and uploaded it. After some time I got the pingbacks on my burp collaborator server, so I checked the IP address using whois command and it was of the company itself but was different from the IP of my target and was not accessible from the internet. It was a basic SSRF attack where I was able to find the internal IP but was not able to exploit it further. The bug got triaged as P3 and I was rewarded bounty of 500 USD. Later the severity was changed to P4.

Press enter or click to view image in full size

How I found this vulnerability ?

I created an account and after logging in I got the option of uploading the document
Press enter or click to view image in full size
Document Upload

2. I started burp collaborator client for generating the payload and copied the payload by clicking on “Copy to clipboard”

Press enter or click to view image in full size
Burp Collaborator Client
Press enter or click to view image in full size
Copy to clipboard

3. I created .html file with the code and pasted the copied payload and saved the file

Press enter or click to view image in full size
Payload

4. I uploaded the .html file on my target website

Press enter or click to view image in full size
Uploading File

5. After sometime I got the pingbacks on my burp collaborator client

Press enter or click to view image in full size
Internal Ping-backs

Why it happened ?

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In my opinion,

When I uploaded the .html file to the server, the server read the content of the file and tried to fetch the image from my burp collaborator client using its internal IP which got reflected on my burp collaborator client.

Exploit Code :

<html>
<body>
<img src=http://<BurpCollaboratorURL></img>
</body>
</html>

Then save it as .html and upload it.

Impact :

An attacker can exploit trust relationships to escalate an attack from the vulnerable application and perform unauthorized actions.

Mitigation :

A good way to mitigate ssrf attacks is to whitelist IP address or DNS name that the application needs to access. There is no universal fix to SSRF because it highly depends on the application functionality and business requirements.

In my case the mitigation should be that, that an application should only allow image files like pdf, png, jpeg, tiff etc to upload.

Press enter or click to view image in full size
