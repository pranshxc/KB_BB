---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-17_how-i-chained-multiple-high-impact-vulnerabilities-to-create-a-critical-one.md
original_filename: 2023-03-17_how-i-chained-multiple-high-impact-vulnerabilities-to-create-a-critical-one.md
title: How I chained multiple High-impact vulnerabilities to create a critical one.
category: documents
detected_topics:
- otp
- idor
- command-injection
- api-security
tags:
- imported
- documents
- otp
- idor
- command-injection
- api-security
language: en
raw_sha256: 645de11c47ed94a92e0ab3fff47e2820569d422641dce3b21f86e765e9941a1f
text_sha256: 5295e61f7d35bd9811fd7d2829ed2179249de1fcd4d1a587436f3e18ae504ff6
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# How I chained multiple High-impact vulnerabilities to create a critical one.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-17_how-i-chained-multiple-high-impact-vulnerabilities-to-create-a-critical-one.md
- Source Type: markdown
- Detected Topics: otp, idor, command-injection, api-security
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `645de11c47ed94a92e0ab3fff47e2820569d422641dce3b21f86e765e9941a1f`
- Text SHA256: `5295e61f7d35bd9811fd7d2829ed2179249de1fcd4d1a587436f3e18ae504ff6`


## Content

---
title: "How I chained multiple High-impact vulnerabilities to create a critical one."
url: "https://princej-76.medium.com/how-i-chained-multiple-high-impact-vulnearbilities-to-create-a-critical-one-476950a3bb9f"
authors: ["Vinay Jagetiya (@princej_76)"]
bugs: ["Account takeover", "IDOR", "OTP bypass", "HTTP response manipulation"]
publication_date: "2023-03-17"
added_date: "2023-03-18"
source: "pentester.land/writeups.json"
original_index: 1365
scraped_via: "browseros"
---

# How I chained multiple High-impact vulnerabilities to create a critical one.

How I chained multiple High-impact vulnerabilities to create a critical one.
Vinay Jagetiya (princej_76)
Follow
2 min read
·
Mar 17, 2023

33

1

Hello Everyone!!! I am Vinay Jagetiya (princej_76) and I am back again with my one of the most interesting finding.

I will explain how I found high impact vulnerabilities and chained them to create critical one.

Here we go!!!

Lets say the domain is ‘xyz.com’. I created an account and it created a subdomain of my username for my profile (username.xyz.com).

I logged in with my email and password and entered my mobile number and saved. I got link on my email to get my number verified.

The link was like ‘username.xyz.com/<token>’ (and token was an integer like ‘xxxxxx’)

I thought to tamper with that token so i changed (incremented and decremented the token number).

Get Vinay Jagetiya (princej_76)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

After some 404 errors, at some tokens I got redireced to other users subdomains for mobile verification.

I can now see User’s name, email id, his/her subdomain address and Phone number, with a button for mobile verification so I clicked on that button and it sent an OTP on the respective number, hence I didn’t have access to OTP so I tried response manipulation and it worked, I changed reponse in burp-suite.

Then it redireccted me to enter new password. I entered new password.

Now I had everything his credentials, his profile subdomain, username.

So I logged in to the account(s) and I took over many user account, even suspended accounts, which i can reactivate by generating ticket in help center.

SUMMARY: Those were three high or critical vulnerabilities (PII, OTP bypass and Account takeover) chained together to form a mass account takeover without social engineering or user interaction.

If you like the blog you can connect me on

Twitter: https://twitter.com/princej_76

Linkedin: https://www.linkedin.com/in/vinay-jagetiya/
