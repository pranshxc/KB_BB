---
source: imported
source_type: markdown
original_path: knowledge-inbox/blogs-incoming/2019-02-18_stored-xss-on-edmodo_2.md
original_filename: 2019-02-18_stored-xss-on-edmodo_2.md
title: Stored XSS on Edmodo
category: documents
detected_topics:
- xss
- command-injection
- api-security
tags:
- imported
- documents
- xss
- command-injection
- api-security
language: en
raw_sha256: d8fe8acc5f3d3b3bdbf2b7e97e9e5dff640de9ddc182b93df38f0931f5efff2e
text_sha256: bb23b97bb0bdc4987a21c21801e59d39c3a489708ef452ec26681c891db9f09b
ingested_at: '2026-06-28T07:31:58Z'
sensitivity: unknown
redactions_applied: false
---

# Stored XSS on Edmodo

## Source Metadata

- Original Path: knowledge-inbox/blogs-incoming/2019-02-18_stored-xss-on-edmodo_2.md
- Source Type: markdown
- Detected Topics: xss, command-injection, api-security
- Ingested At: 2026-06-28T07:31:58Z
- Redactions Applied: False
- Raw SHA256: `d8fe8acc5f3d3b3bdbf2b7e97e9e5dff640de9ddc182b93df38f0931f5efff2e`
- Text SHA256: `bb23b97bb0bdc4987a21c21801e59d39c3a489708ef452ec26681c891db9f09b`


## Content

---
title: "Stored XSS on Edmodo"
url: "https://medium.com/@futaacmcyber/stored-xss-on-edmodo-11a3fbc6b6d0"
authors: ["Rohit kumar (@rohitcoder)"]
programs: ["Edmodo"]
bugs: ["Stored XSS"]
publication_date: "2019-02-18"
added_date: "2022-09-15"
source: "pentester.land/writeups.json"
original_index: 5405
scraped_via: "browseros"
---

# Stored XSS on Edmodo

Stored XSS on Edmodo
Futaacm Cyber
Follow
4 min read
·
Feb 18, 2019

4

1

Hi guys,

Today i will be sharing about the exploit i found in Edmodo which could have allowed me to take over the account of any user of my choice.

About the target?

Edmodo is an educational technology company offering a communication, collaboration, and coaching platform to K-12 schools and teachers. The Edmodo network enables teachers to share content, distribute quizzes, assignments, and manage communication with students, colleagues, and parents.

Let’s get started!!!

So I saw a post on twitter where some guys posted about the swag they got from edmodo and I decided to try my luck out probably I might be able to find something. Below I will be talking about one of the bug I found on this target.

Reconnaissance

I visited the website and signed up as a normal user, I tried playing around the application for a while trying to understand the work flow of the application before creating another account which I will be using for attacking.

After playing with the application for a while, I thought I understood the application and I was set to attacking it which happened to the biggest lie of all time.

Thinking i was set to attack, so I decided to create a new account which I will be using to attack. To sign up on this application, the application takes you through four stages which are:

Stage 1: The application ask you for your email and password

Stage 2: The application ask you for your first name and last name. (This is the vulnerable endpoint)

Stage 3: The application ask you for the school you will be teaching from

Stage 4: The application ask you to link your other social media account with your edmodo account.

The Exploit

Get Futaacm Cyber’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Remember me for faster sign in

In the first stage, I filled in the form as required, i entered my email and password, then I was redirected to the second stage where I was asked for my firstname and lastname, this was where I injected my payload, I used <img src=x onerror=alert(1)> as the firstname and the same as the lastname, luckily for me my payload slipped through without being filtered or rejected by the server, at this stage I was already dancing.

my current mood

I filled the rest of the forms as required then I got logged in to my account. Upon logging in I was a bit disappointed, I was expecting my payload to be executed in the home page since my first name and last name were reflected their, instead of being executed as a script, they were reflected as a raw text, I checked my profile page probably I might get lucky and my payload will be executed their but still no luck, at this stage I was getting discouraged.

me feeling discouraged

I tried for couple of days to get it work but damn!!, I got nothing, this is where my insufficient reconnaissance showed but I was determined to make it work, as the infosec community always say #TryHarder which is what I did, on one faithful day, I was playing with the application again then I searched for my Account A from my Account B, I found my other Account A and I sent a connection request from my Account B to my Account A and I logged in to my Account A and I accepted the request, I viewed my Profile, I saw I had a new connection, I clicked on the connection tag and Boom!!! my payload was executed.

At this stage I didn’t know how to feel because I have being trying to make this work for days and finally It worked, straight away I reported the bug, I didn’t try exploiting it further because I didn’t want to get a “duplicate report” response and which sadly for me that was what I got.

But it’s good, I did learn something from exploiting the application which is: “Reconnaissance is the key” and “Being persistence pays off”.

Screenshot of P.O.C:

Press enter or click to view image in full size

Response from the triage team:

Press enter or click to view image in full size

That’s all for now,

Thank you.

Credit: Afolic
