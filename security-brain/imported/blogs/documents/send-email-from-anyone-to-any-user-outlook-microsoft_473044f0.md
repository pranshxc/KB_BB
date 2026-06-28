---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-06-04_send-email-from-anyone-to-anyuser-outlook-microsoft.md
original_filename: 2023-06-04_send-email-from-anyone-to-anyuser-outlook-microsoft.md
title: Send email from anyone to any(user outlook Microsoft)
category: documents
detected_topics:
- command-injection
- api-security
tags:
- imported
- documents
- command-injection
- api-security
language: en
raw_sha256: 473044f031a3907d49f3f55588e8f0a6a1191efc28f1a24cc6ac696abe362236
text_sha256: 8af4aaf743c4c953143465949398659aef1ee04360b760c61de4e0f1d8d407b2
ingested_at: '2026-06-28T07:32:21Z'
sensitivity: unknown
redactions_applied: false
---

# Send email from anyone to any(user outlook Microsoft)

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-06-04_send-email-from-anyone-to-anyuser-outlook-microsoft.md
- Source Type: markdown
- Detected Topics: command-injection, api-security
- Ingested At: 2026-06-28T07:32:21Z
- Redactions Applied: False
- Raw SHA256: `473044f031a3907d49f3f55588e8f0a6a1191efc28f1a24cc6ac696abe362236`
- Text SHA256: `8af4aaf743c4c953143465949398659aef1ee04360b760c61de4e0f1d8d407b2`


## Content

---
title: "Send email from anyone to any(user outlook Microsoft)"
url: "https://infosecwriteups.com/send-email-from-anyone-to-any-user-outlook-microsoft-69fce333066d"
authors: ["Abbas Heybati (@abbas_heybati)"]
programs: ["Microsoft"]
bugs: ["Open mail relay", "Email spoofing", "SMTP", "SPF bypass"]
publication_date: "2023-06-04"
added_date: "2023-06-05"
source: "pentester.land/writeups.json"
original_index: 1086
scraped_via: "browseros"
---

# Send email from anyone to any(user outlook Microsoft)

Send email from anyone to any(user outlook Microsoft)
Abbas.heybati
Follow
4 min read
·
Jun 4, 2023

718

5

Hi guys

I was researching SMTP and mail server for some time.
I decided to start researching Microsoft Outlook.
When I went further and deepened my research, I realized that this vulnerability can exist on many mail servers.

That’s why I wrote this write-up so that (Bug hunters and Security researcher and Penetration testing) and even security defence teams will notice it.

I will explain about the bug first
I have noticed a bug in SMTP and Mail server in Microsoft Exchange
That would allow me to send emails(Example: secure@microsoft.com or x@outlook.com) from anyone I want to anyone in user Outlook
That is, any email that was related to Microsoft

The point is that this could only be done from Outlook’s own e-mails, for example, it cannot be done from Gmail to Outlook.

In the picture below, I sent myself an email from secure@microsoft.com

Press enter or click to view image in full size

I reported this vulnerability to Microsoft security experts and they fixed this bug

Press enter or click to view image in full size
Report bug to msrc.microsoft.com

OK
This was a summary of the vulnerability I found
Before I talk about vulnerability, I would like to show you how I got this vulnerability.

Before I started researching, I had no idea how to start, I just knew that I wanted to find a vulnerability on Mail Servers and I just started.

Get Abbas.heybati’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

That’s why I went to read RFC 5321 to understand SMTP architecture well.

Press enter or click to view image in full size

After reading the RFC I went to find out what happens when an email is sent?

Press enter or click to view image in full size

And after this I realized that there are security mechanisms
For example, I researched DKIM and SPF again.
And in the end, with all the research I did, a question came to me, what happens if I connect directly with the Outlook server and try to send email through this server?

Press enter or click to view image in full size
The bug started

For this, I needed to find the main Outlook mail server first, which was not a complicated task

Press enter or click to view image in full size
Mail is handled by outlook-com.olc.protection.outlook.com

After I got the address of the mail server, I started connecting to it with telnet

Press enter or click to view image in full size
Telnet port 25

Well, for this you need to read about smtp commands
which is easily obtained by searching on Google

Press enter or click to view image in full size

As you can see in the photo above, I came, first I connected with the EHLO server and the server answered me.
Then I specified with mail from who I want to send the email from, here I wanted to send the email from secure@microsoft.com and the status 250 was returned to me OK
Then I specified to whom the email(RCPT TO) should be sent, here I put my email, and again the status returned to me was 250 OK.
And then I specified with data that I want to send a data (text).

Press enter or click to view image in full size

Tip “ In order to understand how the server is behaving, be sure to read about the status codes”

After specifying the source of the email and the destination of the email, I added my data to the email
(From/To/Subject)
And I added a text and body the end of the email with a dot
And here my email was successfully forwarded to my email from secure@microsoft.com.

successfully send
History email

And finally, I want to tell you another scenario(Another company) where I bypassed SPF using a technique

Press enter or click to view image in full size

In this scenario, it was very interesting to me that when I was sending the email, it did not allow me to send the email. I defined a Content-Type in the header and put a charset with ISO-8859–1 value for it.
I tested the charset section with different patterns until ISO-8859–1 worked and bypassed.

I hope this writeup has helped you :)

twitter.com/abbas_heybati

www.linkedin.com/in/abbas-heybati-76432220b
