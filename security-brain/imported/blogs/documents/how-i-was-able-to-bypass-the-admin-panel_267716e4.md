---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2023-07-20_how-i-was-able-to-bypass-the-admin-panel_2.md
original_filename: 2023-07-20_how-i-was-able-to-bypass-the-admin-panel_2.md
title: How I was Able To Bypass The Admin Panel
category: documents
detected_topics:
- access-control
- command-injection
- rate-limit
- information-disclosure
- api-security
tags:
- imported
- documents
- access-control
- command-injection
- rate-limit
- information-disclosure
- api-security
language: en
raw_sha256: 267716e4f9e8d95bb251c0c2d8fada0827de82202ea1b88fb676f4d04a75404e
text_sha256: ac45fa063409afe0bf887d05a33d7fb46a250e4a75d456d21cbcceff6a4ad4ad
ingested_at: '2026-06-28T07:32:24Z'
sensitivity: unknown
redactions_applied: true
---

# How I was Able To Bypass The Admin Panel

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2023-07-20_how-i-was-able-to-bypass-the-admin-panel_2.md
- Source Type: markdown
- Detected Topics: access-control, command-injection, rate-limit, information-disclosure, api-security
- Ingested At: 2026-06-28T07:32:24Z
- Redactions Applied: True
- Raw SHA256: `267716e4f9e8d95bb251c0c2d8fada0827de82202ea1b88fb676f4d04a75404e`
- Text SHA256: `ac45fa063409afe0bf887d05a33d7fb46a250e4a75d456d21cbcceff6a4ad4ad`


## Content

---
title: "How I was Able To Bypass The Admin Panel"
url: "https://medium.com/@mohameddiv77/how-i-was-able-to-bypass-the-admin-panel-9a5a81e2ec11"
authors: ["Mohamed Ibrahim (@mOhamedd7w)"]
bugs: ["Information disclosure", "Authentication bypass"]
publication_date: "2023-07-20"
added_date: "2023-08-08"
source: "pentester.land/writeups.json"
original_index: 907
scraped_via: "browseros"
---

# How I was Able To Bypass The Admin Panel

1

How I was Able To Bypass The Admin Panel
Mohamed Ibrahim
Follow
4 min read
·
Jul 21, 2023

1.4K

22

Hello Amazing Hackers… Mohamed Ibrahim is Here

This is my first Article and we will talk about how I was able to bypass the admin panel and login to Admin dashboard on one of the public bug bounty program

Press enter or click to view image in full size

Lets call our program redacted.com for privacy. First I start my recon process with some shodan dorking like: org:”redacted” || ssl:”redacted.com” and play with filters like: http.title || port, till I found an ip that was running on port 8080 and has a basic auth

Press enter or click to view image in full size
Basic Auth

Now lets try to bypass it..

1. Default Credentials

In this situation, first thing I do is check for default credentials like:

admin:admin

admin:password

user:user

but nothing worked here, searched on google for default credentials of the panel name but nothing found.

But when I saw the Authentication failure error on the panel:

Press enter or click to view image in full size
Auth error

I thought that the username and the password is a default credentials comes with the product|application installed here. It something like PIN-CODE or Serial Number or Product Number|Version. Like WiFi device in your home, it comes with default PIN-CODE .

2. Directory Fuzzing

I moved to the next step, and used FFUF for Directory Fuzzing with my custom wordlist that get me some interesting results :

Press enter or click to view image in full size
first fuzzing

I go to http://<ip>:8080/api/v1/roles/ but found nothing then I go to http://<ip>:8080/api/v1/users/ and found the only username of the panel!

Press enter or click to view image in full size
users path

Now we have the username, lets see what we can do with it

3. Brute Forcing .

I fired up my burp to capture the login request for brute forcing attack. I entered username:admin & password=***REDACTED*** and capture the request:

Press enter or click to view image in full size
login request

the request has an Authorization header with the credentials . I can see the value of the username(admin) but can not see the password value(12345678) that I entered . Seems the application make some kind of Encryption(I don’t know). so I can’t do brute force attack.

Get Mohamed Ibrahim’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Back to the Directory Fuzzing again to get some more result . this time I start fuzzing under /api/v1/ directory and get some new result :

Press enter or click to view image in full size
second Fuzzing

OK, Lets go to http://<ip>:8080/api/v1/devices/ ..

I open the above url and again found nothing. but wait, I found another directory: /api/v1/devices/snapshot ..

Press enter or click to view image in full size
devices path

I go to http://<ip>:8080/api/1/devices/1/snapshot and it was a downloaded file(compressed). I open it and take a round in it.

Press enter or click to view image in full size
compressed file

I opened every file searching for something useful till I found this file /tmp/hw_info.txt . From it’s name ,it seems it has some information about the product|Application:

Press enter or click to view image in full size
hw_info.txt

The file has Serial Number & Product Number of the product|Application.

I though that why not use those numbers as a password for the username(admin)..?? Lets give a try… Back to login with:

user:admin &pass:<Product number> -> Username||password is wrong

user:admin & pass:<Serial number> -> ( BooOooM )Login Successful ..

Press enter or click to view image in full size
Login Successful

I Immediately write a good report mentioned the above steps and sen it to the program on hackerone.

Fortunately, I didn’t get Duplicated …And my report Triaged as a Resolved(CRITICAL).

Resolved (critical)

Thank you Amazing Hackers for reading my writeup.

For any FAQ or any FeedBack, I’m here:

Twitter

LinkedIn
