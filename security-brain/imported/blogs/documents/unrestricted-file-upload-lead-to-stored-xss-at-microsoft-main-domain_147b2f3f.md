---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-01-15_unrestricted-file-upload-lead-to-stored-xss-at-microsoft-main-domain.md
original_filename: 2024-01-15_unrestricted-file-upload-lead-to-stored-xss-at-microsoft-main-domain.md
title: Unrestricted File Upload Lead to Stored XSS at Microsoft main domain
category: documents
detected_topics:
- xss
- sso
- command-injection
- file-upload
- api-security
tags:
- imported
- documents
- xss
- sso
- command-injection
- file-upload
- api-security
language: en
raw_sha256: 147b2f3f9962b8bad06c31711a5abba2dc7e419627909039422f624758b9fae6
text_sha256: b35dd13fb8e3a68d732e04465c8989ae317270a9e02b2b617b9c36734487c978
ingested_at: '2026-06-28T07:32:29Z'
sensitivity: unknown
redactions_applied: false
---

# Unrestricted File Upload Lead to Stored XSS at Microsoft main domain

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-01-15_unrestricted-file-upload-lead-to-stored-xss-at-microsoft-main-domain.md
- Source Type: markdown
- Detected Topics: xss, sso, command-injection, file-upload, api-security
- Ingested At: 2026-06-28T07:32:29Z
- Redactions Applied: False
- Raw SHA256: `147b2f3f9962b8bad06c31711a5abba2dc7e419627909039422f624758b9fae6`
- Text SHA256: `b35dd13fb8e3a68d732e04465c8989ae317270a9e02b2b617b9c36734487c978`


## Content

---
title: "Unrestricted File Upload Lead to Stored XSS at Microsoft main domain"
url: "https://medium.com/@cavdarbashas/unrestricted-file-upload-lead-to-stored-xss-at-microsoft-main-domain-baa9cadac6bd"
authors: ["Sokol Çavdarbasha (@sokolicav)"]
programs: ["Microsoft"]
bugs: ["Unrestricted file upload", "Stored XSS"]
publication_date: "2024-01-15"
added_date: "2024-01-18"
source: "pentester.land/writeups.json"
original_index: 547
scraped_via: "browseros"
---

# Unrestricted File Upload Lead to Stored XSS at Microsoft main domain

Unrestricted File Upload Lead to Stored XSS at Microsoft main domain
Sokol Çavdarbasha
Follow
3 min read
·
Jan 15, 2024

138

1

Press enter or click to view image in full size

Welcome Security Researchers,

I am Sokol Çavdarbasha, a 21-year-old Security Researcher from Kosovo. My engagement in the field of cybersecurity is marked by an unyielding dedication to enhance the safety of the digital realm, striving to contribute to a more secure internet environment.

Introduction

In today’s digital world, cybersecurity vulnerabilities continue to pose a significant threat to organizations. One such vulnerability is unrestricted file upload, which can lead to devastating consequences if not properly addressed. In this blog post, we will explore a recent case involving unrestricted file upload at Microsoft’s main domain, highlighting the potential risks and impacts of such a security flaw.

Understanding Unrestricted File Upload:
Unrestricted file upload refers to a vulnerability that allows an attacker to upload arbitrary files to a web application, without any type of validation or restriction. This vulnerability can occur when the application does not properly check the file type or content during the upload process. As a result, an attacker can upload malicious files, such as scripts or executables, and potentially compromise the security of the application and its users.

The Importance of Security at Microsoft’s Main Domain:
As one of the leading tech giants, Microsoft plays a critical role in maintaining the world’s digital infrastructure. With millions of users accessing their services, security becomes paramount. However, even industry leaders like Microsoft can fall victim to vulnerabilities if not thoroughly assessed and addressed in a timely manner.

The Stored Cross-Site Scripting (XSS) Vulnerability:
One of the primary risks associated with unrestricted file upload is the potential for a stored Cross-Site Scripting (XSS) attack. In a stored XSS attack, malicious code is injected into a vulnerable web application and then permanently stored on the server. When other users access the affected page, the malicious code is executed in their browsers, leading to various adverse consequences.

The Impact of the Vulnerability:
In the case of Microsoft’s main domain, if an attacker were to exploit the unrestricted file upload vulnerability, they could upload a file containing malicious code. This code could then be executed whenever a user accesses the compromised page, potentially leading to sensitive data theft, unauthorized access, or even complete control over the victim’s browser.

Steps To Reproduce:

Visit the https://www.microsoft.com/en-us/concern/bing
Press enter or click to view image in full size

2. Go to File Upload form and choose a file with .jpg extension

3. Turn on the Intercepter and press “Upload” button

Get Sokol Çavdarbasha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

4. Change the “name” to test.svg, the “filename” to test.svg and Content-Type to image/svg+xml and upload your svg code with xss payload on it

Press enter or click to view image in full size

5. Respond the Request and you will get in response the endpoint where that file has been uploaded

Press enter or click to view image in full size

6. Visit the endpoint and you will get XSS triggered.

Press enter or click to view image in full size

The PoC Video:

Stored XSS on Microsoft PoC

The Response from MSRC Team:

Press enter or click to view image in full size

Thanks for attention and i hope that you enjoyed reading this article.

You Can Follow me on :

Instagram: https://www.instagram.com/sokolcav

Linkedin: https://www.linkedin.com/in/sokol-%C3%A7avdarbasha-845426232/

Twitter: https://twitter.com/sokolicav

Sincerely,

Sokol Çavdarbasha.
