---
source: hackerone
dataset: elamaran619/hackerone_disclosed_reports
h1_id: '97657'
original_report_id: '97657'
title: File upload XSS (Java applet) on http://slackatwork.com/
weakness: Command Injection - Generic
team_handle: slack
created_at: '2015-11-04T11:10:53.600Z'
disclosed_at: '2015-11-11T18:03:55.984Z'
has_bounty: true
visibility: full
substate: resolved
vote_count: 1
tags:
- hackerone
- command-injection-generic
---

# File upload XSS (Java applet) on http://slackatwork.com/

## Metadata

- HackerOne Report ID: 97657
- Weakness: Command Injection - Generic
- Program: slack
- Disclosed At: 2015-11-11T18:03:55.984Z
- Has Bounty: Yes
- Visibility: full
- Substate: resolved

## Original Report

The web application supports file uploads and I was able to upload a Java Applet (.class/.jar) file. If a web browser loads a Java applet from a trusted site, the browser provides no security warning. If an attacker can upload a CLASS/JAR file with an applet, the file is executed even if the web page, which embeds the applet is located on a different site. An attacker could use a file upload function to build an XSS attack using active content.

The impact of this vulnerability
Malicious users may inject JavaScript, VBScript, ActiveX, HTML or Flash into a vulnerable application to fool a user in order to gather data from them. An attacker can steal the session cookie and take over the account, impersonating the user. It is also possible to modify the content of the page presented to the user.


Here is the link of the file i was able to upload with class extension:-

Successfully uploaded file Applet3863.class with content type image/jpeg.

The file is available at: http://slackatwork.com/wp-content/uploads/job-manager-uploads/company_logo/2015/11/Applet3863.class.

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
