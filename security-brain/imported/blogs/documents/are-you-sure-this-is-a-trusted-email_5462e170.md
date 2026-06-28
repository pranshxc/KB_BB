---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2018-06-05_are-you-sure-this-is-a-trusted-email.md
original_filename: 2018-06-05_are-you-sure-this-is-a-trusted-email.md
title: Are you sure this is a trusted email?
category: documents
detected_topics:
- sso
- command-injection
- password-reset
- api-security
tags:
- imported
- documents
- sso
- command-injection
- password-reset
- api-security
language: en
raw_sha256: 5462e170ce7ee2ef04f39d4ec26a247873809937f1a763f8979037e981a96f2f
text_sha256: 7898a34e6f1c54a3892bef6e659af23147ffc796a31a2422d6c0ae3d07e54e53
ingested_at: '2026-06-28T07:31:57Z'
sensitivity: unknown
redactions_applied: false
---

# Are you sure this is a trusted email?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2018-06-05_are-you-sure-this-is-a-trusted-email.md
- Source Type: markdown
- Detected Topics: sso, command-injection, password-reset, api-security
- Ingested At: 2026-06-28T07:31:57Z
- Redactions Applied: False
- Raw SHA256: `5462e170ce7ee2ef04f39d4ec26a247873809937f1a763f8979037e981a96f2f`
- Text SHA256: `7898a34e6f1c54a3892bef6e659af23147ffc796a31a2422d6c0ae3d07e54e53`


## Content

---
title: "Are you sure this is a trusted email?"
url: "https://medium.com/@khaled.hassan/are-you-sure-this-is-a-trusted-email-291121028320"
authors: ["Khaled Hassan"]
bugs: ["Open mail relay"]
bounty: "900"
publication_date: "2018-06-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5854
scraped_via: "browseros"
---

# Are you sure this is a trusted email?

Are you sure this is a trusted email?
Khaled Hassan
Follow
4 min read
·
Jun 5, 2018

283

2

Hey,

This is my first writeup about a security vulnerability that I have recently found in a private bug bounty program.

This program is a popular accountant software. The story started when I was going to send an Invoice that I have created on the website to an external email address.

So I sent the invoice to my test email address and I noticed something strange, I noticed that the website emailing system uses the customer email address to send the invoice email on behalf of his email address and that was rather odd to me because I didn’t see this function before , So I decided to take a deep look at this feature.

The HTTP request of sending invoice was something like this

Press enter or click to view image in full size

Quickly I noticed that mail_from parameter is under control of attacker. Then I tried to modify this parameter to the email address that website uses to emailing their customers which is ( info@website.com ) and I changed my account name to be the same which is ( Team reacted )

And after a few seconds of sending the request. I found this in my inbox.

Press enter or click to view image in full size

I really was shocked by the result. The email has been sent behalf of website system itself. So I started to figure out the cause of this vulnerability and thought of ways to exploit it.

So let me explain how this happened. The first step, I started to compare between two emails , that I sent from ( info@website.co ) using vulnerability I found, and another one that website emailing system has sent when I required to resetting my password.

The header of two emails was as follows:

Details of email that I sent to myself using the vulnerability:

From: Team reacted <info@reacted.co> Using PHPMailer 6.0.3 (https://github.com/PHPMailer/PHPMailer)
To: team@seecureapp.com
Subject: Just a message
SPF: PASS with IP 203.25.220.41 Learn more
DKIM:'PASS' with domain zonevs.eu Learn more``

Details of email that website system has sent to me when I required password reset:

From: Team reacted  <info@reacted.co> Using PHPMailer 5.2.21 (https://github.com/PHPMailer/PHPMailer)
To: khaled <khaled.hassan@seecureapp.com>
Subject: Password reset
SPF: PASS with IP 203.25.220.41 Learn more
DKIM: 'PASS' with domain zonevs.eu Learn more

As we can see, there is no any difference in two examples. From here we can find out that the SMTP server that responsible for sending emails using the vulnerable endpoint, is the same server that website using to emailing their customers.

H
ow I exploited this?

So I wanted to make the attack more successfully. Quickly I browsed to one of emails that website has sent to me when I was resting my password. Then I copied the HTML code of this email template.

A
busing website features

The website allows you to make email templates that you can use when send invoices. So I copied the HTML code of their original email and put it as email template

Get Khaled Hassan’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Original email

Press enter or click to view image in full size

Adding source code of their email >>>

Press enter or click to view image in full size

Email template after I put it as invoice e-mail:

Press enter or click to view image in full size

But what is inside Click here button? I have reported Subdomain takeover to the program and it has been fixed now. so I can’t use the subdomain takeover issue here. But I have good trick.

When you register an account at the website. The accounts of users are being registered like ( seecureapp.website.com ) so I registered an account username with this name ( payments.reacted.com ) To convince the user that this is the payment page.

Abusing webforms on the website:

This website also allows you to create a web form on your account to survey your customers. so I created a webform in payments account by this way.

Press enter or click to view image in full size

Another exploit:

So now I can ask website users to enter their passwords and credit cards as well and their credentials will be sent to me as webform answers.

Lessons learned:

When you test a website that sends emails behalf on user email. Don’t forget to test this attack, I tested it many many times and it get success in every website I face.
Try to abuse website features as you can. This was not too exploitable until I used some features in the attack.

Timeline.

Report Submitted : 30–4–2018

Report Triaged : 30–4–2018

$900 bounty Awarded : 7–5–2018
