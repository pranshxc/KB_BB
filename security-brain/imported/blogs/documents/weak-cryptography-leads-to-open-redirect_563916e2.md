---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-05-30_weak-cryptography-leads-to-open-redirect.md
original_filename: 2020-05-30_weak-cryptography-leads-to-open-redirect.md
title: Weak Cryptography Leads To Open Redirect
category: documents
detected_topics:
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
tags:
- imported
- documents
- command-injection
- otp
- automation-abuse
- api-security
- supply-chain
language: en
raw_sha256: 563916e2547de4f57079761b150954e70ac4c73da68050408cd4f58520e7aed1
text_sha256: beb0ce2fee94cf6d26538afa713b99aed10c5e6ffb4fc05ecd2056d27eb97736
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# Weak Cryptography Leads To Open Redirect

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-05-30_weak-cryptography-leads-to-open-redirect.md
- Source Type: markdown
- Detected Topics: command-injection, otp, automation-abuse, api-security, supply-chain
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `563916e2547de4f57079761b150954e70ac4c73da68050408cd4f58520e7aed1`
- Text SHA256: `beb0ce2fee94cf6d26538afa713b99aed10c5e6ffb4fc05ecd2056d27eb97736`


## Content

---
title: "Weak Cryptography Leads To Open Redirect"
url: "https://medium.com/bugbountywriteup/weak-cryptography-leads-to-open-redirect-3fe052c12995"
authors: ["DarkLotus (@darklotuskdb)"]
bugs: ["Open redirect"]
publication_date: "2020-05-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4547
scraped_via: "browseros"
---

# Weak Cryptography Leads To Open Redirect

Weak Cryptography Leads To Open Redirect
DarkLotus
Follow
3 min read
·
May 30, 2020

220

Press enter or click to view image in full size

Hello Everyone!,
I hope you are doing good and safe. If you are a noob in bug hunting you can check my previous blog and today I am going to share an interesting finding of mine, that is Open Redirect Vulnerability.

What is Open Redirect?
Open redirection vulnerabilities arise when an application incorporates user-controllable data into the target of a redirection in an unsafe way. An attacker can construct a URL within the application that causes a redirection to an arbitrary external domain. This behaviour can be leveraged to facilitate phishing attacks against users of the application. The ability to use an authentic application URL, targeting the correct domain and with a valid SSL certificate (if SSL is used), lends credibility to the phishing attack because many users and even if they verify these features, they will not notice the subsequent redirection to a different domain.

Let's start!, We call our target as target.com. My first step is to always do recon because it plays an important role in finding bugs. Through waybackurls tool, I got many endpoints of the target and then I filtered the URLs having “redirect” parameter through grep command and the result was like this:

https://login.target.com/login?redirect=aHR0cHM6Ly9hcHAudGFyZ2V0LmNvbS9kYXNoYm9hcmR8MzJ8YUhSMGNITTZMeTloY0hBdWRHRnlaMlYwTG1OdmJTOWtZWE5vWW05aGNtUT0%3D

first of all, I copied the redirect value and changed “%3D” to “=” (URL-decoded), so now its look like this:

aHR0cHM6Ly9hcHAudGFyZ2V0LmNvbS9kYXNoYm9hcmR8MzJ8YUhSMGNITTZMeTloY0hBdWRHRnlaMlYwTG1OdmJTOWtZWE5vWW05aGNtUT0=

Its look like Base64 Encoded value so straight forward I decoded it and got this:

https://app.target.com/dashboard|32|aHR0cHM6Ly9hcHAudGFyZ2V0LmNvbS9kYXNoYm9hcmQ=

For a few seconds, I was wondering what the hell it is after URL. then I got to know that “32” is the length of the URL from “https” first “h” to “dashboard” last “d” and after this, they have given a token which is nothing but just Base64 Encoded value of the URL.

Get DarkLotus’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Server Backend Flow:
User Login -> Base64 decode redirect value -> checking the integrity by URL length & Encoded value -> If all good -> Redirect

Now you can imagine how I was feeling and my next step is to create a redirect to a malicious site. so for this, my first step is to count the length of the URL and then encode URL to Base64, very simple know?

Steps To Create:
1. First Count the Number of characters, symbols, numbers, etc in the URL:
https://evil.com => 16

2. Now simply Base64 Encode the URL:
https://evil.com => aHR0cHM6Ly9ldmlsLmNvbQ==

3. Use a pipe as separator and combine both the values along with malicious URL and now our payload looks like:
https://evil.com|16|aHR0cHM6Ly9ldmlsLmNvbQ==

4. Now just encode the payload in Base64:
aHR0cHM6Ly9ldmlsLmNvbXwxNnxhSFIwY0hNNkx5OWxkbWxzTG1OdmJRPT0=

5. Do URL encoding of “=” i.e “%3D”.

Simply put the final Base64 encoded value in the “redirect” parameter of vulnerable URL and we are ready to execute.

https://login.target.com/login?redirect=aHR0cHM6Ly9ldmlsLmNvbXwxNnxhSFIwY0hNNkx5OWxkbWxzTG1OdmJRPT0%3D

And after login, the site smoothly redirected to EVIL.COM. I hope you enjoyed this writeup! If you like my work buy-me-a-coffee and follow me on twitter for some cool tricks.

Thank You
