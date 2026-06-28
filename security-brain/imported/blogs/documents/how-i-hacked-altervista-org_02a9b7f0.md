---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-01-05_how-i-hacked-altervistaorg.md
original_filename: 2019-01-05_how-i-hacked-altervistaorg.md
title: How I hacked Altervista.org
category: documents
detected_topics:
- oauth
- access-control
- command-injection
- otp
- mobile-security
tags:
- imported
- documents
- oauth
- access-control
- command-injection
- otp
- mobile-security
language: en
raw_sha256: 02a9b7f0fea12c9a2aa2c0f043d12e7d3f654bdc6638117c40f2a9cf62159d58
text_sha256: e7ad8856252619ec36e9d202f588bdf5b8b1ea6b4f7d11ad3092ab2e2117e0df
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# How I hacked Altervista.org

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-01-05_how-i-hacked-altervistaorg.md
- Source Type: markdown
- Detected Topics: oauth, access-control, command-injection, otp, mobile-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `02a9b7f0fea12c9a2aa2c0f043d12e7d3f654bdc6638117c40f2a9cf62159d58`
- Text SHA256: `e7ad8856252619ec36e9d202f588bdf5b8b1ea6b4f7d11ad3092ab2e2117e0df`


## Content

---
title: "How I hacked Altervista.org"
url: "https://medium.com/@jacopotediosi/how-i-hacked-altervista-org-f23d011cdb96"
authors: ["Jacopo Tediosi (@jacopotediosi)"]
programs: ["Altervista"]
bugs: ["Open redirect"]
publication_date: "2019-01-05"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5486
scraped_via: "browseros"
---

# How I hacked Altervista.org

How I hacked Altervista.org
(and I found a vulnerability that allowed to steal access tokens)
Jacopo Tediosi
Follow
3 min read
·
Jan 5, 2019

84

1

By @jacopoMii — https://linktr.ee/jacopotediosi

Disclaimer

This was the first bug bounty I attended, and this is my first writeup in English here on Medium.
I’m just a young Italian student with a solid wish to learn new IT-Security stuff and a strong belief in ethical hacking.

About Altervista.org

From Wikipedia:

AlterVista is an Italian web platform where you can open a website for free.
On AlterVista, you can create a website with PHP, MySQL database, and FTP access.
Use of the space is free, but some additional services are subject to charges.
Altervista was bought by Mondadori spa in 2016, and today it hosts about 3 million sites.

Altervista allows you to manage your website via a comfortable web panel after logging in.

It also has a forum where people can ask programming questions and participate in community life:

Press enter or click to view image in full size
The Altervista Forum
How the Altervista login system works

I wandered on Altervista for a while until I noticed that if you had already logged in to the administration panel of your site, to log in on the forum, you just have to click on the “Login” button without having to retype your credentials; so I started studying how that button works:

It was a simple link to https://aa.altervista.org/?client_id=altervista&response_type=code&redirect_uri=http://forum.it.altervista.org/

Get Jacopo Tediosi’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

If a user has already authenticated, that page does nothing more than generate an “authorization_code” and then redirect them to http://forum.it.altervista.org/login.php?do=login-aHR0cDovL2ZvcnVtLml0LmFsdGVydmlzdGEub3JnL2ZvcnVtLnBocA%3D%3D&authorization_code=XXXXXXXXXXXXXXXXXXX
The strange parameter “do” contains the word “login” and then the link “http://forum.it.altervista.org/forum.php" coded in base64 (I know, that’s an odd choice).
Parameter “authorization_code” contains the “authorization_code” generated before.
If the user hasn’t authenticated yet, it first asks for username and password and then redirects the same way.

How I came to discover the vulnerability

Suppose we can change the value of the “redirect_uri” get-parameter.
In that case, we can create a particular link that, when clicked, redirects the user to our servers instead of the Altervista server, allowing us to steal the authorization_code added at the end of the URL (and then login with that).

Unfortunately, there seemed to be a filter on the parameter, which accepted only subdomains of it.altervista.org.

At this point, I remembered the following video of LiveOverflow:

Video: “HOW FRCKN’ HARD IS IT TO UNDERSTAND A URL?!”

It shows that programmers often make mistakes when they have to parse URLs, especially when the input is not compliant with specifications.

So, I started fuzzing until I found a way to bypass the filter:
https://aa.altervista.org/?client_id=altervista&response_type=code&redirect_uri=http://google.it/http://it.altervista.org/

It redirects as follows:

Press enter or click to view image in full size
We can steal access token

So, if we put our malicious server address there instead of google.it, we can steal the access token and then log in with it: http://forum.it.altervista.org/login.php?do=login-aHR0cDovL2ZvcnVtLml0LmFsdGVydmlzdGEub3JnL2ZvcnVtLnBocA%3D%3D&authorization_code=XXXXXXXXXXXXXXXXXXX

Press enter or click to view image in full size
Logging in with another person’s account
Epilogue

I immediately reported my discovery to Altervista via the appropriate form, and they fixed it almost instantly.
As a reward, they added my name to their thanks list:

Press enter or click to view image in full size
Thanks list screenshot
Timeline

- 02 January 2018: Started looking for vulnerabilities on Altervista.org
- 03 January 2018: Discovered the vulnerability and sent a PoC to their Security Team
- 04 January 2018: Patch went online and my name was added to thanks list
