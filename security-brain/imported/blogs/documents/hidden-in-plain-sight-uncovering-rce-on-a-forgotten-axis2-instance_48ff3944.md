---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2024-08-23_hidden-in-plain-sight-uncovering-rce-on-a-forgotten-axis2-instance.md
original_filename: 2024-08-23_hidden-in-plain-sight-uncovering-rce-on-a-forgotten-axis2-instance.md
title: 'Hidden in Plain Sight: Uncovering RCE on a Forgotten Axis2 Instance'
category: documents
detected_topics:
- command-injection
- rate-limit
- api-security
- mobile-security
tags:
- imported
- documents
- command-injection
- rate-limit
- api-security
- mobile-security
language: en
raw_sha256: 48ff39446a495cdf4562306bef902d0f52ace3b149abe6ed66c03d69d0a231ac
text_sha256: 11d2b8979bf6e339a19212e6f6c7a02477047f7f899951f7741698e148112b8d
ingested_at: '2026-06-28T07:32:37Z'
sensitivity: unknown
redactions_applied: false
---

# Hidden in Plain Sight: Uncovering RCE on a Forgotten Axis2 Instance

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2024-08-23_hidden-in-plain-sight-uncovering-rce-on-a-forgotten-axis2-instance.md
- Source Type: markdown
- Detected Topics: command-injection, rate-limit, api-security, mobile-security
- Ingested At: 2026-06-28T07:32:37Z
- Redactions Applied: False
- Raw SHA256: `48ff39446a495cdf4562306bef902d0f52ace3b149abe6ed66c03d69d0a231ac`
- Text SHA256: `11d2b8979bf6e339a19212e6f6c7a02477047f7f899951f7741698e148112b8d`


## Content

---
title: "Hidden in Plain Sight: Uncovering RCE on a Forgotten Axis2 Instance"
url: "https://medium.com/@domenicoveneziano/hidden-in-plain-sight-uncovering-rce-on-a-forgotten-axis2-instance-86ddc91f1415"
authors: ["Domenico Veneziano"]
bugs: ["RCE", "Default credentials", "Axis2"]
publication_date: "2024-08-23"
added_date: "2024-08-26"
source: "pentester.land/writeups.json"
original_index: 47
scraped_via: "browseros"
---

# Hidden in Plain Sight: Uncovering RCE on a Forgotten Axis2 Instance

Hidden in Plain Sight: Uncovering RCE on a Forgotten Axis2 Instance
Domenico Veneziano
Follow
2 min read
·
Aug 23, 2024

44

2

Press enter or click to view image in full size
Introduction

While looking for interesting assets on one of Tryber’s bug bounty programs, I identified a simple yet impactful vulnerability.
The affected asset, which could not be located via other well known methods like Google Dorking or Wayback Machine logs, was discovered using the SecurityTrails API.
This hidden asset was hosting an Apache Axis2 instance, which, when accessed, revealed an admin login page.
The login page was vulnerable due to default credentials being left in place, that allowed me to access the administration panel and ultimately obtain a remote code execution.

Getting Access

The discovery of the Axis2 admin panel was not straightforward.
After identifying the asset using the SecurityTrails API, I proceeded to brute-force potential directories using a set of known paths.
To avoid detection by the Akamai WAF protecting the site, I employed residential rotating proxies while using a Nuclei template (CVE-2010–0219) for the scan.
Once the Axis2 login page was found, I could access it using the default credentials.
Although the website did not handle the login process correctly, it was still possible to navigate the admin panel by manually managing session cookies, which the server inconsistently applied.

Get Domenico Veneziano’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Getting RCE

With access to the Axis2 admin panel, I was able to exploit the system further by uploading a malicious .aar file.

Press enter or click to view image in full size

This file was crafted to implement a new service that could execute arbitrary commands on the server.
After successfully uploading the exploit, I gained remote code execution (RCE) capabilities, confirmed by accessing the reverse shell at redacted.com/axis2/services/config/exec?cmd=dir

Press enter or click to view image in full size
Conclusions

This report shows that sometimes the best finds are in places where no one else has thought to look.
Even websites that seem basic or unimportant can have serious vulnerabilities like RCE just a click away.
Using some creative techniques to bypass a strong web application firewall — like custom wordlists and rotating proxies — eventually pays off in these scenarios.
Don’t overlook any site, no matter how unappealing it might seem, because you never know where a major vulnerability might be hiding.
