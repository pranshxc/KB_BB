---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-03-14_privilege-escalation-on-private-program.md
original_filename: 2019-03-14_privilege-escalation-on-private-program.md
title: Privilege escalation on private program.
category: documents
detected_topics:
- access-control
- command-injection
- otp
- information-disclosure
tags:
- imported
- documents
- access-control
- command-injection
- otp
- information-disclosure
language: en
raw_sha256: a0d7932660a7052605767eea86520a1968d04cd99958e882807fdc7669b1fd10
text_sha256: 59e62e322d6ef462be8c74f45e0e21bd0d635c3e7823c631624721e436a1c00d
ingested_at: '2026-06-28T07:31:59Z'
sensitivity: unknown
redactions_applied: false
---

# Privilege escalation on private program.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-03-14_privilege-escalation-on-private-program.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, otp, information-disclosure
- Ingested At: 2026-06-28T07:31:59Z
- Redactions Applied: False
- Raw SHA256: `a0d7932660a7052605767eea86520a1968d04cd99958e882807fdc7669b1fd10`
- Text SHA256: `59e62e322d6ef462be8c74f45e0e21bd0d635c3e7823c631624721e436a1c00d`


## Content

---
title: "Privilege escalation on private program."
url: "https://medium.com/@imranparray/privilege-escalation-on-private-program-a2a5548cde09"
authors: ["Imran Parray (@imranparray101)"]
bugs: ["Privilege escalation", "Information disclosure"]
publication_date: "2019-03-14"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5358
scraped_via: "browseros"
---

# Privilege escalation on private program.

Privilege escalation on private program.
Imran Parray
Follow
3 min read
·
Mar 15, 2019

204

2

Press enter or click to view image in full size

Hey Guys,

Hope everyone is doing fine, So today i am going to share another Privilege escalation issue which i came across few days before while hunting on one of the private programs on bugcrowd.

Non technical details about issue

The issue was simple, I was able to get access to one of the functionalities in the appilication which was meant to be for admin only. So i was able to perform several actions on admins behalf. So yeah... it was a kinda of Privilege escalation issue.

Technical details about issue

The website was using different “User Roles” like “users,Admins,Mangers” etc in the Application. One of the functionalities in the application was to add new “Subscribers” to our the (account) which was limited to to admin only.

And the endpoint to do that looks like
http://website.com/add/subscribers?token=a3sd123as1d1as31sa21d

This endpoint was only visible to “admin” based role in the application. So my goal was to add new subscribers to my account without having admin “Privileges”

My approach

So i knew that admin can add new subscribers to our account using this endpoint. So simply browsing this endpoint [ http://website.com/add/subscriber ] from “Non-Admin” role gave a an blank html page.

Press enter or click to view image in full size
http://website.com/add/subscribers

this means that the website was validating the token at the end of the url. So i need to get access to token anyhow to add new subscribers to the account.

Get Imran Parray’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

So i cleaned my previous burp traffic and started browsing the application from the “non-admin” account. After few minutes i tried to copy the token from admin account and searched in burp traffic.

I was amazed to see that this token was getting leaked to non-admin users into the JavaScript tag.

Press enter or click to view image in full size

So i copied the token and added it to the URL and my final URL will looked like:

http://website.com/add/subscribers?token=a3sd123as1d1as31sa21d

on browsing the url i was able to add new subscribers to the account without having the “admin privilages ”

Press enter or click to view image in full size

So after checking the issue once again. I immediately submitted the vulnerability to the company.

So that’s it for now. All the best and Good bye.

Sharing is caring.
