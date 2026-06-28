---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-15_lfi-an-interesting-tweak.md
original_filename: 2023-03-15_lfi-an-interesting-tweak.md
title: LFI - An Interesting Tweak
category: documents
detected_topics:
- path-traversal
- command-injection
- api-security
tags:
- imported
- documents
- path-traversal
- command-injection
- api-security
language: en
raw_sha256: 2bdc91438965dbc95e30fdf54326d651b1b68471c6f8f0c77c6c3151e4d9b1ff
text_sha256: 72f3d7b2336161ec531378e7b59d337f90aee8b0b95319d273ed5d1811988434
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# LFI - An Interesting Tweak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-15_lfi-an-interesting-tweak.md
- Source Type: markdown
- Detected Topics: path-traversal, command-injection, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `2bdc91438965dbc95e30fdf54326d651b1b68471c6f8f0c77c6c3151e4d9b1ff`
- Text SHA256: `72f3d7b2336161ec531378e7b59d337f90aee8b0b95319d273ed5d1811988434`


## Content

---
title: "LFI - An Interesting Tweak"
url: "https://shahjerry33.medium.com/lfi-an-interesting-tweak-9c5638dbdd1b"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["LFI"]
publication_date: "2023-03-15"
added_date: "2023-03-15"
source: "pentester.land/writeups.json"
original_index: 1372
scraped_via: "browseros"
---

# LFI - An Interesting Tweak

Top highlight

LFI - An Interesting Tweak
Jerry Shah (Jerry)
Follow
4 min read
·
Mar 15, 2023

230

2

Press enter or click to view image in full size

Summary

Local File Inclusion (LFI) is a type of web application vulnerability that allows an attacker to include and execute arbitrary files on the web server. An attacker can take advantage of this vulnerability by passing a malicious file path as a parameter, which could be a local file on the server. This can allow the attacker to view sensitive information, such as configuration files or user credentials, execute arbitrary code, or even gain complete control of the server.

Description

I have found a local file inclusion (LFI) vulnerability on one of the program where I was able to download the web.xml file from WEB-INF/ directory. However the bug is quite simple with a small tweak.

The website had a Download Course Details option where it was fetching course details from a server via filename= parameter, it was a POST request. The website was running on IIS server so initially I thought of downloading some sensitive files however they were all restricted but then I thought of downloading the web.xml file which was successfully downloaded. The downloaded file had the username and password of admin but I was not able to find a login portal so the severity was downgraded. I did not report the bug as the target was OOS (Out-Of-Scope).

How I found this vulnerability ?

I went to the website where there was an option to “Download Course Details”
Press enter or click to view image in full size
Download Course Details

2. I right clicked on the button and clicked on Inspect to check the hyperlink and from where it is fetching the file

Press enter or click to view image in full size
Inspect Element
Press enter or click to view image in full size
Hyperlink and filename= Parameter

3. I knew that it was using the IIS server so I searched for the path of web.xml

Press enter or click to view image in full size
WEB-INF/

4. I edited the path to ?filename=/WEB-INF/web.xml

Press enter or click to view image in full size
web.xml

5. Then I clicked on the button and downloaded the file and opened it, I got the credentials

Press enter or click to view image in full size
Download
Press enter or click to view image in full size
Downloaded
Press enter or click to view image in full size
Credentials

Why it happened ?

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In my opinion,

The website was not validating and sanitizing the user input before processing it. However major of the sensitive files were blocked but blocking particular files is not the ideal solution from my perspective, the user input should validated and sanitized before processing it.

Impact

The impact of an LFI vulnerability can be severe, as it can lead to a complete compromise of the web server and its data. However in my case the impact was limited to downloading the web.xml file as all the major sensitive files were restricted for downloading, so the impact would be medium.

NOTE : If I could have found the login panel that gives me the access with the credentials I obtained then the severity would have been high.

Press enter or click to view image in full size

Calculated CVSS

Vector String - CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N

Score - 5.3 (Medium)

Mitigation

Input validation and sanitization should be done if any user input arrives. Server should not process the user input without validation. The validation and sanitization should be done on the client-side as well as server-side. Additionally, the application should avoid using user input to construct file paths and instead use a whitelist approach to specify allowed file paths. Web application firewalls can also be used to detect and block attempts to exploit LFI vulnerabilities.

Press enter or click to view image in full size
