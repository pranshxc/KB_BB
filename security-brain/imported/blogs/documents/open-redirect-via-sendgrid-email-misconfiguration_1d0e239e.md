---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-03-13_open-redirect-via-sendgrid-email-misconfiguration.md
original_filename: 2022-03-13_open-redirect-via-sendgrid-email-misconfiguration.md
title: Open Redirect via Sendgrid Email Misconfiguration
category: documents
detected_topics:
- otp
- command-injection
- api-security
tags:
- imported
- documents
- otp
- command-injection
- api-security
language: en
raw_sha256: 1d0e239ebbe03cc03fa68e97024834ee6bc133d09c5be6e7f3d63516e1e66d64
text_sha256: c77e0f7f0e73f1b42f1b66242a1d41ff5246ae6c5b62f07b42198a8d07fd5698
ingested_at: '2026-06-28T07:32:10Z'
sensitivity: unknown
redactions_applied: false
---

# Open Redirect via Sendgrid Email Misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-03-13_open-redirect-via-sendgrid-email-misconfiguration.md
- Source Type: markdown
- Detected Topics: otp, command-injection, api-security
- Ingested At: 2026-06-28T07:32:10Z
- Redactions Applied: False
- Raw SHA256: `1d0e239ebbe03cc03fa68e97024834ee6bc133d09c5be6e7f3d63516e1e66d64`
- Text SHA256: `c77e0f7f0e73f1b42f1b66242a1d41ff5246ae6c5b62f07b42198a8d07fd5698`


## Content

---
title: "Open Redirect via Sendgrid Email Misconfiguration"
url: "https://medium.com/@rifqihz/open-redirect-via-sendgrid-email-misconfiguration-cec4ccb07f9a"
authors: ["Rifqi Hilmy Zhafrant"]
bugs: ["Open redirect"]
bounty: "250"
publication_date: "2022-03-13"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2828
scraped_via: "browseros"
---

# Open Redirect via Sendgrid Email Misconfiguration

Press enter or click to view image in full size
Link
Open Redirect via Sendgrid Email Misconfiguration
Rifqi Hilmy Zhafrant
Follow
3 min read
·
Mar 13, 2022

84

1

Hello developer , bug hunter and cyber security enthusiast. In this opportunity i wanna show you my first Bug Bounty writeup from one of a Hackerone public bug bounty program

Brief Information

Bug Type : Open Redirect

Severity : Low

Bounty : $200 Bounty + $50 Retest

Timeline :

26 January — Reported
28 January — Closed as Informative
28 January — Add new attack flow
5 February — Triaged
14 February — Bounty rewarded
24 February — Retest
24 February — Resolved

Open redirect (CWE-601) is a vulnerability when a user can control the input to the external website and use that to redirect.

When this article published , the report is not disclosed yet . So lets call the company website as xyz.com.

Let’s Start

I was looking for an account takeover vulnerability via change email address feature. To change the email address we need an OTP from the new email address. After sometime looking around unfortunately i didn’t find the vulnerability.

Then i moved on to the profile page and saw there’s a nickname form. I tried to change the nickname to “www.evil.com” and “http://evil.com”. But no error occurred , so i assume there’s no restriction to using symbol in the nickname.

Get Rifqi Hilmy Zhafrant’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

I was check the email from the change email address before and found that my nickname is included in the email. Then i changed my email again to see how my nickname get converted in the email

Dear www.evil.com,
We have received your change e-mail address request.
As soon as  you've confirmed your identity with the verification code, you'll be  able to use your new e-mail address with our services.
Please enter the following verification code on the e-mail address change page.

Verification code: 123456
....
--------------------------------------------------------------------
Dear http://www.evil.com,
We have received your change e-mail address request.
As soon as  you've confirmed your identity with the verification code, you'll be  able to use your new e-mail address with our services.
Please enter the following verification code on the e-mail address change page.

Verification code: 123456
....

The www.evil.com was become a redirect link to http://www.evil.com. But when i tried to use the http://www.evil.com , it generated a link like link.xyz.com/ls/click?upn=some_long_random_string which also redirect to http://www.evil.com.

Why did that happen?

click?upn=some_long_random_string was a Sendgrid click tracking feature.

https://docs.sendgrid.com/ui/account-and-settings/tracking

There’s a misconfiguration in xyz’s Sendgrid email causing the nickname get overwritten to link.xyz.com .

At that point i thought i found an open redirect bug and immediately report it. But later on the report was disclosed as informative.

Press enter or click to view image in full size
“Light Bulb” Moment

In the same day as the report closed as informative , i found out that the xyz.com have return_to parameter in the root path to redirect to external link but it was limited to only accept whitelisted domain.

Then i got a new idea for a better attack flow. Since i could generate a link with my nickname and the generated link was in link.xyz.com domain. So why i don’t try to use the link.xyz.com as a redirect parameter?

Yes , my theory worked. We can redirect to evil.com using link.xyz.com as parameter

Finally the final open redirect payload was like :
xyz.com/?return_to=link.xyz.com/ls/click?upn=some_long_random_string

Redirect flow :
xyz.com -> link.xyz.com/ls/click?upn=some_long_random_string -> www.evil.com

References
https://docs.sendgrid.com/ui/sending-email/universal-links
https://docs.sendgrid.com/ui/account-and-settings/tracking
https://docs.sendgrid.com/ui/analytics-and-reporting/click-tracking-html-best-practices

Thank you for reading. Hopefully you learn something from this article.

Regards , Writer
