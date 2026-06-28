---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-08-15_how-i-was-able-to-send-authentic-emails-as-others-google-vrp-resolved.md
original_filename: 2020-08-15_how-i-was-able-to-send-authentic-emails-as-others-google-vrp-resolved.md
title: How I was able to send Authentic Emails as others — Google VRP [Resolved]
category: documents
detected_topics:
- xss
- idor
- ssrf
- command-injection
- business-logic
- api-security
tags:
- imported
- documents
- xss
- idor
- ssrf
- command-injection
- business-logic
- api-security
language: en
raw_sha256: 90fc546057335435c38dd27b214dec274fb32840edb05c4f4a03412d5a421962
text_sha256: 600af75d3c67c0a9be10b9228299536f121048cfd2c9080138827cdfc1bccaef
ingested_at: '2026-06-28T07:32:03Z'
sensitivity: unknown
redactions_applied: false
---

# How I was able to send Authentic Emails as others — Google VRP [Resolved]

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-08-15_how-i-was-able-to-send-authentic-emails-as-others-google-vrp-resolved.md
- Source Type: markdown
- Detected Topics: xss, idor, ssrf, command-injection, business-logic, api-security
- Ingested At: 2026-06-28T07:32:03Z
- Redactions Applied: False
- Raw SHA256: `90fc546057335435c38dd27b214dec274fb32840edb05c4f4a03412d5a421962`
- Text SHA256: `600af75d3c67c0a9be10b9228299536f121048cfd2c9080138827cdfc1bccaef`


## Content

---
title: "How I was able to send Authentic Emails as others — Google VRP [Resolved]"
url: "https://medium.com/bugbountywriteup/how-i-was-able-to-send-authentic-emails-as-others-google-vrp-resolved-2af94295f326"
authors: ["Sriram Kesavan (@sriramoffcl)"]
programs: ["Google"]
bugs: ["Logic flaw", "HTML injection", "Email spoofing", "Open mail relay"]
publication_date: "2020-08-15"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4319
scraped_via: "browseros"
---

# How I was able to send Authentic Emails as others — Google VRP [Resolved]

How I was able to send Authentic Emails as others — Google VRP [Resolved]
Sriram Kesavan
Follow
4 min read
·
Aug 15, 2020

477

2

Report ID: 161777102 — Google VRP

Well I went back to Google VRP after 3 months to rank up on the Hall of Fame. And Google Cloud caught my attention and I decided to hunt bugs there.

Press enter or click to view image in full size

NOTE: This isn’t my usual complicated write-up, but this is about a simple and clean logical vulnerability that I found on Google Cloud product which I wanted to share here.

I went through Google Cloud and one product got my attention. It was Appsheet which became my favorite target on entire Google Cloud products list. Coz I spent days understanding the application which made me easier to hunt for more bugs.

After 20 mins of understanding the application I found a interesting page on https://www.appsheet.com/partners

It had a form to enroll as a partner with some input fields like Name, Email and Request to send a mail to the respective organization.

Press enter or click to view image in full size

At first this contact form did not draw my much attention instead I found a couple of IDOR’s on the application which was reported to Google VRP and resolved. You can find the write-ups here

Then the contact form totally got my attention when I found something suspicious on the request.

I found four parameters on the request, they were

“PartnerEmail”: ”Destination Partner Email”

“userName”: “My Username”

“userEmail”: “My Email”

“userRequest”: “My Message”

I tried Server Side Injection on the userRequest parameter but had no luck. But It was vulnerable to HTML Injection. When I sent userRequest as <img src=“test.png”> the image got reflected on the mail.

Get Sriram Kesavan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

But Google isn’t gonna accept HTML Injection until it cannot be escalated to XSS. I couldn’t fire up a XSS or test for SSRF coz, it had a Cloud-flare at the back-end which literally blocked all my XSS payloads.

And then I tried replacing the partner Email to “admin@google.com” and forwarded the request. I had no belief that I will receive a email but to my surprise I received a email. Just like “admin@google.com” sent a mail with my message included on the form.

Wait, whaaat?!

Whaaaaaaaaaaaaaat !!

No blocking mechanism, Passed the super cool Google Spam filter without any issues and the most important thing is Google Magic automatically marked the email as Important. And I was even able to send emails as any gmail user.

userEmail parameter can be also replaced with any email, which means I can send emails as Donald Trump to Kim Jong-un without exposing my identity.

And soon realized it was vulnerable to Open Mail Relay attack which really happens on applications these days.

Google Magic added my spoofed mail as Important

I can send emails as any person to even fire an employee from a organization and even send emails for phishing or other possible attacks. On the other hand it can be used as a mail box to roll out massive email campaign without any issues and even without spending a single penny. And, no worries about mails getting ended up in spam Coz, They are from Google Systems and even signed by google.com from a Google Cloud — Appsheet and since the message parameter was vulnerable to HTML Injection it was even more possible to send emails with more authenticity by adding images and href tags.

An attacker simply has to fill the form with all details with simply tamper the request to send this authentic spoofed mail as any mail user.

I quickly reported the issue to Google and issue was accepted and resolved within 48 hours :)

Write-ups on the IDOR vulnerabilities I found on Google Cloud will be published once issues gets resolved ! Stay Tuned !!

Well if you love this write up drop a clap 👏, let’s connect then:

Twitter: sriramoffcl

Instagram: sriram_offcl

LinkedIn: sriramkesavan

Donate: https://paypal.me/sri123

Peace ✌️ !!!
