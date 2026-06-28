---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-26_account-takeover-smoking-with-null.md
original_filename: 2021-02-26_account-takeover-smoking-with-null.md
title: Account Takeover - Smoking with ‘null’
category: documents
detected_topics:
- otp
- command-injection
- mfa
- csrf
- api-security
tags:
- imported
- documents
- otp
- command-injection
- mfa
- csrf
- api-security
language: en
raw_sha256: 346fa2e4daae6eec826131b345ff6ce7f5fd0487eecbd1d5b1ba9d5d3ee351f2
text_sha256: d4b92b076d4c56600ff730ac5c12354984dacdfdfb50274cb50ea2c7cd29e702
ingested_at: '2026-06-28T07:32:05Z'
sensitivity: unknown
redactions_applied: false
---

# Account Takeover - Smoking with ‘null’

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-26_account-takeover-smoking-with-null.md
- Source Type: markdown
- Detected Topics: otp, command-injection, mfa, csrf, api-security
- Ingested At: 2026-06-28T07:32:05Z
- Redactions Applied: False
- Raw SHA256: `346fa2e4daae6eec826131b345ff6ce7f5fd0487eecbd1d5b1ba9d5d3ee351f2`
- Text SHA256: `d4b92b076d4c56600ff730ac5c12354984dacdfdfb50274cb50ea2c7cd29e702`


## Content

---
title: "Account Takeover - Smoking with ‘null’"
url: "https://shahjerry33.medium.com/account-takeover-smoking-with-null-e43df2c3bb41"
authors: ["Jerry Shah (@Jerry)"]
bugs: ["Account takeover", "Broken authentication"]
publication_date: "2021-02-26"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3866
scraped_via: "browseros"
---

# Account Takeover - Smoking with ‘null’

Account Takeover - Smoking with ‘null’
Jerry Shah (Jerry)
Follow
3 min read
·
Feb 25, 2021

604

2

Press enter or click to view image in full size

Hello everyone I want to share one of my recent findings for which I was paid $50 because it was the highest amount they were offering. I found an interesting account takeover using JSON null value.

Summary :

Few days back I was hunting on a program where there was a normal option of signup but while logging into the application I was having two different options :

Login with Password
Login with Token

So I chose “Login with Token” and as a normal behaviour a token was sent to my email. At first I tried parameter pollution but it failed, so after reading some of the JSON data types I came to know about a null value in JSON data types.

What is null value in JSON data types ?

Press enter or click to view image in full size
https://www.ibm.com/support/knowledgecenter/SS8JB4_19.x/com.ibm.wbpm.wid.integ.doc/topics/rjsonnullunsempprops.html

So I capture the login request where a token needs to be entered for a successful login and sent it to burp repeater. Then I simply changed the value of the token parameter to null and got a successful login.

I thought of taking over an account of support@comany.com so I went further and tried to signup using the support email at first but as usual the account was already created, so I went to login function > chose the option of token > captured the request using burp > sent it to repeater > entered the value null in token parameter and got a successful login.

Get Jerry Shah (Jerry)’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

How I found this vulnerability ?

I went to a signup page and registered my self
Signup Page
Press enter or click to view image in full size
Signup Request

2. Then I captured the request of the login page where you need a token and changed the value of token parameter to null eg. {“token”:null}

Press enter or click to view image in full size
Login Request

Here you can see I got a successful login.

3. Now I checked for the support@company.com email but it was already registered so I chose the “Login with Token” option and took over the company’s support account.

Press enter or click to view image in full size
Account Takeover

→ Points to Remember

You can try injection null value where a csrf token is passed to bypass it
You can try injection null value where an OTP is required for login
You can try injection null value where 2FA is required
Press enter or click to view image in full size
