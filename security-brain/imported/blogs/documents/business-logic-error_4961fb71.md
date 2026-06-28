---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2022-07-16_business-logic-error.md
original_filename: 2022-07-16_business-logic-error.md
title: Business logic error
category: documents
detected_topics:
- business-logic
- idor
- xss
- command-injection
- cloud-security
tags:
- imported
- documents
- business-logic
- idor
- xss
- command-injection
- cloud-security
language: en
raw_sha256: 4961fb7115efc2c56ce4d0b2184e7035965670e4c19e225044d181ed191b10c2
text_sha256: cbd299ef5429da7b46e60d28a1fc7468b79570b3ba42ec985f81867d955c3c4f
ingested_at: '2026-06-28T07:32:12Z'
sensitivity: unknown
redactions_applied: false
---

# Business logic error

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2022-07-16_business-logic-error.md
- Source Type: markdown
- Detected Topics: business-logic, idor, xss, command-injection, cloud-security
- Ingested At: 2026-06-28T07:32:12Z
- Redactions Applied: False
- Raw SHA256: `4961fb7115efc2c56ce4d0b2184e7035965670e4c19e225044d181ed191b10c2`
- Text SHA256: `cbd299ef5429da7b46e60d28a1fc7468b79570b3ba42ec985f81867d955c3c4f`


## Content

---
title: "Business logic error"
url: "https://medium.com/@anjaneyulukanakatla1996/business-logic-error-6922ba75cad8"
authors: ["anjaneyulu kanakatla"]
bugs: ["Logic flaw"]
publication_date: "2022-07-16"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 2443
scraped_via: "browseros"
---

# Business logic error

Business logic error
anjaneyulu kanakatla
Follow
1 min read
·
Jul 16, 2022

53

3

I Can Delete your email, you can’t register on the website

Hello My Dear Buggies!!!

Happy to write my fourth article in medium. kindly excuse me if any Grammarly mistakes in this article,still iam learner

I Hope your good,lets begin our show

I Got private program in hackerone, so i deside to test that website full scope, searching in github any shodan nothing find , lets move into the website I have tested broken access issues but saidly nothing found. tested idor and xss and many more but nothing found

lastly I decide one conclusion to leave so I decided to delete my account aaa@gmail.com , deleted my account.something happen in mind again register with same email , but the web application throughs an error you can’t register in this website, so I got an the Idea. the application is not verfiying your mail id in signup

Steps to reproduce

Get anjaneyulu kanakatla’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

1-signup with any email aaa@gmail.com (application sends verfication don’t verfiy the mail)

2-login into the application

3-go to settings →click on delete

4-deleted your account → Try to login with same email aaa@gmaail.com (it shows an error)

5-you can’t register aaa@gmail.com (because the server is storing the data )

Impact…

An attacker can disable any sets of emails (for example company emails)and they can’t be used in any future work

Thanks for reading

catch you in next writeup.bye bye

HAPPY HUNTING BUGGIES
