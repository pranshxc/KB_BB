---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-02-08_how-i-gain-access-to-the-server-administration-of-a-million-dollar-company.md
original_filename: 2021-02-08_how-i-gain-access-to-the-server-administration-of-a-million-dollar-company.md
title: How I Gain Access to the Server Administration of a Million-Dollar Company
category: documents
detected_topics:
- idor
- api-security
- access-control
- command-injection
- mfa
- otp
tags:
- imported
- documents
- idor
- api-security
- access-control
- command-injection
- mfa
- otp
language: en
raw_sha256: 2b78d17d3dd53d2b55779257faff0f4a18d678e0f80a5b433db6aa8e0078cd19
text_sha256: 5ace8e8134a0143c2eabb479d748648bfcf27622c7e1e52be9885928b10a3d07
ingested_at: '2026-06-28T07:32:04Z'
sensitivity: unknown
redactions_applied: false
---

# How I Gain Access to the Server Administration of a Million-Dollar Company

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-02-08_how-i-gain-access-to-the-server-administration-of-a-million-dollar-company.md
- Source Type: markdown
- Detected Topics: idor, api-security, access-control, command-injection, mfa, otp
- Ingested At: 2026-06-28T07:32:04Z
- Redactions Applied: False
- Raw SHA256: `2b78d17d3dd53d2b55779257faff0f4a18d678e0f80a5b433db6aa8e0078cd19`
- Text SHA256: `5ace8e8134a0143c2eabb479d748648bfcf27622c7e1e52be9885928b10a3d07`


## Content

---
title: "How I Gain Access to the Server Administration of a Million-Dollar Company"
url: "https://marxchryz.medium.com/how-i-gain-access-to-the-server-administration-of-a-million-dollar-company-14da68c7a9dd"
authors: ["Marx Chryz Del Mundo"]
bugs: ["Privilege escalation", "Mass assignment"]
bounty: "5,000"
publication_date: "2021-02-08"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3931
scraped_via: "browseros"
---

# How I Gain Access to the Server Administration of a Million-Dollar Company

How I Gain Access to the Server Administration of a Million-Dollar Company
Marx Chryz Del Mundo
Follow
5 min read
·
Feb 6, 2021

163

1

Hello everyone, I am Marx Chryz and I am new to bug bounty hunting even though I do web penetration testing for more than a year.

Background

Wayback November 2020, I started playing around on some labs like OWASP Juice Shop and WebGoat. I chose this 2 labs since I have already tried the DVWA (Damn Vulnerable Web Application) back in late 2019.

Press enter or click to view image in full size
OWASP Juice Shop

Under the “Improper Input Validation” in OWASP Juice Shop, there is a task with the description of “Register as a user with administrator privileges.”

So how that works is during registration, you need to guess and pass a parameter with the name of “role” and a value of “admin” to complete the task. Upon completing this task, I thought “Can I really apply this in real world scenario?”

I always think that the answer that question is “no”. But not until January this year. Where I managed to do that method (with some bypasses) in order to gain access on a server administration of a million-dollar company.

Introduction

The site I am hunting on is a private program so I won’t disclose any info or screenshot of it so I want to apologize for that.

The program has a subdomain that requires signup/login so I created an account immediately. During account registration, everything is normal. For simplicity and demonstration purposes, lets say that this is the request:

POST /register HTTP/1.1
Host: www.redacted.com
Content-Type: application/json

{“email”: “user@tld.xyz”, “password”: “password123”}

The request above then returns a 302 redirect to the homepage. I guess there’s nothing suspicious on that so I proceed on exploring the site.

Upon exploring the site, I checked the “My Account” functionality, hoping for some CSRF and IDOR vulnerabilities in there. But there is none, there are CSRF tokens that are bonded to the userID so IDORs and CSRFs cannot be exploited.

After some time, I got bored so I rest and after that, I reviewed my HTTP logs on Burp Suite. Then I saw the request for updating my account on the said program.

The request looks something like:

POST /updateUserInfo HTTP/1.1
Host: www.redacted.com
CSRF-Token: XXXXXXXXXXXXXXXXXXXXXXX
Content-Type: application/json

{
“User”: {“id”: “123”, “email”: “user@tld.xyz”, “fullName”: “User A”},
“Address”: {“city”: “Some City”}
}

and the response returned a very long content, this is a part of it:

HTTP/1.1 200 OK

{
“response”: “success”,
“info”: {
“id”: “123”,
“email”: “user@tld.xyz”,
“fullName”: “User A”,
…
}
}

There are a lot of fields shown in the response that are not on my request, what caught my eyes is there is a field with the name “companyUser” and a value of “0”. Hmm, that’s looks pretty interesting… Can I changed that value too? But how and where should I place it.

Get Marx Chryz Del Mundo’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So I tried modifying the request above and changing it to:

POST /updateUserInfo HTTP/1.1
Host: www.redacted.com
CSRF-Token: XXXXXXXXXXXXXXXXXXXXXXX
Content-Type: application/json

{
“User”: {“id”: “123”, “email”: “user@tld.xyz”, “fullName”: “User A”, “companyUser”: “1”},
“Address”: {“city”: “Some City”}
}

But nothing happened. I thought that the “companyUser” must not be inside the “User” field so I tried guessing what should it be. After thinking, I thought of using {“companyUser”: { “companyUser”: “1” }} but still, nothing happened.

So I tried to follow their naming convention (first letter capitalized). So I changed it to {“CompanyUser”: { “companyUser”: “1” }}

Then boom! I saw the request returned the “companyUser” with the value of “1”. I was so excited! I logged out and logged in to check it ASAP but it did not worked. I was prompted by a 2FA pin code :(

I can’t bruteforce this 2FA since I don’t know its length and combination. It can be alphanumeric with symbols, so it’s a no for me.

I repeated the steps above on my other account, then I reviewed the response again. I noticed something related to 2FA, it is the field “companyUser2FA”

I immediately added this field to my request, so my final request is {“CompanyUser”: { “companyUser”: “1”, “companyUser2FA”: “1234” }}

The 2FA field is shown on the response, which means it worked. So I logged out and logged in again but…

Press enter or click to view image in full size

I was prompted that my IP is not on whitelisted. I tried again repeating the steps above on my third account and I also reviewed the response. I noticed that there is something related to IP and it is a field named “companyUserIP”.

I added this parameter to my request hoping that it will bypass the IP restriction. The final request is now:
{“CompanyUser”: { “companyUser”: “1”, “companyUser2FA”: “1234”, “companyUserIP”: “<My Public IP>” }}

I logged out and logged in again. Then…

Press enter or click to view image in full size

Finally! I am now redirected on a route inside the website that only admins have access. I saw everything only admins can see. To my surprise, it is not only on that subdomain that I gain admin access. But also including all their admin panels on other subdomains. In that, I saw also a lot of subdomains that never came up during my subdomain enumeration.

I explored the site but I did not test further because I don’t know if I have the program’s permission to test on that (Always remember to ask and clarify because you might violate the program’s rules)

I quickly made a report and I sent it to them. After few hours, the vulnerability is already fixed. And after few days, my report was triaged as P1 and the bounty amount for it. It’s my highest paid bug!! I’m really happy for it.

Report Timeline

Jan 22, 2021 — Bug Submitted
Jan 23, 2021 — Bug Fixed
Feb 6, 2021 — Triaged as P1 and eligible for $5000 bounty
