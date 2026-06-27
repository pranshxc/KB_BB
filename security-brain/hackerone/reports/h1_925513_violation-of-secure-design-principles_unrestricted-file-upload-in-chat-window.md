---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '925513'
original_report_id: '925513'
title: Unrestricted File Upload in Chat Window
weakness: Violation of Secure Design Principles
team_handle: owox
created_at: '2020-07-16T16:12:54.368Z'
disclosed_at: '2020-08-16T06:35:33.740Z'
has_bounty: false
visibility: full
substate: resolved
vote_count: 13
tags:
- hackerone
- violation-of-secure-design-principles
---

# Unrestricted File Upload in Chat Window

## Metadata

- HackerOne Report ID: 925513
- Weakness: Violation of Secure Design Principles
- Program: owox
- Disclosed At: 2020-08-16T06:35:33.740Z
- Has Bounty: No
- Visibility: full
- Substate: resolved

## Original Report

#Summary:
The application allows the attacker to upload dangerous file types that can be automatically processed within the product's environment.

#Steps To Reproduce:
- Hit the browser and navigate to https://bi.owox.com and sign in.
- Open The Chat window.
- Upload any .rb or .php file .
- Click on send button.

## Impact

-> The impact of this vulnerability is high, supposed code can be executed in the server context or on the client side. The likelihood of detection for the
attacker is high. The prevalence is common. As a result the severity of this type of vulnerability is high.
->It is important to check a file upload module’s access controls to examine the risks properly.
-> Server-side attacks: The web server can be compromised by uploading and executing a web-shell which can run commands, browse system files,
browse local resources, attack other servers, or exploit the local vulnerabilities, and so forth.
->Client-side attacks: Uploading malicious files can make the website vulnerable to client-side attacks such as XSS or Cross-site Content Hijacking.
->Uploaded files can be abused to exploit other vulnerable sections of an application when a file on the same or a trusted server is needed (can again
lead to client-side or server-side attacks)
->Uploaded files might trigger vulnerabilities in broken libraries/applications on the client side (e.g. iPhone MobileSafari LibTIFF Buffer Overflow).
->Uploaded files might trigger vulnerabilities in broken libraries/applications on the server side (e.g. ImageMagick flaw that called ImageTragick!).
->Uploaded files might trigger vulnerabilities in broken real-time monitoring tools (e.g. Symantec antivirus exploit by unpacking a RAR file)
->A malicious file such as a Unix shell script, a windows virus, an Excel file with a dangerous formula, or a reverse shell can be uploaded on the server in
order to execute code by an administrator or webmaster later – on the victim’s machine.
->An attacker might be able to put a phishing page into the website or deface the website.
->The file storage server might be abused to host troublesome files including malwares, illegal software, or adult contents. Uploaded files might also
contain malwares’ command and control data, violence and harassment messages, or steganographic data that can be used by criminal organisations.
->Uploaded sensitive files might be accessible by unauthorised people.
->File uploaders may disclose internal information such as server internal paths in their error messages.

## Extracted Security Notes

### Likely Vulnerability Class

*Leave this section for future enrichment.*

### Likely Root Cause

*Leave this section for future enrichment.*

### Potential Impact

*Leave this section for future enrichment.*

### Defensive Test Cases

*Leave this section for future enrichment.*

### Remediation Ideas

*Leave this section for future enrichment.*
