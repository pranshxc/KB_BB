---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-03-01_exfiltrating-aws-credentials-via-pdf-rendering-of-unsanitized-input.md
original_filename: 2023-03-01_exfiltrating-aws-credentials-via-pdf-rendering-of-unsanitized-input.md
title: Exfiltrating AWS Credentials via PDF Rendering of Unsanitized Input
category: documents
detected_topics:
- access-control
- ssrf
- xss
- cloud-security
- sso
- command-injection
tags:
- imported
- documents
- access-control
- ssrf
- xss
- cloud-security
- sso
- command-injection
language: en
raw_sha256: 95c95be0a1b281f80574f91ee0c30e537b7805e3bfe7a01c9f103e642089ae14
text_sha256: 08f5b1388252ed6835b2d761315be4f3c550aeaea24928dfc052cff6a744cb4a
ingested_at: '2026-06-28T07:32:19Z'
sensitivity: unknown
redactions_applied: false
---

# Exfiltrating AWS Credentials via PDF Rendering of Unsanitized Input

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-03-01_exfiltrating-aws-credentials-via-pdf-rendering-of-unsanitized-input.md
- Source Type: markdown
- Detected Topics: access-control, ssrf, xss, cloud-security, sso, command-injection
- Ingested At: 2026-06-28T07:32:19Z
- Redactions Applied: False
- Raw SHA256: `95c95be0a1b281f80574f91ee0c30e537b7805e3bfe7a01c9f103e642089ae14`
- Text SHA256: `08f5b1388252ed6835b2d761315be4f3c550aeaea24928dfc052cff6a744cb4a`


## Content

---
title: "Exfiltrating AWS Credentials via PDF Rendering of Unsanitized Input"
url: "https://cristivlad.medium.com/exfiltrating-aws-credentials-via-pdf-rendering-of-unsanitized-input-63f39d60d963"
authors: ["Cristi Vlad (@CristiVlad25)"]
bugs: ["SSRF", "HTML injection", "XSS"]
publication_date: "2023-03-01"
added_date: "2023-03-02"
source: "pentester.land/writeups.json"
original_index: 1450
scraped_via: "browseros"
---

# Exfiltrating AWS Credentials via PDF Rendering of Unsanitized Input

Exfiltrating AWS Credentials via PDF Rendering of Unsanitized Input
Cristi Vlad
Follow
4 min read
·
Mar 1, 2023

266

1

I know the title is a mouthful; submissions are open for better candidates. If you have one, suggest it below!

In a recent pentest I did for a client, the scope included a banking/financial application.

From the very start, mostly nothing worked from my side of the testing, but this is good because it means that the client has a solid app.

Testing for broken access controls and permissions was close to impossible. The session token had a TTL of 10 minutes, after which you’d be logged out, the app would hang for a few minutes (technical glitch presumably), then you’d have to login again with password and 2FA.

And after setting up two accounts for testing, which took 2–3 minutes, you’d have about 6–7 minutes of testing until being logged out again. Pain in the ass, I tell you. It got me very frustrated.

At one point, I was cataloging all the functionalities of the app when I saw a feature to download a void check. This was a feature that allowed you to preview a check with your details and the company’s logo/name.

Upon clicking the download button, it would take you to an API of the company, where your voided check was rendered. The URL looked something like this:

https://example.com/api/docs/check?name=MarcusAu&address=12 Main Street&checkNo=12&accNo=12&routing=12

This was a simple GET request, unauthenticated. Harmless, right?

So I thought too. These guys/gals have very hardened security for this app. They couldn’t fail to validate or properly sanitize all these URL parameters, right? Right?

But, let me just try and replace name=MarcusAu with name=<h1>this</h1>that.

No way! Ok, let’s try some XSS payloads! I don’t like XSS and aside from the generic XSS testing in my pentests for compliance purposes, I rarely go deeper.

Get Cristi Vlad’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

And, for that matter, nothing worked here. When I would try to alert, prompt, or confirm something, the request would hang indefinitely. So, something was definitely happening in the backend. But me not being XSS astute…

Let me take a step back, instead of alert, prompt, or confirm, let me make sure the script tags can be used: <script>document.write(window.location)</script>

Now what? What would be the most impactful thing that I could try and gain from here? I tried a bunch of stuff from the browser’s API. It all worked (like getting some location information, stuff about the operating system, etc), but it didn’t seem too important.

Just to clarify, in pentesting you have to show the impact of your findings, but it’s not like in bug bounties, where unless you dump the entire database, it’s N/A, dupe, or informational. This is one of the reasons I rarely do bounties. I don’t even have the time for them, given the amount of pentesting work I get from clients.

With this vulnerability, I could have just specified the ability to inject HTML and suggest they should sanitize the parameter and move on. But I wanted to play more!

Then I remembered I read a write-up a while ago of someone getting metadata via XSS.

Let me take another step back here and say (as I keep saying on my YouTube channel and on Twitter) that one of the fastest ways to grow your skills in penetration testing is to read write-ups and (maybe, just maybe) participate in VDPs (not paid bounties). No CTFs, no hacking the boxes or similar platforms, but straight-forward, hands-on, real-world experience by reading what worked for others and by doing via VDPs. My $0.02, don’t take it personally.

And this proved to me (one more time) to be the right decision. After some back and forth, my final crafted payload was: <script>window.location=”http://169.254.169.254/latest/meta-data/iam/security-credentials/<hostname>"</script>

Press enter or click to view image in full size

One of the lessons I learned from my pentesting experience and reconfirmed here was that I should never trust appearances. This app was rock solid when it comes to permissions, authorization, BAC, and overall input sanitization.

However, with an issue like this, it often is all in vain. You only need one malicious actor to get their hands on your secret keys to spell disaster.

I’ve got some other cool vulnerabilities I found recently and keep finding in my pentests and I might write about them if and when I have the time. Stay tuned here and on my Substack weekly blog.
