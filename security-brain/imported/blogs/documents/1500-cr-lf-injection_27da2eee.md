---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-03-23_1500-crlf-injection.md
original_filename: 2024-03-23_1500-crlf-injection.md
title: '1500$: CR/LF Injection'
category: documents
detected_topics:
- xss
- command-injection
- file-upload
- path-traversal
- otp
tags:
- imported
- documents
- xss
- command-injection
- file-upload
- path-traversal
- otp
language: en
raw_sha256: 27da2eee2ad981fb7ea215f1bddfa092c81e4291a6433eed4869ab8f7974fd09
text_sha256: a6b70a72997db754f7cc98299d85dc7d70c2494b18d806fb5fdb59debca9bce6
ingested_at: '2026-06-28T07:32:32Z'
sensitivity: unknown
redactions_applied: false
---

# 1500$: CR/LF Injection

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-03-23_1500-crlf-injection.md
- Source Type: markdown
- Detected Topics: xss, command-injection, file-upload, path-traversal, otp
- Ingested At: 2026-06-28T07:32:32Z
- Redactions Applied: False
- Raw SHA256: `27da2eee2ad981fb7ea215f1bddfa092c81e4291a6433eed4869ab8f7974fd09`
- Text SHA256: `a6b70a72997db754f7cc98299d85dc7d70c2494b18d806fb5fdb59debca9bce6`


## Content

---
title: "1500$: CR/LF Injection"
url: "https://medium.com/@a13h1/1500-cr-lf-injection-0d2a75f02ef3"
authors: ["Abhi Sharma (@a13h1_)"]
bugs: ["CRLF injection"]
bounty: "1,500"
publication_date: "2024-03-23"
added_date: "2024-05-08"
source: "pentester.land/writeups.json"
original_index: 363
scraped_via: "browseros"
---

# 1500$: CR/LF Injection

1500$: CR/LF Injection
Abhi Sharma
Follow
3 min read
·
Mar 23, 2024

1K

10

Hi Everyone, How you all doing. In this article, I’m going to talk about a CR/LF bug I discovered in an private program which i m going to represent as Exahub that allowed me to get paid 1500$ in bounty.

Press enter or click to view image in full size

Understanding CR/LF (Carriage Return/Line Feed) Injection

CR/LF (Carriage Return/Line Feed) injection is a type of security vulnerability. CR/LF refers to a sequence of two ASCII control characters: Carriage Return (CR, ASCII code 13) and Line Feed (LF, ASCII code 10). These characters are used in text files to signify the end of a line and control the positioning of the cursor or print head when displaying or printing text. CR/LF injection vulnerabilities occur when attackers insert CR/LF characters into input fields, file extensions or file uploads to manipulate application behavior. This can lead to exploits such as altering headers, injecting malicious code, or manipulating file content.

Understanding the target: Exahub

ExaHub (Virtual name of private program) is a platform tailored for enthusiasts and professionals alike who work with the Exa programming language. Exa, a high-level programming language renowned for its speed and performance, has gained significant traction in fields like scientific computing, machine learning, and data science. ExaHub serves as a centralized hub where users can access a range of resources, collaborate on projects, and leverage tools tailored to the Julia ecosystem. From project management to data visualization, ExaHub provides a suite of features designed to streamline development workflows and foster community engagement.

Understanding the Issue:

The vulnerability identified in ExaHub revolves around CR/LF injection during file uploads. This flaw allows malicious actors to manipulate headers, potentially leading to cookie manipulation and forced logout of other users. The root cause of this issue lies in inadequate input validation during the file upload process.

Steps to Reproduce:
Access your ExaHub account.
Navigate to the “Files” section.
Upload a file and intercept the uploading request.
Modify the Content-Disposition header by appending the payload %0AClear-Site-Data%3A%22cookies%22%0A after the filename.
Send the modified request and attempt to download the uploaded file.
When other user download the file they got locked out this is one of the multiple task which can be performed by cr/lf injection.
Get Abhi Sharma’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Press enter or click to view image in full size

Potential Exploits:

Apart from forced logout and session manipulation, attackers can exploit this vulnerability to manipulate and set cookies of other users. By injecting payloads such as %0ASet-Cookie%3A+crlfinjection%3D+value+ , or for xss

 • /%3f%0d%0aLocation:%0d%0aContent-Type:text/html%0d%0aX-XSS-Protection%3a0%0d%0a%0d%0a%3Cscript%3Ealert%28document.domain%29%3C/script%3E ``

they can hijack sessions, gain unauthorized access, or execute other malicious activities.

Response and Resolution:

Upon reporting the issue, the ExaHub security team promptly acknowledged its validity and initiated a fix. While the severity was initially classified as critical, further analysis revealed a high severity rating. As a token of appreciation for the responsible disclosure, EXAHub awarded a $1,500 bounty to the individual who identified the vulnerability.

Takeaway:

Always be thorough in your testing and try injecting various payloads, including special characters like CR/LF. You never know what vulnerabilities you might uncover, and by testing comprehensively, you can discover and address potential security risks before they can be exploited by malicious actors. Remember, thorough testing is key to ensuring the security and integrity of your systems and applications.

Leave some clap if you enjoyed this read, leave your feedback in comment and consider following me for more exciting findings.

buymeacoffee.com/a13h1

Find me on Twitter: @a13h1_

Thank you everyone

Keep Supporting, Keep Clapping, Keep Commenting.
