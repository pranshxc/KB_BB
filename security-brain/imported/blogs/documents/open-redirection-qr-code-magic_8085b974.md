---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-12-11_open-redirection-qr-code-magic.md
original_filename: 2021-12-11_open-redirection-qr-code-magic.md
title: Open Redirection - QR Code Magic
category: documents
detected_topics:
- mobile-security
- xss
- sqli
- command-injection
- api-security
- supply-chain
tags:
- imported
- documents
- mobile-security
- xss
- sqli
- command-injection
- api-security
- supply-chain
language: en
raw_sha256: 8085b974ea4494278263fea05e545a3ea9a9fcbebd075e0d4911b7196bd1d83c
text_sha256: 73f3a327e1c642ffb019a276f175c239167f8c535b3af7ccddc88782a9037b37
ingested_at: '2026-06-28T07:32:08Z'
sensitivity: unknown
redactions_applied: false
---

# Open Redirection - QR Code Magic

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-12-11_open-redirection-qr-code-magic.md
- Source Type: markdown
- Detected Topics: mobile-security, xss, sqli, command-injection, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:08Z
- Redactions Applied: False
- Raw SHA256: `8085b974ea4494278263fea05e545a3ea9a9fcbebd075e0d4911b7196bd1d83c`
- Text SHA256: `73f3a327e1c642ffb019a276f175c239167f8c535b3af7ccddc88782a9037b37`


## Content

---
title: "Open Redirection - QR Code Magic"
url: "https://shahjerry33.medium.com/open-redirection-qr-code-magic-18ace1a0170f"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Open redirect"]
publication_date: "2021-12-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3093
scraped_via: "browseros"
---

# Open Redirection - QR Code Magic

Open Redirection - QR Code Magic
Jerry Shah (Jerry)
Follow
3 min read
·
Dec 11, 2021

185

Press enter or click to view image in full size

Summary :

Open redirection vulnerabilities arise when an application incorporates user-controllable data into the target of a redirection in an unsafe way. By modifying untrusted URL input to a malicious site, an attacker may successfully launch a phishing scam and steal user credentials.

The cybersecurity community doesn’t put enough emphasis on Open Redirect Vulnerabilities because it is considered a simple flaw commonly connected to phishing scams and social engineering.

Description :

I have found an Open Redirection vulnerability in one of the public program of YesWeHack but it went duplicate. The mobile application was using a QR Code scanner to track the consignments (check package details). After somewhat research I found a blog on how a QR Code functionality can be exploited. In the blog it was exploited to XSS but in my case I was only able to escalate it to an Open Redirection vulnerability.

Press enter or click to view image in full size
Duplicate

QR Code Scanner Briefing :

A QR code scanner is an optical scanning device that is able to read QR codes. Now-a-days many applications are using this feature, so it can be used for browsing websites, checking address details, payments, adding users etc.

Many applications have restricted the use of this feature to limited things. For example, the QR Code Scanner is implemented in Google Pay so it will only be used for sending and receiving payments, you will not be able to use it to surf the internet and if this feature is implemented on any browser then you will be able to surf the internet and will not be able to make payments. In my case the company didn’t restrict the use of its functionality to only track consignments and that thing lead to Open Redirection vulnerability.

How I found this vulnerability ?

I registered on the target’s android application
Then I found the QR Code scanner feature
Press enter or click to view image in full size
QR Code Scanner

3. I went to https://www.the-qrcode-generator.com/ to generate a custom QR Code for Open Redirection vulnerability

Press enter or click to view image in full size
QR Code - Open Redirection

4. After generating the custom QR Code I scanned it with the scanner of target’s android application and it got redirected

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Proof Of Concept (Use full screen to view) : https://drive.google.com/file/d/1eXUMu9ZzN9aAUJ8pEyMM5vZsn3wTJgnt/view?usp=sharing

Why this happen ?

In my opinion,

This happened due to no restriction on what to scan. The scan should have been restricted to only track consignments and not to scan URLs. The XSS did not happened because it was not supporting “javascript URI”.

Issue Escalations :

Open Redirection
XSS (https://payatu.com/blog/nikhil-mittal/firefox-ios-qr-code-reader-xss-%28cve-2019-17003%29)
SQLi (https://www.irongeek.com/xss-sql-injection-fuzzing-barcode-generator.php)

Impact :

An attacker can exploit this kind of and can construct a URL within the application that causes a redirection to an arbitrary external domain. This behavior can be leveraged to facilitate phishing attacks against users of the application.

Mitigation :

A proper fix would be having there company’s symbol in the QR Code just like WhatsApp and Instagram has it, so it will not scan any customize QR Code. Moving forward for another fix would be restricting the scan to its function only (track consignments in my case).

Press enter or click to view image in full size
