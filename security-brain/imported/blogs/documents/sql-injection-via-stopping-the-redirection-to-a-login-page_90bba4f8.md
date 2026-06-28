---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-03-03_sql-injection-via-stopping-the-redirection-to-a-login-page.md
original_filename: 2020-03-03_sql-injection-via-stopping-the-redirection-to-a-login-page.md
title: SQL Injection Via Stopping the redirection to a login page
category: documents
detected_topics:
- access-control
- sqli
- command-injection
- api-security
tags:
- imported
- documents
- access-control
- sqli
- command-injection
- api-security
language: en
raw_sha256: 90bba4f8d4c6184e0b4d40d0c021657b54032b99efd2e4a71c844b9694c265a2
text_sha256: 6653ccff8a6c3c94093ee8666fea0c1e4901805062e1dd37bd4d49406f921544
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# SQL Injection Via Stopping the redirection to a login page

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-03-03_sql-injection-via-stopping-the-redirection-to-a-login-page.md
- Source Type: markdown
- Detected Topics: access-control, sqli, command-injection, api-security
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `90bba4f8d4c6184e0b4d40d0c021657b54032b99efd2e4a71c844b9694c265a2`
- Text SHA256: `6653ccff8a6c3c94093ee8666fea0c1e4901805062e1dd37bd4d49406f921544`


## Content

---
title: "SQL Injection Via Stopping the redirection to a login page"
page_title: "SQL Injection Via Stopping redirection to a login page | by Abde Ouabala | Medium"
url: "https://medium.com/@St00rm/sql-injection-via-stopping-the-redirection-to-a-login-page-52b0792d5592"
authors: ["Abde Ouabala (@4mgh0z)"]
bugs: ["SQL injection", "Broken authorization"]
publication_date: "2020-03-03"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4740
scraped_via: "browseros"
---

# SQL Injection Via Stopping the redirection to a login page

Abde Ouabala
 highlighted

Abde Ouabala
 highlighted

SQL Injection Via Stopping redirection to a login page
Abde Ouabala
Follow
2 min read
·
Mar 3, 2020

468

3

Hi everyone,

in this simple small write up, I’ll describe how I was able to exploit a SQL injection vulnerability Via stopping redirection to a login Amin page!

Actualy while testing on a subdomains , related to razer company called “ rsa3072.razersynapse.com“

going to access /admin page → page 200 → redirects again to the login page , Decided to stop the redirection using an known extention named “Noredirect” , and here is what i got exactly ( See the image down )!

Press enter or click to view image in full size

Actulay this is a bypass for the /admin part ! we got many sensitive data like game Keys , Emails , users creds ,..

After that i decided to search for more links , maybe there will be something interesting !

Access’d a game link , looks like →/source-data/view?source_data_id=[id]

Get Abde Ouabala’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

tried to inject (‘) after the id , got a 500 inernal server error !

Tried a sql injection command to see if the response with return to 200!, the first thing i tried is order by 1- -, and yes i was right! the page returned 200 ok.

So i decided to use sqlmap for auto detecting the type of injection and for easy injecting !

Here is a small picture to show the final injection with sqlmap , Never forget to stopp the redirection while injecting with sqlmap tool ! cuz it will automatiquuely redirects you to login page ! so no injection can be performed there!

Press enter or click to view image in full size

For manual injection , i’ll shot over other write ups Nshallah !

So That’s all !
Thank you for reading!

Regards,

St00rm

📝 Save this story in Journal.

👩‍💻 Wake up every Sunday morning to the week’s most noteworthy stories in Tech waiting in your inbox. Read the Noteworthy in Tech newsletter.
