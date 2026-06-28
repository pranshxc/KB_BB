---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-07-16_what-do-netcat-smtp-and-self-xss-have-in-common-stored-xss.md
original_filename: 2019-07-16_what-do-netcat-smtp-and-self-xss-have-in-common-stored-xss.md
title: What do Netcat, SMTP and self XSS have in common? Stored XSS
category: documents
detected_topics:
- xss
- oauth
- command-injection
tags:
- imported
- documents
- xss
- oauth
- command-injection
language: en
raw_sha256: 7dbf7cafefc9cf277f1adf0e41f0538a7b90b696043e3815aa81bb50c97c3fdc
text_sha256: 25b172456a93b36043dbfe16e97812ff66f3326ebeb333074a2ada643cf2eaaf
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# What do Netcat, SMTP and self XSS have in common? Stored XSS

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-07-16_what-do-netcat-smtp-and-self-xss-have-in-common-stored-xss.md
- Source Type: markdown
- Detected Topics: xss, oauth, command-injection
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `7dbf7cafefc9cf277f1adf0e41f0538a7b90b696043e3815aa81bb50c97c3fdc`
- Text SHA256: `25b172456a93b36043dbfe16e97812ff66f3326ebeb333074a2ada643cf2eaaf`


## Content

---
title: "What do Netcat, SMTP and self XSS have in common? Stored XSS"
url: "https://medium.com/bugbountywriteup/what-do-netcat-smtp-and-self-xss-have-in-common-stored-xss-a05648b72002"
authors: ["Plenum (@plenumlab)"]
bugs: ["Stored XSS"]
publication_date: "2019-07-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5145
scraped_via: "browseros"
---

# What do Netcat, SMTP and self XSS have in common? Stored XSS

What do Netcat, SMTP and self XSS have in common? Stored XSS
Plenum
Follow
2 min read
·
Jul 16, 2019

98

1

If you are reading this you are probably wondering what is this? is this some kind of a joke? The answer is No, and it is not a clickbait, this is the story of chaining small issues and pivoting from a self XSS to a fully blown Stored XSS.

Press enter or click to view image in full size
JUST A RANDOM PHOTO

T
he journey began when i started hacking on a private program, and while doing my research i came across a self XSS issue which hey were aware of and it was explicitly out of scope. So i kept digging and started to learn how the app worked, it had CRM and other related stuff which is not really important for now. The app had multiple parts and one of them was client management with regular functionalities like create/delete/modify clients, create/attach invoices… the self xss existed in the information fields of the client’s view.

<a tlclick=”sendEmail(&quot;email_here&quot;)”>email_here</a>

By adding a simple ‘ to the email i was able to break the html and then add my own attributes.

After some more digging i found out that if you send an email to the invoice email address the app would check if the email address of the sender existed in the client’s database and if found it would create a new ticket for that client but what if we send an email from a non client address? A new client is created along side with the new ticket.

Now since i can control parts of client information (email address), i need to be able to send really miss formed emails and the easiest way to do that is to use NETCAT. So i just opened a new terminal queried for their email server and started building the exploit.

Get Plenum’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

First i had to build a working XSS then i had to figure out which characters break the SMTP syntax and encode them, ended up with a an email like this

‘onmouseover=’alert&#40localStorage.oauth&#41'@plenumsec.com

The final attack looked something like this

nc -C mxa.mailgun.org 25 
>HELO plenumsec.com
>MAIL FROM: <'onmouseover='alert&#40localStorage.oauth&#41'@plenumsec.com> 
>RCPT TO: <random@target.com>
>DATA
From: Attacker <'onmouseover='alert&#40localStorage.oauth&#41'@plenumsec.com>
To: Victim  <random@target.com>
Subject: Urgent
Date: Wed, 26 Sep 2018 14:21:26 -0400
Hello,
This is a stored xss poc.
Goodbye.

Now an attacker would just wait for the employee to visit the client management page or perform any action that includes the attacker’s email. The company email was completely guessable and thus could be targeted by just bruteforcing and automating the process.

One would argue that this attack could have been avoided by implementing SPF but sometimes security is not convenient for businesses so they have to make compromises.

Thanks for reading,

Regards, Plenum
