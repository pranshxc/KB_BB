---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2021-08-29_information-disclosure-via-api-misconfiguration.md
original_filename: 2021-08-29_information-disclosure-via-api-misconfiguration.md
title: Information disclosure via api misconfiguration
category: documents
detected_topics:
- jwt
- xss
- command-injection
- file-upload
- otp
- information-disclosure
tags:
- imported
- documents
- jwt
- xss
- command-injection
- file-upload
- otp
- information-disclosure
language: en
raw_sha256: f511ca93c0063a11dc657d1731d80c995e02027415184447005abe1c545edb93
text_sha256: f970e00548e699d773d8ebc67cbbbef4359bbc28570f1113a245c7b033d5612d
ingested_at: '2026-06-28T07:32:07Z'
sensitivity: unknown
redactions_applied: false
---

# Information disclosure via api misconfiguration

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2021-08-29_information-disclosure-via-api-misconfiguration.md
- Source Type: markdown
- Detected Topics: jwt, xss, command-injection, file-upload, otp, information-disclosure
- Ingested At: 2026-06-28T07:32:07Z
- Redactions Applied: False
- Raw SHA256: `f511ca93c0063a11dc657d1731d80c995e02027415184447005abe1c545edb93`
- Text SHA256: `f970e00548e699d773d8ebc67cbbbef4359bbc28570f1113a245c7b033d5612d`


## Content

---
title: "Information disclosure via api misconfiguration"
url: "https://rizwansiddiqu1.medium.com/information-disclosure-via-api-misconfiguration-c05ed327f9d2"
authors: ["Rizwan_siddiqui (@Rizwan_SiDdiqu1)"]
bugs: ["Information disclosure"]
publication_date: "2021-08-29"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 3376
scraped_via: "browseros"
---

# Information disclosure via api misconfiguration

Top highlight

Information disclosure via api misconfiguration
rizwansiddiqu1
Follow
2 min read
·
Aug 28, 2021

252

3

As-Salaam-Alaikum (Peace be unto you)

Get rizwansiddiqu1’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Hello, Amazing hackers My name is Rizwan Siddiqui I am a Bug Hunter. This is my First Write-up hope You guys will enjoy it and learn something new from it. Let’s get started on how I found this API misconfiguration.

Let’s Goooooooooooooooo

scenario: The web application is some car or bus selling web application and there are also jobs related stuff there. I try file upload XSS but nothing works then I Go To id.target.com there is some profile type function where I can upload my file and there is my login log my IP address who login in to my account through which IP. I try some XSS again file upload vulnerability but nothing works

After that i thought i should give up and change my target but in id.target.com there is api endpoint that is fetching my personal details like my ip address and name stuff. That time i thought i should fuzz here i try fuzzing after that i notice that this is authenticated endpoint i should fuzz with my cookie so i can find something juice info and i start fuzz like this ffuf -u https://id.target.com/api/FUZZ -w wordlist -c COOKIE_HERE after some time it give me https://id.target.com/api/work and guess what there is some misconfiguration in api endpoint which is leaking company employee data like there position in company jobs Descriptions profile pic that time i thought this is just some basic or someone person info but i am wrong when i send it to repeater tab and i send that request, again and again, they give me new employee data every time.

Step To reproduce:

Go to id.target.com login with your credential.
open burp suite forward requests until u see the request like this :
GET /api/personal HTTP 1.1
HOST: id.target.com
Cookie : JWT TOKEN
Accept: application/json

3. Just remove “personal” and add “work” then see the magic.

Takeaway:

Always Fuzz with your cookies if there is an API endpoint. And never lose hope.
