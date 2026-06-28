---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2020-04-18_how-was-i-able-to-find-privilege-escalation.md
original_filename: 2020-04-18_how-was-i-able-to-find-privilege-escalation.md
title: How was i able to find privilege escalation.
category: documents
detected_topics:
- access-control
- jwt
- idor
- command-injection
- otp
tags:
- imported
- documents
- access-control
- jwt
- idor
- command-injection
- otp
language: en
raw_sha256: 205eae77c9d11f8aee5d8a630630e3839ce0ede814cd4bb92a088b67c9765474
text_sha256: 17b84ecfdc0293e05aac5eae5308b7ea0fdcb48346312cfa7a90c11f974fd543
ingested_at: '2026-06-28T07:32:01Z'
sensitivity: unknown
redactions_applied: false
---

# How was i able to find privilege escalation.

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2020-04-18_how-was-i-able-to-find-privilege-escalation.md
- Source Type: markdown
- Detected Topics: access-control, jwt, idor, command-injection, otp
- Ingested At: 2026-06-28T07:32:01Z
- Redactions Applied: False
- Raw SHA256: `205eae77c9d11f8aee5d8a630630e3839ce0ede814cd4bb92a088b67c9765474`
- Text SHA256: `17b84ecfdc0293e05aac5eae5308b7ea0fdcb48346312cfa7a90c11f974fd543`


## Content

---
title: "How was i able to find privilege escalation."
url: "https://medium.com/@np20121996/how-was-i-able-to-find-privilege-escalation-b13366b97706"
authors: ["Akshar Tank (@Akshar__tank)"]
bugs: ["IDOR", "Broken authorization"]
publication_date: "2020-04-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 4647
scraped_via: "browseros"
---

# How was i able to find privilege escalation.

How was i able to find privilege escalation.
Akshar Tank
Follow
3 min read
·
Apr 18, 2020

82

1

So this is my first write up related to my findings hope you all can learn.

So, One day i join a program on Bugcrowd from their Joinable program list. It was a set of application which provide email services to the clients. I dont know why i didnt start hunting as soon as i joined the program but i left it for two months.

So the flow of the applications was as follow there was one application(Central admin) which controls all the clients data and infrastructure (like how much resource should be allocated to client, Shall services like SFTP should be enabled, user management of the client admin etc) so let it be called tier one. On the tier two was the client admin panel from which he can mostly manage users(like making user groups, adding and removing them, resetting their password and making user access policies) and on the final tier there was the email application.

So i was just using the application trying to understand its flow while traffic being proxied through burp. I noticed that the cookies of the tier one and tier two applications were alike but the tier three was using a JWT token.

Thus i thought, What if admin of one client can access the main admin panel?

Press enter or click to view image in full size

So this is how i thought the flow of the two application could be! So i started burp, Open tier 2 application in one browser and tier 1 app in another. I traverse the whole tier 1 one application and capture all the API calls. It was almost 100 API calls for that(i might have missed some :P).

Get Akshar Tank’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

Then i took those and start replaying it in session of tier 2 admin. As the application was mature(kind of :)), Most of them gave the error User is authenticated but has no rights to perform this action.

But after some time i successfully found 11 endpoints where access control was not implemented correctly and was leaking sensitive data. At that time my initial doubt was confirmed that APIs from tier one and tier two applications are being processed by one server only.

This data included how my clients are there, their IP, domain name, CPU/RAM/HDD usage, licenses other clients had of, how many user profile other client had made with their ACL and other details and many more details were leaked.

Press enter or click to view image in full size
Press enter or click to view image in full size

So that is it. Hope you all liked it. You can find me on Twitter and LinkedIn.

Please feel free to ping me in case there is something missing.
