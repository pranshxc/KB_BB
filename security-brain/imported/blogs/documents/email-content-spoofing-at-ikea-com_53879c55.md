---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-04-06_email-content-spoofing-at-ikeacom.md
original_filename: 2019-04-06_email-content-spoofing-at-ikeacom.md
title: Email content spoofing at IKEA.com
category: documents
detected_topics:
- path-traversal
- xss
- command-injection
- file-upload
- password-reset
- api-security
tags:
- imported
- documents
- path-traversal
- xss
- command-injection
- file-upload
- password-reset
- api-security
language: en
raw_sha256: 53879c551483c4d04ec2978bae9c68c79ff08340d2349509fc60422ac9ae4a2f
text_sha256: 29369c1874a0564f1eec8ebb658c0f62aa790e6ebf5d42b4fed303851fc582fe
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Email content spoofing at IKEA.com

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-04-06_email-content-spoofing-at-ikeacom.md
- Source Type: markdown
- Detected Topics: path-traversal, xss, command-injection, file-upload, password-reset, api-security
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `53879c551483c4d04ec2978bae9c68c79ff08340d2349509fc60422ac9ae4a2f`
- Text SHA256: `29369c1874a0564f1eec8ebb658c0f62aa790e6ebf5d42b4fed303851fc582fe`


## Content

---
title: "Email content spoofing at IKEA.com"
url: "https://medium.com/@jonathanbouman/email-content-spoofing-at-ikea-com-ea76c17605ee"
authors: ["Jonathan Bouman (@JonathanBouman)"]
programs: ["Ikea"]
bugs: ["Email content spoofing"]
bounty: "50"
publication_date: "2019-04-06"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5324
scraped_via: "browseros"
---

# Email content spoofing at IKEA.com

Email content spoofing at IKEA.com
Jonathan Bouman
Follow
4 min read
·
Apr 6, 2019

273

3

Press enter or click to view image in full size
Proof of concept

Background
Previously we discussed XSS, open redirect bugs and unrestricted file uploads. Today we will focus on email content spoofing.

Phishing someone is way more easy if we are able to send emails from the servers of a well known brand. The email looks legitimate, is digitally signed by the sending domain and due to that it won’t be flagged as spam or phishing. Perfect.

IKEA.com
As mentioned in our previous bug report, IKEA is a nice brand with a proper responsible disclosure statement. So we’re safe to help them find bugs, maybe even in exchange for a reward ;-)!

Finding targets
An important rule is that once you find a bug in a system, most of the time more bugs are nearby.

This is a good example, we previously found an local file inclusion bug in the same application, bathroomplanner.ikea.com. So today we will have a closer look at this application and see if it is also vulnerable to email content spoofing.

Press enter or click to view image in full size
The frontpage
Press enter or click to view image in full size
Email yourself the list, a nice pop-up

Let’s have a closer look at this form. We start Burp Suite and intercept the form submission.

Press enter or click to view image in full size
Form submission intercepted with Burp Suite

As we can see there are multiple interesting fields:
- senderName
- subject
- HTML

Get Jonathan Bouman’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Inside the HTML field there is some code that is encoded. We can easily decode it, first urldecode, after that base64decode.

The HTML content is:
<html> <head></head> <body style=”padding:0; margin:0;”> <table cellpadding=”0" cellspacing=”0" style=”width:100%; background-color:#fff; border:3px solid #007ab9;”> <tr height=”120px”> <td style=”text-align:center;”> <img src=”cid:logo” alt=”Ikea logo”> </td> </tr> <tr> <td align=”center”> <table cellpadding=”0" cellspacing=”0"> <tr height=”20px”></tr> <tr height=”40px”> <td colspan=”2" style=”font-family:Verdana,sans-serif; font-size:16px; color:#333; text-align:center;”> Use this code to recover your project in the store or at home. </td> </tr> <tr height=”20px”></tr> <tr> <td style=”font-family:Verdana,sans-serif; font-size:34px; font-weight:bold; color:#333; padding-top:25px;text-align:center;”> VJ5G3 </td> </tr> <tr height=”20px”></tr> </table> </td> </tr> <tr height=”20px”></tr> </table> </body></html>

Changing the email contents
What if we change it to
- senderName: IKEA Account Recovery
- subject: WARNING: ACCOUNT COMPROMISED, ACTION REQUIRED!
- HTML:

<html> <head></head> <body style=”padding:0; margin:0;”> <table cellpadding=”0" cellspacing=”0" style=”width:100%; background-color:#fff; border:3px solid #007ab9;”> <tr height=”120px”> <td style=”text-align:center;”> <img src=”cid:logo” alt=”Ikea logo”> </td> </tr> <tr> <td align=”center”> <table cellpadding=”0" cellspacing=”0"> <tr height=”20px”></tr> <tr height=”40px”> <td colspan=”2" style=”font-family:Verdana,sans-serif; font-size:16px; color:#333; text-align:center;”> <h1 style=”color:red”>WARNING</h1><p>Someone tried to login into your IKEA account, action required!</p> </td> </tr> <tr height=”20px”></tr> <tr> <td style=”font-family:Verdana,sans-serif; font-size:18px; font-weight:bold; padding-top:25px;text-align:center;”><h2><a href=”https://s3-eu-west-1.amazonaws.com/pentesting-target/ikea.html" style=”color:#333;”>RECOVER ACCOUNT (FAKE PHISHING LOGIN LINK)</a></h2> </td> </tr> <tr height=”20px”></tr> </table> </td> </tr> <tr height=”20px”></tr> </table> </body></html>

Press enter or click to view image in full size
We use the Burp Suite Repeater to resend the form with our payload

Let’s open our email box and see if we’ve got mail.

Press enter or click to view image in full size
Received email from IKEA.com
Press enter or click to view image in full size
Digital signed, passing all the security tests.

Perfect. We just received a digitally signed phishing email from the IKEA.com domain.

Conclusion
IKEA.com did not check the fields being used in one of their email forms. This resulted in the creation of fully signed phishing email, passing all the spam filters.

Solutions
Never allow the user to set the HTML, subject & from contents of an email.
Scan outgoing emails for malicious content, drop the mail if it looks suspicious.

Rewards
€ 50

Timeline
16–06–18 Discovered the bug, report sent by using the Zerocopter submission form.

See the IKEA LFI Report for the timeline for the initial difficulties I had to get in touch. After a while it resolved and I was able to coordinate the disclosure.

09–08–18 Discovered that the bug still exists, informed Zerocopter that it is not resolved, requested Zerocopter to share this post (draft) with IKEA for review, I understand IKEA needs more time, requested direct contact for further coordination of disclosure; email or Zerocopter platform is fine for me.

Press enter or click to view image in full size

13–08–18 Zerocopter: no updates yet, requested status update from IKEA, sent this blog to IKEA for review.
13–08–18 IKEA their CDN/WAF (Akamai) banned my private IP site wide, asked Zerocopter if they could ask IKEA to unban me (if they want me to confirm other bug fixes in the future).
13–10–18 Requested an update from IKEA
15–10–18 IKEA requests to me to retest the bug, a fix is deployed
15–10–18 Created a bypass for the bug fix, informed IKEA about this
23–11–18 Requested an update from IKEA
26–11–18 IKEA informs me a new fix will be released 17–12–18, update will be sent through Zerocopter platform
21–03–19 Zerocopter requests me to test the fix
27–03–19 I confirmed the fix
01–04–19 Asked IKEA if I’m allowed to publish this report
02–04–19 IKEA allowed me to publish the report
06–04–19 Published the report
