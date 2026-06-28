---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-09-01_a-story-about-how-i-found-xss-in-asus.md
original_filename: 2024-09-01_a-story-about-how-i-found-xss-in-asus.md
title: A Story About How I Found XSS in ASUS
category: documents
detected_topics:
- xss
- supply-chain
- command-injection
- api-security
- mobile-security
tags:
- imported
- documents
- xss
- supply-chain
- command-injection
- api-security
- mobile-security
language: en
raw_sha256: 8a6ba0a246990621f140c3761973a88e33c6d4048d857e945180ad65b961b3ed
text_sha256: 68daf087a0162aeb7f7fd562f8b242db4ed03f8c7a1f319fd2ff9cc4fbbc7095
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# A Story About How I Found XSS in ASUS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-09-01_a-story-about-how-i-found-xss-in-asus.md
- Source Type: markdown
- Detected Topics: xss, supply-chain, command-injection, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `8a6ba0a246990621f140c3761973a88e33c6d4048d857e945180ad65b961b3ed`
- Text SHA256: `68daf087a0162aeb7f7fd562f8b242db4ed03f8c7a1f319fd2ff9cc4fbbc7095`


## Content

---
title: "A Story About How I Found XSS in ASUS"
url: "https://infosecwriteups.com/a-story-about-how-i-found-xss-in-asus-cb233ce3bb9c"
authors: ["Karthikeyan.V (@karthithehacker)"]
programs: ["Asus"]
bugs: ["XSS"]
publication_date: "2024-09-01"
added_date: "2024-09-04"
source: "pentester.land/writeups.json"
original_index: 27
scraped_via: "browseros"
---

# A Story About How I Found XSS in ASUS

Top highlight

A Story About How I Found XSS in ASUS
Karthikeyan.V
Follow
2 min read
·
Sep 1, 2024

136

1

A few months ago, during a routine security assessment, I uncovered a significant cross-site scripting (XSS) vulnerability in the ASUS Laravel Ignition debugging tool. This vulnerability, identified as R-XSS, posed a high risk due to the potential for unauthorized script execution in users’ browsers. Here’s how I discovered and explored this vulnerability.

Press enter or click to view image in full size
The Discovery

While examining the target, I noticed that the Laravel Ignition debug mode was enabled on adam.asus.com, and the endpoint was vulnerable to XSS. The vulnerability was exposed through the following URL:

Vulnerable URL: http://adam.asus.com/_ignition/scripts/--%3E%3Csvg%20onload=alert('cappriciosec.com')%3E

When accessing this URL, the embedded script was executed in the user’s browser, confirming the presence of an XSS vulnerability.

Understanding the Vulnerability
Bug Name: R-XSS
Bug Priority: High
Vulnerable URL: http://adam.asus.com/_ignition/scripts/--%3E%3Csvg%20onload=alert('cappriciosec.com')%3E
Impact

The impact of this XSS vulnerability depends on the application’s context and the privileges of the compromised user. For example:

Minimal Impact: In applications with public information, the impact might be negligible.
Serious Impact: In applications handling sensitive data, such as financial transactions or healthcare records, the impact could be severe, allowing unauthorized access to private information.
Critical Impact: If a user with elevated privileges is compromised, the attacker could gain full control of the application, affecting all users and data.
Steps to Reproduce

To confirm the vulnerability, follow these steps:

Access the Vulnerable URL: Open the URL in your browser: http://adam.asus.com/_ignition/scripts/--%3E%3Csvg%20onload=alert('cappriciosec.com')%3E
Observe the Script Execution: The script will execute in your browser, displaying an alert with the text cappriciosec.com.
Automating the Hunt

To streamline the process, I built a Python tool specifically for detecting this vulnerability. You can install it using pip and automate your testing:

Get Karthikeyan.V’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

ToolPOC: laravel-ignition-rxss on github

pip install laravel-ignition-rxss 
laravel-ignition-rxss --chatid <YourTelegramChatID>
To Check a Single URL:
laravel-ignition-rxss -u http://mytargetprogram.com
To Check a List of URLs:
laravel-ignition-rxss -i urls.txt
Remediation

To mitigate this vulnerability, it is essential to disable debug mode by setting APP_DEBUG to false in the environment configuration. This will prevent unauthorized script execution and protect users from potential XSS attacks.

POC by: @karthithehacker
Mail: contact@karthithehacker.com
Website: https://www.karthithehacker.com/

If you’re interested in our VAPT service, contact us at ceo@cappriciosec.com or contact@cappriciosec.com.

For enrolling my cybersecurity and Bugbounty course,

WhatsApp +91 82709 13635.

Connect with me:

Twitter: https://twitter.com/karthithehacker

Instagram: https://www.instagram.com/karthithehacker/

LinkedIn: https://www.linkedin.com/in/karthikeyan--v/

Website: https://www.karthithehacker.com/

Github : https://github.com/karthi-the-hacker/

npmjs: https://www.npmjs.com/~karthithehacker

Youtube: https://www.youtube.com/@karthi_the_hacker

Thank you

Karthikeyan.V
