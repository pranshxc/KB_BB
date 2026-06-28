---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-07-17_i-am-able-to-see-users-sensitive-data-through-json-file.md
original_filename: 2020-07-17_i-am-able-to-see-users-sensitive-data-through-json-file.md
title: I am able to see user’s sensitive data through JSON file.
category: documents
detected_topics:
- access-control
- command-injection
- information-disclosure
tags:
- imported
- documents
- access-control
- command-injection
- information-disclosure
language: en
raw_sha256: 9dc5c53e2c29a44b9924c38c00527f6b0472ce574bb9cfe6a0d828b344fed5ca
text_sha256: 9d212d5364412965e830fda73fa95f5319ae5482e7536936c9d6c710cfc5bb13
ingested_at: '2026-06-28T07:32:02Z'
sensitivity: unknown
redactions_applied: false
---

# I am able to see user’s sensitive data through JSON file.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-07-17_i-am-able-to-see-users-sensitive-data-through-json-file.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, information-disclosure
- Ingested At: 2026-06-28T07:32:02Z
- Redactions Applied: False
- Raw SHA256: `9dc5c53e2c29a44b9924c38c00527f6b0472ce574bb9cfe6a0d828b344fed5ca`
- Text SHA256: `9d212d5364412965e830fda73fa95f5319ae5482e7536936c9d6c710cfc5bb13`


## Content

---
title: "I am able to see user’s sensitive data through JSON file."
url: "https://medium.com/@saurabhsanmane06/i-am-able-to-see-users-sensitive-data-from-json-file-905e330278df"
authors: ["Saurabh siddharam sanmane (@saurabhsanmane2)"]
bugs: ["Information disclosure", "Broken authorization"]
bounty: "150"
publication_date: "2020-07-17"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4406
scraped_via: "browseros"
---

# I am able to see user’s sensitive data through JSON file.

I am able to see user’s sensitive data through JSON file.
Saurabh sanmane
Follow
3 min read
·
Jul 17, 2020

212

Hey guys its my first simple writeup, So then just ignore grammer mistake’s and enjoy it.
In the current marketplace multiple web-application’s or website’s are using the JSON file format to exchange the data.

What is JSON file ?

A JSON file is a file that stores simple data structures and objects in
JavaScript Object Notation (JSON) format, which is a standard data interchange format.
It is primarily used for transmitting data between a web application and a server.

The Vulnerability :

Sometimes what happen’s that JSON file format is used to retrive data(using GET Method) from server for authentication purpose & many more reasons.
I am going to explain this vulnerability by 2 Scenario’s.

1st scenario:
So i just trying to find vulnerabilities in target.com and tried almost all
ways to exploit any vulnerability . But i failed then i just started to see its all files and pages.
Then i saw that , in this target.com their is option to create or invite users
with username & password. I just created one .

Description:
When we add or configure User in the domain it stores that information on server by using json file and when i inspect particular file that time i saw that json file leakaging information related added user.

I think it is showing information because i logged in but when
i logout still it is showing information with the password.There is no problem
if the password is visible in parameters but it is visible in response so that’s the issue.

Steps to reproduce :
Instead of Burpsuite i used mozilla’s inspector to verify vulnerability.

1: Open the website inspector.
2: Then add the user and then saw the json file whish have ID as a name.
3: Check the information like cookies , parameter & response.
4: In response there is data leakage (password , username,id) .

Get Saurabh sanmane’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

see the image , in this image their is GET method which used by JSON file to retrive data.

Press enter or click to view image in full size
see sensitive data

I reported bug to program on bugcrowd.
They change it to p3 -> p4
And I got reward .

Press enter or click to view image in full size

2nd Scenario:
In 2nd Scenario ,their is target.com. When i go to account details page that’s time
lots of data leakaging realted to user like username, password in encrypted form, address & contact details.
Follow same steps on profile page and you got details like this.

details realted user
password

So it was a cool bug and it’s super easy.

Suggestions are most welcome as always.
I will keep posting my findings. If you got anything from it,
you can press the clap icon below and ya, don’t forget to follow me on linkedin & twitter as well.
See you all next time. :)

Bugcrowd : click here

Twitter: click here

Linkedin: click here

Cheers!
